#pragma once
#include <vector>
#include "pigpio.h"
#include <regex>
#include <iostream>
using std::vector;
using std::string;
using std::regex;

class RPiUPSPack
{
public:
	RPiUPSPack();
	~RPiUPSPack();
	void refreshStats();
	void checkStale();
	bool hasExternalPower();
	int getPowerPercent();
	double getVoltage();
private:
	unsigned long m_lastCheckTick=0;
	int m_handle;
	bool m_initialised;
	bool m_lastPower=false;
	int m_lastPowerPercent=0;
	double m_lastVoltage=0;
	string m_deviceName = "/dev/serial0";
	char* m_cDeviceName = &m_deviceName[0];
	const regex m_regex = regex(".*Vin ([a-zA-Z]+),BATCAP ([0-9]+),Vout ([0-9]+).*");
};
