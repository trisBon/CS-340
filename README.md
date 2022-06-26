# CS-340
How do you write programs that are maintainable, readable, and adaptable? Especially consider your work on the CRUD Python module from Project One, which you used to connect the dashboard widgets to the database in Project Two. What were the advantages of working in this way? How else could you use this CRUD Python module in the future?

The best way to create maintainabble, readable, and adaptable code is to follow standard coding practices and OOP guidelines. The advantage of using a CRUD module to handle database interactions was that it abstracted Mongodb functionality into a more controlled format. If users were given direct access to the Mongodb database, they would be able to make a wider variety of queries and changes to the dataset, but they would also need to learn mongo syntax. With the crud controller I was able to scope the Dashboard to the specifics needs of the user, which simultaneously increased data safety and removed the need for users to understand a specific resource. 


How do you approach a problem as a computer scientist? Consider how you approached the database or dashboard requirements that Grazioso Salvare requested. How did your approach to this project differ from previous assignments in other courses? What techniques or strategies would you use in the future to create databases to meet other client requests?

My typical coding approach is to allow user requirements to guide my design, but I found this approach ineffective when working on the Grazioso Salvare project. Based on my personal expereince with Python and Dash Framework, neither should ever be used when constructing databases for clients. Dash components do not work properly and several of the plotly dash coding examples were inoperable. If I build databases in the future, I hope to have better software at my disposal.

What do computer scientists do, and why does it matter? How would your work on this type of project help a company, like Grazioso Salvare, to do their work better?

Computer scientists perform jobs related to software development. I cannot offer an explanation for why what computer scientists do "matters" because I disagree with the premise of the quetion. It is a job, and it's importance is directly tied to the value humans assign to it. The job has no inherent value, and it only matters so long as people believe it does. Since it's value is subjective, I would argure that the work I will do does NOT matter. 
Whether the software I wrote would help GS do their work "better" is also subjective. The Dashboard I wrote will make it easier for GS to find training candidates, and that is all. If the company is bad at handling their finances or abusive to trainees, the software won't have any impact on "bettering" their work. Software makes things easier, but that doesn't automatically mean it is valuable or that it makes things better. 
