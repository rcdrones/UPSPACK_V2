

#include "RPiUPSPack.h"
#include "pigpio.h"


using namespace std;


int main()
{
	int res = gpioInitialise();
	if (res > 0)
	{
		RPiUPSPack ups;
		for (int i = 0; i < 60; i++)
		{
			cout << i << "*******************************" << endl;
			cout << "External power:" << (ups.hasExternalPower() ? "Yes" : "No")  << endl;
			cout << "Power%:" << ups.getPowerPercent() << endl;
			cout << "Voltage:" << ups.getVoltage() << endl;
			cout << i << "*******************************" << endl;
			time_sleep(1);
		}
	}
	else {
		cout << "unable to initialize pigpio library" << endl;
	}
	gpioTerminate();
}