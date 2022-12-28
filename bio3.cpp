#include <iostream>
#include <string>

using namespace std;

struct programmer {
string name;
int age;
string location;
string education;
string skills[3];
string language[3];
string tools[3];

};

int main() {
programmer me;
me.name = "Sadia Afrin";
me.age = 29;
me.location = "Hamburg, Germany";
me.education = "A graduate student of the Hamburg University of Technology";
me.skills[0] = "C";
me.skills[1] = "C++";
me.skills[2] = "HTML/CSS";

cout << "Name: " << me.name << endl;
cout << "Age: " << me.age << endl;
cout << "Location: " << me.location << endl;
cout << "Education: " << me.education << endl;
cout << "Skills: " << endl;
for (int i = 0; i < 3; i++) {
cout << " - " << me.skills[i] << endl;
}

return 0;
}