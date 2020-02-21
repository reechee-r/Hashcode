#pragma once
#include "GetLetters.h"
class FirstFile : private GetLetters
{
private:
	int max = GetLetters::getMax1();
	int min = GetLetters::getMin1();
public:
	FirstFile();
	void tryTwo();
	void tryThree();
};

