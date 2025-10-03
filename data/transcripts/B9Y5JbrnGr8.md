---
video_id: "B9Y5JbrnGr8"
title: "Tailscale Up: Opportunity, connectivity and Tailscale"
description: "This talk was given by David Rio Deiros at Tailscale Up in San Francisco on Wednesday, May 31, 2023...."
channel_name: "Tailscale"
channel_id: "UCcdv38QxPjSMqbt5ffLhJLA"
published_at: "2023-07-07"
duration_seconds: 939
youtube_url: "https://www.youtube.com/watch?v=B9Y5JbrnGr8"
thumbnail_url: "https://i.ytimg.com/vi_webp/B9Y5JbrnGr8/maxresdefault.webp"

# Transcription metadata
transcribed_at: "2025-10-03T16:19:16.270445"
transcription_method: "cpu"
model_used: "base"
language: "en"
word_count: 2221
transcription_time_seconds: 22.0
---

# Tailscale Up: Opportunity, connectivity and Tailscale

**[00:00](https://youtube.com/watch?v=B9Y5JbrnGr8&t=0s)** All right. Before we start, I'd like to, well, I know how difficult it is to put together

**[00:07](https://youtube.com/watch?v=B9Y5JbrnGr8&t=7s)** something like this, a conference like this one, so I'd like to thank a few people, Katie,

**[00:12](https://youtube.com/watch?v=B9Y5JbrnGr8&t=12s)** Jeremy, and the developer relations team. Anyone from the team here? No? Yes? Come on. Yes,

**[00:18](https://youtube.com/watch?v=B9Y5JbrnGr8&t=18s)** yes, yes. Also, every underday, which for approving this event, and then the marketing

**[00:27](https://youtube.com/watch?v=B9Y5JbrnGr8&t=27s)** and the design teams, anyone from those teams here? No? Yes? Anyway, give it up. Yes. All right.

**[00:35](https://youtube.com/watch?v=B9Y5JbrnGr8&t=35s)** So, my name is David. I'm an engineer at Tafs University, where I help indirectly shape

**[00:41](https://youtube.com/watch?v=B9Y5JbrnGr8&t=41s)** the minds of the future generation, and it's going to be all right. Don't worry. I also

**[00:46](https://youtube.com/watch?v=B9Y5JbrnGr8&t=46s)** live in Charleston, South Carolina, and about that, if you have read the Howtela Scale

**[00:52](https://youtube.com/watch?v=B9Y5JbrnGr8&t=52s)** Works blog post, you probably have seen this visualization, and one of the cities that they

**[00:59](https://youtube.com/watch?v=B9Y5JbrnGr8&t=59s)** use there is Charleston. So, I always wonder if there was anyone from Tela Scale living

**[01:04](https://youtube.com/watch?v=B9Y5JbrnGr8&t=64s)** in Charleston, but my guess is that probably was the design decision, but I'll ask the designers

**[01:10](https://youtube.com/watch?v=B9Y5JbrnGr8&t=70s)** later. So, yeah, do they just want to talk about how I started with Tela Scale, how I started

**[01:18](https://youtube.com/watch?v=B9Y5JbrnGr8&t=78s)** using it at work, and then we'll have a little tutorial. We'll talk about funneling, which

**[01:23](https://youtube.com/watch?v=B9Y5JbrnGr8&t=83s)** seems to be the highlight of these conferences, and then just talk briefly about some future

**[01:30](https://youtube.com/watch?v=B9Y5JbrnGr8&t=90s)** plans that I have for Tela Scale at work. So, how many here work at university? Three, four,

**[01:40](https://youtube.com/watch?v=B9Y5JbrnGr8&t=100s)** awesome. Yeah, I know one at least. And to me, I think that universities are interesting

**[01:46](https://youtube.com/watch?v=B9Y5JbrnGr8&t=106s)** organizations. A couple of things that come to mind are, we have a lot of different teams

**[01:52](https://youtube.com/watch?v=B9Y5JbrnGr8&t=112s)** working on different projects, mostly independently, and we have hundreds of subnets, and that

**[01:59](https://youtube.com/watch?v=B9Y5JbrnGr8&t=119s)** translates in basically operational charm. But to me, everything I started with Warguard.

**[02:06](https://youtube.com/watch?v=B9Y5JbrnGr8&t=126s)** I was in the market for a better VPN, just a way to connect my devices in a secure way,

**[02:13](https://youtube.com/watch?v=B9Y5JbrnGr8&t=133s)** and I remember finding Warguard and thinking, wow, I really can build a good mental model on

**[02:21](https://youtube.com/watch?v=B9Y5JbrnGr8&t=141s)** how the tool works. And then I read this comment from Avery that made total sense. He said that

**[02:32](https://youtube.com/watch?v=B9Y5JbrnGr8&t=152s)** over 20 years of more working with VPNs, we now know what cryptographic constructs work and

**[02:38](https://youtube.com/watch?v=B9Y5JbrnGr8&t=158s)** which one's good work and Warguard, the author of Warguard basically implemented only the things

**[02:44](https://youtube.com/watch?v=B9Y5JbrnGr8&t=164s)** that work and remove all the other stuff, and that made total sense. But still, it requires

**[02:52](https://youtube.com/watch?v=B9Y5JbrnGr8&t=172s)** a lot of maintenance. It has a high operational cost. You have to do a lot of things, and logically,

**[02:58](https://youtube.com/watch?v=B9Y5JbrnGr8&t=178s)** you try to build some tooling around it, but it's not quite right. So then Tela Scale comes

**[03:05](https://youtube.com/watch?v=B9Y5JbrnGr8&t=185s)** along. Well, it solves the issues that you had running Warguard, running a standalone. So

**[03:15](https://youtube.com/watch?v=B9Y5JbrnGr8&t=195s)** basically, open imports, and also this tribute in the keys in a secure manner. So you get a

**[03:23](https://youtube.com/watch?v=B9Y5JbrnGr8&t=203s)** taste of CiroTrack, or I like to call it 1% because I trust Tela Scale, and then Tela Scale

**[03:32](https://youtube.com/watch?v=B9Y5JbrnGr8&t=212s)** will trust my IDP for identity. And then you also quickly realize that Tela Scale is just amazing.

**[03:41](https://youtube.com/watch?v=B9Y5JbrnGr8&t=221s)** I mean, it just keeps running there and providing this rigidity. And then at some point, you

**[03:51](https://youtube.com/watch?v=B9Y5JbrnGr8&t=231s)** experience this, right? You are using Tela Scale at the personal level, but then at work, it's

**[03:57](https://youtube.com/watch?v=B9Y5JbrnGr8&t=237s)** completely different. So, yeah, this gives capture, I think, very well-high-feld at that time.

**[04:03](https://youtube.com/watch?v=B9Y5JbrnGr8&t=243s)** By the way, does anyone recognize the second gift, what movie that is coming from? Thank God. Okay,

**[04:15](https://youtube.com/watch?v=B9Y5JbrnGr8&t=255s)** thank you. I just wanted to make sure. So you start thinking about it, and you think, okay,

**[04:24](https://youtube.com/watch?v=B9Y5JbrnGr8&t=264s)** it would be super easy just to grab one note from my, from work, and just incorporating that into

**[04:30](https://youtube.com/watch?v=B9Y5JbrnGr8&t=270s)** your telnet. And then that's it. And you also think about, whoa, I could have a setup like this one

**[04:35](https://youtube.com/watch?v=B9Y5JbrnGr8&t=275s)** where I only route work traffic through a Warguard tunnel, only that traffic, and then all the other

**[04:44](https://youtube.com/watch?v=B9Y5JbrnGr8&t=284s)** traffic goes through whatever you want to use for either a Warguard tunnel against a VM or just

**[04:51](https://youtube.com/watch?v=B9Y5JbrnGr8&t=291s)** directly through your internet provider. And this is a super convenient setup that it wasn't

**[04:58](https://youtube.com/watch?v=B9Y5JbrnGr8&t=298s)** trivial to set up to me at least prior Tela Scale. So the first stage is, well, you at least,

**[05:07](https://youtube.com/watch?v=B9Y5JbrnGr8&t=307s)** I asked for permission. You don't have to, but I did ask for permission. So, and that can be tough,

**[05:13](https://youtube.com/watch?v=B9Y5JbrnGr8&t=313s)** depending, depending on the code organization. So be prepared, and pick the right person to talk

**[05:22](https://youtube.com/watch?v=B9Y5JbrnGr8&t=322s)** about this. So the typical arguments that I heard about were, okay, we're going to have another

**[05:30](https://youtube.com/watch?v=B9Y5JbrnGr8&t=330s)** piece of software that is going to be, it's going to increase our attack surface, and all that is

**[05:37](https://youtube.com/watch?v=B9Y5JbrnGr8&t=337s)** great, and it's reasonable, but to me, just the increase in connectivity that you had with

**[05:43](https://youtube.com/watch?v=B9Y5JbrnGr8&t=343s)** Tela Scale really sets all the security concerns. But still, the way I try to address that is by talking

**[05:50](https://youtube.com/watch?v=B9Y5JbrnGr8&t=350s)** about the founders expertise on this domain, the networking domain, and also in the programming

**[05:57](https://youtube.com/watch?v=B9Y5JbrnGr8&t=357s)** language that drives Tela Scale. I also talk about the openness of the company. All the, to me,

**[06:03](https://youtube.com/watch?v=B9Y5JbrnGr8&t=363s)** that's very important. All the code is basically open source, perhaps with the exception of the

**[06:09](https://youtube.com/watch?v=B9Y5JbrnGr8&t=369s)** control plane, but then we have headspace. I talk about the, I show the internal policy, which

**[06:16](https://youtube.com/watch?v=B9Y5JbrnGr8&t=376s)** highlights how the company thinks about security. Talk about the security bulletins that allow you

**[06:22](https://youtube.com/watch?v=B9Y5JbrnGr8&t=382s)** to, you know, react quickly when inevitably security issues happen. And then this final one that I

**[06:31](https://youtube.com/watch?v=B9Y5JbrnGr8&t=391s)** really, really enjoy, where, you know, Tela Scale periodically releases either blog posts or

**[06:38](https://youtube.com/watch?v=B9Y5JbrnGr8&t=398s)** technical documents about how Tela Scale works, and that really helps you use the tool more

**[06:45](https://youtube.com/watch?v=B9Y5JbrnGr8&t=405s)** more effectively. But then, okay, you, you hopefully win the argument, and then you run Tela Scale,

**[06:54](https://youtube.com/watch?v=B9Y5JbrnGr8&t=414s)** you extend your, your talent net to incorporate the systems that you, that you built that work,

**[07:02](https://youtube.com/watch?v=B9Y5JbrnGr8&t=422s)** right? But then you want to spread the law and just make sure that your teams can also enjoy Tela Scale.

**[07:10](https://youtube.com/watch?v=B9Y5JbrnGr8&t=430s)** So you write more slides and talk about the first thing that you, you have to decide is,

**[07:19](https://youtube.com/watch?v=B9Y5JbrnGr8&t=439s)** okay, do I introduce Tela Scale as a VPN or a summation network? And if we introduce Tela

**[07:26](https://youtube.com/watch?v=B9Y5JbrnGr8&t=446s)** as a VPN, then that's easy in a sense that everybody knows what a VPN is. But then I has very

**[07:32](https://youtube.com/watch?v=B9Y5JbrnGr8&t=452s)** negative connotations. But then if you talk about a machine network, that's more of a exotic topic.

**[07:38](https://youtube.com/watch?v=B9Y5JbrnGr8&t=458s)** Maybe we don't know that much about it. But then I think that it's the right way to go because

**[07:42](https://youtube.com/watch?v=B9Y5JbrnGr8&t=462s)** sets the foundations to then talking about all the functionality that Tela Scale provides on top of

**[07:49](https://youtube.com/watch?v=B9Y5JbrnGr8&t=469s)** that network. So then here are some things that I talk about on that, on that presentation. I'm

**[07:56](https://youtube.com/watch?v=B9Y5JbrnGr8&t=476s)** not going to go through it, but at the end I talk about all that extra functionality, right? And

**[08:03](https://youtube.com/watch?v=B9Y5JbrnGr8&t=483s)** one of those pieces of functionality is funneling. And just so we are on the same page,

**[08:11](https://youtube.com/watch?v=B9Y5JbrnGr8&t=491s)** funneling basically allows you to route internet traffic to your tell note. But that is not what I

**[08:18](https://youtube.com/watch?v=B9Y5JbrnGr8&t=498s)** want to show you here today. What I really want to talk about is that visualization or maybe

**[08:25](https://youtube.com/watch?v=B9Y5JbrnGr8&t=505s)** animation that I think shame growth is shame here today. Oh, it's awesome. I think that we are

**[08:32](https://youtube.com/watch?v=B9Y5JbrnGr8&t=512s)** going to be able to trace the success of Tela Scale back to this animation. But yeah, so the

**[08:40](https://youtube.com/watch?v=B9Y5JbrnGr8&t=520s)** way it works, you can check that code there. But uses the library, this library manager is that

**[08:47](https://youtube.com/watch?v=B9Y5JbrnGr8&t=527s)** basically implements a physics engine. And what that allows you to do is to define a 2D wall

**[08:54](https://youtube.com/watch?v=B9Y5JbrnGr8&t=534s)** that where you can create objects and define parameters that you can tell how those objects

**[09:02](https://youtube.com/watch?v=B9Y5JbrnGr8&t=542s)** interact in the wall, right? And then at some point you say, okay, well, now render the state of

**[09:08](https://youtube.com/watch?v=B9Y5JbrnGr8&t=548s)** this wall over time in this Canvas element. So that's great. And shown what he did there was to

**[09:18](https://youtube.com/watch?v=B9Y5JbrnGr8&t=558s)** just he dropped circles at the very top of the wall. And then those circles like follow the

**[09:23](https://youtube.com/watch?v=B9Y5JbrnGr8&t=563s)** funnel, which is basically four rectangles, right? But then I thought, what if we map

**[09:31](https://youtube.com/watch?v=B9Y5JbrnGr8&t=571s)** actual funnel requests to the creation of the circles? And that's what I have running here

**[09:38](https://youtube.com/watch?v=B9Y5JbrnGr8&t=578s)** on with this slide. I have a little HTTP server that is listening for traffic at the other side

**[09:46](https://youtube.com/watch?v=B9Y5JbrnGr8&t=586s)** of the funnel. And then sends the request or web socket to a piece of code running in the browser,

**[09:52](https://youtube.com/watch?v=B9Y5JbrnGr8&t=592s)** which is JavaScript. And then that JavaScript code creates new circles on the wall.

**[10:01](https://youtube.com/watch?v=B9Y5JbrnGr8&t=601s)** So now let's add a counter here, hopefully, demo time again. So just to make it more

**[10:08](https://youtube.com/watch?v=B9Y5JbrnGr8&t=608s)** that, ooh, is someone already going there? What is happening? It's all those are now requests from

**[10:14](https://youtube.com/watch?v=B9Y5JbrnGr8&t=614s)** someone. So it's very cool. How many we have? So yeah, this is really a toy example,

**[10:23](https://youtube.com/watch?v=B9Y5JbrnGr8&t=623s)** but it really highlights the countdown. But yeah, try to break it. Try to break it.

**[10:32](https://youtube.com/watch?v=B9Y5JbrnGr8&t=632s)** It's on by actually, if you if you keep sending requests, it's going to break the funnel. I have seen

**[10:38](https://youtube.com/watch?v=B9Y5JbrnGr8&t=638s)** that. So keep going. Yeah, actually, it's not very logic, right? Because the circles are pushing

**[10:45](https://youtube.com/watch?v=B9Y5JbrnGr8&t=645s)** each other, but it's pretty cool. Anyway, come down. Come on. All right. So that was a toy example,

**[10:54](https://youtube.com/watch?v=B9Y5JbrnGr8&t=654s)** but definitely funneling is a super useful feature of TeleScale. I encourage you to read that blog post

**[11:00](https://youtube.com/watch?v=B9Y5JbrnGr8&t=660s)** from Z. So yeah, so back to the main topic of the slides. I feel it's given the presentation

**[11:09](https://youtube.com/watch?v=B9Y5JbrnGr8&t=669s)** to the team and then my manager comes and asks, hey, we're having some issues,

**[11:14](https://youtube.com/watch?v=B9Y5JbrnGr8&t=674s)** connecting some on-premise machines with an AWS resource. And he asked if I could help. I said,

**[11:22](https://youtube.com/watch?v=B9Y5JbrnGr8&t=682s)** sure. And basically, the RDS service was a or the service was an RDS service, which is a mana,

**[11:29](https://youtube.com/watch?v=B9Y5JbrnGr8&t=689s)** serverless blah, blah, blah, blah. And the KVDocs have a great document on how to solve that

**[11:37](https://youtube.com/watch?v=B9Y5JbrnGr8&t=697s)** problem. And basically involves adding an AWS to instance that acts as a bridge relay between

**[11:45](https://youtube.com/watch?v=B9Y5JbrnGr8&t=705s)** the subnet where you have the service and then the on-premise holes, right? Okay.

**[11:58](https://youtube.com/watch?v=B9Y5JbrnGr8&t=718s)** So yeah, so everything was fine with the exception that the people that created the service

**[12:03](https://youtube.com/watch?v=B9Y5JbrnGr8&t=723s)** created a service as a public service. So I didn't have access to the subnet or AWS. I couldn't

**[12:11](https://youtube.com/watch?v=B9Y5JbrnGr8&t=731s)** see or get the subnet where the RDS service was running. So I couldn't advertise that subnet when

**[12:18](https://youtube.com/watch?v=B9Y5JbrnGr8&t=738s)** I was starting TeleScale. So what I end up using is just advertise the public IP. And you may be

**[12:27](https://youtube.com/watch?v=B9Y5JbrnGr8&t=747s)** thinking why you didn't have direct access to that public IP from the on-premise boxes.

**[12:34](https://youtube.com/watch?v=B9Y5JbrnGr8&t=754s)** And the reason for that was that the direct connect, which is this piece of hardware that

**[12:40](https://youtube.com/watch?v=B9Y5JbrnGr8&t=760s)** well connects on-premise networks to your BPCs, that wasn't properly set up at that time.

**[12:47](https://youtube.com/watch?v=B9Y5JbrnGr8&t=767s)** So the package were not reaching the destination.

**[12:51](https://youtube.com/watch?v=B9Y5JbrnGr8&t=771s)** So I just run that EC2 instance in a BPC for which I knew the TeleScale was able to reach directly

**[13:01](https://youtube.com/watch?v=B9Y5JbrnGr8&t=781s)** the machine and then create direct connections. So yeah, in a day or so I had that working and,

**[13:10](https://youtube.com/watch?v=B9Y5JbrnGr8&t=790s)** a couple of things were able to just carry on with their tasks and running their analysis

**[13:15](https://youtube.com/watch?v=B9Y5JbrnGr8&t=795s)** and accessing the RDS service. So yeah, a small victory. But a couple of observations about that

**[13:22](https://youtube.com/watch?v=B9Y5JbrnGr8&t=802s)** little project. The first one is that I wouldn't have been able to do this with

**[13:27](https://youtube.com/watch?v=B9Y5JbrnGr8&t=807s)** so quickly, definitely, without TeleScale. I will have to open tickets and get the right

**[13:34](https://youtube.com/watch?v=B9Y5JbrnGr8&t=814s)** connection set up so it wouldn't have been possible. And then the other one made me more

**[13:38](https://youtube.com/watch?v=B9Y5JbrnGr8&t=818s)** interesting is that I built this like very quickly. It was super simple and maybe it was a quick

**[13:45](https://youtube.com/watch?v=B9Y5JbrnGr8&t=825s)** hack. It definitely was only running for a week or something. But it didn't feel it was a hack

**[13:51](https://youtube.com/watch?v=B9Y5JbrnGr8&t=831s)** and that was because TeleScale hides really well these tedious networking operational tasks

**[13:58](https://youtube.com/watch?v=B9Y5JbrnGr8&t=838s)** that are very prone to errors. And then the other thing which is a theme of this talk is that

**[14:05](https://youtube.com/watch?v=B9Y5JbrnGr8&t=845s)** TeleScale is just extremely robust. I know if unless there's like a physical failure in the

**[14:13](https://youtube.com/watch?v=B9Y5JbrnGr8&t=853s)** network, that guy is going to keep like just providing connectivity. So it's super, super cool.

**[14:20](https://youtube.com/watch?v=B9Y5JbrnGr8&t=860s)** So what are we now? After this little success, I got approval to get our tone net

**[14:29](https://youtube.com/watch?v=B9Y5JbrnGr8&t=869s)** and now the team of about like 5-10 people is using TeleScale for just accessing the services

**[14:38](https://youtube.com/watch?v=B9Y5JbrnGr8&t=878s)** that we built, infrastructure that we built way easy in a much easier manner. And yeah,

**[14:45](https://youtube.com/watch?v=B9Y5JbrnGr8&t=885s)** just basically replace the also the all VPN. So I hope that in the near future we can have more

**[14:53](https://youtube.com/watch?v=B9Y5JbrnGr8&t=893s)** teams that have using having their own tone nets to just experience the same level of connectivity

**[14:59](https://youtube.com/watch?v=B9Y5JbrnGr8&t=899s)** that we do. And that may be more advanced or ambitious. But I hope that we can slowly migrate

**[15:07](https://youtube.com/watch?v=B9Y5JbrnGr8&t=907s)** the all VPN to use TeleScale for all the users. And just a final thought,

**[15:16](https://youtube.com/watch?v=B9Y5JbrnGr8&t=916s)** in that transition between running my own telnet and then running a telnet for like 10 people,

**[15:27](https://youtube.com/watch?v=B9Y5JbrnGr8&t=927s)** that's an interesting transition. And I definitely learned many things there. So hopefully

**[15:32](https://youtube.com/watch?v=B9Y5JbrnGr8&t=932s)** next time I can talk a little bit more about that. But yeah, that's everything I have for you

**[15:37](https://youtube.com/watch?v=B9Y5JbrnGr8&t=937s)** today. Thank you so much.

---

*Automatically generated transcript. May contain errors.*
