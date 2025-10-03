---
video_id: "4AxaKxZIO4Y"
title: "Modernizing Remote Access to EKS with Tailscale"
description: "Simplify Kubernetes management with Tailscale's mesh networking solution by replacing legacy VPN configurations and intricate security groups for your AWS EKS clusters. 

This practical webinar walks ..."
channel_name: "Tailscale"
channel_id: "UCcdv38QxPjSMqbt5ffLhJLA"
published_at: "2025-09-26"
duration_seconds: 2834
youtube_url: "https://www.youtube.com/watch?v=4AxaKxZIO4Y"
thumbnail_url: "https://i.ytimg.com/vi_webp/4AxaKxZIO4Y/maxresdefault.webp"

# Transcription metadata
transcribed_at: "2025-10-03T16:00:30.517508"
transcription_method: "cpu"
model_used: "base"
language: "en"
word_count: 7703
transcription_time_seconds: 75.6
---

# Modernizing Remote Access to EKS with Tailscale

**[00:05](https://youtube.com/watch?v=4AxaKxZIO4Y&t=5s)** Hello, everyone. Welcome. As we're filtering in, grab a seat, grab something to drink. We'll

**[00:13](https://youtube.com/watch?v=4AxaKxZIO4Y&t=13s)** get started here in a minute. All right. Nice hello.

**[00:23](https://youtube.com/watch?v=4AxaKxZIO4Y&t=23s)** Hello, hello. While you're coming in, something always like to do on webinars is you should

**[00:30](https://youtube.com/watch?v=4AxaKxZIO4Y&t=30s)** have the ability to chat with us, but drop a note and chat where you're zooming in from

**[00:38](https://youtube.com/watch?v=4AxaKxZIO4Y&t=38s)** today. Love to find out where our attendees are coming from across the world. Oh, Trinidad.

**[00:49](https://youtube.com/watch?v=4AxaKxZIO4Y&t=49s)** That sounds like a nice place right now. Trinidad sounds like somewhere that's a little

**[00:54](https://youtube.com/watch?v=4AxaKxZIO4Y&t=54s)** bit warmer than where I'm based.

**[00:56](https://youtube.com/watch?v=4AxaKxZIO4Y&t=56s)** You choose Norway, Poland, UK. So it's in the evening for you folks in Europe. So thank

**[01:04](https://youtube.com/watch?v=4AxaKxZIO4Y&t=64s)** you for taking your evening and spending it with us here today. This is awesome. Korea.

**[01:10](https://youtube.com/watch?v=4AxaKxZIO4Y&t=70s)** Well, let me see, too. Is it 2 a.m. in Korea? I think so or something like that, maybe?

**[01:17](https://youtube.com/watch?v=4AxaKxZIO4Y&t=77s)** I was asked, Matt Allen. I am very impressed.

**[01:21](https://youtube.com/watch?v=4AxaKxZIO4Y&t=81s)** If they're like the Philippines, which is 12 hours ahead or 13. So, yeah, Estonia, Angola.

**[01:28](https://youtube.com/watch?v=4AxaKxZIO4Y&t=88s)** Nice. Great crew. This is awesome.

**[01:30](https://youtube.com/watch?v=4AxaKxZIO4Y&t=90s)** I've got a solid representation globally. Shadow to everybody that is online to join us live.

**[01:35](https://youtube.com/watch?v=4AxaKxZIO4Y&t=95s)** And it's like the middle of the night for you.

**[01:37](https://youtube.com/watch?v=4AxaKxZIO4Y&t=97s)** Yeah, for sure.

**[01:40](https://youtube.com/watch?v=4AxaKxZIO4Y&t=100s)** We appreciate you so, so much.

**[01:43](https://youtube.com/watch?v=4AxaKxZIO4Y&t=103s)** All right. It looks like attendance is starting to flatten out a little bit.

**[01:50](https://youtube.com/watch?v=4AxaKxZIO4Y&t=110s)** So I think we've got everybody that was waiting. So I think we can go ahead and get started.

**[01:54](https://youtube.com/watch?v=4AxaKxZIO4Y&t=114s)** So here we go. Hi, everyone. Welcome to today's webinar, modernizing remote access to EKS with

**[02:01](https://youtube.com/watch?v=4AxaKxZIO4Y&t=121s)** tail scale. We are so glad you could join us today. My name is Kate. I'll be your host today.

**[02:06](https://youtube.com/watch?v=4AxaKxZIO4Y&t=126s)** Before we get started, just a quick couple of housekeeping notes.

**[02:09](https://youtube.com/watch?v=4AxaKxZIO4Y&t=129s)** The first is that this session is being recorded. We will share this recording with you after

**[02:14](https://youtube.com/watch?v=4AxaKxZIO4Y&t=134s)** the fact. If you miss anything, don't worry about it.

**[02:16](https://youtube.com/watch?v=4AxaKxZIO4Y&t=136s)** If it's the middle of the night for you, and you decide that you'd rather catch up on the

**[02:19](https://youtube.com/watch?v=4AxaKxZIO4Y&t=139s)** recording later, I promise we won't be offended. We will have time for live Q and A at the end

**[02:25](https://youtube.com/watch?v=4AxaKxZIO4Y&t=145s)** of today's session. As you have questions as we as we go through the presentation,

**[02:29](https://youtube.com/watch?v=4AxaKxZIO4Y&t=149s)** please drop them in the Q and A box at the bottom of your screen.

**[02:33](https://youtube.com/watch?v=4AxaKxZIO4Y&t=153s)** If you use the chat box, we may miss it. So your best bet to get your question answered is to

**[02:38](https://youtube.com/watch?v=4AxaKxZIO4Y&t=158s)** throw it in that Q and A box. We also have one of our solutions engineers monitoring the chat

**[02:43](https://youtube.com/watch?v=4AxaKxZIO4Y&t=163s)** and the Q and A box today shout out to Cartic. He will be answering as many questions as he can

**[02:49](https://youtube.com/watch?v=4AxaKxZIO4Y&t=169s)** in the chat directly. We'll go through the main presentation first and then Alan and Raj will

**[02:54](https://youtube.com/watch?v=4AxaKxZIO4Y&t=174s)** answer some of your questions live at the end. With that, I will hand things over to Alan to kick

**[03:00](https://youtube.com/watch?v=4AxaKxZIO4Y&t=180s)** us off. Awesome. Thank you, Kate. I appreciate it. Again, welcome, everyone. Good morning,

**[03:06](https://youtube.com/watch?v=4AxaKxZIO4Y&t=186s)** good afternoon, good evening, wherever you're calling in from. It looks like we have folks from

**[03:10](https://youtube.com/watch?v=4AxaKxZIO4Y&t=190s)** all over the world. So that's always super excited. If you're not sure why you're here, well,

**[03:16](https://youtube.com/watch?v=4AxaKxZIO4Y&t=196s)** this is our slide, modernizing remote access to EKS with tailscale. We've got some cool things.

**[03:22](https://youtube.com/watch?v=4AxaKxZIO4Y&t=202s)** We're going to show about leveraging tailscale along with EKS. We'll get to those in a few minutes.

**[03:28](https://youtube.com/watch?v=4AxaKxZIO4Y&t=208s)** But as a quick intro, my name is again, Alan. I'm one of the solutions engineers over here at

**[03:34](https://youtube.com/watch?v=4AxaKxZIO4Y&t=214s)** tailscale. I've been here for just over two years or so and it's seen a lot of excitement, a lot of

**[03:39](https://youtube.com/watch?v=4AxaKxZIO4Y&t=219s)** growth, talking to customers that are leveraging tailscale or new to tailscale. So I'm excited to

**[03:45](https://youtube.com/watch?v=4AxaKxZIO4Y&t=225s)** help co-host this along with Raj and I'll pass over to you for your intro, Raj.

**[03:51](https://youtube.com/watch?v=4AxaKxZIO4Y&t=231s)** Hey guys, my name is Raj. I'm a customer success engineer here at tailscale and

**[03:57](https://youtube.com/watch?v=4AxaKxZIO4Y&t=237s)** at going Alan. I'm kind of doing same kind of stuff, helping our customers on board and

**[04:02](https://youtube.com/watch?v=4AxaKxZIO4Y&t=242s)** utilize things like our Kubernetes upgrade. Cool. Awesome. So let's jump right into it and

**[04:09](https://youtube.com/watch?v=4AxaKxZIO4Y&t=249s)** definitely drop a note in comments in our Q&A as Kate mentioned and we'd love to answer these

**[04:17](https://youtube.com/watch?v=4AxaKxZIO4Y&t=257s)** questions. And the goal of today and today's agenda is to educate you a little bit more.

**[04:22](https://youtube.com/watch?v=4AxaKxZIO4Y&t=262s)** Hopefully you leave today, have a little bit of better understanding of tailscale and our

**[04:27](https://youtube.com/watch?v=4AxaKxZIO4Y&t=267s)** Kubernetes operator and some of the cool things you can do with it. So that is what we're going to

**[04:31](https://youtube.com/watch?v=4AxaKxZIO4Y&t=271s)** cover working with AWS even though the titles EKS, you know, Kubernetes can be run anywhere but

**[04:38](https://youtube.com/watch?v=4AxaKxZIO4Y&t=278s)** we are partners with AWS and so we're grateful for that partnership and being able to work

**[04:45](https://youtube.com/watch?v=4AxaKxZIO4Y&t=285s)** and within AWS and a lot of our customers are there as well. Then we'll be talking through

**[04:51](https://youtube.com/watch?v=4AxaKxZIO4Y&t=291s)** Kubernetes around tailscale. Then the fun stuff, Raj will be leading a really cool demo of showing

**[04:57](https://youtube.com/watch?v=4AxaKxZIO4Y&t=297s)** how tailscale with our operator can work and how you can even implement some of that today.

**[05:02](https://youtube.com/watch?v=4AxaKxZIO4Y&t=302s)** And then at the end, we're going to have a Q&A so definitely bring those questions and we'll do

**[05:07](https://youtube.com/watch?v=4AxaKxZIO4Y&t=307s)** our best to get to them for sure. So for those that are brand new and have never heard of tailscale,

**[05:14](https://youtube.com/watch?v=4AxaKxZIO4Y&t=314s)** you signed up, someone said, hey, join this webinar. Thank you for coming. So I'm going to do a

**[05:18](https://youtube.com/watch?v=4AxaKxZIO4Y&t=318s)** quick high level overview for some of you that are familiar with tailscale have been using it already.

**[05:24](https://youtube.com/watch?v=4AxaKxZIO4Y&t=324s)** You know, some of this might be a repeat, but I'll just do a little bit of a high level of what is

**[05:29](https://youtube.com/watch?v=4AxaKxZIO4Y&t=329s)** tailscale. Tailscale is a zero trust network goal of overlay, excuse me, built on wire guard.

**[05:36](https://youtube.com/watch?v=4AxaKxZIO4Y&t=336s)** Wire guard, which is an awesome open source VPN networking protocol that layers end-to-end

**[05:44](https://youtube.com/watch?v=4AxaKxZIO4Y&t=344s)** encryption for any of those devices. Tailscale is built on top of that and we just make it

**[05:50](https://youtube.com/watch?v=4AxaKxZIO4Y&t=350s)** easier for those that have played with wire guard in the past. Maybe you've set up your own

**[05:55](https://youtube.com/watch?v=4AxaKxZIO4Y&t=355s)** wire guard systems and tunnels and it's great for home lab work, but what happens after

**[05:59](https://youtube.com/watch?v=4AxaKxZIO4Y&t=359s)** while if you're trying to scale it, you start realizing, oh, I've got a lot of technical debt

**[06:04](https://youtube.com/watch?v=4AxaKxZIO4Y&t=364s)** or burden potentially on this. So we've come along and we've tried to simplify that to make tailscale

**[06:09](https://youtube.com/watch?v=4AxaKxZIO4Y&t=369s)** really work well for those folks and I have to worry about maintaining a ton of that infrastructure

**[06:15](https://youtube.com/watch?v=4AxaKxZIO4Y&t=375s)** behind the scenes. Tailscale operates on layer three. So the geeks in the room here, those that

**[06:23](https://youtube.com/watch?v=4AxaKxZIO4Y&t=383s)** are familiar with the OSI model, recognizing all these different layers. Tailscale lives on layer three

**[06:30](https://youtube.com/watch?v=4AxaKxZIO4Y&t=390s)** predominantly. We are, as mentioned previously, an encrypted network overlay. So you know,

**[06:36](https://youtube.com/watch?v=4AxaKxZIO4Y&t=396s)** devices get a IP address and, you know, they bridge across whatever your internet service provider

**[06:43](https://youtube.com/watch?v=4AxaKxZIO4Y&t=403s)** is or that physical and data link layer to talk to other, you know, tailscale devices around the world.

**[06:51](https://youtube.com/watch?v=4AxaKxZIO4Y&t=411s)** Different tools out there also operate a variety of layers. Some tools out there operate on

**[06:57](https://youtube.com/watch?v=4AxaKxZIO4Y&t=417s)** pure layer seven like an application layer. Some are layer six, even some on layer five,

**[07:03](https://youtube.com/watch?v=4AxaKxZIO4Y&t=423s)** but bring it down to the network layer as tailscale does introduces, you know, a lot more

**[07:10](https://youtube.com/watch?v=4AxaKxZIO4Y&t=430s)** ability to be granular and how you manage that network access. And when you can tie access to

**[07:18](https://youtube.com/watch?v=4AxaKxZIO4Y&t=438s)** devices on a network level, you can layer some of these other pieces on top of it and just makes it

**[07:24](https://youtube.com/watch?v=4AxaKxZIO4Y&t=444s)** a really nice experience for end users. So it is a, because it's wire guard, so it's a mesh

**[07:32](https://youtube.com/watch?v=4AxaKxZIO4Y&t=452s)** networking tool. Again, if you're not familiar with tailscale and you think, well, you know,

**[07:37](https://youtube.com/watch?v=4AxaKxZIO4Y&t=457s)** what's mesh networking, the traditional VPN or a lot of the traditional connectivity tools out there

**[07:44](https://youtube.com/watch?v=4AxaKxZIO4Y&t=464s)** that, you know, L2TP, IPSEC, SSL VPNs, tend to operate on a hub and spoke type of model.

**[07:51](https://youtube.com/watch?v=4AxaKxZIO4Y&t=471s)** Tailscale, because wire guard, it's mesh based and it's really designed as a point to point.

**[07:57](https://youtube.com/watch?v=4AxaKxZIO4Y&t=477s)** And on top of that, we layer a user's identity within that. So we're not just saying, hey,

**[08:04](https://youtube.com/watch?v=4AxaKxZIO4Y&t=484s)** you know, this laptop can see this or do do whatever. It's based on that identity of that person

**[08:10](https://youtube.com/watch?v=4AxaKxZIO4Y&t=490s)** that's trying to accomplish or trying to access something. And in today's world of zero trust

**[08:16](https://youtube.com/watch?v=4AxaKxZIO4Y&t=496s)** and being able to tie into identity, that's a huge thing because now you can say, hey,

**[08:22](https://youtube.com/watch?v=4AxaKxZIO4Y&t=502s)** Allen's identity, when he authenticates, he's multi factor authentication into different

**[08:28](https://youtube.com/watch?v=4AxaKxZIO4Y&t=508s)** applications and sites and tools, tailscale is going to take that identity and then leverage that

**[08:33](https://youtube.com/watch?v=4AxaKxZIO4Y&t=513s)** with our adaptive policy engine in order to grant access across the board. And the nice thing

**[08:40](https://youtube.com/watch?v=4AxaKxZIO4Y&t=520s)** about when you have it with like identity and things around that line is you get the ability to do

**[08:48](https://youtube.com/watch?v=4AxaKxZIO4Y&t=528s)** least privilege access. So traditionally, for those of us that are old, been around and maybe

**[08:55](https://youtube.com/watch?v=4AxaKxZIO4Y&t=535s)** working in an office that has a traditional firewall, corporate land, you hop in, you plug in,

**[09:01](https://youtube.com/watch?v=4AxaKxZIO4Y&t=541s)** you start working, you may or may not realize you might have access and can see all the things

**[09:07](https://youtube.com/watch?v=4AxaKxZIO4Y&t=547s)** on a corporate land. And that's traditionally how a lot of access has been done in the past.

**[09:13](https://youtube.com/watch?v=4AxaKxZIO4Y&t=553s)** Fast forward today where you've got workers working remote, working hybrid and doing all kinds

**[09:19](https://youtube.com/watch?v=4AxaKxZIO4Y&t=559s)** of stuff, different areas might not even be in an office at a the same workstation or along that line.

**[09:27](https://youtube.com/watch?v=4AxaKxZIO4Y&t=567s)** Now you say how we can't just segment and base security on a border perimeter of a firewall

**[09:34](https://youtube.com/watch?v=4AxaKxZIO4Y&t=574s)** going along that line. So we need to add that through the identity and no better way to do it,

**[09:39](https://youtube.com/watch?v=4AxaKxZIO4Y&t=579s)** than that users identity. So when I sign in, we can look at that and say, hey, Alan signing in,

**[09:45](https://youtube.com/watch?v=4AxaKxZIO4Y&t=585s)** so our policy engine is going to look at Alan again, look at these access control is based on his

**[09:50](https://youtube.com/watch?v=4AxaKxZIO4Y&t=590s)** name and his identity. And then we're going to grant them access as needed. And it's even, you know,

**[09:57](https://youtube.com/watch?v=4AxaKxZIO4Y&t=597s)** you're explicitly authorizing again, tail scale operates on a initially as a denied by default,

**[10:04](https://youtube.com/watch?v=4AxaKxZIO4Y&t=604s)** that's this part of tail scale, it's also part of wire guard. So unless someone has been given

**[10:09](https://youtube.com/watch?v=4AxaKxZIO4Y&t=609s)** its explicit permissions to access a resource, they're not going to be able to see it.

**[10:16](https://youtube.com/watch?v=4AxaKxZIO4Y&t=616s)** So you have to, you know, put in the special rules that, hey, we're going to give Alan access,

**[10:21](https://youtube.com/watch?v=4AxaKxZIO4Y&t=621s)** we're going to give Raj access to this Kubernetes cluster because we trust him, he's in the right group,

**[10:26](https://youtube.com/watch?v=4AxaKxZIO4Y&t=626s)** et cetera. You can integrate this policy that we have our policy management using tools like

**[10:33](https://youtube.com/watch?v=4AxaKxZIO4Y&t=633s)** infrastructures code using get ops, ways that you can implement and the policies from tail scale

**[10:40](https://youtube.com/watch?v=4AxaKxZIO4Y&t=640s)** into your workflow, your day-to-day managing access. One other cool thing that is out now for those

**[10:46](https://youtube.com/watch?v=4AxaKxZIO4Y&t=646s)** that might be have been using tail scale for a while, you notice previously we've had this

**[10:52](https://youtube.com/watch?v=4AxaKxZIO4Y&t=652s)** text editor, it's JSON editor for our policies within the tail scale application.

**[10:58](https://youtube.com/watch?v=4AxaKxZIO4Y&t=658s)** Nowadays, we have a visual editor, which is really cool. So it gives, again, users the ability to

**[11:04](https://youtube.com/watch?v=4AxaKxZIO4Y&t=664s)** quickly look at and say, hmm, let's make a rule that gives this person access to this device

**[11:10](https://youtube.com/watch?v=4AxaKxZIO4Y&t=670s)** from a human to machine perspective. Or maybe let's give an access rule that gives these two

**[11:14](https://youtube.com/watch?v=4AxaKxZIO4Y&t=674s)** Kubernetes clusters access to one another using machine to machine policies. And with our visual

**[11:20](https://youtube.com/watch?v=4AxaKxZIO4Y&t=680s)** editor or tying it into something like get ops or infrastructure as code allows you the ability to

**[11:27](https://youtube.com/watch?v=4AxaKxZIO4Y&t=687s)** be very granular and how you're managing access for your users and your user user, excuse me,

**[11:33](https://youtube.com/watch?v=4AxaKxZIO4Y&t=693s)** user devices as well. So a few deployment models. And then one I just thought of here,

**[11:39](https://youtube.com/watch?v=4AxaKxZIO4Y&t=699s)** it's not mentioned here is the Kubernetes model here. So tail scale on a high level when you're

**[11:45](https://youtube.com/watch?v=4AxaKxZIO4Y&t=705s)** looking at from deploying it, you have device to device where I've got tail scale running on my laptop,

**[11:50](https://youtube.com/watch?v=4AxaKxZIO4Y&t=710s)** I've got it running on my phone, I've got it running on a virtual machine in AWS,

**[11:54](https://youtube.com/watch?v=4AxaKxZIO4Y&t=714s)** that kind of device device piece there. There's also the model of a subnet router where you have

**[12:01](https://youtube.com/watch?v=4AxaKxZIO4Y&t=721s)** tail scale running on your laptop or phone, but then I need to get access to a printer. And,

**[12:06](https://youtube.com/watch?v=4AxaKxZIO4Y&t=726s)** or maybe we have an old Windows server that we can't put tail scale on for some reason.

**[12:10](https://youtube.com/watch?v=4AxaKxZIO4Y&t=730s)** Well, you can use a subnet router, which allows your connectivity to bridge into local area

**[12:18](https://youtube.com/watch?v=4AxaKxZIO4Y&t=738s)** networks and even add multiple different routes across the board.

**[12:22](https://youtube.com/watch?v=4AxaKxZIO4Y&t=742s)** An app connector is another model of deploying in tail scale. It's the ability to leverage tail scale

**[12:30](https://youtube.com/watch?v=4AxaKxZIO4Y&t=750s)** as a exit node or direct proxy in the essence to a SAS type application. How this comes into play

**[12:39](https://youtube.com/watch?v=4AxaKxZIO4Y&t=759s)** a lot is where we see customers that have whitelisted SAS apps or applications where they need to have

**[12:47](https://youtube.com/watch?v=4AxaKxZIO4Y&t=767s)** only allowing ingress from this known IP address. Well, if you're on an office, it's easy. You just

**[12:53](https://youtube.com/watch?v=4AxaKxZIO4Y&t=773s)** get the corporate land, the corporate WAN IP address, plug it in, call it a day. Well, what happens

**[12:59](https://youtube.com/watch?v=4AxaKxZIO4Y&t=779s)** when people travel, they're at a conference, they're at a hotel, they're working from home.

**[13:03](https://youtube.com/watch?v=4AxaKxZIO4Y&t=783s)** Now they have to open up a ticket and say, oh, I've got a new home IP address. Can you add this

**[13:07](https://youtube.com/watch?v=4AxaKxZIO4Y&t=787s)** to the white list? That just doesn't scale effectively. Whereas if you had something like the app

**[13:14](https://youtube.com/watch?v=4AxaKxZIO4Y&t=794s)** connector, now you can just say, you know what, as long as that person's on the tail net,

**[13:19](https://youtube.com/watch?v=4AxaKxZIO4Y&t=799s)** and they're connecting through, we're going to allow and proxy that connectivity into that third

**[13:24](https://youtube.com/watch?v=4AxaKxZIO4Y&t=804s)** party app. So it's a great way of managing that. And then the last piece here is exit node is tail

**[13:30](https://youtube.com/watch?v=4AxaKxZIO4Y&t=810s)** scale operates split tunnel for those that are like, hey, can I use tail scale full tunnel split tunnel

**[13:36](https://youtube.com/watch?v=4AxaKxZIO4Y&t=816s)** out of the box? It does operate as a split tunnel network overlay. So if you're working and you're

**[13:42](https://youtube.com/watch?v=4AxaKxZIO4Y&t=822s)** accessing, you know, corporate resources, it's going to go over tail scale along that line.

**[13:49](https://youtube.com/watch?v=4AxaKxZIO4Y&t=829s)** But if you're on lunch break, you're going to YouTube or listen to Spotify or whatever, you know,

**[13:54](https://youtube.com/watch?v=4AxaKxZIO4Y&t=834s)** do something else, it's going to route through your general public internet and bypassing

**[13:59](https://youtube.com/watch?v=4AxaKxZIO4Y&t=839s)** that exit node. I mean, excuse me, bypassing tail scale, but you can flip it and turn it on,

**[14:03](https://youtube.com/watch?v=4AxaKxZIO4Y&t=843s)** saying, you know, we're going to full tunnel our traffic. We've got some people traveling out of

**[14:07](https://youtube.com/watch?v=4AxaKxZIO4Y&t=847s)** a conference and maybe there's some sketchy Wi-Fi and we just want to be a little bit more secure.

**[14:13](https://youtube.com/watch?v=4AxaKxZIO4Y&t=853s)** So now we've just put up some exit nodes out there that employees and others can take advantage

**[14:18](https://youtube.com/watch?v=4AxaKxZIO4Y&t=858s)** of and leverage that. So as mentioned earlier, you know, tail scale and AWS. We are partners,

**[14:26](https://youtube.com/watch?v=4AxaKxZIO4Y&t=866s)** we are an ISV partner with AWS, we're verified on there. You can find this in the marketplace.

**[14:33](https://youtube.com/watch?v=4AxaKxZIO4Y&t=873s)** And AWS actually helps us a lot with some of our webinars. So in this case, for those that

**[14:39](https://youtube.com/watch?v=4AxaKxZIO4Y&t=879s)** have AWS spend or you are doing a lot within the end, excuse me, AWS marketplace, you can find

**[14:47](https://youtube.com/watch?v=4AxaKxZIO4Y&t=887s)** tail scale there, reach out to us as well. We have a whole team that's dedicated to helping

**[14:52](https://youtube.com/watch?v=4AxaKxZIO4Y&t=892s)** customers transact and work within AWS. But we're excited and we're thankful for their

**[14:58](https://youtube.com/watch?v=4AxaKxZIO4Y&t=898s)** partnership for this as well. All right. So let me take a glass of water here. So that's it from

**[15:06](https://youtube.com/watch?v=4AxaKxZIO4Y&t=906s)** a high level what tail scale is. So let's jump into why you're here today, right? The meat of

**[15:11](https://youtube.com/watch?v=4AxaKxZIO4Y&t=911s)** tail scale and today's webinar, tail scale and Kubernetes. So one deployment option that didn't show

**[15:18](https://youtube.com/watch?v=4AxaKxZIO4Y&t=918s)** up on that last screen is that ability to leverage Kubernetes. So over the last year or so,

**[15:24](https://youtube.com/watch?v=4AxaKxZIO4Y&t=924s)** we've our team has built out a Kubernetes operator, which is really awesome. It allows you to

**[15:31](https://youtube.com/watch?v=4AxaKxZIO4Y&t=931s)** extend tail scale to your Kubernetes clusters, providing secure access to your control plane,

**[15:37](https://youtube.com/watch?v=4AxaKxZIO4Y&t=937s)** access those non-cubanity services and from Kubernetes, as well as enable cross cluster connectivity.

**[15:45](https://youtube.com/watch?v=4AxaKxZIO4Y&t=945s)** And that is some of the cool stuff that Raj will be showing later on today.

**[15:51](https://youtube.com/watch?v=4AxaKxZIO4Y&t=951s)** From an authentication piece there, what tail scale looks like on, you know, the frictionless

**[15:56](https://youtube.com/watch?v=4AxaKxZIO4Y&t=956s)** piece there is it can leverage and manage the cube API access. So when we talk about

**[16:05](https://youtube.com/watch?v=4AxaKxZIO4Y&t=965s)** identity-based networking and we're hey, we're now introducing Kubernetes into our network.

**[16:13](https://youtube.com/watch?v=4AxaKxZIO4Y&t=973s)** Well, we don't want everyone to be system masters. Maybe the DevOps team needs to be, but maybe

**[16:18](https://youtube.com/watch?v=4AxaKxZIO4Y&t=978s)** this engineering group only needs to have access to certain namespaces. Well, tail scale, you can leverage

**[16:24](https://youtube.com/watch?v=4AxaKxZIO4Y&t=984s)** the tail scale operator to manage access to the cube API, as well as even down to some of the

**[16:32](https://youtube.com/watch?v=4AxaKxZIO4Y&t=992s)** authentication, some of the permissions pieces there, which is a really, you know, fundamental use case,

**[16:38](https://youtube.com/watch?v=4AxaKxZIO4Y&t=998s)** but also something we see some great usage out of for sure. Another thing that is really cool with

**[16:45](https://youtube.com/watch?v=4AxaKxZIO4Y&t=1005s)** Kubernetes is this is a relatively new feature, I think the last two to three months.

**[16:51](https://youtube.com/watch?v=4AxaKxZIO4Y&t=1011s)** We've had SSH recording for a while now and it's a really cool feature if you're doing a lot of

**[16:56](https://youtube.com/watch?v=4AxaKxZIO4Y&t=1016s)** SSH, but one thing where we have now and more coming out is the ability to connect to those

**[17:05](https://youtube.com/watch?v=4AxaKxZIO4Y&t=1025s)** Kubernetes sessions, those pods, exec in, but having a session recording and the ability to audit

**[17:12](https://youtube.com/watch?v=4AxaKxZIO4Y&t=1032s)** what's happening on there. So now you can cube exec into a pod, do some work on it,

**[17:20](https://youtube.com/watch?v=4AxaKxZIO4Y&t=1040s)** you get out, but now we have this nice session recording that's recorded in ASCII cinema format

**[17:26](https://youtube.com/watch?v=4AxaKxZIO4Y&t=1046s)** allows you to parse it, download it or view it. Again, this is all stored within your

**[17:31](https://youtube.com/watch?v=4AxaKxZIO4Y&t=1051s)** tailnet and infrastructure that you control tail scale does not see this, but allows companies,

**[17:36](https://youtube.com/watch?v=4AxaKxZIO4Y&t=1056s)** security teams to be able to have these recordings from a security compliance, an audit and even

**[17:43](https://youtube.com/watch?v=4AxaKxZIO4Y&t=1063s)** training capabilities within their Kubernetes clusters. The other thing that we have here,

**[17:52](https://youtube.com/watch?v=4AxaKxZIO4Y&t=1072s)** and I think Raj will flip it over to you here on the next slide, is the cross cluster connectivity

**[17:58](https://youtube.com/watch?v=4AxaKxZIO4Y&t=1078s)** piece. As I mentioned, Kubernetes allows you that ability to network Kubernetes clusters wherever

**[18:05](https://youtube.com/watch?v=4AxaKxZIO4Y&t=1085s)** they might be around the world or in different AWS regions and data centers. So you can use the

**[18:12](https://youtube.com/watch?v=4AxaKxZIO4Y&t=1092s)** Kubernetes operator to help manage that. In this case, in this example, showing that how we have

**[18:18](https://youtube.com/watch?v=4AxaKxZIO4Y&t=1098s)** tailscale operator, you got an ingress, egress proxy pair, they can see one another, those services

**[18:24](https://youtube.com/watch?v=4AxaKxZIO4Y&t=1104s)** and those clusters can communicate securely over a fully encrypted tunnel over the general

**[18:30](https://youtube.com/watch?v=4AxaKxZIO4Y&t=1110s)** public internet or within region or whatever it might be knowing that's all managed from a tail

**[18:35](https://youtube.com/watch?v=4AxaKxZIO4Y&t=1115s)** scale side of the fence. And Raj, I'll let you kick in here on this piece here, so this ties in

**[18:44](https://youtube.com/watch?v=4AxaKxZIO4Y&t=1124s)** I think to some of your demo stuff. Yeah, of course. Yeah, so now let's go a little bit over the demo

**[18:50](https://youtube.com/watch?v=4AxaKxZIO4Y&t=1130s)** that I'm going to kind of show you guys. So I have like two major use cases that I will essentially

**[18:56](https://youtube.com/watch?v=4AxaKxZIO4Y&t=1136s)** showcase here. The first one is like, okay, you have a singular Kubernetes cluster that's kind

**[19:02](https://youtube.com/watch?v=4AxaKxZIO4Y&t=1142s)** of running for fauna, and then you have multiple other clusters that are kind of posting from

**[19:06](https://youtube.com/watch?v=4AxaKxZIO4Y&t=1146s)** metheist instances. Using the Kubernetes operator, we can actually establish connectivity across regions

**[19:16](https://youtube.com/watch?v=4AxaKxZIO4Y&t=1156s)** or across different clusters to actually expose the other clusters, chometheist instances

**[19:23](https://youtube.com/watch?v=4AxaKxZIO4Y&t=1163s)** directly to your fauna instance. And I will showcase that in a little bit. Then the other

**[19:32](https://youtube.com/watch?v=4AxaKxZIO4Y&t=1172s)** option is actually like a high availability, almost like a failover aspect. So in this case,

**[19:37](https://youtube.com/watch?v=4AxaKxZIO4Y&t=1177s)** another example I'm going to get used, like kind of running your own chatchy BT. So I'll be using

**[19:41](https://youtube.com/watch?v=4AxaKxZIO4Y&t=1181s)** like open web UI to kind of expose the front end interface and then have other clusters that kind

**[19:48](https://youtube.com/watch?v=4AxaKxZIO4Y&t=1188s)** of have some GPUs attached to them, and you know, are running inference models. So like in this

**[19:55](https://youtube.com/watch?v=4AxaKxZIO4Y&t=1195s)** case, we're going to be running quen, which will allow your gateway clusters to access the inference

**[20:01](https://youtube.com/watch?v=4AxaKxZIO4Y&t=1201s)** clusters to make their queries. So this is kind of, you know, what the EKCTL configuration kind of

**[20:10](https://youtube.com/watch?v=4AxaKxZIO4Y&t=1210s)** looks like here. We have one cluster in US East one and then another one in inference cluster in

**[20:16](https://youtube.com/watch?v=4AxaKxZIO4Y&t=1216s)** US West two. The node groups are, you'll notice they're kind of slightly different is that the

**[20:21](https://youtube.com/watch?v=4AxaKxZIO4Y&t=1221s)** inference cluster actually has, I believe, T40 and video GPUs attached to them. So to first like expose

**[20:33](https://youtube.com/watch?v=4AxaKxZIO4Y&t=1233s)** something into the town that we call this ingress, right? We're going to spin up something we call

**[20:39](https://youtube.com/watch?v=4AxaKxZIO4Y&t=1239s)** a proxy group ingress, which you'll see at the top left there. I'll assign some identity tags in,

**[20:45](https://youtube.com/watch?v=4AxaKxZIO4Y&t=1245s)** in this case, you know, what location they're in, and you know, what kind of thing is this in this

**[20:49](https://youtube.com/watch?v=4AxaKxZIO4Y&t=1249s)** case? It's K8s. It's highly available. So we'll spin up a couple of them, three replicas,

**[20:56](https://youtube.com/watch?v=4AxaKxZIO4Y&t=1256s)** and then, you know, have some host name prefixes so that there, you know, these proxy groups that

**[21:04](https://youtube.com/watch?v=4AxaKxZIO4Y&t=1264s)** you will define will actually spin up tail scale clients within your cluster that kind of act as that,

**[21:10](https://youtube.com/watch?v=4AxaKxZIO4Y&t=1270s)** you know, I guess it's a proxy that's essentially funneling traffic in and out of tail scale in your

**[21:16](https://youtube.com/watch?v=4AxaKxZIO4Y&t=1276s)** private network. So at the bottom left, you'll see like the tail scale service. And here we're

**[21:22](https://youtube.com/watch?v=4AxaKxZIO4Y&t=1282s)** defining a host name. So like what do we want? The connectivity point to be in this case, we named it

**[21:28](https://youtube.com/watch?v=4AxaKxZIO4Y&t=1288s)** Quinn. We attached a proxy group ingress via the annotation as well. And, you know, instead of a cluster

**[21:36](https://youtube.com/watch?v=4AxaKxZIO4Y&t=1296s)** IP, it's very similar to like an EC2 ELB or load balancer will actually set a load balancer class

**[21:44](https://youtube.com/watch?v=4AxaKxZIO4Y&t=1304s)** of tail scale. And then expose, I guess, in this case, port 80 of our Quinn model to our talent.

**[21:55](https://youtube.com/watch?v=4AxaKxZIO4Y&t=1315s)** So I guess like the path here is kind of like your client, your any client, whether that be

**[22:01](https://youtube.com/watch?v=4AxaKxZIO4Y&t=1321s)** another Kubernetes cluster or your tail scale laptop will first reach a proxy pod running within

**[22:08](https://youtube.com/watch?v=4AxaKxZIO4Y&t=1328s)** your cluster. And then forward its traffic to through the cluster IP service running in your

**[22:14](https://youtube.com/watch?v=4AxaKxZIO4Y&t=1334s)** Kubernetes cluster. And as you can see, you know, we've, the operator has came in and assigned an

**[22:20](https://youtube.com/watch?v=4AxaKxZIO4Y&t=1340s)** IP address in the CG not range, which is where tail tail scale IPs kind of live. And then also

**[22:27](https://youtube.com/watch?v=4AxaKxZIO4Y&t=1347s)** provided you a host name. In this case, it's quen.rashafu. And then this is the idea of

**[22:36](https://youtube.com/watch?v=4AxaKxZIO4Y&t=1356s)** egressing a service. So you'll similarly deploy a proxy group egress. And then I'll, within a service,

**[22:43](https://youtube.com/watch?v=4AxaKxZIO4Y&t=1363s)** you'll define something we call an external name service, which is kind of, you know, how we are

**[22:50](https://youtube.com/watch?v=4AxaKxZIO4Y&t=1370s)** exposing tail net services to a cluster. So in this case, you know, we want to expose

**[22:57](https://youtube.com/watch?v=4AxaKxZIO4Y&t=1377s)** usw2's AI, quen model via that annotation there to the tail net as the service name of usw2

**[23:09](https://youtube.com/watch?v=4AxaKxZIO4Y&t=1389s)** AI, quen. And you can see the operators came in. It's assigned a name to the external name and

**[23:18](https://youtube.com/watch?v=4AxaKxZIO4Y&t=1398s)** created a actually headless service within your cluster to actually, sorry, sorry about that.

**[23:31](https://youtube.com/watch?v=4AxaKxZIO4Y&t=1411s)** Forward traffic from your tail net into the cluster. So that's kind of what's going on here.

**[23:40](https://youtube.com/watch?v=4AxaKxZIO4Y&t=1420s)** So I guess now I'll take over screen sharing here. And the first thing I'll share is I kind

**[23:47](https://youtube.com/watch?v=4AxaKxZIO4Y&t=1427s)** of have given you, I kind of have examples of everything. So first is like API server connectivity,

**[23:53](https://youtube.com/watch?v=4AxaKxZIO4Y&t=1433s)** the recorder, and then obviously the cross cluster connectivity as well. So the first thing

**[24:00](https://youtube.com/watch?v=4AxaKxZIO4Y&t=1440s)** I will show is what things look like within the cluster. So from a, I guess, user perspective.

**[24:17](https://youtube.com/watch?v=4AxaKxZIO4Y&t=1457s)** So I'm going to share my browser here. And as you can see, I'm coming in through TS.net

**[24:23](https://youtube.com/watch?v=4AxaKxZIO4Y&t=1463s)** domain. So some cluster is actually advertising this. And currently, I don't know if it's usw1,

**[24:29](https://youtube.com/watch?v=4AxaKxZIO4Y&t=1469s)** but west two or east one, but they're both, you know, advertising this graphana instance. And they

**[24:35](https://youtube.com/watch?v=4AxaKxZIO4Y&t=1475s)** also have established connectivity to other, other clusters via like, in this case, graphana data

**[24:41](https://youtube.com/watch?v=4AxaKxZIO4Y&t=1481s)** sources. So I'm kind of pointing graphana to say, Hey, you have a, for me, for instance,

**[24:46](https://youtube.com/watch?v=4AxaKxZIO4Y&t=1486s)** at this point, and then you have another, another for me, for instance, at the west two clusters. So

**[24:52](https://youtube.com/watch?v=4AxaKxZIO4Y&t=1492s)** and this all works and it's really cool. So, you know, I can come in here, grab here, and,

**[24:57](https://youtube.com/watch?v=4AxaKxZIO4Y&t=1497s)** and kind of view both clusters at the same, at the same graphana instance. And that's really

**[25:03](https://youtube.com/watch?v=4AxaKxZIO4Y&t=1503s)** cool. The other really cool thing that'll happen since that both clusters are kind of advertising

**[25:08](https://youtube.com/watch?v=4AxaKxZIO4Y&t=1508s)** this graphana instance is that if, you know, your users are closer to, I guess, California,

**[25:14](https://youtube.com/watch?v=4AxaKxZIO4Y&t=1514s)** they'll actually go to the west two graphana instance versus me. In this case, I'm in Chicago. So

**[25:20](https://youtube.com/watch?v=4AxaKxZIO4Y&t=1520s)** I reached the usw1. And I think that's pretty cool. So that's what I'll show there. The really

**[25:29](https://youtube.com/watch?v=4AxaKxZIO4Y&t=1529s)** cool one is open web UI, which is just kind of like, you're a self-hostable, you know, ChatchyBT.

**[25:36](https://youtube.com/watch?v=4AxaKxZIO4Y&t=1536s)** So I've exposed, obviously, like an external name service to do cluster egress. And I've defined

**[25:43](https://youtube.com/watch?v=4AxaKxZIO4Y&t=1543s)** in our, you know, admin settings here, like, Hey, anytime we want to make a query to an inference

**[25:49](https://youtube.com/watch?v=4AxaKxZIO4Y&t=1549s)** model, we will do it over this external name service. And point seven, in this case, it's an AI

**[25:55](https://youtube.com/watch?v=4AxaKxZIO4Y&t=1555s)** name space. And then this is the name of the external service. And this all works. So I can say,

**[26:01](https://youtube.com/watch?v=4AxaKxZIO4Y&t=1561s)** like, what is tail scale? And from here, we're making the query directly from, in this case, US East

**[26:09](https://youtube.com/watch?v=4AxaKxZIO4Y&t=1569s)** one to US West two, West two being the one with the GPUs. And that's incredibly cool.

**[26:18](https://youtube.com/watch?v=4AxaKxZIO4Y&t=1578s)** On top of that, I also have reporting up here for you. So this is kind of what it looks like,

**[26:23](https://youtube.com/watch?v=4AxaKxZIO4Y&t=1583s)** you know, user comes in, they kind of shell in, they do some stuff in this case where I have my

**[26:29](https://youtube.com/watch?v=4AxaKxZIO4Y&t=1589s)** buddy here, Kartek, he's, you know, come in through his MacBook and he's deep, and he's shell

**[26:33](https://youtube.com/watch?v=4AxaKxZIO4Y&t=1593s)** into this plot here. And as this continues. And, you know, that's really cool. So

**[26:41](https://youtube.com/watch?v=4AxaKxZIO4Y&t=1601s)** that's some other use case. We also have this ability, which we didn't really touch on,

**[26:44](https://youtube.com/watch?v=4AxaKxZIO4Y&t=1604s)** which is the idea of exposing some, some, I guess, Kubernetes service up onto the internet.

**[26:51](https://youtube.com/watch?v=4AxaKxZIO4Y&t=1611s)** So the way I'm showcasing this is using web hooks within GitHub. So this repo, I believe,

**[26:59](https://youtube.com/watch?v=4AxaKxZIO4Y&t=1619s)** will probably show share within the chat, but essentially what we're doing is, you know, I use

**[27:04](https://youtube.com/watch?v=4AxaKxZIO4Y&t=1624s)** get ops to kind of manage my clusters. And every time I make a commit, I kind of want to let my

**[27:10](https://youtube.com/watch?v=4AxaKxZIO4Y&t=1630s)** clusters know that there's a new change within make it repository. So every time I make a commit,

**[27:15](https://youtube.com/watch?v=4AxaKxZIO4Y&t=1635s)** you'll see like the last delivery was successful. We're actually going out and we are

**[27:20](https://youtube.com/watch?v=4AxaKxZIO4Y&t=1640s)** pushing traffic, I guess, I can show it in this case, but we're actually pushing, I guess,

**[27:26](https://youtube.com/watch?v=4AxaKxZIO4Y&t=1646s)** GitHub is pushing a web hook saying, hey, there's a new commit, and it's going directly to both

**[27:33](https://youtube.com/watch?v=4AxaKxZIO4Y&t=1653s)** clusters, which is the way through. And again, I did write in an app called TSflow, which kind of

**[27:41](https://youtube.com/watch?v=4AxaKxZIO4Y&t=1661s)** lets you visualize this. So this is like another way of kind of, you know, capturing our network

**[27:46](https://youtube.com/watch?v=4AxaKxZIO4Y&t=1666s)** logs. That's something else you didn't really touch on, but, you know, we have layer three,

**[27:51](https://youtube.com/watch?v=4AxaKxZIO4Y&t=1671s)** where layer three solution, and we also capture, you know, device to device connectivity,

**[27:57](https://youtube.com/watch?v=4AxaKxZIO4Y&t=1677s)** so we know source and destination of who's accessing what. And all I've done is just, you know,

**[28:01](https://youtube.com/watch?v=4AxaKxZIO4Y&t=1681s)** kind of visualize that. So you can see that like my map book is essentially, you know,

**[28:06](https://youtube.com/watch?v=4AxaKxZIO4Y&t=1686s)** reaching the chat application in this case, its own TSflow application, as well as a

**[28:11](https://youtube.com/watch?v=4AxaKxZIO4Y&t=1691s)** profanum. And then obviously the two Kubernetes operators running in each cluster.

**[28:19](https://youtube.com/watch?v=4AxaKxZIO4Y&t=1699s)** And then the other thing we can see here is, you know, when we made that query to

**[28:25](https://youtube.com/watch?v=4AxaKxZIO4Y&t=1705s)** from the open web UI to our inference model, you can see that the US East one Egress proxy pods

**[28:33](https://youtube.com/watch?v=4AxaKxZIO4Y&t=1713s)** made a request to US West too. And then similarly, you can see the Prometheus instances,

**[28:39](https://youtube.com/watch?v=4AxaKxZIO4Y&t=1719s)** also being something that we're connecting to here. And yeah, I can share things like, you know,

**[28:47](https://youtube.com/watch?v=4AxaKxZIO4Y&t=1727s)** Cube CTL access and how we do like cluster impersonation as well. But I think overall,

**[28:53](https://youtube.com/watch?v=4AxaKxZIO4Y&t=1733s)** I think that's a pretty good demo. Alan, what do you think?

**[28:57](https://youtube.com/watch?v=4AxaKxZIO4Y&t=1737s)** That was great. Question for you off the top here is, you know, you said US East, you have

**[29:04](https://youtube.com/watch?v=4AxaKxZIO4Y&t=1744s)** stuff US East, your inference cluster is in US West. What kind of latencies are you seeing through

**[29:10](https://youtube.com/watch?v=4AxaKxZIO4Y&t=1750s)** that? Anything that tail scale has helped improve on that versus go through a NAT gateway or anything

**[29:17](https://youtube.com/watch?v=4AxaKxZIO4Y&t=1757s)** along that line has been pretty good on that response. Yeah, so the way tail scale kind of does,

**[29:23](https://youtube.com/watch?v=4AxaKxZIO4Y&t=1763s)** it's like natural versatile across, I guess, regions from one client to another.

**[29:29](https://youtube.com/watch?v=4AxaKxZIO4Y&t=1769s)** You're going to see, like, near the same performance of, you know, what AWS's

**[29:35](https://youtube.com/watch?v=4AxaKxZIO4Y&t=1775s)** connectivity is to their ISPs. So I think in this case, like, I probably see like a 30 millisecond,

**[29:42](https://youtube.com/watch?v=4AxaKxZIO4Y&t=1782s)** you know, latency between the two regions. But that's, you know, mostly just, you know,

**[29:49](https://youtube.com/watch?v=4AxaKxZIO4Y&t=1789s)** that fit the, you know, overall physics of the world, we're asking you to risk that packet to

**[29:56](https://youtube.com/watch?v=4AxaKxZIO4Y&t=1796s)** the illusion. So we're going to get near, you know, ISP line rate, you know, the real bottom

**[30:03](https://youtube.com/watch?v=4AxaKxZIO4Y&t=1803s)** that gives you just an identity. So yeah. That's pretty awesome. And the, the, the recorder that

**[30:13](https://youtube.com/watch?v=4AxaKxZIO4Y&t=1813s)** you have that show the session recording, I think I mentioned this, these are stored within a

**[30:19](https://youtube.com/watch?v=4AxaKxZIO4Y&t=1819s)** user's tailnet itself. Is this on a S3 storage you have or a Kubernetes instance with a mounted

**[30:27](https://youtube.com/watch?v=4AxaKxZIO4Y&t=1827s)** volume that you have these session recording stored at? Yeah, that's a great question. You can

**[30:32](https://youtube.com/watch?v=4AxaKxZIO4Y&t=1832s)** actually store these in multiple places. In this case, I'm not storing it at all, but you could

**[30:35](https://youtube.com/watch?v=4AxaKxZIO4Y&t=1835s)** store it in a PVC as always. But another thing you can do, which we actually recently added,

**[30:40](https://youtube.com/watch?v=4AxaKxZIO4Y&t=1840s)** was the ability to attach like a service account to it, to the recorder pod. And then that will

**[30:47](https://youtube.com/watch?v=4AxaKxZIO4Y&t=1847s)** give the authentic baking into something like an AWS S3 bucket. And then you can configure the

**[30:53](https://youtube.com/watch?v=4AxaKxZIO4Y&t=1853s)** recorder to store its recordings there. And you can actually be it have like multiple recorders

**[30:58](https://youtube.com/watch?v=4AxaKxZIO4Y&t=1858s)** all over the world and kind of dumping into a centralized. That's pretty cool. Now, is your

**[31:05](https://youtube.com/watch?v=4AxaKxZIO4Y&t=1865s)** Grafana? Is that also self hosted? I didn't notice that or using Grafana cloud. Yeah, no, this is

**[31:11](https://youtube.com/watch?v=4AxaKxZIO4Y&t=1871s)** self hosted as well. It's within the cluster. I'm using CUBE Prometheus stack, which is a pretty

**[31:16](https://youtube.com/watch?v=4AxaKxZIO4Y&t=1876s)** popular way of deploying like a monitoring stack apart from like a data dog or something.

**[31:23](https://youtube.com/watch?v=4AxaKxZIO4Y&t=1883s)** So it kind of like bootstrap everything for you makes the connection between the Prometheus and

**[31:27](https://youtube.com/watch?v=4AxaKxZIO4Y&t=1887s)** Grafana. And then, you know, it kind of lets you grab like pod metrics. So as you can see, we're seeing

**[31:34](https://youtube.com/watch?v=4AxaKxZIO4Y&t=1894s)** kind of all the Kubernetes namespaces, utilization, but yeah, we are self hosting.

**[31:46](https://youtube.com/watch?v=4AxaKxZIO4Y&t=1906s)** What's really cool is we've recently launched a partnership with Grafana. They have the ability

**[31:52](https://youtube.com/watch?v=4AxaKxZIO4Y&t=1912s)** now for those in audience here that are like, oh, yeah, use Grafana is we use Grafana. You can do

**[31:58](https://youtube.com/watch?v=4AxaKxZIO4Y&t=1918s)** a PDC private data connection and add Grafana or have Grafana cloud ingest your on-prem or your

**[32:07](https://youtube.com/watch?v=4AxaKxZIO4Y&t=1927s)** tail scale related data within that. It's a really cool feature. It's an I think private preview with

**[32:14](https://youtube.com/watch?v=4AxaKxZIO4Y&t=1934s)** Grafana today, but you can reach out to your rep there. And I think we have a blog post about it

**[32:20](https://youtube.com/watch?v=4AxaKxZIO4Y&t=1940s)** from a couple weeks ago that talks about that as well. Yeah, another thing that we didn't really

**[32:25](https://youtube.com/watch?v=4AxaKxZIO4Y&t=1945s)** touch on is the operator has the ability to kind of also deploy the other deployment models that you

**[32:31](https://youtube.com/watch?v=4AxaKxZIO4Y&t=1951s)** touched on. So we can deploy subnet routers and we can deploy app connectors. So a popular use case,

**[32:37](https://youtube.com/watch?v=4AxaKxZIO4Y&t=1957s)** I've seen, you know, dropping a subnet router somewhere in your cluster and then exposing the pod

**[32:43](https://youtube.com/watch?v=4AxaKxZIO4Y&t=1963s)** and service ciders so that, you know, your developers or anyone can come in and

**[32:49](https://youtube.com/watch?v=4AxaKxZIO4Y&t=1969s)** directly reach individual pods or cluster IP services. That's pretty awesome, for sure.

**[32:57](https://youtube.com/watch?v=4AxaKxZIO4Y&t=1977s)** See a few questions coming in there on that line. And we'll get to those as well just trying to

**[33:03](https://youtube.com/watch?v=4AxaKxZIO4Y&t=1983s)** think if there's anything else that because I'm, you know, seeing this, I'm like, oh, what if I do

**[33:08](https://youtube.com/watch?v=4AxaKxZIO4Y&t=1988s)** this? Oh, yeah, I know this is, you know, heavily geared obviously today with AWS, but let's say I'm,

**[33:14](https://youtube.com/watch?v=4AxaKxZIO4Y&t=1994s)** you know, I'm a, I'm a customer, but I don't use AWS. I use another cloud provider out there.

**[33:20](https://youtube.com/watch?v=4AxaKxZIO4Y&t=2000s)** How complex would be implementing tail scale and this kind of, I say demo, but this kind of model

**[33:26](https://youtube.com/watch?v=4AxaKxZIO4Y&t=2006s)** with multiple clusters. Is that fairly easy to do? Yeah, I would say it overall is,

**[33:32](https://youtube.com/watch?v=4AxaKxZIO4Y&t=2012s)** a test girl kind of like lives in this path of like, hey, it just works, right? So you could drop the

**[33:37](https://youtube.com/watch?v=4AxaKxZIO4Y&t=2017s)** test, you could drop test girl proxies in any of your clusters and kind of have a hybrid approach.

**[33:41](https://youtube.com/watch?v=4AxaKxZIO4Y&t=2021s)** So you could drop a Kubernetes cluster in Nebius that's doing the GPU training and then another

**[33:48](https://youtube.com/watch?v=4AxaKxZIO4Y&t=2028s)** one in AWS and established connectivity. And that's like kind of a really great on path there,

**[33:53](https://youtube.com/watch?v=4AxaKxZIO4Y&t=2033s)** is that you can be really hybrid in your enclosures of which clusters you're connecting to and kind

**[34:00](https://youtube.com/watch?v=4AxaKxZIO4Y&t=2040s)** of kind of build your own like, I guess network layer or compute layer.

**[34:06](https://youtube.com/watch?v=4AxaKxZIO4Y&t=2046s)** That is cool. We definitely have a number of AI companies and customers that

**[34:11](https://youtube.com/watch?v=4AxaKxZIO4Y&t=2051s)** probably leveraging multiple clouds with, I don't know if they do with Kubernetes, maybe they are,

**[34:16](https://youtube.com/watch?v=4AxaKxZIO4Y&t=2056s)** but it is kind of just neat to see some of that architecture there.

**[34:20](https://youtube.com/watch?v=4AxaKxZIO4Y&t=2060s)** I do have a question. Someone from is asking, diving a little bit more to the Kubernetes

**[34:26](https://youtube.com/watch?v=4AxaKxZIO4Y&t=2066s)** are back that you highlighted. Is that, I don't know if you want to share a screen kind of dig into

**[34:31](https://youtube.com/watch?v=4AxaKxZIO4Y&t=2071s)** that for a little bit, if you're able to do that, Raj? Yeah, yeah, I can share a little bit.

**[34:37](https://youtube.com/watch?v=4AxaKxZIO4Y&t=2077s)** Yeah, let's do it. Okay, luckily I still have the repo. So

**[34:46](https://youtube.com/watch?v=4AxaKxZIO4Y&t=2086s)** and we did put, I did put the link to the repo in chat and looks, I can't also put in the repo

**[34:52](https://youtube.com/watch?v=4AxaKxZIO4Y&t=2092s)** to the Grafana integration as well for those that are interested. Of course.

**[35:01](https://youtube.com/watch?v=4AxaKxZIO4Y&t=2101s)** Yeah, so this is like what it would typically look like. So there's, there's two configurations you

**[35:06](https://youtube.com/watch?v=4AxaKxZIO4Y&t=2106s)** kind of make within the cluster. So the first thing you're doing is, you're kind of telling the

**[35:15](https://youtube.com/watch?v=4AxaKxZIO4Y&t=2115s)** Kubernetes operator that anytime a super user comes in, so in this case, they can never

**[35:21](https://youtube.com/watch?v=4AxaKxZIO4Y&t=2121s)** miss it. They are allowed to impersonate, we call it clusterable impersonation as a system

**[35:28](https://youtube.com/watch?v=4AxaKxZIO4Y&t=2128s)** type master. And then we're also doing things like enforcing the building.

**[35:33](https://youtube.com/watch?v=4AxaKxZIO4Y&t=2133s)** Now, if you wanted to, you know, give a certain subset of users only read only access or maybe

**[35:41](https://youtube.com/watch?v=4AxaKxZIO4Y&t=2141s)** you want to scope them down to a namespace, what you can do is kind of tell the operator to match the

**[35:48](https://youtube.com/watch?v=4AxaKxZIO4Y&t=2148s)** group, the clusterable group within your cluster. So in this case, any member who's not, I guess,

**[35:54](https://youtube.com/watch?v=4AxaKxZIO4Y&t=2154s)** in this case, a super user will now come in as a reader. So they'll only be able to read what's

**[36:01](https://youtube.com/watch?v=4AxaKxZIO4Y&t=2161s)** on the cluster and also look at it in the first place. So that's kind of what's going on there.

**[36:07](https://youtube.com/watch?v=4AxaKxZIO4Y&t=2167s)** And this is like what a role would look like. So in this case, I'm attaching the group

**[36:13](https://youtube.com/watch?v=4AxaKxZIO4Y&t=2173s)** tailnet readers, which was the same that we had in our ACL defined and saying that they have

**[36:19](https://youtube.com/watch?v=4AxaKxZIO4Y&t=2179s)** the cluster role. That's pretty cool. Go back to your JSON father on the tail scale there.

**[36:28](https://youtube.com/watch?v=4AxaKxZIO4Y&t=2188s)** So for those that were wondering about the recorder piece there, I'm going to highlight a little bit,

**[36:32](https://youtube.com/watch?v=4AxaKxZIO4Y&t=2192s)** the recorder, enforce recorder. What does that mean? The recording is something that's optional

**[36:37](https://youtube.com/watch?v=4AxaKxZIO4Y&t=2197s)** within tail scale. You're not, it doesn't come by default turned on. It is a feature that you can

**[36:43](https://youtube.com/watch?v=4AxaKxZIO4Y&t=2203s)** enable and pretty much on all the plans that we have today with tail scale. And it gives you the

**[36:48](https://youtube.com/watch?v=4AxaKxZIO4Y&t=2208s)** ability to say, Hey, anything that happens when I'm cube exacting in or doing an SSH session,

**[36:55](https://youtube.com/watch?v=4AxaKxZIO4Y&t=2215s)** here's the recorder that it's going to record that session to the enforce piece there is a really

**[37:01](https://youtube.com/watch?v=4AxaKxZIO4Y&t=2221s)** cool kind of security piece there is if that is set to true. And somehow that recorder fails.

**[37:07](https://youtube.com/watch?v=4AxaKxZIO4Y&t=2227s)** And it went offline and then Raj tries to SSH or cube exact in. It's actually going to prevent him

**[37:13](https://youtube.com/watch?v=4AxaKxZIO4Y&t=2233s)** from doing that because we have an enforcement feature that say, you know what, we're only going to allow

**[37:19](https://youtube.com/watch?v=4AxaKxZIO4Y&t=2239s)** connectivity as long as the recorder is up and running. So as you're playing or experimenting,

**[37:23](https://youtube.com/watch?v=4AxaKxZIO4Y&t=2243s)** saying, Hey, I like this recording piece here. I want to have better audit capabilities. Those are

**[37:29](https://youtube.com/watch?v=4AxaKxZIO4Y&t=2249s)** two little features there that can be really helpful for you. Yeah, absolutely.

**[37:36](https://youtube.com/watch?v=4AxaKxZIO4Y&t=2256s)** Let me see here. We've got a few other come other questions here. What level subscription do you

**[37:41](https://youtube.com/watch?v=4AxaKxZIO4Y&t=2261s)** need to get all the functionality you demoed? You say, we hear, do you have custom groups in this one?

**[37:51](https://youtube.com/watch?v=4AxaKxZIO4Y&t=2271s)** Custom groups like like like a skin groups now. Yeah, or you do have a custom name group,

**[37:58](https://youtube.com/watch?v=4AxaKxZIO4Y&t=2278s)** like a named group group, super user group. Okay. So yeah, that question from Pat asked

**[38:03](https://youtube.com/watch?v=4AxaKxZIO4Y&t=2283s)** is I, Hey, what kind of plan? This probably you can probably get this because the operator is not

**[38:08](https://youtube.com/watch?v=4AxaKxZIO4Y&t=2288s)** segmented to any specific tail scale plan. So you can run that. There are some features here like

**[38:15](https://youtube.com/watch?v=4AxaKxZIO4Y&t=2295s)** Raj is using group, super user group, whatever. And that is, I believe, on our premium plan,

**[38:21](https://youtube.com/watch?v=4AxaKxZIO4Y&t=2301s)** because the starter skew, the starter plan has what we call auto groups, which are like auto group

**[38:27](https://youtube.com/watch?v=4AxaKxZIO4Y&t=2307s)** member auto group admin. So if you're comfortable with just a couple of the auto groups, you can just

**[38:32](https://youtube.com/watch?v=4AxaKxZIO4Y&t=2312s)** leverage that. But if you are engineering centric or you want more of those custom groups,

**[38:37](https://youtube.com/watch?v=4AxaKxZIO4Y&t=2317s)** that would be the premium plan. Now personal plans, if you're like a free user or on that line,

**[38:43](https://youtube.com/watch?v=4AxaKxZIO4Y&t=2323s)** I think you have access to all these and can easily leverage them for sure.

**[38:48](https://youtube.com/watch?v=4AxaKxZIO4Y&t=2328s)** Yeah, groups, I believe by default are on the starter plan. But the real difference is if you want to

**[38:56](https://youtube.com/watch?v=4AxaKxZIO4Y&t=2336s)** bring in things like your group sync from a skin provider like like a, I don't know, on trial

**[39:02](https://youtube.com/watch?v=4AxaKxZIO4Y&t=2342s)** or Octa or something like that. So as far as like the only thing that you wouldn't be able to do,

**[39:10](https://youtube.com/watch?v=4AxaKxZIO4Y&t=2350s)** I guess, on the starter plan from a Kubernetes perspective is the reporting aspect. Everything else

**[39:14](https://youtube.com/watch?v=4AxaKxZIO4Y&t=2354s)** can be done by you, obviously, between those three users limit and then the 100 machine count.

**[39:21](https://youtube.com/watch?v=4AxaKxZIO4Y&t=2361s)** Another question, do you have any issues using EKS? If someone's using EKS and EKS is the nice thing

**[39:30](https://youtube.com/watch?v=4AxaKxZIO4Y&t=2370s)** about it, it provides you some quick ability to spin up an AWS cluster scale and do all kinds of

**[39:37](https://youtube.com/watch?v=4AxaKxZIO4Y&t=2377s)** cool stuff with it. By leveraging tail scale from the connectivity glue than that networking layer,

**[39:44](https://youtube.com/watch?v=4AxaKxZIO4Y&t=2384s)** does it help eliminate some manual AWS configuration or EKS configurations that you might have

**[39:53](https://youtube.com/watch?v=4AxaKxZIO4Y&t=2393s)** had to do previously? Or does it kind of help simplify some of that?

**[40:00](https://youtube.com/watch?v=4AxaKxZIO4Y&t=2400s)** I think, I think possibly, it's really dependent on what you're trying to accomplish.

**[40:07](https://youtube.com/watch?v=4AxaKxZIO4Y&t=2407s)** So obviously, establishing connectivity between clusters, traditionally, the way to do that

**[40:17](https://youtube.com/watch?v=4AxaKxZIO4Y&t=2417s)** would be establishing VPC, VPC connectivity and defining things maybe via Terraform and how you

**[40:25](https://youtube.com/watch?v=4AxaKxZIO4Y&t=2425s)** would actually establish that connectivity. So I guess in that aspect, it wouldn't make it much

**[40:30](https://youtube.com/watch?v=4AxaKxZIO4Y&t=2430s)** simpler because essentially what you're doing is just giving authentication to one cluster to your

**[40:35](https://youtube.com/watch?v=4AxaKxZIO4Y&t=2435s)** talent and then giving authentication to another cluster and your talent and then the connectivity

**[40:40](https://youtube.com/watch?v=4AxaKxZIO4Y&t=2440s)** kind of just gets established magically like that. So hoping that answers your question,

**[40:47](https://youtube.com/watch?v=4AxaKxZIO4Y&t=2447s)** but it's really dependent. Awesome. I do see another question that didn't come in,

**[40:52](https://youtube.com/watch?v=4AxaKxZIO4Y&t=2452s)** came through our chat. Does tail scale work well with key cloak? So I know we didn't really touch

**[40:59](https://youtube.com/watch?v=4AxaKxZIO4Y&t=2459s)** on the identity provider side here, but tail scale, you know, kind of rewinding a little bit.

**[41:05](https://youtube.com/watch?v=4AxaKxZIO4Y&t=2465s)** We support a number of anything that's OIDC compliant kind of out of the box. Microsoft,

**[41:11](https://youtube.com/watch?v=4AxaKxZIO4Y&t=2471s)** Google, Workspace, Octa, Office 365, tools I jump cloud, off the zero, et cetera.

**[41:19](https://youtube.com/watch?v=4AxaKxZIO4Y&t=2479s)** Key cloak does work. If we have customers that are using it today, we don't have a specific guide

**[41:25](https://youtube.com/watch?v=4AxaKxZIO4Y&t=2485s)** on our side around key cloak. But if you do have a key cloak instance configured and set up,

**[41:30](https://youtube.com/watch?v=4AxaKxZIO4Y&t=2490s)** it should you look at our documentation under custom OIDC providers and follow the instructions

**[41:37](https://youtube.com/watch?v=4AxaKxZIO4Y&t=2497s)** there and that should enable you to get key cloak working well. The only thing tail scale does

**[41:43](https://youtube.com/watch?v=4AxaKxZIO4Y&t=2503s)** not work for those are like, oh, I've got a on-prem active directory here. It's not going to work with

**[41:49](https://youtube.com/watch?v=4AxaKxZIO4Y&t=2509s)** that because OIDC requires a web end point, secure web end point, typically on-prem, OIDC,

**[41:58](https://youtube.com/watch?v=4AxaKxZIO4Y&t=2518s)** on-prem active directly does not, but a lot of times our customers that are running those might

**[42:03](https://youtube.com/watch?v=4AxaKxZIO4Y&t=2523s)** have a federation with Entra or something to that effect and they can leverage that identity

**[42:08](https://youtube.com/watch?v=4AxaKxZIO4Y&t=2528s)** along the line. No, these are great questions along the line. No, that was an awesome kind of demo

**[42:15](https://youtube.com/watch?v=4AxaKxZIO4Y&t=2535s)** showcasing how you can leverage the operator in EKS, cross-class US East, US West, and just pulling

**[42:25](https://youtube.com/watch?v=4AxaKxZIO4Y&t=2545s)** that data across. Thank you for that. Looking at some of the questions, another one here from Charm.

**[42:31](https://youtube.com/watch?v=4AxaKxZIO4Y&t=2551s)** There is a computer count mentioned. Is this count per subscription level? So every tail scale

**[42:38](https://youtube.com/watch?v=4AxaKxZIO4Y&t=2558s)** account, if you create a free one right now after here, you're like, sweet, let me just sign

**[42:42](https://youtube.com/watch?v=4AxaKxZIO4Y&t=2562s)** it with my Gmail and go, you'll have 100 devices. So every tail scale, every tail net gets a baseline

**[42:49](https://youtube.com/watch?v=4AxaKxZIO4Y&t=2569s)** of 100 devices, but let's say you have 10 employees in your company and you're on one of our starter

**[42:54](https://youtube.com/watch?v=4AxaKxZIO4Y&t=2574s)** plans or something like that. You now have 100 devices plus 10 per user, so you would have a total

**[43:01](https://youtube.com/watch?v=4AxaKxZIO4Y&t=2581s)** of 200 devices, and then it goes up their premiums, 20, et cetera, et cetera. Now, if you are saying,

**[43:08](https://youtube.com/watch?v=4AxaKxZIO4Y&t=2588s)** well, there's only 10 of us, but we've got 7,000 IoT devices because we're big in that word,

**[43:14](https://youtube.com/watch?v=4AxaKxZIO4Y&t=2594s)** and we have customers that do that. Reach out to someone on our account team, our sales team,

**[43:21](https://youtube.com/watch?v=4AxaKxZIO4Y&t=2601s)** here at tail scale. They can work with you with a custom device pricing model. We do have customers

**[43:28](https://youtube.com/watch?v=4AxaKxZIO4Y&t=2608s)** that have tens of thousands of devices running on tail scale today, and not as many employees,

**[43:34](https://youtube.com/watch?v=4AxaKxZIO4Y&t=2614s)** so it does scale very well on that line. So hopefully that was an answer to that question there.

**[43:40](https://youtube.com/watch?v=4AxaKxZIO4Y&t=2620s)** No great questions. You can see what else we got here. Anything else you guys like to see?

**[43:50](https://youtube.com/watch?v=4AxaKxZIO4Y&t=2630s)** We do have a little bit of time left, so take this time for if you've got something that,

**[43:56](https://youtube.com/watch?v=4AxaKxZIO4Y&t=2636s)** hey, I want to see this in action or why not? Let me know. Let me get back to my slideshow here,

**[44:07](https://youtube.com/watch?v=4AxaKxZIO4Y&t=2647s)** and I'll just get this screen shared, and then, oh, QA, there we go. We'll go to the QA piece here.

**[44:18](https://youtube.com/watch?v=4AxaKxZIO4Y&t=2658s)** Do you have any other questions? We'll go. Any other, go ahead.

**[44:30](https://youtube.com/watch?v=4AxaKxZIO4Y&t=2670s)** No, one last thing I just thought of, sorry Kate, Raj, any kind of gotchas to be on the look out for

**[44:37](https://youtube.com/watch?v=4AxaKxZIO4Y&t=2677s)** if I am, you know, I look at this today, and I'm like, oh, this is awesome. I want to set up my own,

**[44:43](https://youtube.com/watch?v=4AxaKxZIO4Y&t=2683s)** you know, LM cluster and do some testing. Are there any kind of security gotchas or things that

**[44:49](https://youtube.com/watch?v=4AxaKxZIO4Y&t=2689s)** I need to be aware of before I download your repo and start poking around and rolling it out on

**[44:55](https://youtube.com/watch?v=4AxaKxZIO4Y&t=2695s)** AWS with tail scale? Yeah, yeah, absolutely. So I'm using Flux CD, which is kind of like

**[45:03](https://youtube.com/watch?v=4AxaKxZIO4Y&t=2703s)** this open source, get apps to them. So I probably would recommend you kind of just, you know,

**[45:10](https://youtube.com/watch?v=4AxaKxZIO4Y&t=2710s)** I would use it as a reference point, but you know, things like there that are in there are like

**[45:15](https://youtube.com/watch?v=4AxaKxZIO4Y&t=2715s)** minecrafted sops, you know, passwords to kind of, you know, download models from Pugging Face,

**[45:23](https://youtube.com/watch?v=4AxaKxZIO4Y&t=2723s)** provide a tail scale, OAuth key to actually authenticate my cluster into our tailnet.

**[45:31](https://youtube.com/watch?v=4AxaKxZIO4Y&t=2731s)** But then everything else is in there. So it's a great reference point for, you know,

**[45:37](https://youtube.com/watch?v=4AxaKxZIO4Y&t=2737s)** running all of our different kinds of deployment strategies. So whether that be app connectors,

**[45:42](https://youtube.com/watch?v=4AxaKxZIO4Y&t=2742s)** submit routes, recorders, there's also, you know, bonuses in there, like tail scale side cars,

**[45:48](https://youtube.com/watch?v=4AxaKxZIO4Y&t=2748s)** which is another thing that some of our customers utilize. Yeah, so a great reference point,

**[45:56](https://youtube.com/watch?v=4AxaKxZIO4Y&t=2756s)** probably not one that you just, you know, kind of just fork and then try to replicate.

**[46:01](https://youtube.com/watch?v=4AxaKxZIO4Y&t=2761s)** Yeah, you really understand how Flux works in general.

**[46:05](https://youtube.com/watch?v=4AxaKxZIO4Y&t=2765s)** Cool, awesome. Let me see here. We got another question.

**[46:11](https://youtube.com/watch?v=4AxaKxZIO4Y&t=2771s)** Kartik has been a huge on answering those on chat. So thank you for doing that. And I think we're

**[46:18](https://youtube.com/watch?v=4AxaKxZIO4Y&t=2778s)** good unless anyone else has any other questions. I'll turn it back over to you, Kate, on your

**[46:25](https://youtube.com/watch?v=4AxaKxZIO4Y&t=2785s)** side of the fence. Yeah, sounds good. Thank you guys so much. Shout out to Alan and Raj for

**[46:32](https://youtube.com/watch?v=4AxaKxZIO4Y&t=2792s)** hosting an incredible session today. Thank you to Kartik for absolutely crushing the Q&A in the

**[46:37](https://youtube.com/watch?v=4AxaKxZIO4Y&t=2797s)** comments. Kartik, you are amazing. Thank you, thank you, thank you. And of course, thank you to all

**[46:42](https://youtube.com/watch?v=4AxaKxZIO4Y&t=2802s)** of you for hanging out with us this afternoon or evening or early morning, depending on where you are

**[46:47](https://youtube.com/watch?v=4AxaKxZIO4Y&t=2807s)** in the world. As a reminder, today's session has been recorded. So I will work on getting that

**[46:52](https://youtube.com/watch?v=4AxaKxZIO4Y&t=2812s)** recording out to all of you and any related resources as well. It will take me a couple days to get

**[46:57](https://youtube.com/watch?v=4AxaKxZIO4Y&t=2817s)** all of that together, but look for that early next week. On behalf of the entire tail scale team,

**[47:03](https://youtube.com/watch?v=4AxaKxZIO4Y&t=2823s)** thanks again for joining us today. We hope you found it valuable and we look forward to seeing

**[47:06](https://youtube.com/watch?v=4AxaKxZIO4Y&t=2826s)** you again at a future webinar. Have a great day, everyone. Thank you so much. Thank you all.

**[47:11](https://youtube.com/watch?v=4AxaKxZIO4Y&t=2831s)** Bye, you guys. Have a good day.

---

*Automatically generated transcript. May contain errors.*
