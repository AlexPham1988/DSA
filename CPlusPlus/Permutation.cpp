#include<iostream>
#include <bits/stdc++.h>
using namespace std;


void Permutation(string s, string out,vector<string> &v){
	if(s.length() == 0){
		// cout << out << "\n" ;
		if ( find(v.begin(), v.end(), out) == v.end() ) // Not find out in vector
			v.push_back(out);
	}
	for(int i = 0; i < s.length(); i++){
		char m = s[i];
		string remStr = s.substr(0,i) + s.substr(i+1,s.length());
		Permutation(remStr,out+m,v);
	}
}


void Permutation2(string s, string out){
	cout << "SB:" << s << endl;
	cout << "CB:" << out << endl;
	if (s.size() == 0){
		cout << "YEAH:" << out << endl;
		return;
	}
	
	for (int i = 0; i < s.length(); i++){
		
		cout << "S:" << s.substr(1) << endl;
		cout << "C:" << out + s[0] << endl;
		Permutation2(s.substr(1),out + s[0]);
		rotate(s.begin(), s.begin() + 1, s.end());
	}
}


int main(){
	string s = "AABC";
//	Permutation(s);
//	cout << s.substr(0) << endl;
//	Permutation2(s, "");
	
	vector<string> v;
	Permutation(s,"",v);
	for(int i = 0; i < v.size(); i ++)
		cout << v[i] << endl;
	
}
