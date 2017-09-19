#include<iostream>
using namespace std;
int n = 2, k = 4 ;
int a[4];
string s = "AB";
bool check = false;
void display(){
	for (int i = 1; i <= k; i++){
//		int index = a[i] - 1;
//		cout << s[index];
//		cout << a[0];
		cout << a[i];
	}
	cout << endl;
}
void nextString(){
	int i = k;
	while (a[i]==s.length() && i>0){
		i--;
	}
	if (i == 0){
		check = true;
	} 
	else{
		a[i]++;
		for (int j = i + 1; j <= k; j++){
			a[j] = 1;
		}
	}
}

void print_str(string str,string prefix, const int lenght){
	int n = str.length();
	if (lenght == 1){
		for (int j = 0; j < n; j++)
		cout << prefix + str[j] << std::endl;
	}else{
		for (int i = 0; i < n; i++)
        	print_str(str, prefix + str[i], lenght - 1);
	}
}


int main(){
	#for (int i = 1; i <= k; i++){
	#	a[i] = 1;
	#}
	#while (!check){
	#	display();
	#	nextString();
	#}
	int lenght = 2;
	string str = "ABC";
	print_str(str, "", lenght);
}
