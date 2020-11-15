# Graham Essays Collection

![https://startupquote.com/post/1146924423](https://64.media.tumblr.com/tumblr_l8z2bgzrLh1qz6pqio1_500.png)

> **Alert**: This is a MVP and still a work-in-progress but I wanted to share my current implementation. Sorry if too messy, but following the very YC advise: _"If you are not embarrassed by the first version of your product, you've launched too late"_. If you have any ideas, suggestions, curses or feedback in order to improve the code, please don't hesitate in opening an issue or PR. They'll be very welcomed!

---

Download the *complete collection* of 193 essays from [Paul Graham] website and export them in EPUB and Markdown for easy [AFK] reading.
Running `wc` it turned out to be a whooping ~466K words (a The Lord of the Rings saga in total length) but about crazy travels in the startup worlds. I used the RSS originally made by [Aaron Swartz], `feedparser`, `html2text` and `Unidecode` libraries for data cleaning. To create the EPUB files you should have installed `pandoc` to properly execute the script.

[AFK]: https://www.grammarly.com/blog/afk-meaning/
[Paul Graham]: http://www.paulgraham.com/articles.html
[Aaron Swartz]: https://en.wikipedia.org/wiki/Aaron_Swartz

## Usage

```bash
sudo apt-get install python3.8-venv
python3.8 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
mkdir essays
python graham.py # wait for it
make epub
```

### The Current Essays

* ✅ 001 This Year We Can End the Death Penalty in California
* ✅ 002 Programming Bottom-Up
* ❌ 003 Chapter 2 of Ansi Common Lisp, (I/O operation on * closed file)
* ❌ 004 Chapter 1 of Ansi Common Lisp, (I/O operation on * closed file)
* ✅ 005 Lisp for Web-Based Applications
* ✅ 006 Beating the Averages
* ✅ 007 Java's Cover
* ✅ 008 Being Popular
* ✅ 009 Five Questions about Language Design
* ✅ 010 The Roots of Lisp
* ✅ 011 The Other Road Ahead
* ✅ 012 What Made Lisp Different
* ✅ 013 Why Arc Isn't Especially Object-Oriented
* ✅ 014 Taste for Makers
* ✅ 015 What Languages Fix
* ✅ 016 Succinctness is Power
* ✅ 017 Revenge of the Nerds
* ✅ 018 A Plan for Spam
* ✅ 019 Design and Research
* ✅ 020 Better Bayesian Filtering
* ✅ 021 Why Nerds are Unpopular
* ✅ 022 The Hundred-Year Language
* ✅ 023 If Lisp is So Great
* ✅ 024 Hackers and Painters
* ✅ 025 Filters that Fight Back
* ✅ 026 What You Can't Say
* ✅ 027 The Word "Hacker"
* ✅ 028 How to Make Wealth
* ✅ 029 Mind the Gap
* ✅ 030 Great Hackers
* ✅ 031 The Python Paradox
* ✅ 032 The Age of the Essay
* ✅ 033 What the Bubble Got Right
* ✅ 034 A Version 1.0
* ✅ 035 Bradley's Ghost
* ✅ 036 It's Charisma, Stupid
* ✅ 037 Made in USA
* ✅ 038 What You'll Wish You'd Known
* ✅ 039 How to Start a Startup
* ✅ 040 A Unified Theory of VC Suckage
* ✅ 041 Undergraduation
* ✅ 042 Writing,  Briefly
* ✅ 043 Return of the Mac
* ✅ 044 Why Smart People Have Bad Ideas
* ✅ 045 The Submarine
* ✅ 046 Hiring is Obsolete
* ✅ 047 What Business Can Learn from Open Source
* ✅ 048 After the Ladder
* ✅ 049 Inequality and Risk
* ✅ 050 What I Did this Summer
* ✅ 051 Ideas for Startups
* ✅ 052 The Venture Capital Squeeze
* ✅ 053 How to Fund a Startup
* ✅ 054 Web 2.0
* ✅ 055 Good and Bad Procrastination
* ✅ 056 How to Do What You Love
* ✅ 057 Why YC
* ✅ 058 6,631,372
* ✅ 059 Are Software Patents Evil?
* ✅ 060 See Randomness
* ✅ 061 The Hardest Lessons for Startups to Learn
* ✅ 062 How to Be Silicon Valley
* ✅ 063 Why Startups Condense in America
* ✅ 064 The Power of the Marginal
* ✅ 065 The Island Test
* ✅ 066 Copy What You Like
* ✅ 067 How to Present to Investors
* ✅ 068 A Student's Guide to Startups
* ✅ 069 The 18 Mistakes That Kill Startups
* ✅ 070 How Art Can Be Good
* ✅ 071 Learning from Founders
* ✅ 072 Is It Worth Being Wise?
* ✅ 073 Why to Not Not Start a Startup
* ✅ 074 Microsoft is Dead
* ✅ 075 Two Kinds of Judgement
* ✅ 076 The Hacker's Guide to Investors
* ✅ 077 An Alternative Theory of Unions
* ✅ 078 The Equity Equation
* ✅ 079 Stuff
* ✅ 080 Holding a Program in One's Head
* ✅ 081 How Not to Die
* ✅ 082 News from the Front
* ✅ 083 How to Do Philosophy
* ✅ 084 The Future of Web Startups
* ✅ 085 Why to Move to a Startup Hub
* ✅ 086 Six Principles for Making New Things
* ✅ 087 Trolls
* ✅ 088 A New Venture Animal
* ✅ 089 You Weren't Meant to Have a Boss
* ✅ 090 How to Disagree
* ✅ 091 Some Heroes
* ✅ 092 Why There Aren't More Googles
* ✅ 093 Be Good
* ✅ 094 Lies We Tell Kids
* ✅ 095 Disconnecting Distraction
* ✅ 096 Cities and Ambition
* ✅ 097 The Pooled-Risk Company Management Company
* ✅ 098 A Fundraising Survival Guide
* ✅ 099 Why to Start a Startup in a Bad Economy
* ✅ 100 The Other Half of "Artists Ship"
* ✅ 101 The High-Res Society
* ✅ 102 Could VC be a Casualty of the Recession?
* ✅ 103 After Credentials
* ✅ 104 Keep Your Identity Small
* ✅ 105 Startups in 13 Sentences
* ✅ 106 What I've Learned from Hacker News
* ✅ 107 Can You Buy a Silicon Valley?  Maybe.
* ✅ 108 Why TV Lost
* ✅ 109 How to Be an Angel Investor
* ✅ 110 Relentlessly Resourceful
* ✅ 111 Five Founders
* ✅ 112 The Founder Visa
* ✅ 113 Why Twitter is a Big Deal
* ✅ 114 A Local Revolution?
* ✅ 115 Maker's Schedule, Manager's Schedule
* ✅ 116 Ramen Profitable
* ✅ 117 The Trouble with the Segway
* ✅ 118 What Kate Saw in Silicon Valley
* ✅ 119 The Anatomy of Determination
* ✅ 120 The List of N Things
* ✅ 121 Post-Medium Publishing
* ✅ 122 Persuade xor Discover
* ✅ 123 What Startups Are Really Like
* ✅ 124 Apple's Mistake
* ✅ 125 Organic Startup Ideas
* ✅ 126 How to Lose Time and Money
* ✅ 127 The Top Idea in Your Mind
* ✅ 128 The Acceleration of Addictiveness
* ✅ 129 The Future of Startup Funding
* ✅ 130 What Happened to Yahoo
* ✅ 131 High Resolution Fundraising
* ✅ 132 Where to See Silicon Valley
* ✅ 133 The New Funding Landscape
* ✅ 134 What We Look for in Founders
* ✅ 135 Tablets
* ✅ 136 Founder Control
* ✅ 137 Subject: Airbnb
* ✅ 138 The Patent Pledge
* ✅ 139 Why Startup Hubs Work
* ✅ 140 Snapshot: Viaweb, June 1998
* ✅ 141 Schlep Blindness
* ✅ 142 A Word to the Resourceful
* ✅ 143 Frighteningly Ambitious Startup Ideas
* ✅ 144 Defining Property
* ✅ 145 How Y Combinator Started
* ✅ 146 Writing and Speaking
* ✅ 147 The Top of My Todo List
* ✅ 148 Black Swan Farming
* ✅ 149 Startup = Growth
* ✅ 150 The Hardware Renaissance
* ✅ 151 How to Get Startup Ideas
* ✅ 152 Startup Investing Trends
* ✅ 153 Do Things that Don't Scale
* ✅ 154 How to Convince Investors
* ✅ 155 Investor Herd Dynamics
* ✅ 156 How to Raise Money
* ✅ 157 Before the Startup
* ✅ 158 Mean People Fail
* ✅ 159 The Fatal Pinch
* ✅ 160 How You Know
* ✅ 161 How to Be an Expert in a Changing World
* ✅ 162 Let the Other 95% of Great Programmers In
* ✅ 163 Don't Talk to Corp Dev
* ✅ 164 What Doesn't Seem Like Work?
* ✅ 165 The Ronco Principle
* ✅ 166 What Microsoft Is this the Altair Basic of?
* ✅ 167 Change Your Name
* ✅ 168 Why It's Safe for Founders to Be Nice
* ✅ 169 Default Alive or Default Dead?
* ✅ 170 Write Like You Talk
* ✅ 171 A Way to Detect Bias
* ✅ 172 Jessica Livingston
* ✅ 173 The Refragmentation
* ✅ 174 Economic Inequality
* ✅ 175 Life is Short
* ✅ 176 How to Make Pittsburgh a Startup Hub
* ✅ 177 The Risk of Discovery
* ❌ 178 Charisma / Power, ([Errno 2] No such file or * directory: './essays/178_Charisma / Power.md')
* ✅ 179 General and Surprising
* ✅ 180 The Bus Ticket Theory of Genius
* ✅ 181 Novelty and Heresy
* ✅ 182 The Lesson to Unlearn
* ✅ 183 Having Kids
* ✅ 184 Fashionable Problems
* ✅ 185 The Two Kinds of Moderate
* ✅ 186 Haters
* ✅ 187 Being a Noob
* ✅ 188 How to Write Usefully
* ✅ 189 Coronavirus and Credibility
* ✅ 190 Orthodox Privilege
* ✅ 191 The Four Quadrants of Conformism
* ✅ 192 Modeling a Wealth Tax
* ✅ 193 Early Work

---

![https://startupquote.com/post/3890222281](https://64.media.tumblr.com/tumblr_li4p22jETB1qz6pqio1_500.png)
