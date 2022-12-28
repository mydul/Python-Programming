#include <iostream>
using namespace std;

void personal_inf(void);
void edu(void);
void skills(void);
void hobby(void);
void lang(void);
void plang(void);
void OS(void);
void tools(void);
void swot(void);

int main()
{
    personal_inf();
    edu();
    skills();
    hobby();
    lang();
    plang();
    OS();
    tools();
    swot();
}
void personal_inf(void)
{
    string name = "Sadia Afrin";
    string gender = "Female";
    int age = 30;
    string height = "5 feet 3 inch";
    string weight = "54KG";
    string nationality = "Bangladeshi";
    string date_of_birth = "31.12.1997";
    cout << "   PERSONAL DATA: " << endl
         << endl;
    cout << "\tName: " << name << endl
         << "\tGender: " << gender << endl
         << "\tAge: " << age << endl
         << "\tHeight: " << height << endl
         << "\tWeight: " << weight << endl
         << "\tNationality: " << nationality << endl
         << "\tDate of Birth: " << date_of_birth << endl
         << endl;
}

void edu(void)
{
    string school = "Bogra Cantonment Public School and College ";
    string college = "Bogra Cantonment Public School and College ";
    ;
    string versity = "Daffodil International University";
    cout << "   EDUCATION: " << endl
         << endl;
    cout << "\tSchool: " << school << endl
         << "\tCollege: " << college << endl
         << "\tUniversity: " << versity << endl
         << endl;
}

void skills(void)
{
    string skill1 = "Communication";
    string skill2 = "Coperative";
    string skill3 = "Brave";
    string skill4 = "Creative";
    string skill5 = "Chess";
    cout << "   SKILLS:" << endl
         << endl;
    cout << "\t" << skill1 << endl
         << "\t" << skill2 << endl
         << "\t" << skill3 << endl
         << "\t" << skill4 << endl
         << "\t" << skill5 << endl
         << endl;
}

void hobby(void)
{
    string hobby1 = "Shopping";
    string hobby2 = "Traveling";
    string hobby3 = "Music";
    string hobby4 = "Reading";
    cout << "   HOBBIES:" << endl
         << endl;
    cout << "\t" << hobby1 << endl
         << "\t" << hobby2 << endl
         << "\t" << hobby3 << endl
         << "\t" << hobby4 << endl
         << endl;
}

void lang(void)
{
    string lang1 = "English";
    string lang2 = "Bangla";
    string lang3 = "French(Inshallah Will Learn In Future)";
    cout << "   LANGUAGES: " << endl
         << endl;
    cout << "\t" << lang1 << endl
         << "\t" << lang2 << endl
         << "\t" << lang3 << endl
         << endl;
}
void plang(void)
{
    string lang1 = "C++";
    string lang2 = "C";
    string lang3 = "HTML";
    cout << "   PROGRAMMING LANGUAGES: " << endl
         << endl;
    cout << "\t" << lang1 << endl
         << "\t" << lang2 << endl
         << "\t" << lang3 << endl
         << endl;
}

void tools(void)
{
    string tool1 = "Microsoft Office";
    cout << "   TOOlS: " << endl
         << endl;
    cout << "\t" << tool1 << endl
         << endl;
}

void OS(void)
{
    string os1 = "Windows";
    string os2 = "Linux";
    string os3 = "IOS";
    cout << "   USED TO: " << endl
         << endl;
    cout << "\t" << os1 << endl
         << "\t" << os2 << endl
         << "\t" << os3 << endl
         << endl;
}

void swot(void)
{
    cout << "   MY SWOT ANALYSIS: " << endl
         << endl;
    cout << "\tStrengths: Good for nothing, stupid, useless" << endl;
    cout << "\tWeaknesses: Can't say no, trust people easily, can't hurt people" << endl;
}
