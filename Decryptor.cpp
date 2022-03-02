#include <iostream>
#include <fstream>
#include <string>
#include <vector>
using namespace std;

/*
Project Notes:
1) Both tests contain 500 characters
2) Space will be found between each word

Implementation References:
1) Common letters in English: a, e, h, i, n, o, r, s, t	(9 Letters Total)
2) Begin letters Commonly found: a, d, o, t, w (5 Letters Total)
3) End letters Commonly found: d, e, s, t	(4 Letters Total)
	*For more information and reference:
		https://www.thiagi.com/instructional-puzzles-original/2015/2/13/cryptograms#:~:text=Letter%20Frequency,s%2C%20d%2C%20and%20t.
	*Better Reference:
		https://norvig.com/mayzner.html
4) List of 58,000+ English Words (Dictionary_Words.txt)
	http://www.mieliestronk.com/corncob_lowercase.txt
5) Dictionary 1 Words:
	As Provided (Dict1.txt)
		https://brightspace.nyu.edu/content/enforced/176739-945-1224_SP22CS-GYCS-UY47836903AIINET/dictionary_1.txt
	Removed Unnecessary Headers and Spaces (Dict1_Revised.txt)
6) Dictionary 2 Words:
	As Provided (Dict2.txt)
		https://brightspace.nyu.edu/content/enforced/176739-945-1224_SP22CS-GYCS-UY47836903AIINET/dictionary_2.txt
	Removed Unnecessary Headers and Spaces (Dict2_Revised.txt)

Questions to Ask:
1) Does a new-line character (\n) equate to a space (" ")?
*/



// Function Declarations
void open_file(ifstream& file, string& filename);
void read_lines(ifstream& file, vector<string>& lines);
void get_d1_req(vector<string>& file, vector<int>& d1_freq);

main()
{
	bool complete = false;	// Determines Decryption Completion
	ifstream file;	// Temporarily Holds Encrypted Lines
	vector<int> dict1_freq;	// Holds Letter Occurrence Frequency of Dict_1Revised.txt
	
	

	/*
	Is the follwing line needed?
	vector<string> lines; 	// Store Encrypted Lines
	*/


	open_file(file, "Dict1_Revised.txt");	
	read_lines(lines);


	// Find Occurrence of Characters
	get_d1_freq(file, d1_freq);


	return 0;
}

void open_file(ifstream& file, string& filename) {
	file.open(filename);

	if (!file) {
		cerr << "File " + filename + " not found!!!" << endl;
		exit(1);
	}
}

void read_lines(ifstream& file, vector<string>& lines) {
	string line;

	while (file >> line) {
		lines.push_back(line);
	}
	file.close();
}

void get_d1_freq(vector<string>& dict1, vector<int>& d1_f) {
	for (size_t i = 0; i < dict1.length(); i++) {
		int val = int(dict1[i]);
	}
}