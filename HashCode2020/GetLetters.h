#pragma once

#include <fstream>
#include <iostream>
using namespace std;

class GetLetters
{
	// this part of the code is where i will locate a file and then give it a serial number
private:
	struct pizza {
		int slices; int serialNumber;
	};
	
	long param1[2], param2[2], param3[2], param4[2], param5[2];
	int num1 = 0, num2 = 0, num3 = 0, num4 = 0, num5 = 0;
	void loadLetters1();
	void loadLetters2();
	void loadLetters3();
	void loadLetters4();
	void loadLetters5();

public:
	int data1[4], data2[10], data3[50], data4[2000], data5[10000];
	GetLetters();
	int getMax1();
	int getMin1();
	int getMax2();
	int getMin2();
	int getMin3();
	int getMax3();
	int getMax4();
	int getMin4();
	int getMax5();
	int getMin5();

	long getparam11();
	long getparam12();
	long getparam21();
	long getparam22();
	long getparam31();
	long getparam32();
	long getparam41();
	long getparam42();
	long getparam51();
	long getparam52();
};