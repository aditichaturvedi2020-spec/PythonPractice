
# count numbers of vowels and conconents

def countVC(value):
    vowels = "aeiouAEIOU"
    countVowels = 0 
    countConso = 0
    
    for char in value:
        if(char.isalpha()):
            if (char in vowels):
                countVowels +=1
            else:
                countConso +=1
    return countVowels, countConso
vowels, consonants = countVC("Ashwani3717j")
print("vowels: ", vowels , "consonents: ", consonants)
