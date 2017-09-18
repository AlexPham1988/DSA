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
int main(){
	for (int i = 1; i <= k; i++){
		a[i] = 1;
	}
	while (!check){
		display();
		nextString();
	}
}
