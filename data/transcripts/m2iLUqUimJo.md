---
video_id: "m2iLUqUimJo"
title: "Securing AI's future with Avery Pennarun and Ivan Zhang at Web Summit Vancouver 2025"
description: "As AI takes off, it’s bringing new security challenges—especially around how models are built and accessed. In this talk, Tailscale CEO Avery Pennarun and Cohere Co-founder Ivan Zhang dig into the oft..."
channel_name: "Tailscale"
channel_id: "UCcdv38QxPjSMqbt5ffLhJLA"
published_at: "2025-05-29"
duration_seconds: 1082
youtube_url: "https://www.youtube.com/watch?v=m2iLUqUimJo"
thumbnail_url: "https://i.ytimg.com/vi_webp/m2iLUqUimJo/maxresdefault.webp"

# Transcription metadata
transcribed_at: "2025-10-03T17:42:30.239831"
transcription_method: "cpu"
model_used: "base"
language: "en"
word_count: 3418
transcription_time_seconds: 30.6
---

# Securing AI's future with Avery Pennarun and Ivan Zhang at Web Summit Vancouver 2025

**[00:00](https://youtube.com/watch?v=m2iLUqUimJo&t=0s)** Good morning, everybody. We've got two Canadian unicorns here. One recently minted. Coheres Enterprise AI, Tailscale counts many of the larger, better-known AI companies among its users including Coher. I think all of us want to know what we can learn from you. This moment that we're meeting, how you're thinking about security going into it. What we've seen in the past year of Enterprise AI adoption is everyone

**[00:32](https://youtube.com/watch?v=m2iLUqUimJo&t=32s)** is tired of the POCs, right? When our customers try to move to production, oftentimes they're faced with issues like cost, like governance, where is their data going, and also the stringent security and privacy regulations that they're facing under, right? And so for us, it's very interesting to see that, hey, to get these POCs into production, these are all these host of challenges, which is what we're focused on today. Building a, you know, our north or agentic platform,

**[01:02](https://youtube.com/watch?v=m2iLUqUimJo&t=62s)** that's security by default, and customers can safely experiment and also play with AI, and also take that into production in a safe and secure manner. So my observation is that the AI world is moving really fast, and every couple of weeks there's some new trend, some new change that everybody wants to jump on. The latest trend is a really important one, is they want to connect their AI's two things. They want to connect it to their company data, to databases, to APIs and stuff like that.

**[01:35](https://youtube.com/watch?v=m2iLUqUimJo&t=95s)** And the way people approach stuff like that in the AI world, because everyone's in a hurry, is they do it in a careless, sort of, we'll fix it later, way, tail skills, and networking company, we run into a lot of people who need to do networking, because networking is how you connect your AI's to stuff, and they don't want to think about it, because they're in a hurry, and they're worried about their AI thing, and so the first thing that comes to mind is, why don't I take my private data and put it out on the public internet, so one of the AI engines can then access it, and that's what they do, and then they come to us, and it's like, okay, so we did that.

**[02:05](https://youtube.com/watch?v=m2iLUqUimJo&t=125s)** It's working. Should I fix it? And the answer is, yes, probably, you should fix it.

**[02:11](https://youtube.com/watch?v=m2iLUqUimJo&t=131s)** Which brings me to the point that it feels like that networking layer, somehow that conversation gets overlooked in these conversations about AI security, and my wrong is that you're, I mean, yeah.

**[02:22](https://youtube.com/watch?v=m2iLUqUimJo&t=142s)** I mean, pretty much exactly what I've said. The only real security is network isolation. You could try to harden your systems as much as you want, but really what prevents data or bites from leaving your system is actual network isolation.

**[02:37](https://youtube.com/watch?v=m2iLUqUimJo&t=157s)** Why we really like working with tail scale, for example, is our IT organization is able to manage, safely manage our deployment of tail scale, make an internal network available for our engineers to then experiment with different MCP servers,

**[02:51](https://youtube.com/watch?v=m2iLUqUimJo&t=171s)** in an isolated environment, so they could safely play with this technology and evolve their thinking in the tail net.

**[03:00](https://youtube.com/watch?v=m2iLUqUimJo&t=180s)** AI workloads are typically distributed across different environments. That brings its own challenges.

**[03:07](https://youtube.com/watch?v=m2iLUqUimJo&t=187s)** Any mind to unpack that a bit to just why that's a bit different necessarily?

**[03:13](https://youtube.com/watch?v=m2iLUqUimJo&t=193s)** We run into this a lot. Customers come to us, especially in the AI world. We sort of accidentally became the back plane that all the AI companies are using for their data, just because nobody else was doing it, and we sort of found out after the game was already played that we had sort of won it.

**[03:28](https://youtube.com/watch?v=m2iLUqUimJo&t=208s)** It was kind of funny. Our website didn't have anything about AI on it until AI companies told us, like, hey, you won. How did you do that?

**[03:36](https://youtube.com/watch?v=m2iLUqUimJo&t=216s)** It's a really, really sick product, so that's why.

**[03:40](https://youtube.com/watch?v=m2iLUqUimJo&t=220s)** Yeah, but I think, like, but I wouldn't say networking is overlooked exactly in the AI world. Everybody knows they need it.

**[03:49](https://youtube.com/watch?v=m2iLUqUimJo&t=229s)** It's just that security is like last on their list of priorities, because they need, they want to be first. Everybody needs to be first, because everything's moving so fast.

**[03:57](https://youtube.com/watch?v=m2iLUqUimJo&t=237s)** So they come and they look at security later, and I can't say that's even the wrong approach, even though it always gets you into trouble eventually, but that's eventually.

**[04:05](https://youtube.com/watch?v=m2iLUqUimJo&t=245s)** You also need short term results so that somebody doesn't beat you in the short term.

**[04:09](https://youtube.com/watch?v=m2iLUqUimJo&t=249s)** So we tried to, like, think about a world where, like, hey, shouldn't that easiest thing to do also be the safest thing to do?

**[04:17](https://youtube.com/watch?v=m2iLUqUimJo&t=257s)** And I think cohere is doing the same thing. They're like, look, this is the right way to roll out AI in your company.

**[04:22](https://youtube.com/watch?v=m2iLUqUimJo&t=262s)** You don't have to do it the wrong way. It's actually faster to do it the right way.

**[04:25](https://youtube.com/watch?v=m2iLUqUimJo&t=265s)** And that's the path to, like, helping people build better systems.

**[04:29](https://youtube.com/watch?v=m2iLUqUimJo&t=269s)** Yeah, we take a lot of inspiration from how you guys have built tail scale, obviously, the fact that the end business user doesn't have to really think about security.

**[04:39](https://youtube.com/watch?v=m2iLUqUimJo&t=279s)** And, you know, them using the product is already secure by default. That's how we approach, how we design agents, how we want our, you know, business users actually use our products.

**[04:49](https://youtube.com/watch?v=m2iLUqUimJo&t=289s)** Edge brings convenience. It also brings more exposure. Can you also unpack part of what makes that hard and what's what you see working?

**[05:02](https://youtube.com/watch?v=m2iLUqUimJo&t=302s)** Did you say edge?

**[05:03](https://youtube.com/watch?v=m2iLUqUimJo&t=303s)** Yes.

**[05:04](https://youtube.com/watch?v=m2iLUqUimJo&t=304s)** Okay. Yeah.

**[05:05](https://youtube.com/watch?v=m2iLUqUimJo&t=305s)** I think, well, people want their AI's to be hosted in as many places as possible because you don't necessarily, well, in particular, there's a shortage of GPUs.

**[05:14](https://youtube.com/watch?v=m2iLUqUimJo&t=314s)** It's going to look, it looks like there's going to continue to be a shortage of GPUs for a pretty long time.

**[05:19](https://youtube.com/watch?v=m2iLUqUimJo&t=319s)** And so if you're a company that needs to use AI, you need to find GPUs somewhere at a reasonable price.

**[05:24](https://youtube.com/watch?v=m2iLUqUimJo&t=324s)** And the place where GPUs are the most reasonably priced is probably not your favorite cloud provider because somebody else already went there and bought them all.

**[05:33](https://youtube.com/watch?v=m2iLUqUimJo&t=333s)** And so you need to be able to connect these GPUs that you find at a reasonable price somewhere else to the rest of your system that is not the AI part.

**[05:40](https://youtube.com/watch?v=m2iLUqUimJo&t=340s)** It's just the regular systems part.

**[05:42](https://youtube.com/watch?v=m2iLUqUimJo&t=342s)** And that connectivity layer is how tail scale got dragged into this because nobody was building these so-called multi-cloud connectivity environments.

**[05:51](https://youtube.com/watch?v=m2iLUqUimJo&t=351s)** The advice right up until AI caught on is like, don't do multi-cloud. It just makes everything complicated for no reason, which is also good advice.

**[05:58](https://youtube.com/watch?v=m2iLUqUimJo&t=358s)** It's just now there's a reason, so you have to make everything complicated. So now you have to solve a problem that you didn't want to have to deal with.

**[06:04](https://youtube.com/watch?v=m2iLUqUimJo&t=364s)** Thank you for that. That's the thing that I think is probably most unclear right now.

**[06:09](https://youtube.com/watch?v=m2iLUqUimJo&t=369s)** How to approach security challenges posed by AI agents? I feel like it's keeping people up at night.

**[06:16](https://youtube.com/watch?v=m2iLUqUimJo&t=376s)** It's probably also the hottest topic going. It was, you know, many conferences this spring, including RSA. It's becoming a key theme, right?

**[06:22](https://youtube.com/watch?v=m2iLUqUimJo&t=382s)** So what would you say to companies trying to think about this?

**[06:27](https://youtube.com/watch?v=m2iLUqUimJo&t=387s)** So what we saw in the last year where folks are trying to piece together these POCs, you know, with different models and they're trying to build these rag pipelines and agents is, yeah, you can get the initial example work.

**[06:40](https://youtube.com/watch?v=m2iLUqUimJo&t=400s)** Maybe you index some data that you got an export of your notion or something, right?

**[06:44](https://youtube.com/watch?v=m2iLUqUimJo&t=404s)** But to take that into production, right, you have to think about things like identity providers, right?

**[06:49](https://youtube.com/watch?v=m2iLUqUimJo&t=409s)** Like how are the users going to give the agents permission and authorization to actually access these data?

**[06:56](https://youtube.com/watch?v=m2iLUqUimJo&t=416s)** Also, you know, where you're deploying it, do you even have network access to such tools, to such data sources?

**[07:03](https://youtube.com/watch?v=m2iLUqUimJo&t=423s)** You know, are you able to get the telemetry you need to actually debug when agents go wrong?

**[07:08](https://youtube.com/watch?v=m2iLUqUimJo&t=428s)** So another thing that was interesting is, you know, some other customers, they're downstream systems, they're internal tools, internal APIs.

**[07:14](https://youtube.com/watch?v=m2iLUqUimJo&t=434s)** They built it for a human level of usage, right?

**[07:19](https://youtube.com/watch?v=m2iLUqUimJo&t=439s)** As soon as they deployed agents to it, immediately they saw, oh, these things are starting to die.

**[07:25](https://youtube.com/watch?v=m2iLUqUimJo&t=445s)** They're starting to come down because agents can hit APIs and systems, 10X, 100X more than humans can, within the minute, right?

**[07:34](https://youtube.com/watch?v=m2iLUqUimJo&t=454s)** So, yeah, I mean, there's a ton of these challenges that, you know, I'm proud that we've helped some of our customers solve, and yeah.

**[07:41](https://youtube.com/watch?v=m2iLUqUimJo&t=461s)** As a security person, I find the AI security just sort of, well, it's really, it's fun and exciting because it's so insane.

**[07:49](https://youtube.com/watch?v=m2iLUqUimJo&t=469s)** The whole way we do it, right? This is an entirely new way to use a computer.

**[07:54](https://youtube.com/watch?v=m2iLUqUimJo&t=474s)** And the best analogy for it is it's like, it's a really high energy intern that's super naive, that you've hired at your company.

**[08:03](https://youtube.com/watch?v=m2iLUqUimJo&t=483s)** And like, okay, this intern has a, you know, it can run around and talk to everybody and accesses all your systems.

**[08:08](https://youtube.com/watch?v=m2iLUqUimJo&t=488s)** What are you going to give them access to knowing that this intern, if you tell them the wrong thing, will run away and hand all the information to your competitors?

**[08:16](https://youtube.com/watch?v=m2iLUqUimJo&t=496s)** Because that's what they thought you said to do.

**[08:20](https://youtube.com/watch?v=m2iLUqUimJo&t=500s)** And it's exactly like that, right? So, when you connect these LLMs to one of your internal databases with private stuff, that part is not really the problem.

**[08:30](https://youtube.com/watch?v=m2iLUqUimJo&t=510s)** People kind of overrate the problem of like, oh, they're going to train on my data and it's going to leak out like that.

**[08:34](https://youtube.com/watch?v=m2iLUqUimJo&t=514s)** Like, most of that is solved already. The real problem is like, it reads the data out of your database.

**[08:39](https://youtube.com/watch?v=m2iLUqUimJo&t=519s)** And while it's reading it, it sort of gets what's the word, like, subconsciously influenced.

**[08:46](https://youtube.com/watch?v=m2iLUqUimJo&t=526s)** Like, one of the things that reads out of a database of customers in, like, someone's description field, it might interpret that as instructions.

**[08:53](https://youtube.com/watch?v=m2iLUqUimJo&t=533s)** And then it runs off and applies those instructions and some other thing that you gave it access to.

**[08:57](https://youtube.com/watch?v=m2iLUqUimJo&t=537s)** And it definitely should not have done that. And then it just causes this chain reaction of craziness.

**[09:02](https://youtube.com/watch?v=m2iLUqUimJo&t=542s)** And so, you have to think of it like, how would you manage human threats inside your company?

**[09:07](https://youtube.com/watch?v=m2iLUqUimJo&t=547s)** Because it's the kind of mistakes that humans make.

**[09:10](https://youtube.com/watch?v=m2iLUqUimJo&t=550s)** And I don't mean to say that AI's are human, but they do make a lot of very human mistakes, right?

**[09:14](https://youtube.com/watch?v=m2iLUqUimJo&t=554s)** They have trouble with arithmetic, which computers have never had trouble with before.

**[09:17](https://youtube.com/watch?v=m2iLUqUimJo&t=557s)** We've invented, at very great expense, computers that have trouble with arithmetic.

**[09:21](https://youtube.com/watch?v=m2iLUqUimJo&t=561s)** But they also have trouble with simple following of instructions without getting distracted, right?

**[09:26](https://youtube.com/watch?v=m2iLUqUimJo&t=566s)** And it's these distractions that lead to all sorts of problems.

**[09:29](https://youtube.com/watch?v=m2iLUqUimJo&t=569s)** So one thing you can do is insert auditing layers whenever this, you know, you wouldn't want to do this with a person.

**[09:35](https://youtube.com/watch?v=m2iLUqUimJo&t=575s)** But you do it sometimes with interns, right?

**[09:37](https://youtube.com/watch?v=m2iLUqUimJo&t=577s)** Any time they want to do something, maybe you better just like double check what it is that they're doing before they're allowed to like, you know, carry computers out of the building or whatever.

**[09:47](https://youtube.com/watch?v=m2iLUqUimJo&t=587s)** Right? If you do that, if you build a system like that, then you can keep it under control while we're all doing these wild experiments and moving as fast as we can.

**[09:55](https://youtube.com/watch?v=m2iLUqUimJo&t=595s)** I'll plus one to that intern example, because that's exactly the right way to think about how to make these systems effective as well, not just secure.

**[10:04](https://youtube.com/watch?v=m2iLUqUimJo&t=604s)** Right? You know, if your intern had to ask you every time they want to do an operation for permission, they're not going to be effective.

**[10:11](https://youtube.com/watch?v=m2iLUqUimJo&t=611s)** Right? What's more important is actually giving them an environment where they can safely explore and play around.

**[10:17](https://youtube.com/watch?v=m2iLUqUimJo&t=617s)** You know, you have the proper policies and governance policies to actually let them explore within the environment.

**[10:24](https://youtube.com/watch?v=m2iLUqUimJo&t=624s)** You know, those are the use cases where we see AI agents actually create value rather than becoming nuisance.

**[10:31](https://youtube.com/watch?v=m2iLUqUimJo&t=631s)** So looking across the landscape, what are some of the best practices here that you think you could share with other founders and startups in the room?

**[10:38](https://youtube.com/watch?v=m2iLUqUimJo&t=638s)** So don't put your private API servers on the public internet. Don't do that.

**[10:48](https://youtube.com/watch?v=m2iLUqUimJo&t=648s)** I know you're not going to listen to me, but still don't. I'm going to laugh at you. That's all.

**[10:57](https://youtube.com/watch?v=m2iLUqUimJo&t=657s)** That's all. That's all. Oh, come on.

**[11:01](https://youtube.com/watch?v=m2iLUqUimJo&t=661s)** No, I guess that's not all. The other thing you should do is you want to make sure to give the thing access to what it needs access to and not access to what it doesn't need access to.

**[11:09](https://youtube.com/watch?v=m2iLUqUimJo&t=669s)** And while you're experimenting just like with people, right, you give them read only access first and then you give them read right access later once you've built up like some structure on what their job should be, right?

**[11:21](https://youtube.com/watch?v=m2iLUqUimJo&t=681s)** And I find people like GitHub just announced this thing, I think last week or a few days ago, where now you can give an LLM access to your entire GitHub account so it can read all of the issues and comment on the issues and make pull requests and approve pull requests and change your code.

**[11:35](https://youtube.com/watch?v=m2iLUqUimJo&t=695s)** It's like, okay, you've gone too far in one step, right? You don't need to do that all in one step. Just take it, take it easy a little bit. It can give you lots of great advice about your code, but maybe before you approve the pull request, you should read it first.

**[11:50](https://youtube.com/watch?v=m2iLUqUimJo&t=710s)** Yeah, I mean, I would say, you know, AI is obviously a very interesting technology. There's a lot of hype around it, but don't get lost in building something searching for a problem, right?

**[12:05](https://youtube.com/watch?v=m2iLUqUimJo&t=725s)** But definitely remember, or try to figure out how you produce ROI and perhaps, you know, adopting AI or using AI agents is one part of the solution. But like any other, let's say, era of software, right?

**[12:18](https://youtube.com/watch?v=m2iLUqUimJo&t=738s)** It is just a tool in the toolbox that ultimately solve a business problem, you know, create value for your customers.

**[12:26](https://youtube.com/watch?v=m2iLUqUimJo&t=746s)** Okay, so with all of this said, buy cellar hold, the growing push to use AI to secure your network. Are we there yet?

**[12:36](https://youtube.com/watch?v=m2iLUqUimJo&t=756s)** So it's interesting. So I think I've seen customers become much more ambitious and how they think about automation just in the last year, right?

**[12:48](https://youtube.com/watch?v=m2iLUqUimJo&t=768s)** I think, you know, having reasoning agents, giving them tools, giving them access to essentially the equivalent of an employee work laptop unlocks a lot of possibilities, right?

**[12:59](https://youtube.com/watch?v=m2iLUqUimJo&t=779s)** Now you can trust the agents enough to give them context to do the job. So for some jobs that are, let's say you can easily encode in some standard operating procedures, we do see customers actually go all the way, right?

**[13:16](https://youtube.com/watch?v=m2iLUqUimJo&t=796s)** Like go full, headless, you know, no human in the loop, sort of automation. So I think I'm pretty excited to see more and more of that, right?

**[13:26](https://youtube.com/watch?v=m2iLUqUimJo&t=806s)** And you know, it's interesting to see because some of these jobs are not fun jobs. And so it's maybe good that humans aren't doing those ones.

**[13:38](https://youtube.com/watch?v=m2iLUqUimJo&t=818s)** I guess I go back to my analogy of thinking of AI as like interns, right? We have as humans thousands of years of experience of dealing with effectively interns.

**[13:49](https://youtube.com/watch?v=m2iLUqUimJo&t=829s)** And we can use that experience in a lot of the same way. So in computers, we've certainly built up like, you know, our employees, you install software on their computer to make sure like antivirus, for example, right?

**[13:59](https://youtube.com/watch?v=m2iLUqUimJo&t=839s)** You make sure that's there because people sometimes click the wrong link and sometimes accidentally install a virus, and it's not their fault, and you need to catch it and deal with it.

**[14:06](https://youtube.com/watch?v=m2iLUqUimJo&t=846s)** And you can build systems similarly to help you with your AI systems. But also we have human systems that help with human mistakes, right?

**[14:14](https://youtube.com/watch?v=m2iLUqUimJo&t=854s)** You have seniors who are supervising interns who give them advice or approve things when, okay, it's like, hey, I made a proposal, I've done this whole patch, maybe you can review it for me and make sure I didn't screw anything up.

**[14:26](https://youtube.com/watch?v=m2iLUqUimJo&t=866s)** And you can also, if you're thinking like holistically of the sort of the future world of AI, you can build AI versions of those humans that are watching the other humans, right?

**[14:35](https://youtube.com/watch?v=m2iLUqUimJo&t=875s)** And it starts to sound a little convoluted, right? But you can, for example, even today, you can take, you know, let's put a log in front of every database access that our intern AI does to solve their problem, right?

**[14:48](https://youtube.com/watch?v=m2iLUqUimJo&t=888s)** And log flows into a database, well, that's another database, right? I can now have an AI look at that log and say, is there anything weird in here, right?

**[14:56](https://youtube.com/watch?v=m2iLUqUimJo&t=896s)** And it will surface like, hey, at this moment at this time, this happened that seems kind of unusual, it looks like they were downloading someone's private information or they accidentally deleted a table or something like that.

**[15:06](https://youtube.com/watch?v=m2iLUqUimJo&t=906s)** And so you've got to like one thing counter-balancing the other thing, probably you're going to want to have a human and loop eventually looking at that stuff that got surfaced, right?

**[15:14](https://youtube.com/watch?v=m2iLUqUimJo&t=914s)** But you do have the ability, like you should think of it as building social networks of humans, except that some of them are not humans, right?

**[15:23](https://youtube.com/watch?v=m2iLUqUimJo&t=923s)** And you treat it the same way.

**[15:25](https://youtube.com/watch?v=m2iLUqUimJo&t=925s)** Yeah, right. It takes you back actually some of the older cyber examples for cyber AI, right? Like the fish tank in Las Vegas that tried to access a high rollers database. And the AI was like, hmm, it's not usually typical that the fish tank needs access to this.

**[15:39](https://youtube.com/watch?v=m2iLUqUimJo&t=939s)** Was that a deaf con?

**[15:41](https://youtube.com/watch?v=m2iLUqUimJo&t=941s)** That was actually, I think it was a dark trace, one of the cyber companies really, anyway, one of their case studies.

**[15:47](https://youtube.com/watch?v=m2iLUqUimJo&t=947s)** We're in our final couple of minutes here. I'd love to know as we look out over the next two to five years, what each of you will be watching for in this space?

**[15:55](https://youtube.com/watch?v=m2iLUqUimJo&t=955s)** Yeah, I'm the most excited about controlled automation, right? Like controlled, you know, actually intelligent automation of some of these human tasks that we do.

**[16:05](https://youtube.com/watch?v=m2iLUqUimJo&t=965s)** I think it'll free up a lot of, you know, not fun work that, you know, we have to do day to day.

**[16:12](https://youtube.com/watch?v=m2iLUqUimJo&t=972s)** And I think that's where, you know, we'll see a lot of ROI from just, yeah, like these systems working autonomously in the background.

**[16:21](https://youtube.com/watch?v=m2iLUqUimJo&t=981s)** Well, you've documented wells some way to do this, you know, very boring job. And so now the agent can now do it.

**[16:31](https://youtube.com/watch?v=m2iLUqUimJo&t=991s)** So I'd love to see more and more examples of that.

**[16:34](https://youtube.com/watch?v=m2iLUqUimJo&t=994s)** I'll give you my honest answer. I want to live in a world where Siri doesn't suck.

**[16:39](https://youtube.com/watch?v=m2iLUqUimJo&t=999s)** Thank you. Thank you.

**[16:43](https://youtube.com/watch?v=m2iLUqUimJo&t=1003s)** And so Apple has spent so much time thinking about what Siri should be able to do for you and building like prototype versions of all those features.

**[16:55](https://youtube.com/watch?v=m2iLUqUimJo&t=1015s)** And every single one of them does not work correctly, right? I asked my watch, I say set a timer for five minutes.

**[17:02](https://youtube.com/watch?v=m2iLUqUimJo&t=1022s)** And about 30% of the time it sets something different, right? Like that's just like baseline nonsense.

**[17:10](https://youtube.com/watch?v=m2iLUqUimJo&t=1030s)** And so we all know what we want our phone to be able to do when we ask it to do something.

**[17:15](https://youtube.com/watch?v=m2iLUqUimJo&t=1035s)** Hey, like call my wife, right? That does not work. It supposedly works.

**[17:19](https://youtube.com/watch?v=m2iLUqUimJo&t=1039s)** I can supposedly go through my contact list and tag a bunch of things. It does not work, right?

**[17:23](https://youtube.com/watch?v=m2iLUqUimJo&t=1043s)** There's no reason it shouldn't work. This is stuff that AI's could do like today.

**[17:26](https://youtube.com/watch?v=m2iLUqUimJo&t=1046s)** If we gave it access to the information that it needs to do the work, right? And then just trust it to do that thing.

**[17:31](https://youtube.com/watch?v=m2iLUqUimJo&t=1051s)** But you need to have low latency. You need to have high reliability. You need to have reasonable price.

**[17:37](https://youtube.com/watch?v=m2iLUqUimJo&t=1057s)** It needs to be built into your phone, right? And all that stuff isn't there yet.

**[17:41](https://youtube.com/watch?v=m2iLUqUimJo&t=1061s)** There's a lot of engineering work to do, but I think people are just sort of ignoring because they're so excited about the possibilities.

**[17:46](https://youtube.com/watch?v=m2iLUqUimJo&t=1066s)** We just need to sit and engineer it.

**[17:48](https://youtube.com/watch?v=m2iLUqUimJo&t=1068s)** That's your prediction for the next two years. We're going to sit and engineer it and Siri's going to be great.

**[17:53](https://youtube.com/watch?v=m2iLUqUimJo&t=1073s)** You heard your first.

**[17:54](https://youtube.com/watch?v=m2iLUqUimJo&t=1074s)** All right, gentlemen. This has been lovely. Thank you all very much for joining us.

**[17:59](https://youtube.com/watch?v=m2iLUqUimJo&t=1079s)** Thank you for your time.

**[18:00](https://youtube.com/watch?v=m2iLUqUimJo&t=1080s)** Thanks, everybody.

---

*Automatically generated transcript. May contain errors.*
