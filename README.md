<img src="https://challengepost-s3-challengepost.netdna-ssl.com/photos/production/software_photos/001/410/418/datas/original.png" width="400" style="text-align:center">

Demo video: [here](https://youtu.be/M5-tJGFmfPo)  

## Inspiration
There is a **massive problem** in the cryptocurrency market that can totally destroy these coins and crash the markets, this problem is called the 51% attack. The 51% attack is when one entity or organisation has over 50% control of the hash rate (mining). If this happens then the **entity has total control** and can **alter the blockchain for extreme financial gain**. One way to prevent this is by deterring entities and organisations and increasing the amount of smaller miners with a lottery type mining system. The current mining system used rewards a certain amount of crypto every time a block is created. Our proposal is to **instead reward the miner with a ticket**, and the prize for mining gets added to a pool. Every X blocks mined a lottery takes place and whoever wins takes the whole pool, then the pool resets. Our thought is that large groups and companies do not try to buy extreme amounts of lottery tickets due to the **risk factor**, so this **risk factor would deter them from spending lots of money on computational power** and instead **favour smaller miners using their phones, laptops** etc as it is a lower risk for them. We create a web app and a **decentralized peer to peer network** for this crypto where a user can create an account, buy crypto and transfer it to other users. They also have an option to **mine using their device**.

## What it does
We have created a solution that will solve the problem which is the 51% attack. To solve this, we have created a new cryptocurrency that **uses the same encryption as the leading cryptos** including Bitcoin and Ethereum while having a totally **unique mining system**. This mining system puts small miners using devices such as **phones and laptops at an advantage**. This mining system **does not require any software** and a user can start mining at a press of a button. When the user successfully mines the coin, they are entered into a lottery for a large amount of lottocoin. We have created a web app to display all these features, including user accounts, **transferring coins to others in real-time (without a database)**, mining blocks and **the whole blockchain technology**, the lottery system for the mining and a feature to view all users online and offline.

## How we built it
The front end was created with **HTML**, **CSS** and **JavaScript** with the bank end created mainly with **Flask**. The cryptocurrency was created with multiple **Python** classes and methods, using the **SHA-2** secure hash algorithm (**the same one used in Bitcoin**) to create secure transactions between users. The UI was designed with **Figma**, while the branding was created with Photoshop and other software. For deployment, we used **Azure** with help from **Docker**.

## Challenges we ran into
Our biggest challenge was the **steep learning curve**. As a team, we were **completely new to blockchain and creating cryptocurrencies**, so we had to learn a lot of information about these topics to actually determine if this project was realistic (which we agreed was with a lot of hard work). Our most helpful articles and repositories which helped us learn and understand are **linked at the bottom under references (we used some code as a help guide)**. Another major challenge was **implementing the decentralized system** as we could not use a database, so instead we defined each user as a node on the network so that the blockchain will never be lost.

## Accomplishments that we're proud of
As a team, we knew coordination would be a challenge as we are an international team from **3 different continents** and hence, **3 extreme different time zones**. We stepped up to the challenge and made it work, by delegating each person with tasks of equal work, we managed to lower the workload all while keeping good communication all while being up to 7 hours apart. Another accomplishment that we are proud of is **the speed at which we learned the basics of such a complex field**. At the start of this hackathon, we had **no prior knowledge** in blockchain and cryptocurrencies but now we are able to achieve a much deeper understanding through this project.

## What we learned
As a team, we have excelled in our **knowledge of cryptocurrencies and decentralization**. Decentralization is a very complex idea for us, and even harder to implement. We have learned about multiple new libraries including **pycryptodome**, **expiringdict** and numerous others. We have also learned about the full process of blockchain, including topics such as the **hashing algorithms** and retrieving balances for users by cycling through the transactions. But most importantly I think we have learned that we can **work well with a large time zone difference**. Since this is online timezones are not as impactful as in person, but it still makes an impact on overall communication.

## What's next for Lottocoin
We will continue to implement features including **automated mining**, to increase the amount everyday miners can mine and ultimately generate coins. Another main goal is to **give lottocoin value** by pricing the coins and limiting the number of coins that can be mined. This could be done by **setting up a transaction from USD to lottocoin**. For our crypto to become successful we will need to increase the users by giving this coin a use. We intend to use this crypto in **restaurants and shops, along with online businesses** to maximize our reach.

## References
https://hackernoon.com/wtf-is-the-blockchain-1da89ba19348
https://www.investopedia.com/terms/b/blockchain.asp
https://www.youtube.com/watch?v=malwhCwEosk&ab_channel=nang
https://www.figma.com/file/Sgm8OTfCuTQxeHSNNmjTUi/Untitled?node-id=0%3A1

## Setup  
- Create venv  
- "pip install -r requirements.txt"
- "flask run" 
