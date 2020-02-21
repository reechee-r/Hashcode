#include "GetLetters.h"

GetLetters::GetLetters()
{
	loadLetters1();
	loadLetters2();
	loadLetters3();
	loadLetters4();
	loadLetters5();
}
void GetLetters::loadLetters1()
{
	int count1=0;
	long output1[6];
	ifstream file1("a_example.in");
	
	while (!file1.fail() && !file1.eof())
	{
		file1 >> output1[count1];
		count1++;
	}
	num1 = count1;

	//giving values for the parameters
	param1[0] = output1[0]; param1[1] = output1[1];
	
	//giving values for the data
	for (int i = 0; i < (num1 - 2); i++)
	{
		data1[i] = output1[i+2];
	}
}
void GetLetters::loadLetters2()
{
	int count2 = 0;
	long output2[12];

	ifstream file2("b_small.in");
	
	while (!file2.fail() && !file2.eof())
	{
		file2 >> output2[count2];
		count2++;
	}

	num2 = count2;
	
	param2[0] = output2[0]; param2[1] = output2[1];
	
	for (int i = 0; i < (num2 - 2); i++)
	{
		data2[i] = output2[i+2];
	}
}
void GetLetters::loadLetters3()
{
	int count3 = 0;
	long output3[52];

	ifstream file3("c_medium.in");
	
	while (!file3.fail() && !file3.eof())
	{
		file3 >> output3[count3];
		count3++;
	}

	num3 = count3;

	param3[0] = output3[0]; param3[1] = output3[1];

	for (int i = 0; i < (num3 - 2); i++)
	{
		data3[i] = output3[i+2];
	}
}
void GetLetters::loadLetters4()
{
	int count4 = 0;
	long output4[2002];

	ifstream file4("d_quite_big.in");
	
	while (!file4.fail() && !file4.eof())
	{
		file4 >> output4[count4];
		count4++;
	}

	num4 = count4;

	param4[0] = output4[0]; param4[1] = output4[1];
	
	for (int i = 0; i < (num4 - 2); i++)
	{
		data4[i] = output4[i+2];
	}
}
void GetLetters::loadLetters5()
{
	int count5 = 0;
	long output5[10002];

	ifstream file5("e_also_big.in");

	while (!file5.fail() && !file5.eof())
	{
		file5 >> output5[count5];
		count5++;
	}
	num5 = count5;

	param5[0] = output5[0]; param5[1] = output5[1];

	for (int i = 0; i < (num5 - 2); i++)
	{
		data5[i] = output5[i+2];
	}
}

int GetLetters::getMax1()
{
	return data1[3];
}
int GetLetters::getMin1()
{
	return data1[0];
}

int GetLetters::getMax2()
{
	return data2[9];
}
int GetLetters::getMin2()
{
	return data2[0];
}

int GetLetters::getMax3()
{
	return data3[49];
}
int GetLetters::getMin3()
{
	return data3[0];
}

int GetLetters::getMax4()
{
	return data4[1999];
}
int GetLetters::getMin4()
{
	return data4[0];
}

int GetLetters::getMax5()
{
	return data5[9999];
}
int GetLetters::getMin5()
{
	return data5[0];
}

long GetLetters::getparam11()
{
	return param1[0];
}
long GetLetters::getparam12()
{
	return param1[1];
}

long GetLetters::getparam21()
{
	return param2[0];
}
long GetLetters::getparam22()
{
	return param2[1];
}

long GetLetters::getparam31()
{
	return param3[0];
}
long GetLetters::getparam32()
{
	return param3[1];
}

long GetLetters::getparam41()
{
	return param4[0];
}
long GetLetters::getparam42()
{
	return param4[1];
}

long GetLetters::getparam51()
{
	return param5[0];
}
long GetLetters::getparam52()
{
	return param5[1];
}