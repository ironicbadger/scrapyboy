---
video_id: "2r8YnvXLKFU"
title: "Ask a Tailscale Expert"
description: "Join and have your questions answered by Tailscale expert engineers in real time...."
channel_name: "Tailscale"
channel_id: "UCcdv38QxPjSMqbt5ffLhJLA"
published_at: "2025-03-05"
duration_seconds: 3428
youtube_url: "https://www.youtube.com/watch?v=2r8YnvXLKFU"
thumbnail_url: "https://i.ytimg.com/vi/2r8YnvXLKFU/maxresdefault.jpg"

# Transcription metadata
transcribed_at: "2025-10-03T17:46:41.657057"
transcription_method: "cpu"
model_used: "base"
language: "en"
word_count: 10429
transcription_time_seconds: 96.8
---

# Ask a Tailscale Expert

**[00:00](https://youtube.com/watch?v=2r8YnvXLKFU&t=0s)** We're good. We are live. Hello, YouTube. Hello, Zoom. Welcome into another Tailscale. Ask the experts. I'm Alex. I'm Lee. And I think Lee has some fun show and tell stuff to get us started for this week. But yeah, what have you been up to, Lee? It's been pretty busy. We have sales quarter that ends at the end of January, so pretty busy at the end of January with all the customers excited.

**[00:30](https://youtube.com/watch?v=2r8YnvXLKFU&t=30s)** To become Tailscale customers on the Solutions Engineering team. What about you? How's the content coming at the moment? I've seen some amazing videos. I really enjoyed the monitoring one. What's next on the docket?

**[00:44](https://youtube.com/watch?v=2r8YnvXLKFU&t=44s)** We've got two or three in the bank ready to go. There's one about Nick's OS and Nvidia GPUs and self-hosted Olamas stuff, like all rolled into one as this massive mega video that's coming out in the next couple of days.

**[00:57](https://youtube.com/watch?v=2r8YnvXLKFU&t=57s)** As soon as I finished editing it, because I've got like two hours worth of footage to go through. Another problem. We've got one talking about Tailscale and ZTNA.

**[01:07](https://youtube.com/watch?v=2r8YnvXLKFU&t=67s)** It should be quite cool one coming up probably next week or so. Maybe a little bit behind the scenes, how they make the sausage on how Tailscale makes YouTube videos too. That's coming up soon.

**[01:17](https://youtube.com/watch?v=2r8YnvXLKFU&t=77s)** That's going to be awesome. I'm excited. It's one of the only channels I subscribe to. My algorithm is nice and clean. It's just Tailscale videos all the way through. No complaints for me.

**[01:31](https://youtube.com/watch?v=2r8YnvXLKFU&t=91s)** The monitoring one actually inspired some of the show and tell stuff, but I thought we usually have a little bit of a five minutes while questions roll in.

**[01:41](https://youtube.com/watch?v=2r8YnvXLKFU&t=101s)** I thought I'd just do a little bit of show and tell of the stuff I've been building to make customers lives easier while we wait.

**[01:49](https://youtube.com/watch?v=2r8YnvXLKFU&t=109s)** Please send us any questions in. We will get to them in a few moments. I want to make sure that we've got a little bit of time for people to come up with the questions.

**[01:56](https://youtube.com/watch?v=2r8YnvXLKFU&t=116s)** In the meantime, how about I do a little bit of a demo, Alex? How does that sound?

**[02:00](https://youtube.com/watch?v=2r8YnvXLKFU&t=120s)** That sounds pretty good, but before you do, I just see there's one comment in the YouTube chat saying our audio is out of sync.

**[02:08](https://youtube.com/watch?v=2r8YnvXLKFU&t=128s)** If that's the case, please drop a comment. Let us know. I don't know what I can do to fix it, but we'll try something.

**[02:14](https://youtube.com/watch?v=2r8YnvXLKFU&t=134s)** Hopefully it's just one person that's having the issue. So fingers crossed.

**[02:18](https://youtube.com/watch?v=2r8YnvXLKFU&t=138s)** My voice and my voice and my mouth seem to be in sync. So I don't know what else I can do at that point.

**[02:24](https://youtube.com/watch?v=2r8YnvXLKFU&t=144s)** We're in sync.

**[02:26](https://youtube.com/watch?v=2r8YnvXLKFU&t=146s)** Yeah, indeed.

**[02:28](https://youtube.com/watch?v=2r8YnvXLKFU&t=148s)** Yeah, so for those of you unaware, I lead the solutions engineering team at tail scale.

**[02:34](https://youtube.com/watch?v=2r8YnvXLKFU&t=154s)** And our job is to make enterprise and corporate customers successful with tail scale.

**[02:39](https://youtube.com/watch?v=2r8YnvXLKFU&t=159s)** And as you can probably imagine, we do a lot of repetition, right?

**[02:42](https://youtube.com/watch?v=2r8YnvXLKFU&t=162s)** A lot of the same problems come up and a lot of the same questions get asked.

**[02:47](https://youtube.com/watch?v=2r8YnvXLKFU&t=167s)** And so I've been trying to take it by myself as an engineer and a hobbyist software developer to build tooling that helps us kind of remove the repetition.

**[02:58](https://youtube.com/watch?v=2r8YnvXLKFU&t=178s)** So a couple of things that I've built.

**[03:02](https://youtube.com/watch?v=2r8YnvXLKFU&t=182s)** The number one question that we get is why am I not getting direct connections?

**[03:08](https://youtube.com/watch?v=2r8YnvXLKFU&t=188s)** You know, we we have spent probably a hundred personalities just this year dealing with this particular question.

**[03:15](https://youtube.com/watch?v=2r8YnvXLKFU&t=195s)** And they're the information is in the client.

**[03:18](https://youtube.com/watch?v=2r8YnvXLKFU&t=198s)** It's just not surfaced in a way that is super useful.

**[03:21](https://youtube.com/watch?v=2r8YnvXLKFU&t=201s)** And I wanted to kind of take the opportunity to learn a little bit about how tail scale implements this stuff.

**[03:28](https://youtube.com/watch?v=2r8YnvXLKFU&t=208s)** So I kind of rewrote it from first principles and borrowed some of the libraries from tail scale.

**[03:34](https://youtube.com/watch?v=2r8YnvXLKFU&t=214s)** And what I ended up with is a tool that I've written that's called stunner and stunner will do the same thing that tail scale does as it's navigating out of your network and show you what kind of network you behind and what sort of

**[03:50](https://youtube.com/watch?v=2r8YnvXLKFU&t=230s)** knack to type that you behind.

**[03:52](https://youtube.com/watch?v=2r8YnvXLKFU&t=232s)** So you can see here I'm on my.

**[03:55](https://youtube.com/watch?v=2r8YnvXLKFU&t=235s)** Sorry to interrupt.

**[03:56](https://youtube.com/watch?v=2r8YnvXLKFU&t=236s)** Sorry to interrupt you there Lee.

**[03:57](https://youtube.com/watch?v=2r8YnvXLKFU&t=237s)** Would you mind just making that a little bit bigger?

**[04:00](https://youtube.com/watch?v=2r8YnvXLKFU&t=240s)** Please absolutely.

**[04:01](https://youtube.com/watch?v=2r8YnvXLKFU&t=241s)** Absolutely.

**[04:02](https://youtube.com/watch?v=2r8YnvXLKFU&t=242s)** Thank you very much.

**[04:03](https://youtube.com/watch?v=2r8YnvXLKFU&t=243s)** But there you go.

**[04:04](https://youtube.com/watch?v=2r8YnvXLKFU&t=244s)** Exactly.

**[04:05](https://youtube.com/watch?v=2r8YnvXLKFU&t=245s)** Yeah. That's great. Thanks.

**[04:06](https://youtube.com/watch?v=2r8YnvXLKFU&t=246s)** Yeah.

**[04:07](https://youtube.com/watch?v=2r8YnvXLKFU&t=247s)** So what this does is essentially like copies the logic that we use within tail scale to create directions between clients.

**[04:15](https://youtube.com/watch?v=2r8YnvXLKFU&t=255s)** And you can see I've reached out to a couple of our dirt servers, making a cut out by our connection.

**[04:22](https://youtube.com/watch?v=2r8YnvXLKFU&t=262s)** And if those two requests use the same port, then I have a certain type of nap that I'm behind.

**[04:29](https://youtube.com/watch?v=2r8YnvXLKFU&t=269s)** And I've kind of surfaced this in a way, which I think is more accessible than what we have in the tail scale client.

**[04:36](https://youtube.com/watch?v=2r8YnvXLKFU&t=276s)** Now you can get a lot of this information from the tail scale net check command.

**[04:40](https://youtube.com/watch?v=2r8YnvXLKFU&t=280s)** But it isn't super accessible to, you know, people who aren't familiar with that information.

**[04:46](https://youtube.com/watch?v=2r8YnvXLKFU&t=286s)** So just to rerun it again, you can see it's actually going to tell me what sort of port mapping I'm using the port that I'm actually using when I'm making that out by request.

**[04:56](https://youtube.com/watch?v=2r8YnvXLKFU&t=296s)** And it's going to give me a best yes effort of understanding what sort of map type that I'm behind.

**[05:02](https://youtube.com/watch?v=2r8YnvXLKFU&t=302s)** This is my home internet. I have you PNP enabled on my firewall for better or worse, you know, video games need you PNP generally.

**[05:10](https://youtube.com/watch?v=2r8YnvXLKFU&t=310s)** So another example of what this looks like is behind my nemesis, the AWS managed map gateway.

**[05:17](https://youtube.com/watch?v=2r8YnvXLKFU&t=317s)** So you can see here I'm in an EC2 instance and I'm going to run Stona with the debug command.

**[05:22](https://youtube.com/watch?v=2r8YnvXLKFU&t=322s)** And it will show you all of the requests that it's actually doing, so it shows you the dirt service that's sending to the type of request that it's sending.

**[05:30](https://youtube.com/watch?v=2r8YnvXLKFU&t=330s)** And you can see behind an AWS managed map gateway, I actually see two different ports when I make the same request.

**[05:36](https://youtube.com/watch?v=2r8YnvXLKFU&t=336s)** So it's going to tell me that I am behind a hardnet. And it's going to tell me the map type from like the RFC definition with a little bit more detail.

**[05:45](https://youtube.com/watch?v=2r8YnvXLKFU&t=345s)** So if you're ever really struggling to understand why you're not getting direct connections between two devices run Stona on both sides.

**[05:51](https://youtube.com/watch?v=2r8YnvXLKFU&t=351s)** So I'll get hold of us put the link in the comments so we could put it in YouTube.

**[05:54](https://youtube.com/watch?v=2r8YnvXLKFU&t=354s)** And it will give you a bunch of information about why that's actually happening.

**[05:59](https://youtube.com/watch?v=2r8YnvXLKFU&t=359s)** I am already chatting with some of the engineering team and the product team, but getting this into the client.

**[06:04](https://youtube.com/watch?v=2r8YnvXLKFU&t=364s)** And I think that's the desired end state. But we'd love to get feedback about being able to visualize it in this way to give you this sense of like how these things work.

**[06:15](https://youtube.com/watch?v=2r8YnvXLKFU&t=375s)** So yeah, that's the first thing that I've been building. I don't have any questions or comments that are coming in Alex that you can send my way.

**[06:22](https://youtube.com/watch?v=2r8YnvXLKFU&t=382s)** So I mean, my first I've got a couple of questions just as a curious nerd like what did you write this in?

**[06:28](https://youtube.com/watch?v=2r8YnvXLKFU&t=388s)** I wrote it in go.

**[06:31](https://youtube.com/watch?v=2r8YnvXLKFU&t=391s)** So it's like I said, I'll send a lot of it is, you know, a lot of it is the same logic that we've actually written this in the client.

**[06:45](https://youtube.com/watch?v=2r8YnvXLKFU&t=405s)** You can see I'm actually using tailscales, netmong package and a bunch of other stuff to actually be able to and the part market package to be actually able to figure out all this stuff.

**[06:55](https://youtube.com/watch?v=2r8YnvXLKFU&t=415s)** So I'm just extracting that information and using it in our own way basically.

**[06:59](https://youtube.com/watch?v=2r8YnvXLKFU&t=419s)** But I wrote in go.

**[07:01](https://youtube.com/watch?v=2r8YnvXLKFU&t=421s)** I have I would call myself a hobbyist go software developer, but you know, good enough to I certainly don't want to be running any production infrastructure right now.

**[07:10](https://youtube.com/watch?v=2r8YnvXLKFU&t=430s)** But I think for these kind of little debugging and friendly tools, I know enough to be dangerous.

**[07:16](https://youtube.com/watch?v=2r8YnvXLKFU&t=436s)** So this this a run anywhere that go runs in theory, anywhere that you've got a command line to install like in terms of dependencies and things like that.

**[07:24](https://youtube.com/watch?v=2r8YnvXLKFU&t=444s)** One of the one of the questions that came in from Sam IP 537 is, can I run this on my Apple TV to figure out what's going on?

**[07:31](https://youtube.com/watch?v=2r8YnvXLKFU&t=451s)** So mainly because you don't have like a command line interface on your Apple TV, however, your Apple TV is behind the same network that all your other machines are behind.

**[07:42](https://youtube.com/watch?v=2r8YnvXLKFU&t=462s)** So you can run it on your laptop and it will give you the same output that your Apple TV is seeing right so like, you know, it's generally going to navigate out through your network.

**[07:51](https://youtube.com/watch?v=2r8YnvXLKFU&t=471s)** So all clients that are behind the same router are going to give you the same information basically.

**[07:57](https://youtube.com/watch?v=2r8YnvXLKFU&t=477s)** You can run it on your Apple TV, but you can run on your laptop and that should give you a good reference point basically.

**[08:03](https://youtube.com/watch?v=2r8YnvXLKFU&t=483s)** And next question again, this isn't Alex question, what is easy net and what is hard net.

**[08:10](https://youtube.com/watch?v=2r8YnvXLKFU&t=490s)** Great question. Yes, so the there's there's lots of different types of net and if we look at here, you can see them all defined.

**[08:20](https://youtube.com/watch?v=2r8YnvXLKFU&t=500s)** Different types of maps right because these are very wordy and difficult to like differentiate like I still struggle with the idea differences between end point independent mapping address dependent mapping address dependent filtering like it's just too complicated for me to be able to start that.

**[08:39](https://youtube.com/watch?v=2r8YnvXLKFU&t=519s)** So luckily when the team started building tail scale and there's a wonderful blog post by Dave Anderson who is an incredible talented engineer and a wonderful technical writer who wrote the blog post how natural virtual works, which a lot of this logic is based on what we what happened is they kind of turned it into three different very easy to remember acronyms.

**[09:00](https://youtube.com/watch?v=2r8YnvXLKFU&t=540s)** We have easy net, which is I can open an outbound port and I can reuse that port for inbound connections.

**[09:07](https://youtube.com/watch?v=2r8YnvXLKFU&t=547s)** We have no net, which is basically you have a public IP address directly attached to the machine that you're on and then hard net, which is I can open an outbound port, but using that for an inbound port is not necessarily okay.

**[09:20](https://youtube.com/watch?v=2r8YnvXLKFU&t=560s)** And so those are the kind of definitions when you run stunner, it will give you the official like RFC definition of the net type and then it will also tell you if it's an easy or a hard not just to kind of make it a little bit easier.

**[09:33](https://youtube.com/watch?v=2r8YnvXLKFU&t=573s)** So I would encourage you to go and take a look at the code as well, like we can just see could define in the constants up here that will give you a little bit information and then there's some logic down here all the way down here around like the net detail and like what different things mean basically.

**[09:50](https://youtube.com/watch?v=2r8YnvXLKFU&t=590s)** So this is actually something if you really want to learn how this stuff works it's a good reference point as well, I think again I'm just kind of condensing the things I have to repeat for customers over and over again into a tool that they can run and see that for themselves basically.

**[10:07](https://youtube.com/watch?v=2r8YnvXLKFU&t=607s)** Yes, exactly that's the mark of a good a good solutions engineer rather than repeat the same thing 10 times a day you write a tool or write a blog post about the thing that you're saying so often.

**[10:19](https://youtube.com/watch?v=2r8YnvXLKFU&t=619s)** I did just drop into the YouTube chat a knowledge base article a technical overview about device connectivity and that walks you through all of the different types of net that lead just articulated for us here.

**[10:31](https://youtube.com/watch?v=2r8YnvXLKFU&t=631s)** But yeah, we need to link to that projectly the Github link.

**[10:34](https://youtube.com/watch?v=2r8YnvXLKFU&t=634s)** I will send it as soon as I shop stop screen sharing, but I do have one more things to show you because.

**[10:38](https://youtube.com/watch?v=2r8YnvXLKFU&t=638s)** Okay, all right.

**[10:39](https://youtube.com/watch?v=2r8YnvXLKFU&t=639s)** One thing just seems so and I wrote this a little while ago and you know it was inspired by you know the video that you made around like monitoring client and points and stuff.

**[10:50](https://youtube.com/watch?v=2r8YnvXLKFU&t=650s)** One thing that I think came up from customer conversations is this is really great information on the client.

**[10:56](https://youtube.com/watch?v=2r8YnvXLKFU&t=656s)** So we release client metrics and ask it a wonderful video about like exposing those client metrics and then using Prometheus to scrape them.

**[11:03](https://youtube.com/watch?v=2r8YnvXLKFU&t=663s)** But that the thought process that I had and that we have from customers is like I don't want to have to stand up an entire monitoring stack to just to be able to see what's going on here.

**[11:11](https://youtube.com/watch?v=2r8YnvXLKFU&t=671s)** Because a Prometheus page will generally just display you a static page of values and then every time you refresh it those values update.

**[11:20](https://youtube.com/watch?v=2r8YnvXLKFU&t=680s)** So I wrote another little tool in the go programming language that can actually periodically hit your metrics and point and show you the changes in these values.

**[11:31](https://youtube.com/watch?v=2r8YnvXLKFU&t=691s)** As things happen now obviously I'm not doing very much over telescope right now so not a lot is happening.

**[11:36](https://youtube.com/watch?v=2r8YnvXLKFU&t=696s)** But if you run this tool met and then point at the end point, which is for a telescope client is the quad 100 for slash metrics.

**[11:44](https://youtube.com/watch?v=2r8YnvXLKFU&t=704s)** It will actually show you like the information. This is compatible with any Prometheus end point.

**[11:50](https://youtube.com/watch?v=2r8YnvXLKFU&t=710s)** So if you have any Prometheus stuff in your environment and you just want to be able to very quickly see a visualization of metrics as they change.

**[11:58](https://youtube.com/watch?v=2r8YnvXLKFU&t=718s)** This is a super useful tool is using some very standard goal libraries that are like able to do like ticking so it will refresh every single time that value changes.

**[12:10](https://youtube.com/watch?v=2r8YnvXLKFU&t=730s)** As I said, I'm not actually doing anything with telescope right now, so you're not seeing any values change.

**[12:15](https://youtube.com/watch?v=2r8YnvXLKFU&t=735s)** If I open another terminal and do a tail scale paying and demo exit node US West.

**[12:27](https://youtube.com/watch?v=2r8YnvXLKFU&t=747s)** You should see that these values will start to change and as the packets start to change.

**[12:32](https://youtube.com/watch?v=2r8YnvXLKFU&t=752s)** And for some reason it's not working, but it does promise you it works.

**[12:36](https://youtube.com/watch?v=2r8YnvXLKFU&t=756s)** It's giving you the capability of being able to see these things in a lot more useful visualization.

**[12:42](https://youtube.com/watch?v=2r8YnvXLKFU&t=762s)** And so if that's something that you have always wanted to do, hopefully that's pretty useful and you'd be able to visualize those things in a lot nicer way.

**[12:51](https://youtube.com/watch?v=2r8YnvXLKFU&t=771s)** Just showing the native client metrics output just to connect how that speaks to your tool.

**[12:59](https://youtube.com/watch?v=2r8YnvXLKFU&t=779s)** Yes, let's do window.

**[13:08](https://youtube.com/watch?v=2r8YnvXLKFU&t=788s)** That's high quality.

**[13:10](https://youtube.com/watch?v=2r8YnvXLKFU&t=790s)** Essentially the client metrics expose things like bytes in bytes out packets, you know, dirt.

**[13:16](https://youtube.com/watch?v=2r8YnvXLKFU&t=796s)** You can see at the bottom, for example, outbound packets total path equals dirt.

**[13:20](https://youtube.com/watch?v=2r8YnvXLKFU&t=800s)** Yeah.

**[13:21](https://youtube.com/watch?v=2r8YnvXLKFU&t=801s)** That's all of stuff is going through a relay service.

**[13:23](https://youtube.com/watch?v=2r8YnvXLKFU&t=803s)** You can create a learning rules in Prometheus to say, hey, look, you've got a certain amount of traffic that's going through a relay server.

**[13:31](https://youtube.com/watch?v=2r8YnvXLKFU&t=811s)** And a direct connection you might want to investigate that.

**[13:34](https://youtube.com/watch?v=2r8YnvXLKFU&t=814s)** Exactly. Yeah.

**[13:35](https://youtube.com/watch?v=2r8YnvXLKFU&t=815s)** And you can see when these values change, it will periodically scrape and you'll be able to actually see.

**[13:42](https://youtube.com/watch?v=2r8YnvXLKFU&t=822s)** You know, when those values change, it's just a nice easy quick visualization.

**[13:46](https://youtube.com/watch?v=2r8YnvXLKFU&t=826s)** If you already have a monitoring infrastructure that you're already using, something like met isn't really going to be helpful.

**[13:51](https://youtube.com/watch?v=2r8YnvXLKFU&t=831s)** But if you are just like a home user and you want to be able to get an indication of like how many packets very quickly for a specific thing is going direct versus dirt, it can be super helpful.

**[14:01](https://youtube.com/watch?v=2r8YnvXLKFU&t=841s)** Now before you stop screen sharing, I have one final question that kind of relates to one of the questions in the YouTube chat talking about we're going to we're going to ignore geopolitical issues just for a second just to maintain sanity.

**[14:13](https://youtube.com/watch?v=2r8YnvXLKFU&t=853s)** But there is a question here talking about from Leet saying it's great to see tailscale as a Canadian company.

**[14:20](https://youtube.com/watch?v=2r8YnvXLKFU&t=860s)** But how much exposure does tailscale have to us cloud infrastructure?

**[14:25](https://youtube.com/watch?v=2r8YnvXLKFU&t=865s)** So Leet, I was hoping you might just run tailscale net check and just give a list of all the dirt service and sort of talk through what tailscale's cloud footprint looks like.

**[14:35](https://youtube.com/watch?v=2r8YnvXLKFU&t=875s)** Absolutely. Yes.

**[14:36](https://youtube.com/watch?v=2r8YnvXLKFU&t=876s)** So tailscale has two cloud footprints that are kind of relevant for customers.

**[14:43](https://youtube.com/watch?v=2r8YnvXLKFU&t=883s)** The first is the control plane and the control plane is what tailscale uses to do things like authenticate you against your identity provider and authenticate you like from a key perspective.

**[14:56](https://youtube.com/watch?v=2r8YnvXLKFU&t=896s)** So it uses it we use the control plane to distribute public keys to all the different clients.

**[15:00](https://youtube.com/watch?v=2r8YnvXLKFU&t=900s)** That stuff is all hosted within Amazon Web Services in the Frankfurt region of Amazon Web Services.

**[15:09](https://youtube.com/watch?v=2r8YnvXLKFU&t=909s)** We do have a control plane that is located in the United States that we have for our enterprise customers that have compliance needs for being able to locate all of their infrastructure in the United States.

**[15:23](https://youtube.com/watch?v=2r8YnvXLKFU&t=923s)** It's worth pointing out that the control plane never sees any of your traffic. No traffic goes through the control plane. So that's basically login dot tailscale.com and then control plane control plane dot tailscale.com.

**[15:34](https://youtube.com/watch?v=2r8YnvXLKFU&t=934s)** That's only really used to authenticate you and distribute keys between different devices.

**[15:38](https://youtube.com/watch?v=2r8YnvXLKFU&t=938s)** The dirt servers are what are used to be able to different to be able to connect to clients together.

**[15:44](https://youtube.com/watch?v=2r8YnvXLKFU&t=944s)** Whether that is via the stone protocol, which you saw with stunner earlier, which is basically sending requests to be able to create direct connection between two things or in a situation where you can't create direct connections.

**[15:55](https://youtube.com/watch?v=2r8YnvXLKFU&t=955s)** The dirt servers will actually relay traffic encrypted traffic and its job is to say pass this packet from this client to this client. Don't decrypt it. Don't inspect it. Don't look at it.

**[16:05](https://youtube.com/watch?v=2r8YnvXLKFU&t=965s)** This is a list of all the dirt servers that we currently have in operation. And as you can see, it will use the one that has got the lowest latency to you to be able to be able to do those connections.

**[16:15](https://youtube.com/watch?v=2r8YnvXLKFU&t=975s)** Like, I actually run my own depth server because I am a glutton for punishment and you can see everyone in the London region or one in the Seattle region.

**[16:22](https://youtube.com/watch?v=2r8YnvXLKFU&t=982s)** But we have lots in the United States across geographical distributed across the United States.

**[16:27](https://youtube.com/watch?v=2r8YnvXLKFU&t=987s)** And then we also have lots of dirt servers around the world. So we have some in Tokyo, London, Paris, Amsterdam, you get the idea.

**[16:34](https://youtube.com/watch?v=2r8YnvXLKFU&t=994s)** If you like, you can actually set up your dirt map to only use specific dirt servers if you have a reason to do so.

**[16:43](https://youtube.com/watch?v=2r8YnvXLKFU&t=1003s)** And so that is documented in our knowledge base. So you can just basically update your dirt map and say, I want to emit all United States dirt servers from my connectivity.

**[16:54](https://youtube.com/watch?v=2r8YnvXLKFU&t=1014s)** If you really don't want any of your traffic going through the continental United States, that is easy to do.

**[17:00](https://youtube.com/watch?v=2r8YnvXLKFU&t=1020s)** You know, we often have on the solutions engineering team team. We often have requests from customers that only want to keep their traffic in a specific geographical region because they have compliance needs or, you know, like healthcare providers in the United States generally don't want to use European infrastructure for a variety of reasons.

**[17:19](https://youtube.com/watch?v=2r8YnvXLKFU&t=1039s)** Usually it's compliance base. It is possible to do that. And there is documentation out there to be able to do that for you.

**[17:27](https://youtube.com/watch?v=2r8YnvXLKFU&t=1047s)** That's fascinating stuff. Thank you, Lee. I didn't actually know that you could geo fence dirt servers like that. So I've put a link for the documentation for all of our dirt server stuff into the YouTube chat. And I think our admins just plot it into the zoom chat as well. So follow up question.

**[17:44](https://youtube.com/watch?v=2r8YnvXLKFU&t=1064s)** You mentioned you run your own dirt server to two two questions from me on that one. No one. Why a number to should you.

**[17:53](https://youtube.com/watch?v=2r8YnvXLKFU&t=1073s)** I do it because our some of our customers need to do it. And I want to know how it works and how it operates and I can't really advise them on how to do that unless I have done it myself.

**[18:05](https://youtube.com/watch?v=2r8YnvXLKFU&t=1085s)** That's the main reason the other reason is I have come from an infrastructure background and like hosting infrastructure in the same way that you do.

**[18:14](https://youtube.com/watch?v=2r8YnvXLKFU&t=1094s)** It's one of those things that you just never stop enjoying. Should you do it? The answer for almost every customer and every user of tell scale is no.

**[18:23](https://youtube.com/watch?v=2r8YnvXLKFU&t=1103s)** And the reason for that is running a dirt server has infrastructure implications in terms of cost. It has infrastructure implications in terms of like overhead. It's not easy.

**[18:33](https://youtube.com/watch?v=2r8YnvXLKFU&t=1113s)** The reason it's not easy is because you're essentially running the equivalent of a content distribution network.

**[18:40](https://youtube.com/watch?v=2r8YnvXLKFU&t=1120s)** And you know that is expensive and hard and there's a reason the organization is charging a lot of money for CDNs.

**[18:48](https://youtube.com/watch?v=2r8YnvXLKFU&t=1128s)** But that's mainly the reason now why might want to run a dirt server.

**[18:54](https://youtube.com/watch?v=2r8YnvXLKFU&t=1134s)** The first reason is that if you need to have very specific addresses that your tell scale clients connect to and you don't want those to change.

**[19:03](https://youtube.com/watch?v=2r8YnvXLKFU&t=1143s)** We at tell scale run a whole bunch of dirt servers and we can't guarantee that our on a Lulu.

**[19:09](https://youtube.com/watch?v=2r8YnvXLKFU&t=1149s)** The server is going to change its IP address in the future. It's done by a DNS. So enterprise customers use white listing for outbound connectivity.

**[19:18](https://youtube.com/watch?v=2r8YnvXLKFU&t=1158s)** And as a result, they need to have predictability and what those dirt servers are doing. And so we advise them to run their on dirt server with our support and help.

**[19:26](https://youtube.com/watch?v=2r8YnvXLKFU&t=1166s)** The other reason is that certain countries have restrictions on their outbound internet connectivity and public infrastructure is usually blacklisted.

**[19:37](https://youtube.com/watch?v=2r8YnvXLKFU&t=1177s)** I'm not naming any countries, but I'm sure you can probably bridge the gap there.

**[19:41](https://youtube.com/watch?v=2r8YnvXLKFU&t=1181s)** And in those situations running your own dirt server can be useful.

**[19:45](https://youtube.com/watch?v=2r8YnvXLKFU&t=1185s)** I do actually maintain, again, this is not a official tell scale product. This is maintained by me individually with all of the things that come through that.

**[19:56](https://youtube.com/watch?v=2r8YnvXLKFU&t=1196s)** I do maintain a RPM package for dirt servers. You can see I just posted it in the zoom chat. Hopefully we can share that out to everybody in the YouTube chat as well.

**[20:10](https://youtube.com/watch?v=2r8YnvXLKFU&t=1210s)** If you want to do this, then go ahead. But I will not be helping you because that's too much work for me.

**[20:16](https://youtube.com/watch?v=2r8YnvXLKFU&t=1216s)** So yeah, just just bear that in mind as like a consideration here. It's not something that we recommend for a variety of reasons.

**[20:26](https://youtube.com/watch?v=2r8YnvXLKFU&t=1226s)** Fascinating stuff. Thank you for sharing all of that that Lee. Don't forget to share us the GitHub link for your.

**[20:34](https://youtube.com/watch?v=2r8YnvXLKFU&t=1234s)** And now for us, Stona, yeah.

**[20:37](https://youtube.com/watch?v=2r8YnvXLKFU&t=1237s)** Well, I haven't watched WWE wrestling for 20 years, and I have no intention to start again, but I come from the days of stone call Steve Austin.

**[20:48](https://youtube.com/watch?v=2r8YnvXLKFU&t=1248s)** And when I saw the opportunity to call something, Stona, I jumped at the chance. And I think for the first time in 20 years, I saw a bunch of WWE stuff around.

**[20:59](https://youtube.com/watch?v=2r8YnvXLKFU&t=1259s)** I don't know, John Cena apparently did something that was, you know, I don't know, but I was like, Oh, I'm definitely going to name something after my childhood here.

**[21:09](https://youtube.com/watch?v=2r8YnvXLKFU&t=1269s)** So yeah, welcome to WWE happy hour with Alex and Lee.

**[21:13](https://youtube.com/watch?v=2r8YnvXLKFU&t=1273s)** We know nothing but we'll try.

**[21:16](https://youtube.com/watch?v=2r8YnvXLKFU&t=1276s)** Yeah, goodness me. That takes me back. I can smell what the Rock is cooking even from here.

**[21:21](https://youtube.com/watch?v=2r8YnvXLKFU&t=1281s)** Exactly. Yeah, he's still in there apparently. I heard yesterday. So yeah.

**[21:26](https://youtube.com/watch?v=2r8YnvXLKFU&t=1286s)** Well, let's jump to some of the questions. Thank you for that show and tell Lee. I learned a lot, and I hope some of the audience did too.

**[21:36](https://youtube.com/watch?v=2r8YnvXLKFU&t=1296s)** Calla B.I. 19. I budget that obviously, but says I'm not lying. I literally set up my first outside the network tail for myself using the audio bookshelf self hosted app.

**[21:49](https://youtube.com/watch?v=2r8YnvXLKFU&t=1309s)** Not kidding. Wow. That was easy. Awesome. Not a question. Apparently, but.

**[21:54](https://youtube.com/watch?v=2r8YnvXLKFU&t=1314s)** I'll go. I love it. You know what? We just we just keep the keep the nice words coming. We love it. Yes.

**[22:00](https://youtube.com/watch?v=2r8YnvXLKFU&t=1320s)** We'll take compliments and cash those checks all day. So.

**[22:04](https://youtube.com/watch?v=2r8YnvXLKFU&t=1324s)** Quick question from zoom about stunner, saying, I like the idea of it, and I tried installing it yesterday, but I couldn't quite figure out how to do it on Linux.

**[22:12](https://youtube.com/watch?v=2r8YnvXLKFU&t=1332s)** The doc said to download the binary from the release, but I couldn't quite figure out how to do that. Could you potentially add a snippet for people like me?

**[22:19](https://youtube.com/watch?v=2r8YnvXLKFU&t=1339s)** I will date the read me that shows you exactly how to do that. Absolutely.

**[22:23](https://youtube.com/watch?v=2r8YnvXLKFU&t=1343s)** Good stuff. Okay. So next question is about using a Raspberry Pi to be as an exit node.

**[22:30](https://youtube.com/watch?v=2r8YnvXLKFU&t=1350s)** And this person is called Andreas and they're on YouTube and they're routing incoming traffic through private internet access, a third party privacy VPN.

**[22:40](https://youtube.com/watch?v=2r8YnvXLKFU&t=1360s)** How does this work when PIA starts after tail scale on boot? Can I do this via Docker when tail scales already as the lot on the host?

**[22:50](https://youtube.com/watch?v=2r8YnvXLKFU&t=1370s)** And I'm happy if you want to have to take a stab at this, but I can also take a stab at it.

**[22:56](https://youtube.com/watch?v=2r8YnvXLKFU&t=1376s)** Yeah.

**[22:57](https://youtube.com/watch?v=2r8YnvXLKFU&t=1377s)** I think it's going to be a question of just getting your system D unit dependencies in the correct order.

**[23:02](https://youtube.com/watch?v=2r8YnvXLKFU&t=1382s)** You can do a bunch of stuff with PIA I think about what's called a VPN kill switch. If I'm understanding the question correctly, you don't want traffic to leave the host.

**[23:12](https://youtube.com/watch?v=2r8YnvXLKFU&t=1392s)** Unless it's going through PIA, at least I think that's what the question is asking.

**[23:16](https://youtube.com/watch?v=2r8YnvXLKFU&t=1396s)** So you'll be looking to Google around terms like VPN kill switch and that kind of thing.

**[23:20](https://youtube.com/watch?v=2r8YnvXLKFU&t=1400s)** I'll be honest, I don't know the exact specifics of how to set that up.

**[23:23](https://youtube.com/watch?v=2r8YnvXLKFU&t=1403s)** I've never needed that kind of thing, but lead. Do you know?

**[23:26](https://youtube.com/watch?v=2r8YnvXLKFU&t=1406s)** Yeah. I mean, our recommendation for on the solutions engineering team.

**[23:31](https://youtube.com/watch?v=2r8YnvXLKFU&t=1411s)** And obviously, I think consumer mileage may vary and we recognize that consumer users of tail scale likely want to have different VPNs for different uses.

**[23:39](https://youtube.com/watch?v=2r8YnvXLKFU&t=1419s)** So like they want to be able to do tail scale at home and PIA or other solutions for like full tunnel.

**[23:47](https://youtube.com/watch?v=2r8YnvXLKFU&t=1427s)** Our recommendation on the solution engineering team is.

**[23:50](https://youtube.com/watch?v=2r8YnvXLKFU&t=1430s)** Do not run to VPNs together.

**[23:52](https://youtube.com/watch?v=2r8YnvXLKFU&t=1432s)** And the reason for that is that they both have the same job which to update your route table, right?

**[23:57](https://youtube.com/watch?v=2r8YnvXLKFU&t=1437s)** So let's say you have PIA that is a wire god based implementation that's running on your machine.

**[24:04](https://youtube.com/watch?v=2r8YnvXLKFU&t=1444s)** It's likely added a route to your route table that says for the default route wild zero send all traffic through this particular interface, right, which has been added.

**[24:15](https://youtube.com/watch?v=2r8YnvXLKFU&t=1455s)** Usually it's a ton device if it's Linux or OSX and then windows it's, I don't know, ton device.

**[24:20](https://youtube.com/watch?v=2r8YnvXLKFU&t=1460s)** Maybe I don't know, it's been a long time since I've used windows.

**[24:23](https://youtube.com/watch?v=2r8YnvXLKFU&t=1463s)** Tail scale does exactly the same thing.

**[24:26](https://youtube.com/watch?v=2r8YnvXLKFU&t=1466s)** And so in tail scale split tunnel mode, you basically add a route for the tail net addresses, which is at the carrier grade net space to go through a specific ton device.

**[24:36](https://youtube.com/watch?v=2r8YnvXLKFU&t=1476s)** As soon as you add a exit node, you know, have two things adding default routes right.

**[24:41](https://youtube.com/watch?v=2r8YnvXLKFU&t=1481s)** So you can get it working, but it is very much advanced mode.

**[24:47](https://youtube.com/watch?v=2r8YnvXLKFU&t=1487s)** And it's not something that we recommend for people that just want to have an easy experience with running VPNs right.

**[24:53](https://youtube.com/watch?v=2r8YnvXLKFU&t=1493s)** My recommendation is if you if you if you really like PIA, we recommend using that for, you know, full tall.

**[25:01](https://youtube.com/watch?v=2r8YnvXLKFU&t=1501s)** We do have an exit node add on which I think is extremely competitive and pricing wide with mobile, which has a long history of excellent privacy considerations and zero logging and all the things that you would want offer consumer grade VPN.

**[25:17](https://youtube.com/watch?v=2r8YnvXLKFU&t=1517s)** And you can use those as exit nodes in tail scale.

**[25:22](https://youtube.com/watch?v=2r8YnvXLKFU&t=1522s)** Now I'm going to preempt a question that we often get here, which is basically, well, I have a mobile that subscription.

**[25:28](https://youtube.com/watch?v=2r8YnvXLKFU&t=1528s)** Why can't I bring that over to tail scale, which is something that comes up all the time.

**[25:33](https://youtube.com/watch?v=2r8YnvXLKFU&t=1533s)** The reason for that is that we don't actually know what anything about your mobile subscription.

**[25:37](https://youtube.com/watch?v=2r8YnvXLKFU&t=1537s)** We don't know anything about what you're paying who you are, what you're billing addresses, all those interesting things.

**[25:43](https://youtube.com/watch?v=2r8YnvXLKFU&t=1543s)** So we can't like just grab your mobile that subscription and bring it into tail scale.

**[25:47](https://youtube.com/watch?v=2r8YnvXLKFU&t=1547s)** And that situation is cancel you more that subscription, do it through tail scale.

**[25:51](https://youtube.com/watch?v=2r8YnvXLKFU&t=1551s)** Everything will be great and you will have a wonderful time.

**[25:55](https://youtube.com/watch?v=2r8YnvXLKFU&t=1555s)** There's some questions and sort of follow up discussion happening in the YouTube live chat right now, which I absolutely love by the way.

**[26:01](https://youtube.com/watch?v=2r8YnvXLKFU&t=1561s)** Talking about so you can use glue ton as a sidecar proxy to route traffic through that way and use the network service mode stuff in Docker compose.

**[26:09](https://youtube.com/watch?v=2r8YnvXLKFU&t=1569s)** I've made several videos about on the channel.

**[26:11](https://youtube.com/watch?v=2r8YnvXLKFU&t=1571s)** The other thing talking in there is saying I would from boss man saying I would love to see support for custom exit nodes.

**[26:20](https://youtube.com/watch?v=2r8YnvXLKFU&t=1580s)** Not just Mulvad stuff, so maybe custom wire guard endpoints or open VPN print.

**[26:26](https://youtube.com/watch?v=2r8YnvXLKFU&t=1586s)** You knew there were a wire guard company, right? Open VPN.

**[26:29](https://youtube.com/watch?v=2r8YnvXLKFU&t=1589s)** We're not doing open VPN.

**[26:30](https://youtube.com/watch?v=2r8YnvXLKFU&t=1590s)** Has anybody used open VPN lately?

**[26:32](https://youtube.com/watch?v=2r8YnvXLKFU&t=1592s)** It's a miserable experience for me, but that's just my opinion.

**[26:36](https://youtube.com/watch?v=2r8YnvXLKFU&t=1596s)** Yeah, custom wire guard endpoints would be an interesting one, but I think there's probably a few technical impediments that might stand in the way of that.

**[26:42](https://youtube.com/watch?v=2r8YnvXLKFU&t=1602s)** Unfortunately, not least of which, how do you get the keys on the remote device?

**[26:46](https://youtube.com/watch?v=2r8YnvXLKFU&t=1606s)** One of the things that happens when you enroll and you know it into your tail net is the control server likely was talking about a couple of minutes ago.

**[26:53](https://youtube.com/watch?v=2r8YnvXLKFU&t=1613s)** The control server does the key exchange for you.

**[26:57](https://youtube.com/watch?v=2r8YnvXLKFU&t=1617s)** And so because of the way that wire guard works using public key infrastructure, you can't rely on.

**[27:04](https://youtube.com/watch?v=2r8YnvXLKFU&t=1624s)** Any other mechanism for authentication except keys, so.

**[27:08](https://youtube.com/watch?v=2r8YnvXLKFU&t=1628s)** Not saying it's impossible because all, you know, ostensibly all things are possible really, but there just be.

**[27:16](https://youtube.com/watch?v=2r8YnvXLKFU&t=1636s)** I don't know, like we've already shipped clients for so many operating systems like a custom like vanilla wire guard support.

**[27:23](https://youtube.com/watch?v=2r8YnvXLKFU&t=1643s)** I don't see that one coming.

**[27:25](https://youtube.com/watch?v=2r8YnvXLKFU&t=1645s)** I believe I believe that one of our engineers did like a thought experiment of like, how would you add a wire guard peer to tail scale.

**[27:36](https://youtube.com/watch?v=2r8YnvXLKFU&t=1656s)** And it is definitely possible, but the number of hopes that they have to jump through to make it work was just not something that was.

**[27:44](https://youtube.com/watch?v=2r8YnvXLKFU&t=1664s)** I think it's worth remembering like, you know, we have a very technical audience here and we have a lot of people who are everything from tinkerers to running production infrastructure on the internet like.

**[27:58](https://youtube.com/watch?v=2r8YnvXLKFU&t=1678s)** Tell us those job is to work for everybody, whether it's your, you know, your family member who just wants to be able to watch your totally legal media collection on your.

**[28:08](https://youtube.com/watch?v=2r8YnvXLKFU&t=1688s)** Or you know, whatever media or hosting a whole that we have to cater to every single, you know, technological use case.

**[28:18](https://youtube.com/watch?v=2r8YnvXLKFU&t=1698s)** And you know, when we've designed and build products, we want to make sure that it's approachable for everybody.

**[28:25](https://youtube.com/watch?v=2r8YnvXLKFU&t=1705s)** So, you know, and that is something that you have to think about like I think there's a lot of people who are watching along and like, yeah, I totally love to connect my wire guard to this.

**[28:33](https://youtube.com/watch?v=2r8YnvXLKFU&t=1713s)** So, I think it's really important to increase the complexity in that way, it increased the complexity of the product, which means that less people get the benefits out of it.

**[28:40](https://youtube.com/watch?v=2r8YnvXLKFU&t=1720s)** Yeah, and that actually does tell us pretty nicely into another question I saw come through.

**[28:44](https://youtube.com/watch?v=2r8YnvXLKFU&t=1724s)** I can't find it, but I remember what it was of, is there any progress for ESP 32 supports and microcontrollers and ESP home and that kind of thing.

**[28:53](https://youtube.com/watch?v=2r8YnvXLKFU&t=1733s)** I'm going to be along the same lines, to be honest, and I know that ESP home added native wire guard support a few months ago.

**[29:00](https://youtube.com/watch?v=2r8YnvXLKFU&t=1740s)** But as I'm a, as of right now, I don't think it's capable of running the go based implementation of wire guard that we use as tail scale.

**[29:08](https://youtube.com/watch?v=2r8YnvXLKFU&t=1748s)** So for right now, the answer is no on that one, I'm afraid, but you know, the stranger things have happened.

**[29:15](https://youtube.com/watch?v=2r8YnvXLKFU&t=1755s)** We are a request driven company. If you, if all the people who want to do tail scale on that micro architecture, comment tell us about it.

**[29:26](https://youtube.com/watch?v=2r8YnvXLKFU&t=1766s)** That is a pretty strong product focus for us, right? Like, we want to meet as many people where they are as they can and we start with the most popular requests.

**[29:36](https://youtube.com/watch?v=2r8YnvXLKFU&t=1776s)** Yeah. Go and round up all of your microcontroller colleagues and open get hope issues and upload it that will certainly turn our heads.

**[29:46](https://youtube.com/watch?v=2r8YnvXLKFU&t=1786s)** Are you much of a tail drop family?

**[29:50](https://youtube.com/watch?v=2r8YnvXLKFU&t=1790s)** I certainly am for my own personal use. Again, like I use most of the enterprise features on a solutions engineering team and I think what's so valuable about chatting is that we have that rounded view of tail scale from like customers versus consumers.

**[30:05](https://youtube.com/watch?v=2r8YnvXLKFU&t=1805s)** I use it for my own stuff, but I wouldn't say that we see a lot of usage of it on the enterprise tier.

**[30:11](https://youtube.com/watch?v=2r8YnvXLKFU&t=1811s)** Yeah, primarily because you know, if you're an enterprise, you don't want people to be able to just randomly take intellectual property out of your business.

**[30:19](https://youtube.com/watch?v=2r8YnvXLKFU&t=1819s)** So yeah, it's usually turned off for enterprise customers and is you have to explicitly opt into turning it on.

**[30:27](https://youtube.com/watch?v=2r8YnvXLKFU&t=1827s)** Well, there's a YouTube question from bossman about tail drop asking whether it's possible to work with tagged devices in the future.

**[30:37](https://youtube.com/watch?v=2r8YnvXLKFU&t=1837s)** I'm going to defer to you on that one.

**[30:39](https://youtube.com/watch?v=2r8YnvXLKFU&t=1839s)** Yeah, I'm not sure.

**[30:40](https://youtube.com/watch?v=2r8YnvXLKFU&t=1840s)** I literally just copy photos and videos from my phone to my laptop.

**[30:43](https://youtube.com/watch?v=2r8YnvXLKFU&t=1843s)** Right. Yeah.

**[30:44](https://youtube.com/watch?v=2r8YnvXLKFU&t=1844s)** It's not drops. Oh, yeah.

**[30:45](https://youtube.com/watch?v=2r8YnvXLKFU&t=1845s)** I don't know the answer to that. I'm afraid.

**[30:47](https://youtube.com/watch?v=2r8YnvXLKFU&t=1847s)** Well, it's it's kind of like a drop, but to any device really so you could be a phone, it could be a laptop, it could be a server, whatever.

**[30:55](https://youtube.com/watch?v=2r8YnvXLKFU&t=1855s)** And as long as it's on the tail net tail drop will let you send files between those devices.

**[31:00](https://youtube.com/watch?v=2r8YnvXLKFU&t=1860s)** Boss man, we're going to take that question and follow it up in a future live stream.

**[31:04](https://youtube.com/watch?v=2r8YnvXLKFU&t=1864s)** So keep keep your eyes peeled for that one.

**[31:07](https://youtube.com/watch?v=2r8YnvXLKFU&t=1867s)** YouTube question again from Zachary asking about unrade this time.

**[31:12](https://youtube.com/watch?v=2r8YnvXLKFU&t=1872s)** Is there sometimes I can connect with the supplied numerical IP, but not with the tail net DNS name.

**[31:19](https://youtube.com/watch?v=2r8YnvXLKFU&t=1879s)** Any ideas? Why?

**[31:22](https://youtube.com/watch?v=2r8YnvXLKFU&t=1882s)** Are theories or something of theories? Do you have any ideas?

**[31:25](https://youtube.com/watch?v=2r8YnvXLKFU&t=1885s)** Well, unrade is a Linux based system.

**[31:28](https://youtube.com/watch?v=2r8YnvXLKFU&t=1888s)** So I'm going to assume that there is a option called accept DNS in the tail scale UI in the unrade UI for the tail scale plugin that they just shipped.

**[31:40](https://youtube.com/watch?v=2r8YnvXLKFU&t=1900s)** I think there's a check box saying accept DNS that will affect things from the unrade box going outbound.

**[31:46](https://youtube.com/watch?v=2r8YnvXLKFU&t=1906s)** It won't affect things the other way around though.

**[31:49](https://youtube.com/watch?v=2r8YnvXLKFU&t=1909s)** So I'm not entirely sure what where the issue is whether it's you're trying to connect into unrade from a remote system and are unable to resolve the DNS that way or not.

**[31:59](https://youtube.com/watch?v=2r8YnvXLKFU&t=1919s)** But certainly if it's from the unrade box going outbound, make sure you've got accept DNS turned on.

**[32:04](https://youtube.com/watch?v=2r8YnvXLKFU&t=1924s)** Yeah, I think it's worth and again, it's a common question that we have with with our enterprise customers or our business customers is like,

**[32:15](https://youtube.com/watch?v=2r8YnvXLKFU&t=1935s)** how does the DNS and tail scale work? Right.

**[32:18](https://youtube.com/watch?v=2r8YnvXLKFU&t=1938s)** And as soon as you if you enable magic DNS and accept DNS in the client, as Alex just said, what essentially happens is that if you look at the resolver configuration,

**[32:29](https://youtube.com/watch?v=2r8YnvXLKFU&t=1949s)** you'll see that the default resolver becomes the quad 100 address that is like the meta address for every tail scale client.

**[32:36](https://youtube.com/watch?v=2r8YnvXLKFU&t=1956s)** And that DNS resolver will essentially take a DNS request and say, is this in the tail nets domain? Yes. Okay. Send it off like return an answer.

**[32:46](https://youtube.com/watch?v=2r8YnvXLKFU&t=1966s)** Is it not that I'm going to immediately pass through to the local resolver that's on the operating system, which may have been handed out by your DSP address.

**[32:55](https://youtube.com/watch?v=2r8YnvXLKFU&t=1975s)** It may be DNS mask. It may be something else, right?

**[32:58](https://youtube.com/watch?v=2r8YnvXLKFU&t=1978s)** Almost every single time we see intermittent problems with DNS is because there is some sort of DNS resolver or caching resolver on the local machine that does not like those requests coming from the tail scale DNS like the tail scale DNS resolver.

**[33:14](https://youtube.com/watch?v=2r8YnvXLKFU&t=1994s)** And the reason for that is that lots of these DNS resolvers are very aggressive in believing that something coming from a 100 quad 100 address is actually a DNS rebinding attack.

**[33:26](https://youtube.com/watch?v=2r8YnvXLKFU&t=2006s)** And it will basically just drop that request. So what we generally find is if you know a little bit about the unray DNS resolver.

**[33:34](https://youtube.com/watch?v=2r8YnvXLKFU&t=2014s)** I bet it has a local host resolver that is like DNS mask or something like that. Look at the logs on there and you'll see something like rejected because if you add a white list for the quad 100 address, almost everything fix it that that's fixed for almost everything in our experience.

**[33:51](https://youtube.com/watch?v=2r8YnvXLKFU&t=2031s)** Yeah, because each each tail scale node, including your phone, by the way, is running a local DNS server, like physically on the device.

**[34:00](https://youtube.com/watch?v=2r8YnvXLKFU&t=2040s)** So it actually minimizes a lot of the latency of making those DNS requests across the town, because it's got a copy of all of your talent nodes locally.

**[34:10](https://youtube.com/watch?v=2r8YnvXLKFU&t=2050s)** All right, next question is regarding ACLs and grants.

**[34:14](https://youtube.com/watch?v=2r8YnvXLKFU&t=2054s)** I like this topic, which one should we use and why the documentation around grants is not as complete as ACLs.

**[34:22](https://youtube.com/watch?v=2r8YnvXLKFU&t=2062s)** How do we limit follow up question and how do we limit access to app connector apps using grants.

**[34:28](https://youtube.com/watch?v=2r8YnvXLKFU&t=2068s)** Great question. And I think this is good feedback for us. So ACLs was the initial implementation of how to restrict access from A to B.

**[34:39](https://youtube.com/watch?v=2r8YnvXLKFU&t=2079s)** Still works is not going anywhere is not deprecated is not like, you know, V zero or wherever you want. Everything is going to continue to work with ACLs grants is an enhancement of ACLs with additional capabilities on top of it.

**[34:56](https://youtube.com/watch?v=2r8YnvXLKFU&t=2096s)** So my recommendation for almost every single use gate is to use a grant rather than an ACL. If you have existing ACLs continue to use them.

**[35:04](https://youtube.com/watch?v=2r8YnvXLKFU&t=2104s)** Don't need to pop them over. They're not going to ever be deprecated. But grants have additional things on top of it that you can use around like application connectivity and a whole bunch of other stuff.

**[35:17](https://youtube.com/watch?v=2r8YnvXLKFU&t=2117s)** So hopefully that's very clear use grants if you're doing things for like from scratch use you can continue to use ACLs as needed with regard to app connectors.

**[35:30](https://youtube.com/watch?v=2r8YnvXLKFU&t=2130s)** There is a mechanism within within grants that's called via and there's a really great page, which actually just came up in our solutions engineering chat this morning.

**[35:44](https://youtube.com/watch?v=2r8YnvXLKFU&t=2144s)** Which shows you how to do that route users through app connectors and so I'm going to put it on here.

**[35:53](https://youtube.com/watch?v=2r8YnvXLKFU&t=2153s)** Rather than like type it out, but basically you can route users through our connects is through grants. It's in our knowledge base.

**[36:02](https://youtube.com/watch?v=2r8YnvXLKFU&t=2162s)** The knowledge base article is 1378 with via again via is only available in grants and not ACLs and it's a mechanism for being able to say if you want to reach this remote destination.

**[36:14](https://youtube.com/watch?v=2r8YnvXLKFU&t=2174s)** You must go through this particular tail scale noted order to get there and that will give you the capability of being a lot more prescriptive in how you route traffic through there.

**[36:24](https://youtube.com/watch?v=2r8YnvXLKFU&t=2184s)** So TLDR use grants and not ACLs for all new stuff. ACLs aren't going anywhere grants have a lot more capabilities than ACLs and so that's why you should use them for most things.

**[36:36](https://youtube.com/watch?v=2r8YnvXLKFU&t=2196s)** I like to kind of think of grants like ACLs 2.0.

**[36:39](https://youtube.com/watch?v=2r8YnvXLKFU&t=2199s)** Like if we'd had the engineering, you know, know how that we'd we have now when we wrote ACLs at the beginning, maybe that's how they would just been from the beginning, but.

**[36:49](https://youtube.com/watch?v=2r8YnvXLKFU&t=2209s)** And all the things that our customers told us they want to do can be like that you know that's the next version of how to do it right.

**[36:57](https://youtube.com/watch?v=2r8YnvXLKFU&t=2217s)** Yeah, so what is an app connector would be my would be our next question follow up here for.

**[37:03](https://youtube.com/watch?v=2r8YnvXLKFU&t=2223s)** Yeah, I think app connectors are very commonly used in out for our enterprise customers.

**[37:09](https://youtube.com/watch?v=2r8YnvXLKFU&t=2229s)** So you have kind of a subnet router in tail scale, which is routing traffic into a specific network might be your home network might be an AWS VPC might be a data center, which will allow you to route traffic where you kind of still tell scale you have an exit node, which will basically set a default route of.

**[37:28](https://youtube.com/watch?v=2r8YnvXLKFU&t=2248s)** You know, quad zero and route all traffic, but there is an in between here where you want all of your traffic to go to your private network through a subnet router.

**[37:38](https://youtube.com/watch?v=2r8YnvXLKFU&t=2258s)** But you don't want to have a full tunnel for all users because maybe you don't want to have everyone's YouTube traffic go through your infrastructure because that will have a material cost on your infrastructure build.

**[37:49](https://youtube.com/watch?v=2r8YnvXLKFU&t=2269s)** So an app connectors job is to specify, domains that are outside of your network that you would normally use an exit node for, but only that specific domain.

**[37:59](https://youtube.com/watch?v=2r8YnvXLKFU&t=2279s)** So we often see this used on the enterprise side for things like if you're using GitHub enterprise, there is an option in GitHub enterprise to white list specific inbound IPs to protect your intellectual property right like all of your source code is what makes your business successful if you're a SaaS company.

**[38:17](https://youtube.com/watch?v=2r8YnvXLKFU&t=2297s)** And you don't want to just allow anybody on the public internet to be able to log in and steal that.

**[38:22](https://youtube.com/watch?v=2r8YnvXLKFU&t=2302s)** So an app connector will route all traffic to GitHub.com through a specific tail scale node and then you can white list it on the GitHub side and it will basically say in order to access GitHub, you must be authenticated to telescope, which gives you that additional layer on top of logging into GitHub as well.

**[38:41](https://youtube.com/watch?v=2r8YnvXLKFU&t=2321s)** As British people, Alex and I might consider using an app connector to route to the BBC I player, we totally wouldn't want to violate our British TV licenses by doing that, but it is certainly an option.

**[38:54](https://youtube.com/watch?v=2r8YnvXLKFU&t=2334s)** I'd love to see a TV licensing specter come on knock on my door here in North Carolina.

**[39:00](https://youtube.com/watch?v=2r8YnvXLKFU&t=2340s)** Yeah, we have seen you watching great British bake off Alex and we know that you haven't paid TV license.

**[39:07](https://youtube.com/watch?v=2r8YnvXLKFU&t=2347s)** I know there's going to be a whole bunch of comments now in YouTube, you know, why don't there's a TV license, well, ask us later.

**[39:13](https://youtube.com/watch?v=2r8YnvXLKFU&t=2353s)** But that's a great example use case for a consumer user. If there's a specific website, for example, for us, UK expatriates that want to be able to go to the BBC, I use it to go to the BBC website, because I don't want to see commercials or adverts on my BBC website.

**[39:28](https://youtube.com/watch?v=2r8YnvXLKFU&t=2368s)** So I use an app connector for that that's hosted in the London region.

**[39:33](https://youtube.com/watch?v=2r8YnvXLKFU&t=2373s)** But yeah, it's specific websites really.

**[39:36](https://youtube.com/watch?v=2r8YnvXLKFU&t=2376s)** Yeah, there you go. I think Lee's violated the rule of fight club there. So don't don't tell your mother, we'll be all right.

**[39:45](https://youtube.com/watch?v=2r8YnvXLKFU&t=2385s)** All right, good deal.

**[39:47](https://youtube.com/watch?v=2r8YnvXLKFU&t=2387s)** So I think the way I typically try and describe app connectors to people when they ask is just simply say it's like split DNS, but for specific applications that you white list.

**[39:57](https://youtube.com/watch?v=2r8YnvXLKFU&t=2397s)** So yeah, it is very useful in an enterprise scenario where you've got a hosted GitHub or who knows what else.

**[40:06](https://youtube.com/watch?v=2r8YnvXLKFU&t=2406s)** So quick question from YouTube here, would you say tail scale is something to use for connecting to production servers that are constantly changing IP addresses and generally behind carrier grade net.

**[40:18](https://youtube.com/watch?v=2r8YnvXLKFU&t=2418s)** Yes.

**[40:21](https://youtube.com/watch?v=2r8YnvXLKFU&t=2421s)** Yes, I think so.

**[40:23](https://youtube.com/watch?v=2r8YnvXLKFU&t=2423s)** That's kind of what the products for.

**[40:25](https://youtube.com/watch?v=2r8YnvXLKFU&t=2425s)** I mean, what the uniqueness of tail scale is that it is one of the very few VPNs that will work behind carrier grade nets.

**[40:31](https://youtube.com/watch?v=2r8YnvXLKFU&t=2431s)** So if you have an inter an ISP that hands out addresses from the CG not range, it will still work. So yes, the answer is yes.

**[40:39](https://youtube.com/watch?v=2r8YnvXLKFU&t=2439s)** Go for a great time.

**[40:41](https://youtube.com/watch?v=2r8YnvXLKFU&t=2441s)** What is CG now?

**[40:43](https://youtube.com/watch?v=2r8YnvXLKFU&t=2443s)** Oh, you're throwing all the tough questions.

**[40:45](https://youtube.com/watch?v=2r8YnvXLKFU&t=2445s)** I mean, I'll take it if you want. I'm just trying to play.

**[40:48](https://youtube.com/watch?v=2r8YnvXLKFU&t=2448s)** I would love you to look at your explanation. Yeah.

**[40:51](https://youtube.com/watch?v=2r8YnvXLKFU&t=2451s)** Well, so essentially you get a public IPV for address when you so for example my AT&T router in the basement connects to my ISP and I get an IP version for address of who knows whatever, but it's publicly routable.

**[41:07](https://youtube.com/watch?v=2r8YnvXLKFU&t=2467s)** Other ISPs like Starlink, like often cellular based providers, sometimes the wireless ISPs, the wisps sometimes do this as well.

**[41:17](https://youtube.com/watch?v=2r8YnvXLKFU&t=2477s)** They will have a public IP for their master or whatever, but they won't give you a public IP to the clients that connect to that.

**[41:25](https://youtube.com/watch?v=2r8YnvXLKFU&t=2485s)** So your Starlink box, for example, would have it maybe a 172 kind of private IP address that you might expect to see as like a LAN IP sometimes.

**[41:35](https://youtube.com/watch?v=2r8YnvXLKFU&t=2495s)** So essentially what you've got there is called double NAT. So you've got network address translation happening at the master at the satellite level.

**[41:44](https://youtube.com/watch?v=2r8YnvXLKFU&t=2504s)** And then it's also happening again at your local router.

**[41:48](https://youtube.com/watch?v=2r8YnvXLKFU&t=2508s)** And it's, there's no way for you to put a service on the public internet if you don't have a publicly routable IP address.

**[41:56](https://youtube.com/watch?v=2r8YnvXLKFU&t=2516s)** Well, tailscale kind of gets around that by punching holes out through both levels of NAT and then reverse mapping that back through and look at the how tailscale works blog post for a much more eloquent explanation of the NAT routing stuff that we do.

**[42:09](https://youtube.com/watch?v=2r8YnvXLKFU&t=2529s)** But essentially carrier grade NAT is like the worst case scenario for trying to put host host of service behind a firewall.

**[42:17](https://youtube.com/watch?v=2r8YnvXLKFU&t=2537s)** I think the reason for it to just accentuate Alex's point is, if you're a internet service provider that wasn't lucky enough to buy a slash 16 of public IP addresses back in 1994, you probably have a very limited pool of public IP addresses that you can hand out.

**[42:37](https://youtube.com/watch?v=2r8YnvXLKFU&t=2557s)** And so let's say you are, I don't know, an open coming cell phone provider in the United States that wants to build its own infrastructure.

**[42:47](https://youtube.com/watch?v=2r8YnvXLKFU&t=2567s)** I would love to know where you got the capital from, but as an example, you can't hand out public IP addresses to every single cell phone that connects to your towers, right.

**[42:56](https://youtube.com/watch?v=2r8YnvXLKFU&t=2576s)** And so you need a way of being able to differentiate the public address from the private address and carrier grade NAT is that mechanism, right.

**[43:03](https://youtube.com/watch?v=2r8YnvXLKFU&t=2583s)** And so what about IPv6 Lee?

**[43:06](https://youtube.com/watch?v=2r8YnvXLKFU&t=2586s)** Well, that was going to be my next point, right.

**[43:08](https://youtube.com/watch?v=2r8YnvXLKFU&t=2588s)** Like I know that every year is the year of IPv6 and I know that IPv4 is going nowhere, but it's true.

**[43:14](https://youtube.com/watch?v=2r8YnvXLKFU&t=2594s)** It is. It's the year of the Linux desktop except not working again.

**[43:19](https://youtube.com/watch?v=2r8YnvXLKFU&t=2599s)** I swear almost like if you want me to be unemployed and not have to deal with like natural reversal IPv6 solves that problem, right.

**[43:28](https://youtube.com/watch?v=2r8YnvXLKFU&t=2608s)** Like almost every single problem that we have to deal with on the network connectivity side is because of IPv4 and IPv4 is exhaustive.

**[43:37](https://youtube.com/watch?v=2r8YnvXLKFU&t=2617s)** So, you know, if you, if you're building an app like as an example, if you're building an ABSVPC tomorrow for a new project at work, make it dual stack.

**[43:46](https://youtube.com/watch?v=2r8YnvXLKFU&t=2626s)** There's no reason not to just turn on IPv6. There's lots of reference architecture now. Go and turn it on your life will be so much better. I promise.

**[43:54](https://youtube.com/watch?v=2r8YnvXLKFU&t=2634s)** I mean, most ISPs, residential ones at least don't offer IPv6 out the box.

**[44:01](https://youtube.com/watch?v=2r8YnvXLKFU&t=2641s)** I certainly get it on my big red address because I will often be like, hey, can somebody else test this because I go IPv6 and I get direct connections to everything.

**[44:10](https://youtube.com/watch?v=2r8YnvXLKFU&t=2650s)** So yeah, I know it's geographically geographically decided, but I would love it if we were just have a bit of a push towards IPv6.

**[44:20](https://youtube.com/watch?v=2r8YnvXLKFU&t=2660s)** That's one of those things though. That's one of those things, though, that it's like it's simultaneously both annoying and frustrating to deal with, but also a massively important security feature in the modern Internet.

**[44:32](https://youtube.com/watch?v=2r8YnvXLKFU&t=2672s)** Yeah, I mean, I genuinely understand why it's around, but it is the bait of my existence right now, certainly as the bait of my existence.

**[44:42](https://youtube.com/watch?v=2r8YnvXLKFU&t=2682s)** Job security lead. Look at it like that.

**[44:46](https://youtube.com/watch?v=2r8YnvXLKFU&t=2686s)** Alright, another question from YouTube. This one's about TSIDP. I recently made a video about TSI, which is Tailscales Identity Provider.

**[44:54](https://youtube.com/watch?v=2r8YnvXLKFU&t=2694s)** It's a pre-release alpha piece of software that essentially lets you host an open ID connect server directly in your town there.

**[45:03](https://youtube.com/watch?v=2r8YnvXLKFU&t=2703s)** And the question here is, is there any news on further development for TSIDP and would you recommend setting up TSIDP on a multi-node cluster to make sure it's working reliably?

**[45:14](https://youtube.com/watch?v=2r8YnvXLKFU&t=2714s)** Well, no, to be honest with you, I wouldn't. There are plenty of other much more mature OIDC providers out there. I mean, some are free, some will cost you some money.

**[45:27](https://youtube.com/watch?v=2r8YnvXLKFU&t=2727s)** But TSIDP is a hobby project at best right now. It will work, and I certainly still use it in my own personal infrastructure.

**[45:35](https://youtube.com/watch?v=2r8YnvXLKFU&t=2735s)** But would I put it in the critical path of anything business related? Heck, no.

**[45:40](https://youtube.com/watch?v=2r8YnvXLKFU&t=2740s)** So that may change, you know, at some point we may get a request from a customer that means we spend a whole bunch of development cycles on TSIDP.

**[45:48](https://youtube.com/watch?v=2r8YnvXLKFU&t=2748s)** But certainly for right now, at least it's still just one of those.

**[45:52](https://youtube.com/watch?v=2r8YnvXLKFU&t=2752s)** It comes with a free side of dragons.

**[45:55](https://youtube.com/watch?v=2r8YnvXLKFU&t=2755s)** Okay, so not recommended.

**[45:59](https://youtube.com/watch?v=2r8YnvXLKFU&t=2759s)** Alright, so from Zoom this time, John K. Hill writes in, tail drop works great everywhere I need it.

**[46:06](https://youtube.com/watch?v=2r8YnvXLKFU&t=2766s)** However, if I'm dropping a file on a Raspberry Pi in the workshop, I have to SSH into Linux in order to accept the receive.

**[46:14](https://youtube.com/watch?v=2r8YnvXLKFU&t=2774s)** Is there a way to auto allow sends over tail drop on Linux?

**[46:20](https://youtube.com/watch?v=2r8YnvXLKFU&t=2780s)** I don't know. Do you know?

**[46:22](https://youtube.com/watch?v=2r8YnvXLKFU&t=2782s)** No, it's open you do.

**[46:25](https://youtube.com/watch?v=2r8YnvXLKFU&t=2785s)** Congratulations, John, you've stumped the experts.

**[46:28](https://youtube.com/watch?v=2r8YnvXLKFU&t=2788s)** I think we should probably ask the tail drop developers that question in our internals lack and get back to it.

**[46:34](https://youtube.com/watch?v=2r8YnvXLKFU&t=2794s)** I don't actually know the answer to that one.

**[46:36](https://youtube.com/watch?v=2r8YnvXLKFU&t=2796s)** Well, I mean, if I search the documentation for tail drop for the word auto, nothing comes up.

**[46:41](https://youtube.com/watch?v=2r8YnvXLKFU&t=2801s)** So I'm going to sign.

**[46:42](https://youtube.com/watch?v=2r8YnvXLKFU&t=2802s)** That's a sign, isn't it?

**[46:43](https://youtube.com/watch?v=2r8YnvXLKFU&t=2803s)** That's a fact.

**[46:44](https://youtube.com/watch?v=2r8YnvXLKFU&t=2804s)** No, for right now.

**[46:45](https://youtube.com/watch?v=2r8YnvXLKFU&t=2805s)** But John, we will take that as Lee says to the tail drop development team.

**[46:50](https://youtube.com/watch?v=2r8YnvXLKFU&t=2810s)** It's worth noting that tail drop still officially is in alpha.

**[46:53](https://youtube.com/watch?v=2r8YnvXLKFU&t=2813s)** So, you know, there's plenty of plenty of rough corners you might find unless this may well be one of them.

**[46:59](https://youtube.com/watch?v=2r8YnvXLKFU&t=2819s)** So John has said that that deserves a t-shirt and I agree with John.

**[47:03](https://youtube.com/watch?v=2r8YnvXLKFU&t=2823s)** So John, if you want to send me the marketing teams on it, yes.

**[47:08](https://youtube.com/watch?v=2r8YnvXLKFU&t=2828s)** Yeah, I think maybe we'll make that a new thing if you stump as you get a t-shirt.

**[47:13](https://youtube.com/watch?v=2r8YnvXLKFU&t=2833s)** But yes, I think that is a pretty good, yeah, let's let's go with that.

**[47:17](https://youtube.com/watch?v=2r8YnvXLKFU&t=2837s)** You can't just ask night crazy questions, though.

**[47:20](https://youtube.com/watch?v=2r8YnvXLKFU&t=2840s)** We have to be actual genuine questions.

**[47:22](https://youtube.com/watch?v=2r8YnvXLKFU&t=2842s)** My marketing teams budget manager just message me and said, whoa, now easy.

**[47:25](https://youtube.com/watch?v=2r8YnvXLKFU&t=2845s)** Oh, in public.

**[47:26](https://youtube.com/watch?v=2r8YnvXLKFU&t=2846s)** Like, whoa, easy now Lee.

**[47:27](https://youtube.com/watch?v=2r8YnvXLKFU&t=2847s)** So yeah, bankrupting tail scale for t-shirts is probably not the way to run a business.

**[47:31](https://youtube.com/watch?v=2r8YnvXLKFU&t=2851s)** Is it?

**[47:32](https://youtube.com/watch?v=2r8YnvXLKFU&t=2852s)** Job security just ruined by over promising t-shirts.

**[47:36](https://youtube.com/watch?v=2r8YnvXLKFU&t=2856s)** Of a promising t-shirt.

**[47:38](https://youtube.com/watch?v=2r8YnvXLKFU&t=2858s)** If you do want a t-shirt, by the way, just as an aside, if you do want a t-shirt, we have hundreds of them when we visit conferences.

**[47:44](https://youtube.com/watch?v=2r8YnvXLKFU&t=2864s)** Alex and I have a bunch of conferences coming up.

**[47:47](https://youtube.com/watch?v=2r8YnvXLKFU&t=2867s)** We love to see people come and talk to us about tail scale in person.

**[47:51](https://youtube.com/watch?v=2r8YnvXLKFU&t=2871s)** I am going to pitch you on take in tail scale to work that is going to happen.

**[47:55](https://youtube.com/watch?v=2r8YnvXLKFU&t=2875s)** But I think that's a fair price to pay for being handed a tail scale t-shirt.

**[47:59](https://youtube.com/watch?v=2r8YnvXLKFU&t=2879s)** And I'm wearing one today and it's wonderful.

**[48:02](https://youtube.com/watch?v=2r8YnvXLKFU&t=2882s)** So yeah, if you are at any conferences going on hunt for a tail scale t-shirt.

**[48:07](https://youtube.com/watch?v=2r8YnvXLKFU&t=2887s)** And if there is a conference that you are going to that you want to see is there, let us know in the comments.

**[48:12](https://youtube.com/watch?v=2r8YnvXLKFU&t=2892s)** We really want to know, we are trying to lean heavily.

**[48:15](https://youtube.com/watch?v=2r8YnvXLKFU&t=2895s)** We have a wonderful events coordinator who is on top of everything.

**[48:19](https://youtube.com/watch?v=2r8YnvXLKFU&t=2899s)** I think we would love that sort of feedback on what conferences we should attend.

**[48:23](https://youtube.com/watch?v=2r8YnvXLKFU&t=2903s)** Yeah, there is a question in the chat from stamp overstock.

**[48:27](https://youtube.com/watch?v=2r8YnvXLKFU&t=2907s)** But when is tail scale going to be in the UK?

**[48:30](https://youtube.com/watch?v=2r8YnvXLKFU&t=2910s)** I need a t-shirt.

**[48:31](https://youtube.com/watch?v=2r8YnvXLKFU&t=2911s)** Well, lucky for you.

**[48:33](https://youtube.com/watch?v=2r8YnvXLKFU&t=2913s)** Without like three times this month.

**[48:35](https://youtube.com/watch?v=2r8YnvXLKFU&t=2915s)** Yeah.

**[48:36](https://youtube.com/watch?v=2r8YnvXLKFU&t=2916s)** What else is there?

**[48:38](https://youtube.com/watch?v=2r8YnvXLKFU&t=2918s)** DevOps live.

**[48:39](https://youtube.com/watch?v=2r8YnvXLKFU&t=2919s)** Cubeconny you and then there is.

**[48:42](https://youtube.com/watch?v=2r8YnvXLKFU&t=2922s)** There's one other that I can't remember what I think that's in June.

**[48:45](https://youtube.com/watch?v=2r8YnvXLKFU&t=2925s)** There's like another one in June whose event name escapes me, but like.

**[48:49](https://youtube.com/watch?v=2r8YnvXLKFU&t=2929s)** Cube, if you want to keep calling you want a t-shirt.

**[48:52](https://youtube.com/watch?v=2r8YnvXLKFU&t=2932s)** I will be there.

**[48:53](https://youtube.com/watch?v=2r8YnvXLKFU&t=2933s)** I will personally hand you a t-shirt.

**[48:55](https://youtube.com/watch?v=2r8YnvXLKFU&t=2935s)** If you're going to DevOps live.

**[48:57](https://youtube.com/watch?v=2r8YnvXLKFU&t=2937s)** J who you've seen on this channel a couple of times is going to DevOps live.

**[49:02](https://youtube.com/watch?v=2r8YnvXLKFU&t=2942s)** He will personally hand you a t-shirt.

**[49:04](https://youtube.com/watch?v=2r8YnvXLKFU&t=2944s)** So come up and say, hey, we really love the asking expert and we'll give you a t-shirt.

**[49:07](https://youtube.com/watch?v=2r8YnvXLKFU&t=2947s)** We're also going to be at scale in Pasadena this coming weekend.

**[49:11](https://youtube.com/watch?v=2r8YnvXLKFU&t=2951s)** I'm flying out at 6 a.m. on Friday to go there, but you know, such is life sometimes.

**[49:16](https://youtube.com/watch?v=2r8YnvXLKFU&t=2956s)** We're also going to be at DevOps days Chicago coming up on March the 19th.

**[49:21](https://youtube.com/watch?v=2r8YnvXLKFU&t=2961s)** Great little conference that one.

**[49:23](https://youtube.com/watch?v=2r8YnvXLKFU&t=2963s)** So yeah, lots of places to go.

**[49:25](https://youtube.com/watch?v=2r8YnvXLKFU&t=2965s)** If you want to find out more about our events and things like that, you can sign up for our newsletter.

**[49:29](https://youtube.com/watch?v=2r8YnvXLKFU&t=2969s)** And we'll give you a regular tail scale in real life breakdown.

**[49:33](https://youtube.com/watch?v=2r8YnvXLKFU&t=2973s)** Alrighty.

**[49:36](https://youtube.com/watch?v=2r8YnvXLKFU&t=2976s)** So back to the questions, I think.

**[49:39](https://youtube.com/watch?v=2r8YnvXLKFU&t=2979s)** Where are we at over here?

**[49:41](https://youtube.com/watch?v=2r8YnvXLKFU&t=2981s)** Okay.

**[49:42](https://youtube.com/watch?v=2r8YnvXLKFU&t=2982s)** Is there any chance for tutorial for GCP VPCs and subnet routers, such as the existing one for AWS?

**[49:51](https://youtube.com/watch?v=2r8YnvXLKFU&t=2991s)** That isn't yet.

**[49:53](https://youtube.com/watch?v=2r8YnvXLKFU&t=2993s)** And the primary reason for that is that we have a lot more AWS customers than we do GCP customers.

**[49:59](https://youtube.com/watch?v=2r8YnvXLKFU&t=2999s)** But this is great feedback.

**[50:00](https://youtube.com/watch?v=2r8YnvXLKFU&t=3000s)** We do have a lot of hyperscaler documentation backlog.

**[50:06](https://youtube.com/watch?v=2r8YnvXLKFU&t=3006s)** I have enough GCP knowledge to be dangerous.

**[50:10](https://youtube.com/watch?v=2r8YnvXLKFU&t=3010s)** And so if you would like to open an issue in our docs repo.

**[50:15](https://youtube.com/watch?v=2r8YnvXLKFU&t=3015s)** If our trusty Tim in the background can grab the docs repo.

**[50:19](https://youtube.com/watch?v=2r8YnvXLKFU&t=3019s)** Please open an issue there and then tag me all the docs seem on it.

**[50:23](https://youtube.com/watch?v=2r8YnvXLKFU&t=3023s)** And I will take a stab at it.

**[50:25](https://youtube.com/watch?v=2r8YnvXLKFU&t=3025s)** I think the general practices that I think are useful to understand are.

**[50:30](https://youtube.com/watch?v=2r8YnvXLKFU&t=3030s)** You know, running EC to running an EC to them.

**[50:33](https://youtube.com/watch?v=2r8YnvXLKFU&t=3033s)** So AWS Centric running compute that runs tail scale and then subnet routers for the virtual network will be.

**[50:40](https://youtube.com/watch?v=2r8YnvXLKFU&t=3040s)** You know, nine tenths of the solution to the problem, basically.

**[50:44](https://youtube.com/watch?v=2r8YnvXLKFU&t=3044s)** So what's required on the AWS side?

**[50:47](https://youtube.com/watch?v=2r8YnvXLKFU&t=3047s)** I know the question was about GCP, but I'm now curious.

**[50:50](https://youtube.com/watch?v=2r8YnvXLKFU&t=3050s)** Why is AWS so special?

**[50:52](https://youtube.com/watch?v=2r8YnvXLKFU&t=3052s)** What's special about the subnet router in a VPC?

**[50:55](https://youtube.com/watch?v=2r8YnvXLKFU&t=3055s)** I think this does apply to every hyperscaler or data center is that all these hyperscalers have these managed services Amazon has RDS Google has spanner.

**[51:05](https://youtube.com/watch?v=2r8YnvXLKFU&t=3065s)** All these different managed services where you don't have operating system access to be able to get.

**[51:10](https://youtube.com/watch?v=2r8YnvXLKFU&t=3070s)** Tailscale installed directly on it and like you still probably want to access your database.

**[51:14](https://youtube.com/watch?v=2r8YnvXLKFU&t=3074s)** So you want to access your managed service in that way.

**[51:18](https://youtube.com/watch?v=2r8YnvXLKFU&t=3078s)** And so a subnet router will allow you to advertise in AWS.

**[51:22](https://youtube.com/watch?v=2r8YnvXLKFU&t=3082s)** It's the VPC and Google it's like the network.

**[51:26](https://youtube.com/watch?v=2r8YnvXLKFU&t=3086s)** Google networks are kind of unique in the fact that they're globally distributed.

**[51:29](https://youtube.com/watch?v=2r8YnvXLKFU&t=3089s)** It's kind of an interesting model versus all the other hyperscalers.

**[51:33](https://youtube.com/watch?v=2r8YnvXLKFU&t=3093s)** But you can basically put a compute instance in that network.

**[51:37](https://youtube.com/watch?v=2r8YnvXLKFU&t=3097s)** Advertise the network range and it gives you full access to that entire network.

**[51:41](https://youtube.com/watch?v=2r8YnvXLKFU&t=3101s)** So you know, again, it applies across all the hyperscalers generally.

**[51:46](https://youtube.com/watch?v=2r8YnvXLKFU&t=3106s)** So am I right in thinking that if I put a subnet router inside a VPC that had access to an RDS resource, for example.

**[51:57](https://youtube.com/watch?v=2r8YnvXLKFU&t=3117s)** I'd be able then effectively to put that resource on my talent. Are there any gotchas there?

**[52:04](https://youtube.com/watch?v=2r8YnvXLKFU&t=3124s)** Correct. Yes. Assuming the subnet router can access like there's no security group blocking the particular compute instance to the managed database.

**[52:16](https://youtube.com/watch?v=2r8YnvXLKFU&t=3136s)** Yes, you essentially have full access there. The security groups still apply.

**[52:20](https://youtube.com/watch?v=2r8YnvXLKFU&t=3140s)** But the connection looks like it's coming from the subnet router. So like you create this encrypted tunnel between two telescope clients, like y'all laptop on the subnet router.

**[52:29](https://youtube.com/watch?v=2r8YnvXLKFU&t=3149s)** And then it looks like it's originating from inside that network, like the call is coming from inside the VPC.

**[52:36](https://youtube.com/watch?v=2r8YnvXLKFU&t=3156s)** So they're really useful for these managed service providers and these hyperscalers, you know, and this applies to every single clover.

**[52:42](https://youtube.com/watch?v=2r8YnvXLKFU&t=3162s)** Digital ocean has VPCs now. Linode has VPCs now. Like you can basically advertise the entire network.

**[52:49](https://youtube.com/watch?v=2r8YnvXLKFU&t=3169s)** There are caveats here that we like to point out on the solutions of the inside around like ACL and grants and stuff.

**[52:57](https://youtube.com/watch?v=2r8YnvXLKFU&t=3177s)** Probably not worth going into that because I am aware that we've got about six minutes left. This is absolutely flown by by the way. Wow.

**[53:03](https://youtube.com/watch?v=2r8YnvXLKFU&t=3183s)** So yeah, but that's generally just good practice across the board.

**[53:07](https://youtube.com/watch?v=2r8YnvXLKFU&t=3187s)** Yeah, good deal. So I've put a link, by the way, in the YouTube chat to someone asked earlier on, how do I report issues and make feature requests?

**[53:16](https://youtube.com/watch?v=2r8YnvXLKFU&t=3196s)** Easiest way right now, if you're not already a customer of tail scales is through the GitHub repo.

**[53:21](https://youtube.com/watch?v=2r8YnvXLKFU&t=3201s)** The second easiest way is to reach out to Lee and the sales team. How do people do that?

**[53:28](https://youtube.com/watch?v=2r8YnvXLKFU&t=3208s)** So we have a sales at tail scale.com a list, which will get you in touch with our account executives.

**[53:34](https://youtube.com/watch?v=2r8YnvXLKFU&t=3214s)** Now I'm going to make a pitch here. I spent a long time getting email by an account executives and random companies who wanted to call my desk phone at my office to talk talk to me about this random thing that I didn't care about.

**[53:46](https://youtube.com/watch?v=2r8YnvXLKFU&t=3226s)** That is not how our account team is is operating.

**[53:49](https://youtube.com/watch?v=2r8YnvXLKFU&t=3229s)** We are here to help you be successful with tail scale.

**[53:53](https://youtube.com/watch?v=2r8YnvXLKFU&t=3233s)** And I work closely with the account executives and our job is to make you successful.

**[53:57](https://youtube.com/watch?v=2r8YnvXLKFU&t=3237s)** If you want to get technical advice, we do have an email alias that goes directly to our solutions engineers, but we like those to go through our support team that we work very closely with.

**[54:07](https://youtube.com/watch?v=2r8YnvXLKFU&t=3247s)** So our recommendation is to email support at tail scale.com.

**[54:10](https://youtube.com/watch?v=2r8YnvXLKFU&t=3250s)** And our support team work very, very closely with the solutions engineering team.

**[54:14](https://youtube.com/watch?v=2r8YnvXLKFU&t=3254s)** So if you have a specific question about, hey, I want to, I want to give you folks some money sales at tail scale.com is the right way.

**[54:20](https://youtube.com/watch?v=2r8YnvXLKFU&t=3260s)** If you have a technical question, support at tail scale.com is the right way.

**[54:24](https://youtube.com/watch?v=2r8YnvXLKFU&t=3264s)** And if it needs to be escalated to those in terms of like solutions engineering and to differentiate between support and solutions engineering support is how do I do this thing.

**[54:33](https://youtube.com/watch?v=2r8YnvXLKFU&t=3273s)** Solutions engineering is the conceptual.

**[54:35](https://youtube.com/watch?v=2r8YnvXLKFU&t=3275s)** How would I achieve this thing?

**[54:37](https://youtube.com/watch?v=2r8YnvXLKFU&t=3277s)** You know, in terms of like future state and future looking.

**[54:41](https://youtube.com/watch?v=2r8YnvXLKFU&t=3281s)** How on the SE team with support based questions, and we're all one team at this point for all intensive purposes.

**[54:47](https://youtube.com/watch?v=2r8YnvXLKFU&t=3287s)** But if you have a reactive question, then it would go to support.

**[54:51](https://youtube.com/watch?v=2r8YnvXLKFU&t=3291s)** If you have a proactive question, then it would go to solutions engineering.

**[54:55](https://youtube.com/watch?v=2r8YnvXLKFU&t=3295s)** Absolutely. Now we've got a brand new person that just joined tail scale.

**[55:00](https://youtube.com/watch?v=2r8YnvXLKFU&t=3300s)** I think she's in the YouTube chat already called Natasha. She's our brand new community manager.

**[55:06](https://youtube.com/watch?v=2r8YnvXLKFU&t=3306s)** Keep an eye out for her in the comments and some of the future live streamed as well.

**[55:10](https://youtube.com/watch?v=2r8YnvXLKFU&t=3310s)** I'm sure she'll be involved on camera very soon.

**[55:13](https://youtube.com/watch?v=2r8YnvXLKFU&t=3313s)** And we're going to really invest pretty heavily in trying to make sure that folks have got outlets for some of those technical questions that they don't necessarily want to have the sales, pitter patter, all that kind of stuff.

**[55:23](https://youtube.com/watch?v=2r8YnvXLKFU&t=3323s)** That said, we still need to pay the bills.

**[55:27](https://youtube.com/watch?v=2r8YnvXLKFU&t=3327s)** So tail scale.com slash BTW to find out about how to bring tail scale to work.

**[55:31](https://youtube.com/watch?v=2r8YnvXLKFU&t=3331s)** And everything else that leisure said at supported tail scale.com, the GitHub issues, all that kind of stuff.

**[55:38](https://youtube.com/watch?v=2r8YnvXLKFU&t=3338s)** Now we've got a couple of minutes left, but none of these questions I think that are left really fit into that timeframe.

**[55:43](https://youtube.com/watch?v=2r8YnvXLKFU&t=3343s)** I'm afraid so I'm probably going to wrap things up a couple of minutes later because I do have another call to jump to pretty much straight after this.

**[55:49](https://youtube.com/watch?v=2r8YnvXLKFU&t=3349s)** I think it's it's a symptom of our success Alex that we have so many questions we can't get through them.

**[55:55](https://youtube.com/watch?v=2r8YnvXLKFU&t=3355s)** Hopefully if you didn't get your question answered, we should think about how we can get those questions into a format where we can answer them like asynchronously.

**[56:04](https://youtube.com/watch?v=2r8YnvXLKFU&t=3364s)** So we'll have a chat with the back and team and the community team about how that could look in the future.

**[56:10](https://youtube.com/watch?v=2r8YnvXLKFU&t=3370s)** Keep those questions coming if we didn't get to your question today.

**[56:13](https://youtube.com/watch?v=2r8YnvXLKFU&t=3373s)** We will get to it next time we I love this time.

**[56:16](https://youtube.com/watch?v=2r8YnvXLKFU&t=3376s)** It's my favorite thing to do at tail scale, so I appreciate everybody joining us.

**[56:21](https://youtube.com/watch?v=2r8YnvXLKFU&t=3381s)** The conference silly season is just about to start winding up.

**[56:24](https://youtube.com/watch?v=2r8YnvXLKFU&t=3384s)** So I think you might see a couple of different faces on this channel over the next month or so, but we'll do our best to get to those questions.

**[56:32](https://youtube.com/watch?v=2r8YnvXLKFU&t=3392s)** And Natasha, I hope you're listening. We need to find a way to capture those questions and present them asynchronously to our community people.

**[56:39](https://youtube.com/watch?v=2r8YnvXLKFU&t=3399s)** Thank you very much for watching everybody. We had, wow, several hundred of you watched today. That's pretty awesome.

**[56:45](https://youtube.com/watch?v=2r8YnvXLKFU&t=3405s)** Thank you so much for everybody that showed up on the YouTube side and the zoom side as well.

**[56:50](https://youtube.com/watch?v=2r8YnvXLKFU&t=3410s)** I love you very much. And until next time, I've been Alex from tail scale and I'm Lee.

**[56:56](https://youtube.com/watch?v=2r8YnvXLKFU&t=3416s)** All right. Thanks. Bye.

---

*Automatically generated transcript. May contain errors.*
