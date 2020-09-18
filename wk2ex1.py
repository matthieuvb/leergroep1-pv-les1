# Voorbeeldopgave lists, resultaat: [2, 7, 5, 9]

e = [2, 7, 1]
pi = [3, 1, 4, 1, 5, 9]

answer0 = e[0:2] + pi[-2:]
print(answer0)

answer1 =  e[1:3]
print (answer1)

answer2 = pi[1:4:2] + e[0:1]
print (answer2)

answer3 = pi [1:6]
print (answer3)

answer4 = pi[1:2:2] + e[0:1] + pi[0:1] + pi [2:5:2]
print (answer4)

h = "hanze"
s = "hogeschool"
g = "groningen"

answer5 = s[0:2] + g[4]
print (answer5)

answer6 = s[4:7] + s[1:2] + g[7:9]*2
print (answer6)

answer7 = h[1:6]+s[1:10]
print (answer7)

# answer8 = (g[0:1]+ h[1:3-1])*2+ h[0:2]*5
# print (answer8)

answer8 = (g[0:1] + h[2:3] + h[1:2])*2 + h[0:2]*5
print (answer8)

answer9 = s[9] + s [3:4] + g[0:1] + s[1:2] + g[3:4] + s[1:2]+ s [3:4] + g[0:1] + s[1:2]
print (answer9)

answer10 = s[9] + s[3:4] + g[0:1]*2 +g[4:7] + s[4:5]
print (answer10)
