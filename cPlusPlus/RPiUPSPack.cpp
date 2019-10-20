// RPiUPSPack.cpp : Defines the entry point for the application.
//

#include "RPiUPSPack.h"

//sudo systemctl stop getty@ttyAMA0
using namespace std;

RPiUPSPack::RPiUPSPack()
{
	m_initialised = false;
	while (!m_initialised)
	{
		refreshStats();
	}
}

RPiUPSPack::~RPiUPSPack()
{
	
}

void RPiUPSPack::refreshStats()
{	
	m_handle = serOpen(m_cDeviceName, 9600, 0);
	time_sleep(0.5);
	int bytesAvailable = serDataAvailable(m_handle);
	if (bytesAvailable>45)
	{
		char buff[bytesAvailable];
		int ret = serRead(m_handle, buff, bytesAvailable);
		string res = string(buff);
		smatch matches;
		if (regex_search(res, matches, m_regex))
		{
			m_lastPower = string(matches[1]) == "GOOD";
			m_lastPowerPercent = stoi(matches[2]);
			m_lastVoltage = stod(matches[3]);
			m_lastCheckTick = gpioTick();
			m_initialised = true;
		}
	}
	serClose(m_handle);
	
}

void RPiUPSPack::checkStale()
{
	if (gpioTick() - m_lastCheckTick > 5000000)
	{
		refreshStats();
	}
}

bool RPiUPSPack::hasExternalPower()
{
	checkStale();
	return m_lastPower;
}

int RPiUPSPack::getPowerPercent()
{
	checkStale();
	return m_lastPowerPercent;
}

double RPiUPSPack::getVoltage()
{
	checkStale();
	return m_lastVoltage/1000;
}
