#include <iostream>
#include <fstream>
#include <string>

void writeDataToFile(std::string path, std::string data) {
	std::ofstream fileOutput(path);

	if (fileOutput.fail())
	{
		std::cout << "Cannot open file at " << path << std::endl;
		return;
	}

	fileOutput << "Hello world!" << std::endl;
	fileOutput << "I'm Le Tran Dat" << std::endl;
	fileOutput << "I worked at Singapore over 5 years" << std::endl;

	fileOutput.close();

	fileOutput.open(path, std::ios::app);

	fileOutput << "Goodbye everyone!" << std::endl;
}

void readDataFromFile(std::string path) {
	std::ifstream fileInput(path);

	if (fileInput.fail())
	{
		std::cout << "Cannot open file at " << path << std::endl;
		return;
	}

	while (!fileInput.eof())
	{
		char line[255];
		fileInput.getline(line, 255);
		std::cout << line << std::endl;
	}
}

int main() {
	std::string filePath = "C:/Users/Chinh Tran/Documents/source/points.dat";
	std::string data = "hello from the other";
	//writeDataToFile(filePath,data);
	//readDataFromFile(filePath);
	getchar();
	return 0;
}