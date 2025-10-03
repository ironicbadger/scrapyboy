---
video_id: "7EoCa9HP9Bc"
title: "Tailscale Webinar - NAT Traversal explained with Lee Briggs"
description: "Tailscale will navigate all kinds of networks on your behalf, but sometimes it needs to use our DERP servers to traverse those trickier networks. Lee covers the basics of what NAT is, and why it can b..."
channel_name: "Tailscale"
channel_id: "UCcdv38QxPjSMqbt5ffLhJLA"
published_at: "2024-09-20"
duration_seconds: 4327
youtube_url: "https://www.youtube.com/watch?v=7EoCa9HP9Bc"
thumbnail_url: "https://i.ytimg.com/vi/7EoCa9HP9Bc/maxresdefault.jpg"

# Transcription metadata
transcribed_at: "2025-10-03T16:05:19.357125"
transcription_method: "cpu"
model_used: "base"
language: "en"
word_count: 12963
transcription_time_seconds: 130.4
---

# Tailscale Webinar - NAT Traversal explained with Lee Briggs

**[00:00](https://youtube.com/watch?v=7EoCa9HP9Bc&t=0s)** Excellent. So I'm just kind of ad libbing here. If you join one of my webinars before, you'll realize that I just talk for an hour. I don't like these things to be too stuffy and too professional. I'm going to be my authentic self. And so hopefully that makes it a little bit more easy to follow. I make it two minutes past. I think it's just before on the official clock. So let's get going. I always like to start with some housekeeping. The number one rule of webinars is that there is a live chat here. Please be respectful in the live chat. Remember there's a human being on the other side.

**[00:30](https://youtube.com/watch?v=7EoCa9HP9Bc&t=30s)** I'm excited for conversation. I am a human being. Please be kind to me. This webinar took a very long time to put together. I put a lot of work in here. So please be respectful of my time and respectful of those people in the chat. This is a live webinar. It's very content heavy. But at the end, I'm going to do a demo. I am at the behest of the demo gods. I practiced this a hundred times. It worked every single time when I did the practice. If it goes wrong, I'll laugh about it. And we'll move on with our lives. But I am at the behest of the demo gods. So please be patient. I like to troubleshoot things. If you're

**[01:00](https://youtube.com/watch?v=7EoCa9HP9Bc&t=60s)** going to go wrong, live on the call. So I'm not going to hand wave away and try and pretend everything's okay. I'll tell you what's happening. What I think is happening. If there's a problem, I can set a practice to the lot. We'll see how that goes. The final, one of the final things I want to cover in the housekeeping section is that this webinar covers an extremely complicated topic. I have done everything that I can to fit the content of this into a one hour slot. There's a lot of words. I organized over the way I was

**[01:30](https://youtube.com/watch?v=7EoCa9HP9Bc&t=90s)** going to present this information to you. Got to remember, we've got people live in the webinar. We've got people who are going to watch this on YouTube. We've got people who are going to be able to watch this without listening. So I've really tried to put this together in a way that is accessible to every single type of person who wants to learn. That said, there's a lot of words and a lot more slides than I wanted there to be. So I do apologize for that. But hopefully I'll try and keep it entertaining by cracking a few silly jokes every now and again, terrible jokes. I do ask if you have questions while we've got these complicated topics.

**[02:00](https://youtube.com/watch?v=7EoCa9HP9Bc&t=120s)** Please try and keep them in the Q&A section. There is a Q&A section in Zoom. I will try and get to them if I have time. If you just post them in the chat, it's going to get scroll past. I'm never going to see it. I have my wonderful colleague, Tim, who's mining the chat. He will try and can remind you to put it in the Q&A section. But if you don't put it in there, I'm very unlikely to get to it. So please try and remember to use the Q&A section. And then finally, I am a fallible human. I have learned about this topic in my time. It tells me that I'm not going to be able to do it.

**[02:30](https://youtube.com/watch?v=7EoCa9HP9Bc&t=150s)** There is a Skill and as a till skill user, there are people at TillSkill who are way smarter than I can ever hope to be, who are high about the opportunity to learn from and putting this webinar together. That said, this is my understanding of it. So if I get something wrong, tell me, but please do it politely. I am putting this together to try and solve what I think is the most commonly asked question for us in the solutions engineering team, so I put my understanding it together. Please remember that. The agenda for today.

**[03:01](https://youtube.com/watch?v=7EoCa9HP9Bc&t=181s)** So we're going to talk about what NAT is and why do we need to know about it when it comes to

**[03:05](https://youtube.com/watch?v=7EoCa9HP9Bc&t=185s)** tail scale. Then we're going to learn about the different types of NAT through the lens of tail

**[03:08](https://youtube.com/watch?v=7EoCa9HP9Bc&t=188s)** scales connectivity, we're going to learn how you at home can identify them, and then we're going

**[03:13](https://youtube.com/watch?v=7EoCa9HP9Bc&t=193s)** to define the results of these different NAT types. And then finally, after nerd sniping some of

**[03:20](https://youtube.com/watch?v=7EoCa9HP9Bc&t=200s)** our engineers and also worrying some of our engineers by telling you all about this new special trick,

**[03:25](https://youtube.com/watch?v=7EoCa9HP9Bc&t=205s)** I'm going to tell you about a new special trick at the end. I will be having a huge

**[03:30](https://youtube.com/watch?v=7EoCa9HP9Bc&t=210s)** asterisk against that particular special trick, but stay until the end if you're having trouble

**[03:36](https://youtube.com/watch?v=7EoCa9HP9Bc&t=216s)** with connectivity. I'm going to bore you with a bunch of information. If you stay till the end,

**[03:39](https://youtube.com/watch?v=7EoCa9HP9Bc&t=219s)** I'm going to help you be in a situation where you might be able to get kind of direct connections,

**[03:44](https://youtube.com/watch?v=7EoCa9HP9Bc&t=224s)** where you didn't be where you weren't previously able to get direct connections. So if there was

**[03:48](https://youtube.com/watch?v=7EoCa9HP9Bc&t=228s)** ever an incentive to stay for an hour and listen to me drone on, I think that might be it.

**[03:53](https://youtube.com/watch?v=7EoCa9HP9Bc&t=233s)** Quick introduction for those who haven't met me before on the tail scale webinar. I'm a solutions

**[03:57](https://youtube.com/watch?v=7EoCa9HP9Bc&t=237s)** engineer here at tail scale. I was previously a solutions engineer at another company, and then I

**[04:02](https://youtube.com/watch?v=7EoCa9HP9Bc&t=242s)** spent most of my career in DevOps engineering, systems administration, platform engineering,

**[04:07](https://youtube.com/watch?v=7EoCa9HP9Bc&t=247s)** the name changes every every two years. I had all of those titles. Mainly my responsibility was

**[04:12](https://youtube.com/watch?v=7EoCa9HP9Bc&t=252s)** building infrastructure for a large company, whether it about being in the cloud or the data center.

**[04:17](https://youtube.com/watch?v=7EoCa9HP9Bc&t=257s)** That said, I have unfortunately dealt with all of the topics that we've dealt we're talking to talk

**[04:21](https://youtube.com/watch?v=7EoCa9HP9Bc&t=261s)** about here. I'm far more than I would have wanted to. There is some code that's associated with this

**[04:26](https://youtube.com/watch?v=7EoCa9HP9Bc&t=266s)** that I have on my GitHub account. I chose my GitHub name when I was 13. Please don't laugh at me for

**[04:31](https://youtube.com/watch?v=7EoCa9HP9Bc&t=271s)** it. Then I have a website which I occasionally write on Lebriggs.co.uk. I prove this you're written

**[04:37](https://youtube.com/watch?v=7EoCa9HP9Bc&t=277s)** about tail scale. I write my blog post on my personal blog because some of the way that I communicate

**[04:42](https://youtube.com/watch?v=7EoCa9HP9Bc&t=282s)** with written languages is not necessarily tail scale corporate friendly. If you want to read about

**[04:48](https://youtube.com/watch?v=7EoCa9HP9Bc&t=288s)** some of these topics, please also please visit my blog. That's my shameless picture about myself.

**[04:52](https://youtube.com/watch?v=7EoCa9HP9Bc&t=292s)** Let's get into the topic. What is net net network address translation? What is it? Why do we care

**[05:00](https://youtube.com/watch?v=7EoCa9HP9Bc&t=300s)** about it? Well, the first thing that I realized when I started learning about this topic many

**[05:05](https://youtube.com/watch?v=7EoCa9HP9Bc&t=305s)** moons ago is that the whole reason that exists is because people did not realize when they

**[05:10](https://youtube.com/watch?v=7EoCa9HP9Bc&t=310s)** architected the internet that there was going to be as popular as it was. They came up with an

**[05:15](https://youtube.com/watch?v=7EoCa9HP9Bc&t=315s)** addressing system IPv4 and they thought that many addresses is good plenty of addresses when

**[05:21](https://youtube.com/watch?v=7EoCa9HP9Bc&t=321s)** never going to run out of the addresses like with this huge number and we've realized pretty quickly

**[05:27](https://youtube.com/watch?v=7EoCa9HP9Bc&t=327s)** that with your mobile phone, your laptop, everyone's house, all of those different things being

**[05:34](https://youtube.com/watch?v=7EoCa9HP9Bc&t=334s)** connected to the internet. We've run out of IPv4 addresses multiple times and as a result that

**[05:42](https://youtube.com/watch?v=7EoCa9HP9Bc&t=342s)** has presented a problem for anybody who wants to build complicated large networks.

**[05:48](https://youtube.com/watch?v=7EoCa9HP9Bc&t=348s)** So the high level idea of what that looks like in reality is at the top here you see this diagram

**[05:55](https://youtube.com/watch?v=7EoCa9HP9Bc&t=355s)** where if every single device is on the public internet directly and gets a public internet address

**[06:02](https://youtube.com/watch?v=7EoCa9HP9Bc&t=362s)** that we're going to run out really, really quickly of addresses that we can actually hand out to

**[06:06](https://youtube.com/watch?v=7EoCa9HP9Bc&t=366s)** those devices which means we end up with an internet where there's a queueing system and as a

**[06:10](https://youtube.com/watch?v=7EoCa9HP9Bc&t=370s)** British person I would love a queueing system for the internet because it would also mean that we

**[06:14](https://youtube.com/watch?v=7EoCa9HP9Bc&t=374s)** wouldn't have so much nonsense written on the internet. However, that really isn't a reasonable way

**[06:19](https://youtube.com/watch?v=7EoCa9HP9Bc&t=379s)** of doing things. So what people did and what the architects have not did is they realized that you

**[06:25](https://youtube.com/watch?v=7EoCa9HP9Bc&t=385s)** can actually create a private network behind a public router that has a public address and as a result

**[06:32](https://youtube.com/watch?v=7EoCa9HP9Bc&t=392s)** you can then use network address translation to basically pretend that that device behind this

**[06:40](https://youtube.com/watch?v=7EoCa9HP9Bc&t=400s)** router here is on the public internet and as a result that meant that we had an explosion of

**[06:46](https://youtube.com/watch?v=7EoCa9HP9Bc&t=406s)** devices behind these public IPs behind these routers. Your home router almost certainly is an

**[06:53](https://youtube.com/watch?v=7EoCa9HP9Bc&t=413s)** app device. It almost certainly has a public address which you get from your internet service provider

**[06:59](https://youtube.com/watch?v=7EoCa9HP9Bc&t=419s)** and then you have probably a 192.168.0.1 style address for all of the things that are connected to

**[07:06](https://youtube.com/watch?v=7EoCa9HP9Bc&t=426s)** your Wi-Fi to the public internet when those things reach out to go to a website. What the website

**[07:12](https://youtube.com/watch?v=7EoCa9HP9Bc&t=432s)** sees is the routers public IP. That is the basic definition of what NAT is doing for you. It's giving

**[07:19](https://youtube.com/watch?v=7EoCa9HP9Bc&t=439s)** you the capability of having lots and lots of devices behind a public IP being able to access the

**[07:24](https://youtube.com/watch?v=7EoCa9HP9Bc&t=444s)** public internet. So when we talk about VPNs when it comes to NAT that the VPN itself requires public

**[07:32](https://youtube.com/watch?v=7EoCa9HP9Bc&t=452s)** connectivity so that the client can connect to it. The NAT device that's in front of all these

**[07:38](https://youtube.com/watch?v=7EoCa9HP9Bc&t=458s)** addresses that are in your private network is actually a bit of a problem for a VPN unless you put

**[07:44](https://youtube.com/watch?v=7EoCa9HP9Bc&t=464s)** the VPN directly on the public internet because the public IP doesn't exactly might not correspond to

**[07:49](https://youtube.com/watch?v=7EoCa9HP9Bc&t=469s)** where the VPN actually lives. It might be on a device that's behind the NAT device. Sometimes you

**[07:56](https://youtube.com/watch?v=7EoCa9HP9Bc&t=476s)** put the VPN on your router but a lot of times you actually want that VPN to behind the NAT device

**[08:02](https://youtube.com/watch?v=7EoCa9HP9Bc&t=482s)** and it needs to present itself as the actual public IP that the router has and it looks a little

**[08:10](https://youtube.com/watch?v=7EoCa9HP9Bc&t=490s)** bit like this. The solution here is that you use a port forward or something along those lines

**[08:15](https://youtube.com/watch?v=7EoCa9HP9Bc&t=495s)** where the client connects to the router on a specific port. The router opens that port, let's say

**[08:21](https://youtube.com/watch?v=7EoCa9HP9Bc&t=501s)** 5.432 which is the Postgres port and it's just off the top of my head. The client connects to

**[08:27](https://youtube.com/watch?v=7EoCa9HP9Bc&t=507s)** the router, the router forwards that port, any requests to that port through to the VPN server and

**[08:34](https://youtube.com/watch?v=7EoCa9HP9Bc&t=514s)** you get your direct connection and that means you can run a VPN behind a NAT device. That's great.

**[08:39](https://youtube.com/watch?v=7EoCa9HP9Bc&t=519s)** Excellent. We've done that for a long, long time. I have run multiple VPNs behind routers like that

**[08:45](https://youtube.com/watch?v=7EoCa9HP9Bc&t=525s)** and it generally will sort of work but it will probably suck. It will be a part experience. People

**[08:50](https://youtube.com/watch?v=7EoCa9HP9Bc&t=530s)** will not like it. It's generally the reason why people come to us at tail scale. However, and this

**[08:56](https://youtube.com/watch?v=7EoCa9HP9Bc&t=536s)** is a lovely, wordy slide for everyone, tail scale doesn't work in the same way as other VPNs because

**[09:03](https://youtube.com/watch?v=7EoCa9HP9Bc&t=543s)** tail scale lets you run lots and lots of endpoints behind that NAT. You might run a subnet router as a

**[09:09](https://youtube.com/watch?v=7EoCa9HP9Bc&t=549s)** single device which lots of people do as a successful strategy but if you want to get the full power

**[09:14](https://youtube.com/watch?v=7EoCa9HP9Bc&t=554s)** of tail scale, you probably want to run lots of tail scale devices behind that NAT device and in

**[09:19](https://youtube.com/watch?v=7EoCa9HP9Bc&t=559s)** that case a simple port forward is not going to be enough and it's not going to be manageable

**[09:24](https://youtube.com/watch?v=7EoCa9HP9Bc&t=564s)** because it means let's say you have a NAT device and 100 tail scale clients behind it,

**[09:28](https://youtube.com/watch?v=7EoCa9HP9Bc&t=568s)** you now have to do 100 port forwards and that's a big overhead and it's painful and infuriating

**[09:33](https://youtube.com/watch?v=7EoCa9HP9Bc&t=573s)** to those people who are using it. So tail scale need does something that no other VPN that I'm aware

**[09:41](https://youtube.com/watch?v=7EoCa9HP9Bc&t=581s)** of does for you. It actually manages the NAT traversal and uses a bunch of different protocols

**[09:49](https://youtube.com/watch?v=7EoCa9HP9Bc&t=589s)** like the stun protocol and things like port mapping protocols like UP&P and NAT P&P and PCP

**[09:56](https://youtube.com/watch?v=7EoCa9HP9Bc&t=596s)** and it actually maps those ports for you. Now you're probably familiar with UP&P because it's

**[10:02](https://youtube.com/watch?v=7EoCa9HP9Bc&t=602s)** probably in your home router and it's used for things like your games consoles, we're able to connect

**[10:06](https://youtube.com/watch?v=7EoCa9HP9Bc&t=606s)** to the internet and so you can get things like direct connections with other people that you want

**[10:09](https://youtube.com/watch?v=7EoCa9HP9Bc&t=609s)** to shoot on college duty. Tail scale uses all of these established technologies to be able to create

**[10:16](https://youtube.com/watch?v=7EoCa9HP9Bc&t=616s)** direct connections and connections between two clients behind a NAT device. It handles all of this

**[10:22](https://youtube.com/watch?v=7EoCa9HP9Bc&t=622s)** for you and I think this is something that I personally, when I adopted tail scale a long time ago,

**[10:26](https://youtube.com/watch?v=7EoCa9HP9Bc&t=626s)** it's like wow this is like magic, I don't have to do any setup, I don't have to do any configuration,

**[10:31](https://youtube.com/watch?v=7EoCa9HP9Bc&t=631s)** I just install tail scale and it's able to connect. This is amazing. It also means that tail scale

**[10:36](https://youtube.com/watch?v=7EoCa9HP9Bc&t=636s)** works without needing a public IP address of its own. So with other VPNs you need to like put in

**[10:42](https://youtube.com/watch?v=7EoCa9HP9Bc&t=642s)** the actual IP address that you want to use to connect in the client configuration. You don't

**[10:47](https://youtube.com/watch?v=7EoCa9HP9Bc&t=647s)** need to do that with tail scale because tail scale advertises those addresses and figures out the

**[10:51](https://youtube.com/watch?v=7EoCa9HP9Bc&t=651s)** connectivity path for you. It uses the ice protocol to do that. So my high level whip together diagram

**[11:00](https://youtube.com/watch?v=7EoCa9HP9Bc&t=660s)** shows a little bit like this. So you have lots and lots of devices behind your router, you have a one

**[11:04](https://youtube.com/watch?v=7EoCa9HP9Bc&t=664s)** that's outside of the router, the UP&P and the natural, sorry, the natural virtual technology that

**[11:11](https://youtube.com/watch?v=7EoCa9HP9Bc&t=671s)** you have at your disposal manages all of this for you. However, NAT devices are all often also

**[11:21](https://youtube.com/watch?v=7EoCa9HP9Bc&t=681s)** files. And that means that you can create outbound connections pretty easily using all those

**[11:27](https://youtube.com/watch?v=7EoCa9HP9Bc&t=687s)** port backing protocols, but you cannot create inbound connections very easily. And obviously for

**[11:32](https://youtube.com/watch?v=7EoCa9HP9Bc&t=692s)** tail scale to be able to communicate with each other, you need outbound and inbound connectivity

**[11:37](https://youtube.com/watch?v=7EoCa9HP9Bc&t=697s)** in order to make that happen. So if you think about how that works in your home router or something

**[11:41](https://youtube.com/watch?v=7EoCa9HP9Bc&t=701s)** in your house, you put tail scale behind your home router, it can use one of the port mapping

**[11:47](https://youtube.com/watch?v=7EoCa9HP9Bc&t=707s)** protocols like UP&P to create an outbound connection. How does the tail scale device on the other side

**[11:52](https://youtube.com/watch?v=7EoCa9HP9Bc&t=712s)** on the internet actually communicate back to the tail scale client, and the NAT device, especially when

**[11:57](https://youtube.com/watch?v=7EoCa9HP9Bc&t=717s)** you consider it to firewall? Well, it's magic. I'm going to start by saying that. It's incredibly

**[12:03](https://youtube.com/watch?v=7EoCa9HP9Bc&t=723s)** sophisticated, but what it does is it sends an outbound packet. And then when the NAT device says,

**[12:09](https://youtube.com/watch?v=7EoCa9HP9Bc&t=729s)** okay, you send an outbound packet, I'll also allow return traffic back through it,

**[12:12](https://youtube.com/watch?v=7EoCa9HP9Bc&t=732s)** tail scale leverages that to be able to do this direct communication. So there is a very

**[12:19](https://youtube.com/watch?v=7EoCa9HP9Bc&t=739s)** difficultly drawn diagram in mermaid here, which sort of explains this. You have a NAT device here

**[12:28](https://youtube.com/watch?v=7EoCa9HP9Bc&t=748s)** between a NAT device and a tail scale device here behind another NAT device, the NAT, the first

**[12:36](https://youtube.com/watch?v=7EoCa9HP9Bc&t=756s)** client PA sends a request to our stun server and says, I have these addresses, and the device behind

**[12:44](https://youtube.com/watch?v=7EoCa9HP9Bc&t=764s)** this NAT also does the same thing. So now the two tail scale devices know about each other. They know

**[12:50](https://youtube.com/watch?v=7EoCa9HP9Bc&t=770s)** what the IP address and port they're allowed to use is. As a result, because they've sent those

**[12:55](https://youtube.com/watch?v=7EoCa9HP9Bc&t=775s)** outbound packets, they can also receive inbound packets through that same address. So they send

**[12:59](https://youtube.com/watch?v=7EoCa9HP9Bc&t=779s)** UDP packets on both sides and says, hey, okay, have you received the packet? And as a result,

**[13:04](https://youtube.com/watch?v=7EoCa9HP9Bc&t=784s)** you get direct communication. I have massively hand-waved over a very, very complicated topic here.

**[13:11](https://youtube.com/watch?v=7EoCa9HP9Bc&t=791s)** There is an entire magnum opus written by my absolutely wonderful colleague and somebody who's

**[13:17](https://youtube.com/watch?v=7EoCa9HP9Bc&t=797s)** much more than me, David Anderson, who talks about this in great depth. It's a credible piece of work.

**[13:25](https://youtube.com/watch?v=7EoCa9HP9Bc&t=805s)** I personally believe it is the finest technical blog that has ever been written, which I think is a

**[13:29](https://youtube.com/watch?v=7EoCa9HP9Bc&t=809s)** big statement, but it's my favorite technical blog and I learned so much about this. However,

**[13:36](https://youtube.com/watch?v=7EoCa9HP9Bc&t=816s)** I'm glossing over a very, very long article because I wanted you to have the foundations of how

**[13:41](https://youtube.com/watch?v=7EoCa9HP9Bc&t=821s)** this works so that you can understand all the stuff that I'm going to talk about next. If we want

**[13:46](https://youtube.com/watch?v=7EoCa9HP9Bc&t=826s)** to have an entire webinar about how natural virtual works specifically, I could do a full hour on

**[13:53](https://youtube.com/watch?v=7EoCa9HP9Bc&t=833s)** it, but I had to condense this into about 15, 20 minutes so that we have the foundations of how it

**[13:58](https://youtube.com/watch?v=7EoCa9HP9Bc&t=838s)** works. If you want to see a full webinar on how natural virtual works completely without all the

**[14:03](https://youtube.com/watch?v=7EoCa9HP9Bc&t=843s)** other stuff that I'm going to do, please let us know in the comments we would love to hear about

**[14:06](https://youtube.com/watch?v=7EoCa9HP9Bc&t=846s)** if people are interested in the overall architecture of how natural virtual works. So now that we know

**[14:12](https://youtube.com/watch?v=7EoCa9HP9Bc&t=852s)** why we have NAT and what we need it for, we can talk a little bit about the different types of

**[14:18](https://youtube.com/watch?v=7EoCa9HP9Bc&t=858s)** NAT that you have. Just taking a quick refreshment break there. So the other thing that I really

**[14:26](https://youtube.com/watch?v=7EoCa9HP9Bc&t=866s)** started to realize as I started to investigate into this as a tailskip, before I was a tailskip

**[14:30](https://youtube.com/watch?v=7EoCa9HP9Bc&t=870s)** employee is the terminology that was traditionally used around NAT was really confusing. We have

**[14:37](https://youtube.com/watch?v=7EoCa9HP9Bc&t=877s)** this kind of full cone and then restricted cone and port restricted cone. As I'm learning about

**[14:42](https://youtube.com/watch?v=7EoCa9HP9Bc&t=882s)** NAT terminology, I'm like, is this one of those things they put on dogs to stop them chewing

**[14:46](https://youtube.com/watch?v=7EoCa9HP9Bc&t=886s)** themselves? I don't know, that's the only real time that I use the terminology cone. So in RSE

**[14:55](https://youtube.com/watch?v=7EoCa9HP9Bc&t=895s)** 4787 some new terminology came along which certainly made a lot more sense to me. They define the

**[15:02](https://youtube.com/watch?v=7EoCa9HP9Bc&t=902s)** two NAT types as endpoint dependent and endpoint independent mapping. And these two terms started

**[15:08](https://youtube.com/watch?v=7EoCa9HP9Bc&t=908s)** to actually really form the sense of what is actually happening for me. And in the tailskip SE team

**[15:15](https://youtube.com/watch?v=7EoCa9HP9Bc&t=915s)** and sometimes in the wider tailskip team, we've kind of used two terminologies to be able to

**[15:22](https://youtube.com/watch?v=7EoCa9HP9Bc&t=922s)** separate this endpoint, depending on endpoint independent mapping. We have the term easy NAT

**[15:27](https://youtube.com/watch?v=7EoCa9HP9Bc&t=927s)** and then we have the term hard NAT. And this is a way, this is like a broad umbrella to encapsulate

**[15:33](https://youtube.com/watch?v=7EoCa9HP9Bc&t=933s)** very, very complicated topics. If you think of them as buckets, you can put different NATs in

**[15:38](https://youtube.com/watch?v=7EoCa9HP9Bc&t=938s)** these different types of buckets. It's not a catch all term that is always correct, but generally you

**[15:44](https://youtube.com/watch?v=7EoCa9HP9Bc&t=944s)** can separate the two NAT types into easy and hard. So of course, if you have a NAT that is easy

**[15:52](https://youtube.com/watch?v=7EoCa9HP9Bc&t=952s)** and a NAT that is hard, there's also a situation where you have absolutely no NAT. And that is,

**[15:57](https://youtube.com/watch?v=7EoCa9HP9Bc&t=957s)** if you have kind of, if I've made any sense so far, you may realize that no NAT is exactly what it

**[16:03](https://youtube.com/watch?v=7EoCa9HP9Bc&t=963s)** sounds like. There is no network address translation device in front of the actual clients that

**[16:11](https://youtube.com/watch?v=7EoCa9HP9Bc&t=971s)** are behind it. Your tailskill device has an actual public IP directly attached to it.

**[16:19](https://youtube.com/watch?v=7EoCa9HP9Bc&t=979s)** When we talk about no NAT on the tailskill side, we add a caveat here that in order for us to

**[16:25](https://youtube.com/watch?v=7EoCa9HP9Bc&t=985s)** consider a device that is no NAT, we also need to be able to get direct GP access to the tailskill

**[16:32](https://youtube.com/watch?v=7EoCa9HP9Bc&t=992s)** devices port. And the reason for that will become clear when we talk about easy NAT. But the first

**[16:38](https://youtube.com/watch?v=7EoCa9HP9Bc&t=998s)** term that you really need to take away from the monologue that I've given so far is that no NAT

**[16:44](https://youtube.com/watch?v=7EoCa9HP9Bc&t=1004s)** means that there is a device that has a public IP address directly. And it also has inbound UDP

**[16:51](https://youtube.com/watch?v=7EoCa9HP9Bc&t=1011s)** access. So you don't need any NAT at this point. You don't need to do any public IP mapping or

**[16:58](https://youtube.com/watch?v=7EoCa9HP9Bc&t=1018s)** anything around those lines. You have direct UDP access to the public address. Then we talk a

**[17:04](https://youtube.com/watch?v=7EoCa9HP9Bc&t=1024s)** little bit about easy NAT. And this broadly color correlates to endpoint independent mapping

**[17:10](https://youtube.com/watch?v=7EoCa9HP9Bc&t=1030s)** in the RFC we talked about earlier. So an easy NAT is generally something that you would see in

**[17:16](https://youtube.com/watch?v=7EoCa9HP9Bc&t=1036s)** your home or your smaller networks or your less kind of enterprising networks is generally where I

**[17:24](https://youtube.com/watch?v=7EoCa9HP9Bc&t=1044s)** see most of them. So if you're running tailskill in your organization, I'm almost sure that people

**[17:28](https://youtube.com/watch?v=7EoCa9HP9Bc&t=1048s)** are running tailskill in their home internet. Most home internet generally tends to be somewhere in

**[17:34](https://youtube.com/watch?v=7EoCa9HP9Bc&t=1054s)** the easy NAT bucket. And the reason for that is that they have home routers that have one of these

**[17:40](https://youtube.com/watch?v=7EoCa9HP9Bc&t=1060s)** port mapping protocols enabled on it. Either UP and PCP or NAT PMP. And as a result, the tailskill

**[17:48](https://youtube.com/watch?v=7EoCa9HP9Bc&t=1068s)** device is able to talk to the NAT device and say, hey, I want to open an outbound port please. Can

**[17:53](https://youtube.com/watch?v=7EoCa9HP9Bc&t=1073s)** you give me an outbound port on the NAT device? Sure, here's an outbound port for you and off you go.

**[17:58](https://youtube.com/watch?v=7EoCa9HP9Bc&t=1078s)** And then of course, tailskill can use that outbound port to be able to have inbound traffic as we

**[18:04](https://youtube.com/watch?v=7EoCa9HP9Bc&t=1084s)** already talked about. These protocols help that process. Again, we talked about this a little

**[18:09](https://youtube.com/watch?v=7EoCa9HP9Bc&t=1089s)** bit earlier. You'll generally see this use for things like games consoles when you want to create

**[18:12](https://youtube.com/watch?v=7EoCa9HP9Bc&t=1092s)** direct connections. Tailskill uses those same protocols. The thing that's really important to know

**[18:18](https://youtube.com/watch?v=7EoCa9HP9Bc&t=1098s)** about NAT is that the port opening behind the NAT device is predictable and reusable. And that means

**[18:27](https://youtube.com/watch?v=7EoCa9HP9Bc&t=1107s)** that when tailskill initiates its outbound connection, it can use the same port on the reverse side when

**[18:31](https://youtube.com/watch?v=7EoCa9HP9Bc&t=1111s)** it comes back in. And that's really important for creating these direct connections that everybody

**[18:36](https://youtube.com/watch?v=7EoCa9HP9Bc&t=1116s)** really, really wants to have. So this is a little bit of an idea. And again, it's a really complicated

**[18:42](https://youtube.com/watch?v=7EoCa9HP9Bc&t=1122s)** topic. So I've tried to get a density into something that makes sense. So you'll have a client here

**[18:47](https://youtube.com/watch?v=7EoCa9HP9Bc&t=1127s)** that's behind a NAT router. The NAT router's IP address is here. What happens is the client

**[18:51](https://youtube.com/watch?v=7EoCa9HP9Bc&t=1131s)** connects to our stun server and says, here's where I'm actually coming from. Here's where I'm

**[18:55](https://youtube.com/watch?v=7EoCa9HP9Bc&t=1135s)** originating from. And then the NAT device here says, okay, well, you're going for an outbound

**[19:00](https://youtube.com/watch?v=7EoCa9HP9Bc&t=1140s)** connection from one, two, three, four, five. I'm good to map that map that in my NAT table to port

**[19:06](https://youtube.com/watch?v=7EoCa9HP9Bc&t=1146s)** five, four, three, two, one. And it sends it off to tailskill and the stun server says, ah,

**[19:11](https://youtube.com/watch?v=7EoCa9HP9Bc&t=1151s)** you initiated a connection from this address and five, four, three, two, one. I know about that now.

**[19:17](https://youtube.com/watch?v=7EoCa9HP9Bc&t=1157s)** Thanks for letting me know. And then sends another connection to another stun server.

**[19:23](https://youtube.com/watch?v=7EoCa9HP9Bc&t=1163s)** And so it doesn't create one connection. It creates multiple outbound connections. And so

**[19:28](https://youtube.com/watch?v=7EoCa9HP9Bc&t=1168s)** again, it says, hey, I want to connect to this thing on port one, two, three, four, five. And the

**[19:32](https://youtube.com/watch?v=7EoCa9HP9Bc&t=1172s)** NAT device says, ah, you already made that connection. So I'm going to reuse it. And it says, okay,

**[19:38](https://youtube.com/watch?v=7EoCa9HP9Bc&t=1178s)** cool. Off to the stun server. And the stun server says, ah, I've seen the second connection come in.

**[19:44](https://youtube.com/watch?v=7EoCa9HP9Bc&t=1184s)** And I saw that it's originating from the same IP address and port. Therefore, I can definitely

**[19:49](https://youtube.com/watch?v=7EoCa9HP9Bc&t=1189s)** reuse that IP address and port the inbound connectivity. And as a result, we now know on the tailskill

**[19:57](https://youtube.com/watch?v=7EoCa9HP9Bc&t=1197s)** side, what type of NAT it is because you've sent those multiple connections and they've both come

**[20:01](https://youtube.com/watch?v=7EoCa9HP9Bc&t=1201s)** to this from the same IP and port to pull. We know now that, okay, this is an easy NAT and I can reuse

**[20:07](https://youtube.com/watch?v=7EoCa9HP9Bc&t=1207s)** that port to create that connection. Partnered, the bane of my existence, the thing that keeps me

**[20:14](https://youtube.com/watch?v=7EoCa9HP9Bc&t=1214s)** up at night and the thing that I talked to customers about all the time. Hardnet broadly

**[20:19](https://youtube.com/watch?v=7EoCa9HP9Bc&t=1219s)** concrete to endpoint dependent mapping. And that means that there is no mechanism that tailskill

**[20:26](https://youtube.com/watch?v=7EoCa9HP9Bc&t=1226s)** can use to be able to open an outbound port. It can send an outbound request, but it isn't able

**[20:31](https://youtube.com/watch?v=7EoCa9HP9Bc&t=1231s)** to keep an outbound port open like you can see here. And as a result, that means that when the

**[20:38](https://youtube.com/watch?v=7EoCa9HP9Bc&t=1238s)** outbound connection is created, it's got some element of port randomization happening.

**[20:45](https://youtube.com/watch?v=7EoCa9HP9Bc&t=1245s)** Now, originally, this was introduced because they wanted to have the people who design this sort of

**[20:49](https://youtube.com/watch?v=7EoCa9HP9Bc&t=1249s)** way of natting like, okay, well, if we randomize the outbound connections, that would give us two

**[20:54](https://youtube.com/watch?v=7EoCa9HP9Bc&t=1254s)** benefits. It means we can have lots and lots more clients behind the NAT device and it's also more

**[20:59](https://youtube.com/watch?v=7EoCa9HP9Bc&t=1259s)** secure. It's not really more secure. It's not really a security feature at this point. That was

**[21:06](https://youtube.com/watch?v=7EoCa9HP9Bc&t=1266s)** the original kind of like idea behind it, but I think we've seen lots of different attacks against

**[21:11](https://youtube.com/watch?v=7EoCa9HP9Bc&t=1271s)** this mechanism, which means it's not necessarily the case. It does really help with larger networks

**[21:16](https://youtube.com/watch?v=7EoCa9HP9Bc&t=1276s)** and it does really help with certain situations, especially in larger networks. We generally see this

**[21:22](https://youtube.com/watch?v=7EoCa9HP9Bc&t=1282s)** in situations like airports. We see this pretty often in things like corporate offices. We see this

**[21:28](https://youtube.com/watch?v=7EoCa9HP9Bc&t=1288s)** pretty regularly in things like like we works and all that kind of stuff. And we also see this in

**[21:34](https://youtube.com/watch?v=7EoCa9HP9Bc&t=1294s)** the cloud providers, which I'll talk about at length when we get to that section. But it's almost certainly

**[21:39](https://youtube.com/watch?v=7EoCa9HP9Bc&t=1299s)** a larger and more complicated network. And as a result, the port randomization part is important.

**[21:45](https://youtube.com/watch?v=7EoCa9HP9Bc&t=1305s)** And you can see what this looks like in my, again, very shoddly drawn and hastily drawn example.

**[21:52](https://youtube.com/watch?v=7EoCa9HP9Bc&t=1312s)** So again, we've got a client here. It sends a request to the stun server from port 12345 and the

**[21:59](https://youtube.com/watch?v=7EoCa9HP9Bc&t=1319s)** NAT device says, ah, okay, outbound connection. I'm going to map 12345 to 524321. Awesome. And then on

**[22:05](https://youtube.com/watch?v=7EoCa9HP9Bc&t=1325s)** the second request, it says, well, I never reuse connections. So this is a brand new connection.

**[22:12](https://youtube.com/watch?v=7EoCa9HP9Bc&t=1332s)** So I'm going to map 12345 to port 62,000, at which point the stun server says, hold on a minute,

**[22:18](https://youtube.com/watch?v=7EoCa9HP9Bc&t=1338s)** that came from a completely different port, but it came from the same IP address. And as a result,

**[22:25](https://youtube.com/watch?v=7EoCa9HP9Bc&t=1345s)** I now know that this is a hard NAT. And once you have a hard NAT, you can't reuse that inbound port

**[22:32](https://youtube.com/watch?v=7EoCa9HP9Bc&t=1352s)** anymore, because you don't know if it's going to always remain open. And that's a problem for

**[22:39](https://youtube.com/watch?v=7EoCa9HP9Bc&t=1359s)** creating these direct connections that tailscale would love you to have. So how do you identify

**[22:45](https://youtube.com/watch?v=7EoCa9HP9Bc&t=1365s)** these different NAT types for you as an user? How are you able to notice within tailscale

**[22:51](https://youtube.com/watch?v=7EoCa9HP9Bc&t=1371s)** whether these are the different types of NAT? Well, the first way of identifying if there is

**[22:57](https://youtube.com/watch?v=7EoCa9HP9Bc&t=1377s)** no NAT is you see something a little bit like this. So you can see in the tailscale console,

**[23:02](https://youtube.com/watch?v=7EoCa9HP9Bc&t=1382s)** you can also see this output with tailscale net check, which is a command you can run again as

**[23:07](https://youtube.com/watch?v=7EoCa9HP9Bc&t=1387s)** a tailscale device. The endpoints you can see here, we have one endpoint, which is a private address,

**[23:13](https://youtube.com/watch?v=7EoCa9HP9Bc&t=1393s)** and then a port, and then a public address and a port, right? This is telling me immediately that,

**[23:17](https://youtube.com/watch?v=7EoCa9HP9Bc&t=1397s)** okay, well, this particular endpoint is a public address. And there is no port mapping protocol involved

**[23:24](https://youtube.com/watch?v=7EoCa9HP9Bc&t=1404s)** here. And there's no varies here as well. These these three things will give me a good good idea

**[23:31](https://youtube.com/watch?v=7EoCa9HP9Bc&t=1411s)** that this particular device is known at. This is not a fallible thing. There are situations where

**[23:36](https://youtube.com/watch?v=7EoCa9HP9Bc&t=1416s)** you'll see this exact setting, and it's not actually no NAT. What's really hard for us to be able

**[23:42](https://youtube.com/watch?v=7EoCa9HP9Bc&t=1422s)** to detect on the no NAT side is whether the inbound port is open, right? And the reason for that is

**[23:48](https://youtube.com/watch?v=7EoCa9HP9Bc&t=1428s)** UDP stateless. You send a request to this IP address and port via UDP packet. And you know, we don't

**[23:57](https://youtube.com/watch?v=7EoCa9HP9Bc&t=1437s)** necessarily know if it's been received because it's a fire and forget protocol. You send that

**[24:02](https://youtube.com/watch?v=7EoCa9HP9Bc&t=1442s)** that's packets and you're off to the races. You can definitely tell when you do the connection

**[24:06](https://youtube.com/watch?v=7EoCa9HP9Bc&t=1446s)** between two different tailscale devices, but you cannot tell directly from here whether this is

**[24:12](https://youtube.com/watch?v=7EoCa9HP9Bc&t=1452s)** something that's known at, but this is a pretty good representation of being in a no NAT situation.

**[24:18](https://youtube.com/watch?v=7EoCa9HP9Bc&t=1458s)** How about easy NAT? Well, easy NAT usually is really easy to identify because one of these

**[24:24](https://youtube.com/watch?v=7EoCa9HP9Bc&t=1464s)** poor mapping protocols is enabled. So you can see on this easy NAT device, I have UPNP enabled.

**[24:30](https://youtube.com/watch?v=7EoCa9HP9Bc&t=1470s)** I didn't notice a quick question in the chat that UPNP is a potential security race. What is

**[24:36](https://youtube.com/watch?v=7EoCa9HP9Bc&t=1476s)** tailscale behavior when this port mapping program is a disabled on the round? The answer to that is

**[24:40](https://youtube.com/watch?v=7EoCa9HP9Bc&t=1480s)** you get hard NAT. So hopefully that answers the question Kevin. We sadly on the tailscale side are

**[24:47](https://youtube.com/watch?v=7EoCa9HP9Bc&t=1487s)** not able to come into your houses and fix your UPNP usage. So you know, it's definitely not

**[24:55](https://youtube.com/watch?v=7EoCa9HP9Bc&t=1495s)** something that we can do. It would be great if we could because we could give you all direct

**[24:59](https://youtube.com/watch?v=7EoCa9HP9Bc&t=1499s)** connections, but I think that's probably a little bit too much work for us. So as a result,

**[25:04](https://youtube.com/watch?v=7EoCa9HP9Bc&t=1504s)** for easy NAT, you'll definitely see one of these protocols. Despite UNP being a huge security

**[25:10](https://youtube.com/watch?v=7EoCa9HP9Bc&t=1510s)** risk, it is generally installed in lots and lots of places. That proliferated before we had

**[25:15](https://youtube.com/watch?v=7EoCa9HP9Bc&t=1515s)** tailscale helping you make the connections really easy. So if it's there, we will use it.

**[25:22](https://youtube.com/watch?v=7EoCa9HP9Bc&t=1522s)** In terms of the security consideration there, it's always worth remembering that to

**[25:25](https://youtube.com/watch?v=7EoCa9HP9Bc&t=1525s)** why God does the underlying encryption protocol can protect you from these security risks in terms

**[25:29](https://youtube.com/watch?v=7EoCa9HP9Bc&t=1529s)** of transfer data transfer. So you know, we will use UPNP if it is available for us for an easy

**[25:36](https://youtube.com/watch?v=7EoCa9HP9Bc&t=1536s)** NAT connection. And then the final one, which I think is what most people really care about in this

**[25:41](https://youtube.com/watch?v=7EoCa9HP9Bc&t=1541s)** conversation is hard NAT. How do you identify whether a device is got a hard NAT? Well, the answer

**[25:50](https://youtube.com/watch?v=7EoCa9HP9Bc&t=1550s)** here is the most important indicator here is this varies is yes. And what that is saying is that

**[25:56](https://youtube.com/watch?v=7EoCa9HP9Bc&t=1556s)** every single time we send a request to a stun server, you can see this here, right? Like this,

**[26:01](https://youtube.com/watch?v=7EoCa9HP9Bc&t=1561s)** this device is sent, these address like sent request to our stun servers from this internet address,

**[26:06](https://youtube.com/watch?v=7EoCa9HP9Bc&t=1566s)** this 52.41.2.13 address. And every single time that stun servers receive the response,

**[26:13](https://youtube.com/watch?v=7EoCa9HP9Bc&t=1573s)** it's actually got a different port to pull. So the first one, it was using 416.41 because that was

**[26:18](https://youtube.com/watch?v=7EoCa9HP9Bc&t=1578s)** a first request. And then it sent a subsequent request and it got it from 424.06. Well, now we know

**[26:24](https://youtube.com/watch?v=7EoCa9HP9Bc&t=1584s)** we're in a hard now. And when this happens, we set varies equals yes. So these are how you're

**[26:30](https://youtube.com/watch?v=7EoCa9HP9Bc&t=1590s)** able to identify pretty quickly when what type of NAT your particular device is. Of course,

**[26:37](https://youtube.com/watch?v=7EoCa9HP9Bc&t=1597s)** as with everything in life, there are caveats. We talked a little bit about easy NAT being able to

**[26:44](https://youtube.com/watch?v=7EoCa9HP9Bc&t=1604s)** use port mapping protocols. And we're talking really in broad strokes here about outbound connectivity.

**[26:50](https://youtube.com/watch?v=7EoCa9HP9Bc&t=1610s)** What is particularly important is that if you have something like an AWS security group or a

**[26:55](https://youtube.com/watch?v=7EoCa9HP9Bc&t=1615s)** firewall in front of your device on the NAT side, like on the NAT device side, where it can send

**[27:01](https://youtube.com/watch?v=7EoCa9HP9Bc&t=1621s)** an outbound packet, but it can't send an inbound packet easily. It kind of behaves like easy NAT.

**[27:08](https://youtube.com/watch?v=7EoCa9HP9Bc&t=1628s)** And as a result, you are in a situation where you have an easy NAT situation. It's also worth

**[27:15](https://youtube.com/watch?v=7EoCa9HP9Bc&t=1635s)** remembering that like this public IP that you see here, and I'll go all the way back to my known app.

**[27:20](https://youtube.com/watch?v=7EoCa9HP9Bc&t=1640s)** So this public IP address here, it might be the case if you log into this tail scale client and

**[27:25](https://youtube.com/watch?v=7EoCa9HP9Bc&t=1645s)** look for the IP address, you don't actually see it there because it's not necessarily attached

**[27:30](https://youtube.com/watch?v=7EoCa9HP9Bc&t=1650s)** directly to the device in the sense of it's got an interface on the device with this address on it.

**[27:35](https://youtube.com/watch?v=7EoCa9HP9Bc&t=1655s)** This is particularly case in cloud providers, for example, AWS, AWS, where you can attach an

**[27:40](https://youtube.com/watch?v=7EoCa9HP9Bc&t=1660s)** elastic IP to a device. It still has a public address though, and it's still addressable on there.

**[27:46](https://youtube.com/watch?v=7EoCa9HP9Bc&t=1666s)** So you might not be able to look at the endpoints table that you see the outbound address and see

**[27:51](https://youtube.com/watch?v=7EoCa9HP9Bc&t=1671s)** directly the operating system, but it still has a public IP attached directly to it.

**[27:55](https://youtube.com/watch?v=7EoCa9HP9Bc&t=1675s)** And then the final thing is we talked a little bit about the ISE protocol earlier,

**[27:59](https://youtube.com/watch?v=7EoCa9HP9Bc&t=1679s)** networks change a lot. And what I mean by that is you disconnect from the Wi-Fi, you reconnect

**[28:04](https://youtube.com/watch?v=7EoCa9HP9Bc&t=1684s)** to the Wi-Fi, you move to a different part of the building, and you get room to a new access point,

**[28:10](https://youtube.com/watch?v=7EoCa9HP9Bc&t=1690s)** tail scale, when you do that, we'll renegotiate the connection to other peers and the stone servers.

**[28:18](https://youtube.com/watch?v=7EoCa9HP9Bc&t=1698s)** So while you might have an easy nap connection and one part of your building,

**[28:23](https://youtube.com/watch?v=7EoCa9HP9Bc&t=1703s)** you might have a hard nap connection in another part of your building,

**[28:26](https://youtube.com/watch?v=7EoCa9HP9Bc&t=1706s)** depending on how you're moving around and how your network is set up.

**[28:30](https://youtube.com/watch?v=7EoCa9HP9Bc&t=1710s)** One thing that was as come up for me multiple times in talking to customers is we look through

**[28:35](https://youtube.com/watch?v=7EoCa9HP9Bc&t=1715s)** the logs of the tail scale device and it's like, oh, hold on a minute, you switch from easy

**[28:39](https://youtube.com/watch?v=7EoCa9HP9Bc&t=1719s)** nap to hard nap at this time. What did you do? And they say, well, I closed my laptop and I went

**[28:44](https://youtube.com/watch?v=7EoCa9HP9Bc&t=1724s)** outside. And as a result, we got room to, we got room to a new access point, we had a different

**[28:50](https://youtube.com/watch?v=7EoCa9HP9Bc&t=1730s)** egress IP and all of a sudden I'm now in a hard nap situation. Again, there's only so much

**[28:55](https://youtube.com/watch?v=7EoCa9HP9Bc&t=1735s)** we at tail scale can do about that if the network is changing, but we will renegotiate to make

**[28:59](https://youtube.com/watch?v=7EoCa9HP9Bc&t=1739s)** sure that your connectivity remains. What happens when you have all these different types of connectivity?

**[29:07](https://youtube.com/watch?v=7EoCa9HP9Bc&t=1747s)** Well, we talked a little bit about all the different nap times. What I think everybody's probably

**[29:10](https://youtube.com/watch?v=7EoCa9HP9Bc&t=1750s)** waiting for is like, okay, well, just show me what I need to do to be able to get direct connections,

**[29:14](https://youtube.com/watch?v=7EoCa9HP9Bc&t=1754s)** please leave and stop going on about all this different complicated stuff.

**[29:20](https://youtube.com/watch?v=7EoCa9HP9Bc&t=1760s)** Well, this is the connectivity matrix. This is now on our website. It's on the troubleshooting

**[29:27](https://youtube.com/watch?v=7EoCa9HP9Bc&t=1767s)** device connectivity page. I should have included it in the slides, Tim, if you're listening,

**[29:31](https://youtube.com/watch?v=7EoCa9HP9Bc&t=1771s)** if you could go and look at the troubleshooting device connectivity page, I'm supposed to

**[29:34](https://youtube.com/watch?v=7EoCa9HP9Bc&t=1774s)** in the slot in the zoom chat that will be super eat, super awesome. But this is the result

**[29:40](https://youtube.com/watch?v=7EoCa9HP9Bc&t=1780s)** of all of these different types of nap. You can see that if you have two devices that have easy

**[29:44](https://youtube.com/watch?v=7EoCa9HP9Bc&t=1784s)** nap, you'll get direct connections. If one side of the equation has a hard nap, you will get relay

**[29:51](https://youtube.com/watch?v=7EoCa9HP9Bc&t=1791s)** connections using our DURP servers. That is the thing that is most commonly fixable when you are

**[29:57](https://youtube.com/watch?v=7EoCa9HP9Bc&t=1797s)** getting relay connections. And you can see at the bottom here, the way to fix that, if one side of

**[30:03](https://youtube.com/watch?v=7EoCa9HP9Bc&t=1803s)** the equation has a hard nap, the solution to that is to get the all the side of the equation into a

**[30:09](https://youtube.com/watch?v=7EoCa9HP9Bc&t=1809s)** no-not situation. Now, what's really interesting about this is that most organizations and most

**[30:16](https://youtube.com/watch?v=7EoCa9HP9Bc&t=1816s)** people have full control of a one side of the connection, but not the other side of the connection.

**[30:23](https://youtube.com/watch?v=7EoCa9HP9Bc&t=1823s)** What do I mean by that? Well, you've probably installed tailscale on one side on your home lab,

**[30:28](https://youtube.com/watch?v=7EoCa9HP9Bc&t=1828s)** or you've installed tailscale in your AWS account, or you've installed tailscale on your data center

**[30:32](https://youtube.com/watch?v=7EoCa9HP9Bc&t=1832s)** server. You can modify that side of the connection. What you can't do is all those laptops

**[30:39](https://youtube.com/watch?v=7EoCa9HP9Bc&t=1839s)** that are moving around, you cannot modify the internet connection of every airport that you go

**[30:45](https://youtube.com/watch?v=7EoCa9HP9Bc&t=1845s)** into and every house that you go into. You have no control over that side of the equation.

**[30:50](https://youtube.com/watch?v=7EoCa9HP9Bc&t=1850s)** So, on the solutions engineering side, what we recommend, where possible, if direct connections

**[30:56](https://youtube.com/watch?v=7EoCa9HP9Bc&t=1856s)** are important to you is the side of the connection that you can control, you should try and get that

**[31:02](https://youtube.com/watch?v=7EoCa9HP9Bc&t=1862s)** into no-not, because that means every connection, whether it's an easy nap or whether it's a hard nap,

**[31:09](https://youtube.com/watch?v=7EoCa9HP9Bc&t=1869s)** we'll get direct connections. That is the general solution that we have right now for these

**[31:15](https://youtube.com/watch?v=7EoCa9HP9Bc&t=1875s)** relay connections. If bandwidth is important, if latency is important, if throughput is important,

**[31:21](https://youtube.com/watch?v=7EoCa9HP9Bc&t=1881s)** look at the way you've architected tailscale and put the side of the connection that you have the

**[31:26](https://youtube.com/watch?v=7EoCa9HP9Bc&t=1886s)** most control over into a no-not situation. That usually means getting into a public subnet,

**[31:31](https://youtube.com/watch?v=7EoCa9HP9Bc&t=1891s)** if you're an cloud provider, if you're using your home lab, get a device that's your like

**[31:36](https://youtube.com/watch?v=7EoCa9HP9Bc&t=1896s)** nap device like your Wi-Fi router that gets the, or sorry, your modem that gets the direct IP address

**[31:43](https://youtube.com/watch?v=7EoCa9HP9Bc&t=1903s)** and put that into a no-not situation, you'll always get direct connections. So, what can you do

**[31:48](https://youtube.com/watch?v=7EoCa9HP9Bc&t=1908s)** differently? I already covered this. I already covered some of this, but if you could all just

**[31:55](https://youtube.com/watch?v=7EoCa9HP9Bc&t=1915s)** kind of stop what you're doing and move to IPv6, that would be awesome, because all of these

**[32:00](https://youtube.com/watch?v=7EoCa9HP9Bc&t=1920s)** problems go away with IPv6. There is a concept of naturally worse than IPv6, but because there's

**[32:06](https://youtube.com/watch?v=7EoCa9HP9Bc&t=1926s)** so many more available dresses, you don't need them anymore. You don't need to nap these devices.

**[32:13](https://youtube.com/watch?v=7EoCa9HP9Bc&t=1933s)** Of course, me asking a customer, well, if you want direct connections, it's time to turn on IPv6

**[32:18](https://youtube.com/watch?v=7EoCa9HP9Bc&t=1938s)** and they go, maybe I'll just use a different product, it's probably not the outcome that I want

**[32:23](https://youtube.com/watch?v=7EoCa9HP9Bc&t=1943s)** as a solution to engineer. So, IPv6 adoption is a really, really important part of the future of

**[32:30](https://youtube.com/watch?v=7EoCa9HP9Bc&t=1950s)** the internet. We've been talking about it for 10 years. I think there's a famous Bill Gates

**[32:34](https://youtube.com/watch?v=7EoCa9HP9Bc&t=1954s)** quotes that says, everything in technology that's going to take three years will take 10 years,

**[32:39](https://youtube.com/watch?v=7EoCa9HP9Bc&t=1959s)** and everything that in technology that says that we think will take 10 years will take three years.

**[32:44](https://youtube.com/watch?v=7EoCa9HP9Bc&t=1964s)** So, we're definitely in the kind of, we thought we'd be IPv6 everywhere in three years, and

**[32:49](https://youtube.com/watch?v=7EoCa9HP9Bc&t=1969s)** we're 10 years down the line and we're not even close to that. I will say my ISP has an IPv6 address,

**[32:54](https://youtube.com/watch?v=7EoCa9HP9Bc&t=1974s)** so I'm fine. But, you know, really getting into a place, especially in AWS, right? If you're

**[33:00](https://youtube.com/watch?v=7EoCa9HP9Bc&t=1980s)** spinning up a new AWS VPC and someone in the future and you think, I don't really need IPv6,

**[33:06](https://youtube.com/watch?v=7EoCa9HP9Bc&t=1986s)** please reconsider that. I think it would be really awesome if we just started to think as tail

**[33:10](https://youtube.com/watch?v=7EoCa9HP9Bc&t=1990s)** scale customers, you know, Avery, our CEO put a great blog post out a few weeks back around the

**[33:17](https://youtube.com/watch?v=7EoCa9HP9Bc&t=1997s)** new internet. I think part of the new internet is going to have to be IPv6 everywhere. This will

**[33:22](https://youtube.com/watch?v=7EoCa9HP9Bc&t=2002s)** solve all these problems, by the way. I have yet to see an organization that's using IPv6

**[33:30](https://youtube.com/watch?v=7EoCa9HP9Bc&t=2010s)** not getting direct connections. Generally, they get direct connections. But of course,

**[33:35](https://youtube.com/watch?v=7EoCa9HP9Bc&t=2015s)** we're a long way from IPv6 adoption, true IPv6 adoption. I know I already covered this, but

**[33:42](https://youtube.com/watch?v=7EoCa9HP9Bc&t=2022s)** moving your fiscal device into a public subnet or a non-net situation is the easiest way to fix

**[33:48](https://youtube.com/watch?v=7EoCa9HP9Bc&t=2028s)** this problem. Always make sure that you're opening UDP file 1-6-4-1 to that particular tail

**[33:54](https://youtube.com/watch?v=7EoCa9HP9Bc&t=2034s)** scale device. That will get you direct connections. However, the moment you've all been waiting for,

**[34:00](https://youtube.com/watch?v=7EoCa9HP9Bc&t=2040s)** I'm actually amazed I'm getting through this in this time, by the way. I thought this was going

**[34:03](https://youtube.com/watch?v=7EoCa9HP9Bc&t=2043s)** to take a way longer, which means I'm going to have time for questions at the end, which is great.

**[34:07](https://youtube.com/watch?v=7EoCa9HP9Bc&t=2047s)** There is a new experimental approach, and I can feel our engineering team

**[34:12](https://youtube.com/watch?v=7EoCa9HP9Bc&t=2052s)** when saying, as I talk about this, I am going to make this unequivocal. This is highly experimental,

**[34:19](https://youtube.com/watch?v=7EoCa9HP9Bc&t=2059s)** this will change, this is not something that you should rely on in production yet, and we are not

**[34:25](https://youtube.com/watch?v=7EoCa9HP9Bc&t=2065s)** finished building this capability out. I have to beg our engineering team to talk to you folks about

**[34:31](https://youtube.com/watch?v=7EoCa9HP9Bc&t=2071s)** this, and that's not an exaggeration. I have to beg them. Can we please give people an answer to

**[34:36](https://youtube.com/watch?v=7EoCa9HP9Bc&t=2076s)** this problem that is not IPv6, please? We've got an answer. I'll be honest, I know it's not one of

**[34:43](https://youtube.com/watch?v=7EoCa9HP9Bc&t=2083s)** our engineers into implementing this, and he shipped it, and now I'm talking about it. We're not

**[34:49](https://youtube.com/watch?v=7EoCa9HP9Bc&t=2089s)** documenting this on our website, because one of the reasons for that is when we document something

**[34:53](https://youtube.com/watch?v=7EoCa9HP9Bc&t=2093s)** on our website, we say it's not going to break. The backwards compatibility of tail scale is something

**[34:58](https://youtube.com/watch?v=7EoCa9HP9Bc&t=2098s)** that is breathtaking to me. We're not documenting this in this website, but I'm going to talk about

**[35:02](https://youtube.com/watch?v=7EoCa9HP9Bc&t=2102s)** it in this webinar so that people can try this out and see what it looks like. But we added an

**[35:07](https://youtube.com/watch?v=7EoCa9HP9Bc&t=2107s)** environment variable, and we also have a configuration file, which I'm not going to talk about just yet,

**[35:12](https://youtube.com/watch?v=7EoCa9HP9Bc&t=2112s)** we have a configuration file and an environment variable where you can actually update the endpoints

**[35:18](https://youtube.com/watch?v=7EoCa9HP9Bc&t=2118s)** manually. You are able to set the endpoints that tail scale has identified via its natural

**[35:25](https://youtube.com/watch?v=7EoCa9HP9Bc&t=2125s)** virtual technology. This means that you can get direct connections if you put something in front of

**[35:30](https://youtube.com/watch?v=7EoCa9HP9Bc&t=2130s)** the tail scale device that can forward ports to the tail scale device. Please, please do not mistake

**[35:36](https://youtube.com/watch?v=7EoCa9HP9Bc&t=2136s)** how experimental this is and how it will change in the future. Please be aware of that. I hope

**[35:43](https://youtube.com/watch?v=7EoCa9HP9Bc&t=2143s)** I've made that clear enough. I'm going to look in the chat here. Yes, it looks like people like

**[35:52](https://youtube.com/watch?v=7EoCa9HP9Bc&t=2152s)** experimental things. That's great. Please don't rely on this. It will change. I think this will

**[35:57](https://youtube.com/watch?v=7EoCa9HP9Bc&t=2157s)** still be something that we implement in our production level manner in the future, but for the

**[36:00](https://youtube.com/watch?v=7EoCa9HP9Bc&t=2160s)** time being, give it a try. See if it helps. What does this look like in reality? Well, here's an

**[36:08](https://youtube.com/watch?v=7EoCa9HP9Bc&t=2168s)** example from my cloud provider of choice AWS, where I put an NLB in the actual VPC in a public

**[36:16](https://youtube.com/watch?v=7EoCa9HP9Bc&t=2176s)** submit, and then I do a part forward to the EC2 instance that tail scale is running on.

**[36:20](https://youtube.com/watch?v=7EoCa9HP9Bc&t=2180s)** Cool, and now I'm going to direct connection. Let's have a little bit of demo of all of the

**[36:24](https://youtube.com/watch?v=7EoCa9HP9Bc&t=2184s)** stuff that we've seen today. This is the part where I run these demos a hundred times,

**[36:30](https://youtube.com/watch?v=7EoCa9HP9Bc&t=2190s)** whether it goes well on art, let's see, but let's get to it. First of all, I'm going to show you

**[36:37](https://youtube.com/watch?v=7EoCa9HP9Bc&t=2197s)** my personal telnet, my LBR labs telnet. You can see I provisioned a whole bunch of different

**[36:44](https://youtube.com/watch?v=7EoCa9HP9Bc&t=2204s)** clients here that have been very helpfully named with the type of knap they have. Let's go and take

**[36:49](https://youtube.com/watch?v=7EoCa9HP9Bc&t=2209s)** a look at this. No knap machine here, as we looked at previously. You can see that I've got the

**[36:53](https://youtube.com/watch?v=7EoCa9HP9Bc&t=2213s)** endpoints here. Various is no. There's no port mapping included. I know this is no knap because I know

**[36:59](https://youtube.com/watch?v=7EoCa9HP9Bc&t=2219s)** I also opened the AWS security group for this to make sure that it has inbound UDP access.

**[37:05](https://youtube.com/watch?v=7EoCa9HP9Bc&t=2225s)** Let's go and take a look at my easy knap instance, which is all the way up here. You can see I've got

**[37:10](https://youtube.com/watch?v=7EoCa9HP9Bc&t=2230s)** UPMP enabled here. It's initiated in that bound connection to port 41641. The way that it's done that

**[37:17](https://youtube.com/watch?v=7EoCa9HP9Bc&t=2237s)** is using UPMP. So what's happened again is that tail scale is initiated in that bound connection. It

**[37:22](https://youtube.com/watch?v=7EoCa9HP9Bc&t=2242s)** said, hey, I'm going to open port 41641. The UPMP device is said excellent. That's really great for

**[37:28](https://youtube.com/watch?v=7EoCa9HP9Bc&t=2248s)** you. I'm going to give you port 41641 because nobody's using it. As a result, we have used the

**[37:35](https://youtube.com/watch?v=7EoCa9HP9Bc&t=2255s)** port mapping protocol to be able to actually get that outbound connection. Again, it's behind a

**[37:39](https://youtube.com/watch?v=7EoCa9HP9Bc&t=2259s)** knap device, so be aware that it is still easy knap. You see, we still have a public endpoint here,

**[37:46](https://youtube.com/watch?v=7EoCa9HP9Bc&t=2266s)** and we still have a port here, but this public endpoint is not necessarily attached directly to

**[37:51](https://youtube.com/watch?v=7EoCa9HP9Bc&t=2271s)** the machine. That's the thing to really remember. And then finally, my evil hard knap instance,

**[37:58](https://youtube.com/watch?v=7EoCa9HP9Bc&t=2278s)** right? And you can see it's got all these different endpoints here, and it's got all these

**[38:02](https://youtube.com/watch?v=7EoCa9HP9Bc&t=2282s)** different ports and various is yes. And so as a result, we're in a situation where we know we're

**[38:09](https://youtube.com/watch?v=7EoCa9HP9Bc&t=2289s)** in a hard knap. So what does the result of this look like when I do a bunch of things? And I'll be

**[38:13](https://youtube.com/watch?v=7EoCa9HP9Bc&t=2293s)** honest, everyone listening. I was like, how can I actually make this interesting without just

**[38:18](https://youtube.com/watch?v=7EoCa9HP9Bc&t=2298s)** pinging a bunch of devices? And the answer is you cannot. So what I'm going to do is a bunch of

**[38:25](https://youtube.com/watch?v=7EoCa9HP9Bc&t=2305s)** out known out east. Excellent. You'll notice I'm using tail scale SSH for this because that's

**[38:38](https://youtube.com/watch?v=7EoCa9HP9Bc&t=2318s)** the best way to do these things. And if I do tail scale ping, I can do hard knap west. And you'll

**[38:46](https://youtube.com/watch?v=7EoCa9HP9Bc&t=2326s)** notice that I get a direct connection, obviously, because as we already noticed, one side of the

**[38:51](https://youtube.com/watch?v=7EoCa9HP9Bc&t=2331s)** equation here, this particular machine is in a no-knap situation. So I got a direct connection,

**[38:57](https://youtube.com/watch?v=7EoCa9HP9Bc&t=2337s)** I got lovely low latency, and I don't see a relay server in here. If I do the opposite with the

**[39:02](https://youtube.com/watch?v=7EoCa9HP9Bc&t=2342s)** hard knap instance, where I can do tail scale ping, hard knap, and I've ruined my big surprise here.

**[39:09](https://youtube.com/watch?v=7EoCa9HP9Bc&t=2349s)** Well, let's just keep going and pretend you don't see that. If I do hard knap west, you'll notice that

**[39:16](https://youtube.com/watch?v=7EoCa9HP9Bc&t=2356s)** server misbehaving. Interesting. I did not say that before. Let me ping the IP address instead.

**[39:32](https://youtube.com/watch?v=7EoCa9HP9Bc&t=2372s)** Of course, the service misbehaving on my demo. Why wouldn't it? So you can see here,

**[39:37](https://youtube.com/watch?v=7EoCa9HP9Bc&t=2377s)** this is the thing that most people are frustrated with. They're getting relayed via our depth servers.

**[39:43](https://youtube.com/watch?v=7EoCa9HP9Bc&t=2383s)** Yes, I am a masochist. Yes, I run my own depth server. Don't know why I do this, but I do.

**[39:48](https://youtube.com/watch?v=7EoCa9HP9Bc&t=2388s)** So you can see here that when we do two different hard knap connections on both sides of the

**[39:56](https://youtube.com/watch?v=7EoCa9HP9Bc&t=2396s)** equation, we get this relayed connection here. And this will add a little bit of latency. It will

**[40:04](https://youtube.com/watch?v=7EoCa9HP9Bc&t=2404s)** limit the amount of throughput. We have QOS on our depth servers so that we don't have individuals

**[40:09](https://youtube.com/watch?v=7EoCa9HP9Bc&t=2409s)** or organizations that abuse the amount of throughput we have on our depth servers. We're constantly

**[40:14](https://youtube.com/watch?v=7EoCa9HP9Bc&t=2414s)** growing the fleet. But in some situations, this will kind of have a performance impact on the

**[40:19](https://youtube.com/watch?v=7EoCa9HP9Bc&t=2419s)** ability for you to do low latency things, for example, you can see when we look at the known app,

**[40:23](https://youtube.com/watch?v=7EoCa9HP9Bc&t=2423s)** like this is in 62 milliseconds. I'm using AWS here on both sides of the equation, so I'm only

**[40:29](https://youtube.com/watch?v=7EoCa9HP9Bc&t=2429s)** getting an extra 0.6 milliseconds of latency. But the latency is increased very slightly as we

**[40:39](https://youtube.com/watch?v=7EoCa9HP9Bc&t=2439s)** go through our depth server. And then this one, so I'm not able to actually practice this one

**[40:45](https://youtube.com/watch?v=7EoCa9HP9Bc&t=2445s)** because, and you'll see why in a minute. So what I'm going to do is do tail scale ping EasyNet West.

**[40:52](https://youtube.com/watch?v=7EoCa9HP9Bc&t=2452s)** And you'll notice, so you'll see here that I'm originally getting duped, right? So like it starts

**[40:58](https://youtube.com/watch?v=7EoCa9HP9Bc&t=2458s)** out with duping me. And it says, okay, both sides of the equation are in EasyNet. It starts out

**[41:05](https://youtube.com/watch?v=7EoCa9HP9Bc&t=2465s)** in a dup situation. You can see there's a 86, 87, 86 milliseconds of latency. And then what happens

**[41:11](https://youtube.com/watch?v=7EoCa9HP9Bc&t=2471s)** is that tail scale realizes, because both sides are easy now and it can reuse those parts,

**[41:17](https://youtube.com/watch?v=7EoCa9HP9Bc&t=2477s)** it then establishes a direct connection. So you'll see it started, we've got three dup requests,

**[41:22](https://youtube.com/watch?v=7EoCa9HP9Bc&t=2482s)** and then it got a direct connection. This is what happens when you have both sides of the equation

**[41:27](https://youtube.com/watch?v=7EoCa9HP9Bc&t=2487s)** being in EasyNet. Now I'm going to take a quick refreshment break and then I'll explain why that's

**[41:31](https://youtube.com/watch?v=7EoCa9HP9Bc&t=2491s)** important. Hey Craig, I see a race time. I'm going to come back to it. I want to make sure I finish

**[41:37](https://youtube.com/watch?v=7EoCa9HP9Bc&t=2497s)** the content first. Thank you for being a participant in the webinar. I will come back to you

**[41:42](https://youtube.com/watch?v=7EoCa9HP9Bc&t=2502s)** hopefully. So why is it important that EasyNet dupes and then gets direct connections? Well, what we

**[41:51](https://youtube.com/watch?v=7EoCa9HP9Bc&t=2511s)** generally see in most scenarios where someone goes, well, I was getting direct connections and

**[41:57](https://youtube.com/watch?v=7EoCa9HP9Bc&t=2517s)** now I'm getting relayed and it sucks in the behaviors weird and it's a really poor experience.

**[42:02](https://youtube.com/watch?v=7EoCa9HP9Bc&t=2522s)** The reason for that is that either the net type changed, the EasyNet kind of by the ice protocol

**[42:10](https://youtube.com/watch?v=7EoCa9HP9Bc&t=2530s)** continues to renegotiating the EasyNet changed or something changed in the network that is outside

**[42:14](https://youtube.com/watch?v=7EoCa9HP9Bc&t=2534s)** of the control of tail scale. And as a result, it can no longer get these direct connections anymore.

**[42:20](https://youtube.com/watch?v=7EoCa9HP9Bc&t=2540s)** I've seen this happen when the net table fills up, right? So like you have multiple clients behind

**[42:24](https://youtube.com/watch?v=7EoCa9HP9Bc&t=2544s)** the net device and like all of them are opening ports and then all of a sudden you've got a thousand

**[42:30](https://youtube.com/watch?v=7EoCa9HP9Bc&t=2550s)** tail scale clients behind the net device and all of a sudden the net table is filled up, then it will

**[42:34](https://youtube.com/watch?v=7EoCa9HP9Bc&t=2554s)** start chirping, right? Because now the net device is saying, well, I can't give you that part back

**[42:39](https://youtube.com/watch?v=7EoCa9HP9Bc&t=2559s)** because somebody else is using it and I've actually run out of parts. So as a result, I'm now going

**[42:43](https://youtube.com/watch?v=7EoCa9HP9Bc&t=2563s)** to have to randomize every outbound connection and therefore we're going to have to relay you,

**[42:48](https://youtube.com/watch?v=7EoCa9HP9Bc&t=2568s)** right? This is the thing that I think most people get frustrated with when they're using tail scale.

**[42:53](https://youtube.com/watch?v=7EoCa9HP9Bc&t=2573s)** They're like, well, cool. I had direct connections. The likelihood is that they had EasyNet on both sides

**[42:57](https://youtube.com/watch?v=7EoCa9HP9Bc&t=2577s)** and now all of a sudden they don't have direct connections and they've gone from 64 milliseconds

**[43:02](https://youtube.com/watch?v=7EoCa9HP9Bc&t=2582s)** of latency to 90 milliseconds of latency. It's a noticeable difference if you're doing something

**[43:07](https://youtube.com/watch?v=7EoCa9HP9Bc&t=2587s)** that's latency-sensitive. And as a result, it can be a pretty part experience for people.

**[43:12](https://youtube.com/watch?v=7EoCa9HP9Bc&t=2592s)** So what's the solution to that? Well, the solution to that is of course to turn things into

**[43:16](https://youtube.com/watch?v=7EoCa9HP9Bc&t=2596s)** no-natt. And so what does that look like? So again, I'm on a no-natt device here and I can do

**[43:22](https://youtube.com/watch?v=7EoCa9HP9Bc&t=2602s)** from a no-natt device, I can do EasyNet West. And you should get a direct connection,

**[43:33](https://youtube.com/watch?v=7EoCa9HP9Bc&t=2613s)** right? Because one side of the equation is no-natt and the other side of the connection is EasyNet.

**[43:38](https://youtube.com/watch?v=7EoCa9HP9Bc&t=2618s)** So I'll get direct connections once the kind of negotiations happen. I'll get direct connections

**[43:43](https://youtube.com/watch?v=7EoCa9HP9Bc&t=2623s)** pretty quickly every single time. That's awesome, right? I think that's really, really important

**[43:49](https://youtube.com/watch?v=7EoCa9HP9Bc&t=2629s)** for all of these different things. Try and get one-sided equation into a no-natt situation.

**[43:56](https://youtube.com/watch?v=7EoCa9HP9Bc&t=2636s)** However, the experimental thing that we talked about, well, what does that look like? Well,

**[44:02](https://youtube.com/watch?v=7EoCa9HP9Bc&t=2642s)** what I've done for this hard-knit with load balancer is I put an NLB in front of it.

**[44:09](https://youtube.com/watch?v=7EoCa9HP9Bc&t=2649s)** And let's look at the Terraform code, shall we? If you're not familiar with Terraform,

**[44:12](https://youtube.com/watch?v=7EoCa9HP9Bc&t=2652s)** I apologize. This is how I do things in AWS. So let's have a look what we've got here. We've got

**[44:17](https://youtube.com/watch?v=7EoCa9HP9Bc&t=2657s)** an NLB that I've got for my West Coast, my U.S. West instances. And I've created a target group

**[44:28](https://youtube.com/watch?v=7EoCa9HP9Bc&t=2668s)** that allows 41641 with UDP, right? You'll notice that the health check here, I'm not actually able

**[44:37](https://youtube.com/watch?v=7EoCa9HP9Bc&t=2677s)** to use that core 41641 for the health check because of course, you can't actually do any health checks

**[44:43](https://youtube.com/watch?v=7EoCa9HP9Bc&t=2683s)** on UDP parts. And then also set a listener on here that is also on port 41641 and UDP,

**[44:50](https://youtube.com/watch?v=7EoCa9HP9Bc&t=2690s)** and then I've attached it to the instance, right? So if you imagine what this looks like,

**[44:53](https://youtube.com/watch?v=7EoCa9HP9Bc&t=2693s)** and I probably should have had the AWS console open running, but I don't, so I apologize for that.

**[44:58](https://youtube.com/watch?v=7EoCa9HP9Bc&t=2698s)** What this looks like is that I've got a load balancer in front of this hard-knit device. The

**[45:01](https://youtube.com/watch?v=7EoCa9HP9Bc&t=2701s)** instance itself is in a private subnet. And when a request comes in from port 41641 on a load

**[45:11](https://youtube.com/watch?v=7EoCa9HP9Bc&t=2711s)** balancer on UDP protocol, it immediately forwards that through to the instance, right?

**[45:18](https://youtube.com/watch?v=7EoCa9HP9Bc&t=2718s)** That's great. But the problem is, let's have a look at my hard-knit instance here, the problem is

**[45:25](https://youtube.com/watch?v=7EoCa9HP9Bc&t=2725s)** tail scale doesn't know about this load balancer, right? Because all it knows about is the end points

**[45:31](https://youtube.com/watch?v=7EoCa9HP9Bc&t=2731s)** that we use to initiate outbound connections. So tail scale doesn't know to use this end point.

**[45:38](https://youtube.com/watch?v=7EoCa9HP9Bc&t=2738s)** So you've got this load balancer with all these public IP addresses that's listening on port 41641,

**[45:43](https://youtube.com/watch?v=7EoCa9HP9Bc&t=2743s)** but it doesn't know to use it. So it's effectively irrelevant at this point, right? Like it's just a

**[45:48](https://youtube.com/watch?v=7EoCa9HP9Bc&t=2748s)** pointless load balancer that's in front of an instance. So what we can do with a new mechanism

**[45:54](https://youtube.com/watch?v=7EoCa9HP9Bc&t=2754s)** with the config file is we can update the end points table. And you can see here, these are the IP

**[46:00](https://youtube.com/watch?v=7EoCa9HP9Bc&t=2760s)** addresses of the load balancer with port 41641 open. And so now tail scale knows, hey, there's a

**[46:07](https://youtube.com/watch?v=7EoCa9HP9Bc&t=2767s)** natural end point that is listening on port 41641. And you can see this is still very, is true,

**[46:12](https://youtube.com/watch?v=7EoCa9HP9Bc&t=2772s)** is yes, a very is yet is true. And you can still see that it's the same outbound end points look here

**[46:19](https://youtube.com/watch?v=7EoCa9HP9Bc&t=2779s)** with like port randomization involved. But I also have predictable end points that the LNLB

**[46:26](https://youtube.com/watch?v=7EoCa9HP9Bc&t=2786s)** is providing for me. I've let tail scale know about these end points by doing this. Switch to pseudo,

**[46:35](https://youtube.com/watch?v=7EoCa9HP9Bc&t=2795s)** uh, it looks like my sessions timed out. That's super useful. Let's do SSH Ubuntu

**[46:43](https://youtube.com/watch?v=7EoCa9HP9Bc&t=2803s)** hard not west with LB. Thank you for remembering what I'm doing. So what I've done, all I've done

**[46:49](https://youtube.com/watch?v=7EoCa9HP9Bc&t=2809s)** here is adding an override to the tail scale D demon bound down here. The engineer Brad, who is

**[46:58](https://youtube.com/watch?v=7EoCa9HP9Bc&t=2818s)** easily one of the smartest engineers I've ever worked with, is also one of the funniest engineers

**[47:03](https://youtube.com/watch?v=7EoCa9HP9Bc&t=2823s)** that I worked with was like, we'll call it a pretend point because it's not a real end point. And

**[47:07](https://youtube.com/watch?v=7EoCa9HP9Bc&t=2827s)** I'm like, that's awesome. You'll notice the debug flag here. That debug flag means we'll change,

**[47:13](https://youtube.com/watch?v=7EoCa9HP9Bc&t=2833s)** could go away. Might not be the same. The fact that using a debug flag means your mileage may vary.

**[47:18](https://youtube.com/watch?v=7EoCa9HP9Bc&t=2838s)** Don't blame us if we turn it off. I made it super clear. We haven't documented it on the website.

**[47:23](https://youtube.com/watch?v=7EoCa9HP9Bc&t=2843s)** So it goes away. Don't get upset with us. I've been as clear as I possibly can. But these are all

**[47:28](https://youtube.com/watch?v=7EoCa9HP9Bc&t=2848s)** the actual low-balance IP addresses and ports, right? So as a result, we now have these endpoints that

**[47:35](https://youtube.com/watch?v=7EoCa9HP9Bc&t=2855s)** are advertised on the actual endpoint table. So what does that look like? As a reminder, if I do

**[47:42](https://youtube.com/watch?v=7EoCa9HP9Bc&t=2862s)** tail scale ping for my hard not instance, I get relayed. If I do tail scale ping, hard not

**[47:51](https://youtube.com/watch?v=7EoCa9HP9Bc&t=2871s)** west with LB, I get a direct connection. So I now have two instances in private networks behind

**[48:02](https://youtube.com/watch?v=7EoCa9HP9Bc&t=2882s)** an AWS managed not gateway that I can now get direct connections behind. And I'm using a low-balance

**[48:08](https://youtube.com/watch?v=7EoCa9HP9Bc&t=2888s)** to do that. What are some of the things you need to think about here? Well, AWS likes to build you

**[48:12](https://youtube.com/watch?v=7EoCa9HP9Bc&t=2892s)** for data transfer. So anything that's going to go through this low-balance or any data that's

**[48:15](https://youtube.com/watch?v=7EoCa9HP9Bc&t=2895s)** going to go through this low-balance is going to cost you money. So don't blame me if your

**[48:19](https://youtube.com/watch?v=7EoCa9HP9Bc&t=2899s)** AWS bill goes up because you're doing this and you want to direct connections and you're dumping

**[48:23](https://youtube.com/watch?v=7EoCa9HP9Bc&t=2903s)** your entire 40 terabyte database through tail scale. That is something that you have to think about

**[48:28](https://youtube.com/watch?v=7EoCa9HP9Bc&t=2908s)** in your AWS architecture. But through a low-balance that's a lot of data. If data transfer is a concern

**[48:36](https://youtube.com/watch?v=7EoCa9HP9Bc&t=2916s)** for you and the amount of data that you want to actually transfer as a consideration, put a tail scale

**[48:42](https://youtube.com/watch?v=7EoCa9HP9Bc&t=2922s)** subnet router in a public subnet and do it that way. Put it into no net. This is really usable

**[48:49](https://youtube.com/watch?v=7EoCa9HP9Bc&t=2929s)** for those situations where you don't, you have a security requirement that says no EC2

**[48:55](https://youtube.com/watch?v=7EoCa9HP9Bc&t=2935s)** instance in public subnets. That comes up often with our customers. So this is a solution for you.

**[49:02](https://youtube.com/watch?v=7EoCa9HP9Bc&t=2942s)** So let's finish up. I'm going to take a little second here to scroll through the chat through the

**[49:09](https://youtube.com/watch?v=7EoCa9HP9Bc&t=2949s)** chat. I'll see if there's any questions. Let's look at the time. Oh, I've only got 10 minutes.

**[49:14](https://youtube.com/watch?v=7EoCa9HP9Bc&t=2954s)** I'm going to finish the slides and then I'll try and get through some questions. So what are some

**[49:17](https://youtube.com/watch?v=7EoCa9HP9Bc&t=2957s)** domain-specific considerations here? Well, the one thing that comes up all the time is, well,

**[49:25](https://youtube.com/watch?v=7EoCa9HP9Bc&t=2965s)** I'm running my tail scale clients on Kubernetes. And I can't get direct connections. Why is that?

**[49:30](https://youtube.com/watch?v=7EoCa9HP9Bc&t=2970s)** Well, the reason for that is because Kubernetes is complicated. And it adds a layer of NAT to the

**[49:37](https://youtube.com/watch?v=7EoCa9HP9Bc&t=2977s)** equation that the CNI implements. When you have a pod running on a host, all those connections that

**[49:44](https://youtube.com/watch?v=7EoCa9HP9Bc&t=2984s)** go out to the internet get natted through the host as well. And there are lots of situations that

**[49:50](https://youtube.com/watch?v=7EoCa9HP9Bc&t=2990s)** we've seen with the CNI where they implement on IP tables natting. They implement fully random

**[49:56](https://youtube.com/watch?v=7EoCa9HP9Bc&t=2996s)** outbound connections, which is essentially a hard NAT. So when you run Kubernetes pods with

**[50:01](https://youtube.com/watch?v=7EoCa9HP9Bc&t=3001s)** tail scale in them, most of the time they are hard-natted. And the reason for that, I've just

**[50:07](https://youtube.com/watch?v=7EoCa9HP9Bc&t=3007s)** mentioned is because you got NAT from the host address. However, it is fixable, but you have to use

**[50:15](https://youtube.com/watch?v=7EoCa9HP9Bc&t=3015s)** host networking to get around that CNI thing. We personally are not making any guarantees around

**[50:21](https://youtube.com/watch?v=7EoCa9HP9Bc&t=3021s)** direct connections on Kubernetes right now. I talk to customers every single day who are like, I'm

**[50:26](https://youtube.com/watch?v=7EoCa9HP9Bc&t=3026s)** running this in Kubernetes and I need direct connections. So what can I do about it? And the answer

**[50:31](https://youtube.com/watch?v=7EoCa9HP9Bc&t=3031s)** to that is don't run your tail scale workloads on Kubernetes. If you're using a cloud provider like

**[50:37](https://youtube.com/watch?v=7EoCa9HP9Bc&t=3037s)** EKS, take advantage of the fact that the EKS CNI gives you IP addresses from the VPC. So you

**[50:43](https://youtube.com/watch?v=7EoCa9HP9Bc&t=3043s)** can put a subnet router on a public subnet, no NAT, it still get the same capability that you

**[50:49](https://youtube.com/watch?v=7EoCa9HP9Bc&t=3049s)** would get with tail scale subnet routing running in the cluster. However, you can get direct connections

**[50:55](https://youtube.com/watch?v=7EoCa9HP9Bc&t=3055s)** and you can still reach your Kubernetes pods better than in mind. I could do an entire hour on

**[51:00](https://youtube.com/watch?v=7EoCa9HP9Bc&t=3060s)** thing about this. I'm not going to take too much time. But the thing to take away from it here is

**[51:05](https://youtube.com/watch?v=7EoCa9HP9Bc&t=3065s)** the Kubernetes CNI makes it difficult to get direct connections and hard NATs most connections.

**[51:09](https://youtube.com/watch?v=7EoCa9HP9Bc&t=3069s)** So it's outside of our hands. Complainty cloud provider about it. I wish this was not the case.

**[51:15](https://youtube.com/watch?v=7EoCa9HP9Bc&t=3075s)** Again, if you use IPv6, not necessarily a problem, but there is a lot of stuff here that is outside

**[51:22](https://youtube.com/watch?v=7EoCa9HP9Bc&t=3082s)** of our hands on the tail scale side. AWS, AWS ManagedNetways, which almost everybody that I speak to

**[51:29](https://youtube.com/watch?v=7EoCa9HP9Bc&t=3089s)** uses, we moved away from that instances. There are ways to run your own NAT instances, which will give

**[51:34](https://youtube.com/watch?v=7EoCa9HP9Bc&t=3094s)** you an easy NAT experience, but then you're going to manage NAT and have to manage the ECG compute for

**[51:39](https://youtube.com/watch?v=7EoCa9HP9Bc&t=3099s)** that. I mean, it's managed NAT pathways for all connections to be hard now. At a conversation with

**[51:44](https://youtube.com/watch?v=7EoCa9HP9Bc&t=3104s)** AWS NAT gateway team, they're aware of this. It's a really hard problem to solve. So if you're

**[51:50](https://youtube.com/watch?v=7EoCa9HP9Bc&t=3110s)** interesting in logging the internal feature request that we have with AWS to fix this, so it bumps

**[51:59](https://youtube.com/watch?v=7EoCa9HP9Bc&t=3119s)** up their priority list, please email me, and I can't believe I'm going to do this on a public

**[52:03](https://youtube.com/watch?v=7EoCa9HP9Bc&t=3123s)** webinar, please email me directly, leahtalesscale.com and say, hey, can you add my company to this list of

**[52:09](https://youtube.com/watch?v=7EoCa9HP9Bc&t=3129s)** people that are affected by this problem, and I will make sure it's added, or I can give you instructions

**[52:14](https://youtube.com/watch?v=7EoCa9HP9Bc&t=3134s)** on how your account manager can do that. AWS has a path to fixing this, but it's not easy,

**[52:20](https://youtube.com/watch?v=7EoCa9HP9Bc&t=3140s)** and it's going to be hard to implement in the data plane. So this is something that I would love to

**[52:25](https://youtube.com/watch?v=7EoCa9HP9Bc&t=3145s)** fix. If AWS managed NAT gateways were easy, NAT things will be a lot easier, but they are hard

**[52:29](https://youtube.com/watch?v=7EoCa9HP9Bc&t=3149s)** NAT. Our suggestion, as I've said, over and over again, is to put the instances in public subnets.

**[52:35](https://youtube.com/watch?v=7EoCa9HP9Bc&t=3155s)** Azure managed NAT gateway, very, very simple. It is worth noting that managed NAT gateways,

**[52:41](https://youtube.com/watch?v=7EoCa9HP9Bc&t=3161s)** it's like Azure was realized they can build for outbound data transfer from NAT gateways,

**[52:45](https://youtube.com/watch?v=7EoCa9HP9Bc&t=3165s)** like I want a piece of that. So NAT gateways are pretty new. The last time I looked a few months

**[52:50](https://youtube.com/watch?v=7EoCa9HP9Bc&t=3170s)** ago, this was, they were deprecating the ability to do progress from VNETs without a NAT gateways,

**[52:58](https://youtube.com/watch?v=7EoCa9HP9Bc&t=3178s)** so this is going to become more widespread. So again, public subnets are the way to go here.

**[53:03](https://youtube.com/watch?v=7EoCa9HP9Bc&t=3183s)** And then Google has an actual setting to turn on, on its public NAT, to turn on easy NAT,

**[53:12](https://youtube.com/watch?v=7EoCa9HP9Bc&t=3192s)** which it has as endpoint independent mapping. Take a look at that link. You can Google,

**[53:17](https://youtube.com/watch?v=7EoCa9HP9Bc&t=3197s)** you can search for on Google, Google G cloud, NAT ports and addresses. There's a setting that you

**[53:25](https://youtube.com/watch?v=7EoCa9HP9Bc&t=3205s)** can set that fastest things into easy now. That will give you direct connections in lots and lots

**[53:29](https://youtube.com/watch?v=7EoCa9HP9Bc&t=3209s)** of situations, and there's a little bit better than the situation in both the cloud providers.

**[53:34](https://youtube.com/watch?v=7EoCa9HP9Bc&t=3214s)** That was a lot of words and a lot of slides. I appreciate everybody listening to me drone on.

**[53:41](https://youtube.com/watch?v=7EoCa9HP9Bc&t=3221s)** I'm going to take a quick minute to have a refreshment break and take a drink and then

**[53:47](https://youtube.com/watch?v=7EoCa9HP9Bc&t=3227s)** I'm going to try and see if I can get through the 16 open questions. So give me a few moments.

**[53:55](https://youtube.com/watch?v=7EoCa9HP9Bc&t=3235s)** Excellent. Okay, big, long question from Mark. I've been using Telskil for two years,

**[54:00](https://youtube.com/watch?v=7EoCa9HP9Bc&t=3240s)** so you can start with Telskil. I switched to Mac, it was a little problem. I first tried to use Telskil in my

**[54:03](https://youtube.com/watch?v=7EoCa9HP9Bc&t=3243s)** second Ambrose, so let Telskil use a HC2 proxy. I hate Telskil in McKench, it's a school. So it looks

**[54:08](https://youtube.com/watch?v=7EoCa9HP9Bc&t=3248s)** like here, this is a problem around using a NAT Bob proxy, it's funny how these seven different

**[54:15](https://youtube.com/watch?v=7EoCa9HP9Bc&t=3255s)** entities things are. Telskil makes no guarantees about you being able to use a proxy right now.

**[54:21](https://youtube.com/watch?v=7EoCa9HP9Bc&t=3261s)** And the reason for that is that when it does the outbound connections, it needs to be able to navigate

**[54:26](https://youtube.com/watch?v=7EoCa9HP9Bc&t=3266s)** that outbound connection. We don't have any proxy traversal technology built into the product.

**[54:32](https://youtube.com/watch?v=7EoCa9HP9Bc&t=3272s)** So I don't think we can make any guarantees. It seems like you already reached out to support.

**[54:37](https://youtube.com/watch?v=7EoCa9HP9Bc&t=3277s)** I would love to know if that means that you just don't get any connections at all. My suspicion is

**[54:43](https://youtube.com/watch?v=7EoCa9HP9Bc&t=3283s)** you probably get hard-knotted connections when you have those proxies. But yeah, I do apologize.

**[54:50](https://youtube.com/watch?v=7EoCa9HP9Bc&t=3290s)** Part of the thing that is in play here is that Telskil uses HTTPS to both connect to the DURP

**[54:57](https://youtube.com/watch?v=7EoCa9HP9Bc&t=3297s)** servers and also connect to the control plane. So I do apologize that the restrictive environment

**[55:05](https://youtube.com/watch?v=7EoCa9HP9Bc&t=3305s)** that you're running in is requiring you to use a proxy. But there's no real guarantee that

**[55:14](https://youtube.com/watch?v=7EoCa9HP9Bc&t=3314s)** Telskil is actually able to traverse that situation. So I do apologize for that.

**[55:19](https://youtube.com/watch?v=7EoCa9HP9Bc&t=3319s)** I notice that you're open to GitHub issue. I'll take a look at it afterwards and see if I can

**[55:22](https://youtube.com/watch?v=7EoCa9HP9Bc&t=3322s)** get a response on there for you. But I appreciate you bringing that to my attention. I think that's

**[55:27](https://youtube.com/watch?v=7EoCa9HP9Bc&t=3327s)** answered. Okay. Kevin, can you compare contrast stone turn DURP? Okay. The very quick answer,

**[55:36](https://youtube.com/watch?v=7EoCa9HP9Bc&t=3336s)** I've got four minutes, but I can run a little bit over. Stone is the session traversal for NAT.

**[55:42](https://youtube.com/watch?v=7EoCa9HP9Bc&t=3342s)** I can't remember the acronym's exact thing. Stone is the thing that we use to identify the end

**[55:50](https://youtube.com/watch?v=7EoCa9HP9Bc&t=3350s)** points that we have got from. DURP is a technology that Telskil has developed that will in those

**[55:57](https://youtube.com/watch?v=7EoCa9HP9Bc&t=3357s)** cases where we're in hard now, we can't create direct connections. We'll relay connections for you.

**[56:03](https://youtube.com/watch?v=7EoCa9HP9Bc&t=3363s)** I tried not to go deep into what DURP does and how it works for this particular webinar. I think

**[56:08](https://youtube.com/watch?v=7EoCa9HP9Bc&t=3368s)** that's a potentially great future webinar discussion. But there are actually different things. Stone

**[56:13](https://youtube.com/watch?v=7EoCa9HP9Bc&t=3373s)** is the thing that is detecting the end points. DURP is the thing that is relaying traffic on your

**[56:18](https://youtube.com/watch?v=7EoCa9HP9Bc&t=3378s)** behalf. What's the thing for us is that we run them on the same server. So we have a stone server that

**[56:26](https://youtube.com/watch?v=7EoCa9HP9Bc&t=3386s)** is running on our DURP servers and we use them for both things for obvious reasons. So there's

**[56:32](https://youtube.com/watch?v=7EoCa9HP9Bc&t=3392s)** not a comparison trust to actually use for different things. Okay. Is there a situation where a file

**[56:39](https://youtube.com/watch?v=7EoCa9HP9Bc&t=3399s)** often still be easy now, even when UP and P, etc. are disabled, but ports aren't varied

**[56:43](https://youtube.com/watch?v=7EoCa9HP9Bc&t=3403s)** all between outbound requests? Yes, there is a situation where a firewall can be easy now, even when

**[56:48](https://youtube.com/watch?v=7EoCa9HP9Bc&t=3408s)** UP and P, etc. are disabled. If it's a certain type of firewall and I'm blanking on whether because

**[56:54](https://youtube.com/watch?v=7EoCa9HP9Bc&t=3414s)** I've just talked for an hour straight. I can't remember if it's a state full or stateless firewall,

**[56:58](https://youtube.com/watch?v=7EoCa9HP9Bc&t=3418s)** that will look like an easy now too, because it will allow you to create an outbound connection,

**[57:02](https://youtube.com/watch?v=7EoCa9HP9Bc&t=3422s)** and it will hold that connection open for inbound requests. That kind of looks like an easy now.

**[57:07](https://youtube.com/watch?v=7EoCa9HP9Bc&t=3427s)** If you turn off the if you allow inbound requests for the firewall with UDP port that TillScale's

**[57:13](https://youtube.com/watch?v=7EoCa9HP9Bc&t=3433s)** running on, you'll get a known. So yes, there is definitely situations where things can look like an

**[57:19](https://youtube.com/watch?v=7EoCa9HP9Bc&t=3439s)** easy now. Again, AWS security groups are a great example of that. If you give a public IP address

**[57:25](https://youtube.com/watch?v=7EoCa9HP9Bc&t=3445s)** on an AWS instance, and this is something that comes up really often, people say, well, I move

**[57:29](https://youtube.com/watch?v=7EoCa9HP9Bc&t=3449s)** TillScale into a public subnet in a cloud provider, and I'm still getting relay connections. And I

**[57:35](https://youtube.com/watch?v=7EoCa9HP9Bc&t=3455s)** say, have you opened an inbound port for UDP? And they say, well, my security team won't let me do

**[57:40](https://youtube.com/watch?v=7EoCa9HP9Bc&t=3460s)** that. I'm like, well, the best that you're going to be able to do is easy now in terms of its behavior.

**[57:45](https://youtube.com/watch?v=7EoCa9HP9Bc&t=3465s)** It's not technically easy now, because it has a public address. But as you remember, I have a big

**[57:49](https://youtube.com/watch?v=7EoCa9HP9Bc&t=3469s)** bucket that I'm putting things into. So I'm going to put it in the easy now bucket.

**[57:54](https://youtube.com/watch?v=7EoCa9HP9Bc&t=3474s)** When the result is relayed, how's that fat latency bandwidth and also the cost? There is no

**[57:58](https://youtube.com/watch?v=7EoCa9HP9Bc&t=3478s)** additional cost to using relayed service gap. And so you do not need to worry about additional

**[58:03](https://youtube.com/watch?v=7EoCa9HP9Bc&t=3483s)** cost on the TillScale side. However, there are QOS implementations on per tailnet on the DURP

**[58:10](https://youtube.com/watch?v=7EoCa9HP9Bc&t=3490s)** service that mean that your initial connections will be very, very latency will have good

**[58:18](https://youtube.com/watch?v=7EoCa9HP9Bc&t=3498s)** latency in bandwidth. I think there's a limit in terms of the bandwidth that we can actually push

**[58:22](https://youtube.com/watch?v=7EoCa9HP9Bc&t=3502s)** through DURP servers. However, the more you like the more connections you use over DURP,

**[58:26](https://youtube.com/watch?v=7EoCa9HP9Bc&t=3506s)** the more QOS there is in place there. So you may see that there is lots and lots of different

**[58:31](https://youtube.com/watch?v=7EoCa9HP9Bc&t=3511s)** connections. And then, like, performance is impacted. We generally see this when there's

**[58:35](https://youtube.com/watch?v=7EoCa9HP9Bc&t=3515s)** thousands of connections. If you have 10 clients, you're likely not going to run into this.

**[58:40](https://youtube.com/watch?v=7EoCa9HP9Bc&t=3520s)** Can we enable IPv6 in TillScale? On my TillScale clients, they say support IPv6, but it's not enabled.

**[58:47](https://youtube.com/watch?v=7EoCa9HP9Bc&t=3527s)** That is probably on your operating system. So that likely means that you haven't enabled IPv6

**[58:52](https://youtube.com/watch?v=7EoCa9HP9Bc&t=3532s)** in your operating system. But the actual kernel that you're running on, the device that you're

**[58:58](https://youtube.com/watch?v=7EoCa9HP9Bc&t=3538s)** running on, has support for IPv6, you just need to turn it off. It's an operating system thing.

**[59:03](https://youtube.com/watch?v=7EoCa9HP9Bc&t=3543s)** It's a TillScale thing. By default, all TillScale devices get an IPv6 address. That's

**[59:09](https://youtube.com/watch?v=7EoCa9HP9Bc&t=3549s)** quickly show you what that looks like. So you can see here, the TillScale IPv6 address is here.

**[59:16](https://youtube.com/watch?v=7EoCa9HP9Bc&t=3556s)** And you can see IPv6, no. That means the actual device, like the actual operating system underneath

**[59:22](https://youtube.com/watch?v=7EoCa9HP9Bc&t=3562s)** here, does not IPv6 enable. But if I turn it on, I'll get IPv6, yes. Hopefully that answers that.

**[59:28](https://youtube.com/watch?v=7EoCa9HP9Bc&t=3568s)** Question 11. Oh, no, that's the wrong one. One of the final, it's actually a consideration that

**[59:32](https://youtube.com/watch?v=7EoCa9HP9Bc&t=3572s)** I'm trying to tell you the IPv6. But do a whole thing on this. I'm going to try and do a very,

**[59:36](https://youtube.com/watch?v=7EoCa9HP9Bc&t=3576s)** very quick explanation. IPv6, because it allows every single device, even in what we call

**[59:45](https://youtube.com/watch?v=7EoCa9HP9Bc&t=3585s)** private subnet, because the way it kind of calculates an IPv6 from a prefix, it basically means

**[59:51](https://youtube.com/watch?v=7EoCa9HP9Bc&t=3591s)** that every single device has IPv6 address directly associated with it. There are firewall considerations

**[59:58](https://youtube.com/watch?v=7EoCa9HP9Bc&t=3598s)** around like EasyNet. So like if you don't allow inbound UDP connections, for example, both devices

**[01:00:04](https://youtube.com/watch?v=7EoCa9HP9Bc&t=3604s)** will look like an EasyNet instance. But you don't have that kind of network change kind of

**[01:00:10](https://youtube.com/watch?v=7EoCa9HP9Bc&t=3610s)** configuration that comes into play with IPv6 that you do with IPv4. So there are considerations

**[01:00:16](https://youtube.com/watch?v=7EoCa9HP9Bc&t=3616s)** around like, you don't necessarily need to open inbound UDP access with IPv6. So I would recommend

**[01:00:24](https://youtube.com/watch?v=7EoCa9HP9Bc&t=3624s)** looking at it from that perspective. Long story short, if you can turn on IPv6, I would go ahead

**[01:00:28](https://youtube.com/watch?v=7EoCa9HP9Bc&t=3628s)** and do it. I think that's a great idea. I already answered this one. I don't know really sorry, Larry.

**[01:00:38](https://youtube.com/watch?v=7EoCa9HP9Bc&t=3638s)** I'm not really sure what you're getting at. When you say what about CGNet, just a high level thing,

**[01:00:43](https://youtube.com/watch?v=7EoCa9HP9Bc&t=3643s)** tail scale gives IP addresses out from the CGNet, carrying net space. I'm going to make a leap here

**[01:00:50](https://youtube.com/watch?v=7EoCa9HP9Bc&t=3650s)** and say, well, what if you have CGNet behind the scenes? That is not my area of expertise, but my

**[01:00:56](https://youtube.com/watch?v=7EoCa9HP9Bc&t=3656s)** understanding is you can get it to work. So if you have questions around this around CGNet and

**[01:01:01](https://youtube.com/watch?v=7EoCa9HP9Bc&t=3661s)** the usage of CGNet, we have an office hours with SEs that I run with my wonderful colleague Alex.

**[01:01:07](https://youtube.com/watch?v=7EoCa9HP9Bc&t=3667s)** Please join us to ask that sort of question around CGNet. If a server is running several Docker

**[01:01:13](https://youtube.com/watch?v=7EoCa9HP9Bc&t=3673s)** containers with tail scale side cards in a home lab, what kind of configuration would I need to

**[01:01:17](https://youtube.com/watch?v=7EoCa9HP9Bc&t=3677s)** play IPv6 with Docker side cards? Assuming my ISP provides IPv6 across. Okay, so you have your

**[01:01:24](https://youtube.com/watch?v=7EoCa9HP9Bc&t=3684s)** NAT device, which has an IPv6 address. What you then need to do is enable IPv6 in your home network.

**[01:01:30](https://youtube.com/watch?v=7EoCa9HP9Bc&t=3690s)** So usually on your NAT instance, you'll have like, sorry, in your home router, you'll have the

**[01:01:36](https://youtube.com/watch?v=7EoCa9HP9Bc&t=3696s)** ability, depending on the router model, of course. Most home routers don't actually let you do this.

**[01:01:41](https://youtube.com/watch?v=7EoCa9HP9Bc&t=3701s)** You will need to also give the Docker containers their own IPv6 address from the prefix that the

**[01:01:47](https://youtube.com/watch?v=7EoCa9HP9Bc&t=3707s)** NAT device is handed out. It's an advanced thing at the moment and it's generally because most ISPs

**[01:01:53](https://youtube.com/watch?v=7EoCa9HP9Bc&t=3713s)** don't send you a router that has IPv6 available. If you have your own router, like I have a unified

**[01:01:59](https://youtube.com/watch?v=7EoCa9HP9Bc&t=3719s)** router that I can enable IPv6, so all the addresses in my house get IPv6 addresses. So that's the way

**[01:02:05](https://youtube.com/watch?v=7EoCa9HP9Bc&t=3725s)** to solve that problem. It will depend on the different types of networking, sorry, the different

**[01:02:09](https://youtube.com/watch?v=7EoCa9HP9Bc&t=3729s)** types of equipment that you have at home, but the answer is that you need to enable IPv6 on the

**[01:02:14](https://youtube.com/watch?v=7EoCa9HP9Bc&t=3734s)** actual network that you're on. And what that means is your laptop or your server that is

**[01:02:19](https://youtube.com/watch?v=7EoCa9HP9Bc&t=3739s)** running the Docker containers needs an IPv6 address, and then you could hand an IPv6 address to

**[01:02:23](https://youtube.com/watch?v=7EoCa9HP9Bc&t=3743s)** the Docker container as well. I actually don't know if Docker supports IPv6 very well right now.

**[01:02:28](https://youtube.com/watch?v=7EoCa9HP9Bc&t=3748s)** So I don't know if that's actually even possible, something for me to look up. But again, Kevin,

**[01:02:33](https://youtube.com/watch?v=7EoCa9HP9Bc&t=3753s)** please feel free to come to our SE office hours that are once a month, and we'd love to talk about

**[01:02:38](https://youtube.com/watch?v=7EoCa9HP9Bc&t=3758s)** that in more detail. I think that's a really great question. Answer live. Are you willing to

**[01:02:43](https://youtube.com/watch?v=7EoCa9HP9Bc&t=3763s)** explore solution to that direct connections on the UKS with private or public networks using AWS

**[01:02:47](https://youtube.com/watch?v=7EoCa9HP9Bc&t=3767s)** CNI? I think I've really covered this Gabrielle. It's out about hands. If you use the EKS,

**[01:02:53](https://youtube.com/watch?v=7EoCa9HP9Bc&t=3773s)** CNI, and you have private subnets, you are not going to get direct connections. We really can't

**[01:03:00](https://youtube.com/watch?v=7EoCa9HP9Bc&t=3780s)** offer that right now. That is because the EKS, CNI, implements fully random outbound connections.

**[01:03:07](https://youtube.com/watch?v=7EoCa9HP9Bc&t=3787s)** That is a decision that was made on a EKS, and I'm afraid there's really not much we can do about

**[01:03:13](https://youtube.com/watch?v=7EoCa9HP9Bc&t=3793s)** that right now. What are the benefits of running your own DURP server? We are also considering,

**[01:03:18](https://youtube.com/watch?v=7EoCa9HP9Bc&t=3798s)** please don't do this. It's really not fun. The benefits are that you get slightly increased

**[01:03:25](https://youtube.com/watch?v=7EoCa9HP9Bc&t=3805s)** throughput. It's not much more than the public DURP servers. You can also collect them locally

**[01:03:30](https://youtube.com/watch?v=7EoCa9HP9Bc&t=3810s)** with your infrastructure. So you get a very, very small increase in latency. I would not recommend

**[01:03:38](https://youtube.com/watch?v=7EoCa9HP9Bc&t=3818s)** running your own DURP server at this point. It's really not something that we recommend.

**[01:03:44](https://youtube.com/watch?v=7EoCa9HP9Bc&t=3824s)** The people that really run their own DURP servers are doing it because they have very restrictive

**[01:03:49](https://youtube.com/watch?v=7EoCa9HP9Bc&t=3829s)** egress environments that they can't whitelist all of tailscales, public IP addresses.

**[01:03:55](https://youtube.com/watch?v=7EoCa9HP9Bc&t=3835s)** Excuse me, I would really not recommend doing this at this point. So yeah, I'm just a massive

**[01:04:01](https://youtube.com/watch?v=7EoCa9HP9Bc&t=3841s)** case. I wanted to know how it works. I get very little value out of my DURP server just to be super

**[01:04:05](https://youtube.com/watch?v=7EoCa9HP9Bc&t=3845s)** clear. It's basically the same as a Seattle DURP server. I'm actually a little bit slower in

**[01:04:10](https://youtube.com/watch?v=7EoCa9HP9Bc&t=3850s)** most situations, but because I talk to customers that are running DURP servers, I wanted to know

**[01:04:15](https://youtube.com/watch?v=7EoCa9HP9Bc&t=3855s)** how they work basically. So I would really not recommend doing that. I don't know what that question

**[01:04:22](https://youtube.com/watch?v=7EoCa9HP9Bc&t=3862s)** is. How can you afford free accounts when all relay traffic goes through your servers? Because we

**[01:04:29](https://youtube.com/watch?v=7EoCa9HP9Bc&t=3869s)** love tailscale and because people pay for tailscale. I'm a solutions engineer. If you love tailscale

**[01:04:33](https://youtube.com/watch?v=7EoCa9HP9Bc&t=3873s)** at home and you want to use it at work and you want to be able to keep getting relay traffic,

**[01:04:37](https://youtube.com/watch?v=7EoCa9HP9Bc&t=3877s)** please talk to us about using tailscale at work and buy an enterprise contract and then we can

**[01:04:41](https://youtube.com/watch?v=7EoCa9HP9Bc&t=3881s)** give all of your home lab users all this excellent relay traffic without having to charge money.

**[01:04:50](https://youtube.com/watch?v=7EoCa9HP9Bc&t=3890s)** We're not going to charge money for relay service. It's part of the contract that we have with our

**[01:04:55](https://youtube.com/watch?v=7EoCa9HP9Bc&t=3895s)** users, but the fact that we're a stable, well-run excellent business with an excellent product means

**[01:04:59](https://youtube.com/watch?v=7EoCa9HP9Bc&t=3899s)** that we can offer this for free. So that's a really great question, Peter. Thank you very much.

**[01:05:05](https://youtube.com/watch?v=7EoCa9HP9Bc&t=3905s)** Why is download speed very slow when they want to have direct connections when using an exit? No,

**[01:05:09](https://youtube.com/watch?v=7EoCa9HP9Bc&t=3909s)** that's a very, very broad question, Gerald. I honestly don't know the answer to that

**[01:05:13](https://youtube.com/watch?v=7EoCa9HP9Bc&t=3913s)** without kind of debugging more. I'd love to know a little bit more about what you're downloading.

**[01:05:18](https://youtube.com/watch?v=7EoCa9HP9Bc&t=3918s)** That's a really great question for our office hours. I feel like that would be better suited

**[01:05:22](https://youtube.com/watch?v=7EoCa9HP9Bc&t=3922s)** to a format where they have a full hour to answer questions. Unfortunately, I can't really answer

**[01:05:26](https://youtube.com/watch?v=7EoCa9HP9Bc&t=3926s)** that without a little bit more information. Where the relay service located, you can have a look

**[01:05:32](https://youtube.com/watch?v=7EoCa9HP9Bc&t=3932s)** at tailscale, do-no-up service. There is a do-up service list here. These are where we're all

**[01:05:38](https://youtube.com/watch?v=7EoCa9HP9Bc&t=3938s)** running do-up service right now, so you can see that really easily on the websites. How do I find

**[01:05:46](https://youtube.com/watch?v=7EoCa9HP9Bc&t=3946s)** the SEO for hours? Office hours. Tim, can you help Kevin find the SEO for hours, please? We have a

**[01:05:52](https://youtube.com/watch?v=7EoCa9HP9Bc&t=3952s)** lot of restrictive egress environments. The only one to allow one IP address with specific

**[01:05:58](https://youtube.com/watch?v=7EoCa9HP9Bc&t=3958s)** pass. How would your best should handle this your own derp server? Can you please email

**[01:06:01](https://youtube.com/watch?v=7EoCa9HP9Bc&t=3961s)** seactailscale.com with that question? I think we probably need to have a bit of a longer conversation

**[01:06:05](https://youtube.com/watch?v=7EoCa9HP9Bc&t=3965s)** about what the restrictive egress environments look like. I'm actually talking to another customer

**[01:06:09](https://youtube.com/watch?v=7EoCa9HP9Bc&t=3969s)** right now that's experiencing this problem. It's not an easy problem to solve. Tailscale makes

**[01:06:13](https://youtube.com/watch?v=7EoCa9HP9Bc&t=3973s)** a lot of assumptions about how it's able to do outbound connectivity. I'm starting to think we

**[01:06:19](https://youtube.com/watch?v=7EoCa9HP9Bc&t=3979s)** probably need to bring our product team into these conversations. Are the downsides of using

**[01:06:24](https://youtube.com/watch?v=7EoCa9HP9Bc&t=3984s)** public subnet routers versus putting ACT, using subnet routers, putting ECS on public subnet?

**[01:06:29](https://youtube.com/watch?v=7EoCa9HP9Bc&t=3989s)** The answer to this question around like are the downsides of using subnet routers versus put an

**[01:06:33](https://youtube.com/watch?v=7EoCa9HP9Bc&t=3993s)** EC2 instance on public subnet? There isn't earlier downside over then it's a security consideration

**[01:06:40](https://youtube.com/watch?v=7EoCa9HP9Bc&t=4000s)** for many organizations. They want to have that public surface area. Also EC2 instances, sorry EC2

**[01:06:49](https://youtube.com/watch?v=7EoCa9HP9Bc&t=4009s)** AWS now charges for public subnet. So public IP addresses. I think the $4 a month each or

**[01:06:55](https://youtube.com/watch?v=7EoCa9HP9Bc&t=4015s)** something like that. So it's a cost consideration. If you want to put all of your EC2 instances in

**[01:07:01](https://youtube.com/watch?v=7EoCa9HP9Bc&t=4021s)** public subnet, you're likely going to have a very easy time when it comes to direct connections.

**[01:07:05](https://youtube.com/watch?v=7EoCa9HP9Bc&t=4025s)** But there are trade-offs that you need to think about around different considerations there.

**[01:07:10](https://youtube.com/watch?v=7EoCa9HP9Bc&t=4030s)** I'm going to ask a one more question. What do you think of the trade-offs using public

**[01:07:17](https://youtube.com/watch?v=7EoCa9HP9Bc&t=4037s)** routers and public VPCs to get direct connections between entity and private VPCs versus hosting

**[01:07:21](https://youtube.com/watch?v=7EoCa9HP9Bc&t=4041s)** the entities on public VPCs with the with the tail scale UDP for outside and firewall?

**[01:07:30](https://youtube.com/watch?v=7EoCa9HP9Bc&t=4050s)** Maybe I'm just kind of my brain. It should go on to sleep now, Nantes. So I'm really sorry.

**[01:07:34](https://youtube.com/watch?v=7EoCa9HP9Bc&t=4054s)** I don't know how to answer this question. I think I've just kind of exhausted my brain capacity

**[01:07:38](https://youtube.com/watch?v=7EoCa9HP9Bc&t=4058s)** right now. And I'm not really understanding it very well. If you wouldn't mind sending

**[01:07:42](https://youtube.com/watch?v=7EoCa9HP9Bc&t=4062s)** bringing this to our, bringing this to our SEO office hours, I would love to try and answer it.

**[01:07:51](https://youtube.com/watch?v=7EoCa9HP9Bc&t=4071s)** Okay. I think this has been pretty comprehensive. I haven't had a chance to read the chat.

**[01:08:00](https://youtube.com/watch?v=7EoCa9HP9Bc&t=4080s)** So I haven't had a chance to look through it yet. I really appreciate everybody who has attended.

**[01:08:06](https://youtube.com/watch?v=7EoCa9HP9Bc&t=4086s)** It's been a wonderful experience being able to talk to you about my experience here. I would

**[01:08:10](https://youtube.com/watch?v=7EoCa9HP9Bc&t=4090s)** stop looking at my second screen here on a bit of the camera. It's been a wonderful experience

**[01:08:14](https://youtube.com/watch?v=7EoCa9HP9Bc&t=4094s)** being able to wrap it on for an hour and 15 minutes. Hopefully I have some new questions. Hopefully

**[01:08:17](https://youtube.com/watch?v=7EoCa9HP9Bc&t=4097s)** I didn't create more questions. I love feedback. So if you enjoyed this webinar, please,

**[01:08:24](https://youtube.com/watch?v=7EoCa9HP9Bc&t=4104s)** I'm going to leave the chat open for another five minutes just to give everybody an opportunity

**[01:08:28](https://youtube.com/watch?v=7EoCa9HP9Bc&t=4108s)** to comment. But if you enjoyed this webinar, please let us know in the comments. I run webinars

**[01:08:35](https://youtube.com/watch?v=7EoCa9HP9Bc&t=4115s)** once a month. We do the SEO office hours. Hopefully Tim posted a link in here that will allow you

**[01:08:42](https://youtube.com/watch?v=7EoCa9HP9Bc&t=4122s)** to join us to ask questions. That's my favorite webinar that we do, by the way, Alex and I just get

**[01:08:47](https://youtube.com/watch?v=7EoCa9HP9Bc&t=4127s)** to hang out, chat with each other, answer questions. We bring a guest. We had Avery RCO on the last one,

**[01:08:53](https://youtube.com/watch?v=7EoCa9HP9Bc&t=4133s)** which was awesome. I learned a lot from that conversation. It looks like we've got lots and lots of

**[01:08:58](https://youtube.com/watch?v=7EoCa9HP9Bc&t=4138s)** questions. So please keep looking coming to our SEO office hours. But really appreciate every time

**[01:09:04](https://youtube.com/watch?v=7EoCa9HP9Bc&t=4144s)** I will leave the chat open for a couple of minutes so everybody can can post their comments.

**[01:09:10](https://youtube.com/watch?v=7EoCa9HP9Bc&t=4150s)** But thank you very much. I'm going to go off video now. I'm going to take a big sigh of relief

**[01:09:14](https://youtube.com/watch?v=7EoCa9HP9Bc&t=4154s)** and hopefully you all enjoyed the experience. Thank you so much.

---

*Automatically generated transcript. May contain errors.*
