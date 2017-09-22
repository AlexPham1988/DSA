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


void RepeatCombination(string s,string out, int n){
	if(n == 0){
		cout << out << endl;
		return;
	}
//	if(out.empty() && n > 1)
//		RepeatCombination(s,out,n-1);
//	Small n go first, RepeatCombination(s,out,1) - > RepeatCombination(s,out,2) -> RepeatCombination(s,out,3)
	
	for (int i = 0; i < s.length(); i++)
		RepeatCombination(s,out + s[i],n-1);
	
//	Big n go first, RepeatCombination(s,out,3) - > RepeatCombination(s,out,2) -> RepeatCombination(s,out,1)	
	if(out.empty() && n > 1)
		RepeatCombination(s,out,n-1);
}

int main(){
	#for (int i = 1; i <= k; i++){
	#	a[i] = 1;
	#}
	#while (!check){
	#	display();
	#	nextString();
	#}
	int n = 2;
	string str = "ABC";
//	print_str(str, "", n);
	RepeatCombination(str,"",n);
}
