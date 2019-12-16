# Cyber Matters

## 3. A potential privacy management application

In this post, I'm going to talk about a tool that I think could be helpful in managing one's digital footprint—one that I'm going to be working on a prototype of throughout the rest of this blog. The idea is simple: what if there were a single tool you could go to that would compile and display all of the information about you that one can find on the Internet, as well as strategies and opportunities to minimize the size of that digital footprint? 

Ideally, it would work something like this. The user would input data like their name, state, etc., and would get back a list of the kinds of data that are available about them online, divided into categories like social media, home and mailing addresses, financial data, etc. Then, the application would recommend relevant privacy settings that might change the availability of that data, as well as allow for other data management options like takedown requests. 

```mermaid
graph LR
A[Input name and other relevant info] --> C[Publicly Available Data]
A --> F[Publicly Available Data]
    
    C --> D[Settings Suggestions]
    C --> E[Management Options]
    
    F --> G[Settings Suggestions]
    F --> H[Management Options]
  
```

![](C:\Users\lwpul\Projects\cyber_capstone\markdown\photos\mockup.JPG) 

This is definitely a tool that I would use to scope out my own digital footprint, and I think it could be a valuable way to manage things like social media settings if social media companies provide APIs to enable this kind of programmatic privacy management. As we move farther and farther into the world of big data and all-encompassing social media, it will be by using the same data tools that so far have compromised our privacy that we will be able to protect ourselves from corporations whose default will always be to collect as much data as possible. Clive Humby said in 2006 that "data is the new oil," but in recent years it's starting to seem like he was making an understatement. The difference between the two, though, is that once oil is used, it's gone. Data, on the other hand, can be repurposed, repackaged, and reused, hopefully to the betterment of the people who generate it. 