# 🎉 **Friends Project - Count the Claps** 🎉

## 🌟 Project Description

Welcome to the **Friends Project**! 🎈 This project was born from the idea of calculating the number of **claps** (applause) heard during a party when people greet each other. This project allows for the exploration of various fun scenarios where people either greet each other (or not) and calculates the number of claps based on these interactions.

The main idea of the website is to simulate a social event, considering different relationship dynamics between the guests:
- **Classic Mode**: Calculate the number of claps if everyone greets each other.
- **Enemy Duo**: Calculate the claps with people who refuse to greet each other (enemies).
- **Enemy Mode**: A more complex calculation where multiple people do not greet each other.

## 🚀 How Does the Clap Calculation Work? 🤔

### 1. **Classic Mode**

In this mode, we assume that everyone greets each other. This means that each person will shake hands with every other person present, resulting in a clap. To calculate this, we use a simple combinatorial formula:

$$
\frac{x \times (x - 1)}{2}
$$

where `x` is the number of people at the party. This formula calculates the number of ways two people can meet among a group of `x` people.

**Python Code Used**:
```python
x = int(input("Number of persons at the party: "))
result = int((x*x-x)/2)
print("Number of claps: ", result)
```
| x | Number of claps |
|-----------|-----------|
| 1  | **0** |
| 2  | **1**|
| 3  | **3** |
| 4  | **6**|
| 5  | **10** |
| 6  | **15** |
| 7  | **21** |
| 8  | **28** |
| 9  | **36** |
| 10  | **45** |

### 2. **Enemy Duo**

But beware, there are enemies! 🛑 Two people who do not want to greet each other create an exception to the rule. This mode calculates the claps while excluding the pairs of people who do not greet each other.

Imagine that `y` pairs of people out of `x` do not greed each other. This means we must **subtract one clap** for each of these exceptions from our initial calculation. The formula is:

$$
\frac{x \times (x - 1)}{2} - y
$$

**Python Code Used**:
```python
x = int(input("Number of people at the party: "))
y = int(input("Number of hated pairs (grouped in pairs of 2): "))
z = int((x*x-x)/2 - y)
print("Number of claps: ", z)
```
| x | y |  Number of claps |
|-----------|-----------|-----------|
| 1  | 2 |  **0** |
| 2  | 2 |  **0**|
| 3  | 2 |  **1** |
| 4  | 2 |  **4**|
| 5  | 2 |  **8** |
| 6  | 2 |  **13** |
| 7  | 2 |  **19** |
| 8  | 2 |  **26** |
| 9  | 2 |  **34** |
| 10  | 2 |  **43** |


### 3. **Enemy Mode (More Complex)**

In Enemy Mode, a person decides not to greet one or more other people. To handle this, we need to check for each person if they dislike others, and if so, subtract the corresponding claps from the total.

The calculation is:

$$ 
\frac{x \times (x - 1)}{2} - z
$$

where `z` is the number of claps removed.

> [!IMPORTANT]  
> If two people dislike each other, only one clap should be subtracted.

**Python Code Used**:
```python
x = int(input("Number of people at the party: "))
nb = int(input("How many people hate other people: "))
round = 1
y = 0
while nb >= 1:
    y = y + int(input(f"Number of people hated by person {round}: "))
    round = round + 1
    nb = nb - 1
z = int((x * (x - 1)) / 2 - y)
print("Number of claps: ", z)
```
| x | z |  Number of claps |
|-----------|-----------|-----------|
| 1  | 7 |  **0** |
| 2  | 7 |  **0**|
| 3  | 7 |  **0** |
| 4  | 7 |  **0**|
| 5  | 7 |  **3** |
| 6  | 7 |  **8** |
| 7  | 7 |  **14** |
| 8  | 7 |  **21** |
| 9  | 7 |  **29** |
| 10  | 7 |  **38** |

### 4. **Multi-Claps**

In this final mode, we assume that everyone greets each other with multiple claps. This means that each person shakes hands multiple times with every other person present, resulting in multiple claps. To calculate this, we extend the initial formula:

$$
\frac{x \times (x - 1)}{2} \times a 
$$

where `x` is the number of people at the party and `a` is the number of claps each person gives.

**Python Code Used**:
```python
x = int(input("Number of persons at the party: "))
a = int(input("Number of claps for each person: "))
result = int(((x*x-x)/2)*a)
print("Number of claps: ", result)
```

| x | a | Number of claps |
|-----------|-----------|-----------|
| 1  | 2 | **0** |
| 2  | 2 | **2**|
| 3  | 2 | **6** |
| 4  | 2 | **12**|
| 5  | 2 | **20** |
| 6  | 2 | **30** |
| 7  | 2 | **42** |
| 8  | 2 | **56** |
| 9  | 2 | **72** |
| 10  | 2 | **90** |

# **Part 3: The Site Code and Design**

## 🧑‍💻 Code and Features

Here is the project structure, where each section corresponds to a clap calculation mode:
```markdown
/friends-mej
/img/
- friends.jpg           # Background image
- mej-logo.gif          # MeJ logo
/one-clap/
- classic.html          # Page for classic calculation
- duo-of-enemies.html   # Page for calculation with enemy duo
- enemies.html          # Page for calculation with multiple enemies
/two-claps/
- two-claps.html        # Page for calculation with multiple claps
style.css               # Main stylesheet
index.html              # Homepage
/python/
- classic.py            # Python file for classic calculation
- duo-of-enemies.py     # Python file for calculation with enemy duo
- enemies.py            # Python file for calculation with multiple enemies
- two-claps.py          # Python file for calculation with multiple claps
```

## 🧑‍🏫 **MATh.en.JEANS Project**

This project is part of the **MATh.en.JEANS** initiative, which allows students to explore mathematical research through collaborative projects with professional mathematicians. The students then present their findings at annual congresses.

🎓 **Goal**: To introduce students to real-world math research.

🔗 [Learn more about MATh.en.JEANS](https://www.mathenjeans.fr)
