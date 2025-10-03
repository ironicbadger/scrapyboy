---
video_id: "k3NqliNGo6s"
title: "7 Essential Tailscale CLI Commands Every Admin Should Know"
description: "The Tailscale command line is a powerful way to manage your secure network and interact with devices across your tailnet. Join Alex as he walks through 7 essential Tailscale CLI commands that every us..."
channel_name: "Tailscale"
channel_id: "UCcdv38QxPjSMqbt5ffLhJLA"
published_at: "2025-09-05"
duration_seconds: 1636
youtube_url: "https://www.youtube.com/watch?v=k3NqliNGo6s"
thumbnail_url: "https://i.ytimg.com/vi/k3NqliNGo6s/maxresdefault.jpg"

# Transcription metadata
transcribed_at: "2025-10-03T18:24:18.455541"
transcription_method: "cpu"
model_used: "base"
language: "en"
word_count: 5237
transcription_time_seconds: 44.2
---

# 7 Essential Tailscale CLI Commands Every Admin Should Know

**[00:00](https://youtube.com/watch?v=k3NqliNGo6s&t=0s)** Hi, I'm Alex from Tailscale, and in today's video, we're going to dive into the Tailscale

**[00:04](https://youtube.com/watch?v=k3NqliNGo6s&t=4s)** Command Line Interface, or CLI for short. Absolutely thrilling stuff. I know a video about

**[00:10](https://youtube.com/watch?v=k3NqliNGo6s&t=10s)** the command line, but I promise you, it actually gets interesting later on. Now, before we

**[00:14](https://youtube.com/watch?v=k3NqliNGo6s&t=14s)** get there, I do want to make sure that you know about our brand new Discord server over

**[00:19](https://youtube.com/watch?v=k3NqliNGo6s&t=19s)** at discord.gg slash Tailscale. It only launched a couple of weeks ago. And over there,

**[00:24](https://youtube.com/watch?v=k3NqliNGo6s&t=24s)** you can find our excellent community to ask questions and collaborate and learn more

**[00:29](https://youtube.com/watch?v=k3NqliNGo6s&t=29s)** about Tailscale. Now, those of you who are cis admins or DevOps professionals by trade

**[00:35](https://youtube.com/watch?v=k3NqliNGo6s&t=35s)** have almost certainly dropped to the command line at some point. I'll probably extend

**[00:39](https://youtube.com/watch?v=k3NqliNGo6s&t=39s)** that to our more nerdy home lab users as well. Many of you are probably familiar with

**[00:44](https://youtube.com/watch?v=k3NqliNGo6s&t=44s)** the basics like Tailscale up and serve, and maybe even status to check on what's going

**[00:50](https://youtube.com/watch?v=k3NqliNGo6s&t=50s)** on with your tailnet behind the scenes, but there is a whole world beyond those basic commands

**[00:56](https://youtube.com/watch?v=k3NqliNGo6s&t=56s)** in the Tailscale command line interface as well. And that's exactly what we're going to

**[01:00](https://youtube.com/watch?v=k3NqliNGo6s&t=60s)** be digging into today. Now, let's start with the most basic invocation of how we bring

**[01:07](https://youtube.com/watch?v=k3NqliNGo6s&t=67s)** up the Tailscale command line interface. On a Mac at least, or indeed any other client

**[01:11](https://youtube.com/watch?v=k3NqliNGo6s&t=71s)** where you have Tailscale installed that has a command line, you can just type the word

**[01:15](https://youtube.com/watch?v=k3NqliNGo6s&t=75s)** Tailscale, and it will print out all of the options that you have available. On a Mac,

**[01:20](https://youtube.com/watch?v=k3NqliNGo6s&t=80s)** you will need to go to the client and click on Settings, you will need to go to CLI integration

**[01:25](https://youtube.com/watch?v=k3NqliNGo6s&t=85s)** and show me how. You'll need to make sure that Tailscale is installed. I've got some

**[01:30](https://youtube.com/watch?v=k3NqliNGo6s&t=90s)** fanciness with Nick's under the hood as to why mine is actually working. And then just

**[01:34](https://youtube.com/watch?v=k3NqliNGo6s&t=94s)** click the install button. It'll ask you for your password, and then it will install

**[01:38](https://youtube.com/watch?v=k3NqliNGo6s&t=98s)** Tailscale into your path, and you should be able to type Tailscale and off you go.

**[01:43](https://youtube.com/watch?v=k3NqliNGo6s&t=103s)** The first command we're going to look at today is Tailscale up. This is a very simple

**[01:47](https://youtube.com/watch?v=k3NqliNGo6s&t=107s)** command in essence. It connects your device to a Tailscale network and authenticates

**[01:52](https://youtube.com/watch?v=k3NqliNGo6s&t=112s)** you if needed. But you probably shouldn't use it for anything more than that. Pretty much

**[01:58](https://youtube.com/watch?v=k3NqliNGo6s&t=118s)** every single option that Tailscale has is exposed via the up command. Indeed, if I do a

**[02:03](https://youtube.com/watch?v=k3NqliNGo6s&t=123s)** Tailscale up dash dash help, you ready? Yes, there's an awful lot of stuff here, which you

**[02:08](https://youtube.com/watch?v=k3NqliNGo6s&t=128s)** can see that I have to make the text smaller for it to all fit on the screen. Now there

**[02:13](https://youtube.com/watch?v=k3NqliNGo6s&t=133s)** are some situations where using arguments with Tailscale up is completely valid, things

**[02:18](https://youtube.com/watch?v=k3NqliNGo6s&t=138s)** like login server. For example, this is where you would specify a specific head scale

**[02:22](https://youtube.com/watch?v=k3NqliNGo6s&t=142s)** instance. If you needed to do something and override the default control plane URL for

**[02:28](https://youtube.com/watch?v=k3NqliNGo6s&t=148s)** Tailscale, most people never will. But if you do, that's how you do it. Other stuff like

**[02:32](https://youtube.com/watch?v=k3NqliNGo6s&t=152s)** a dash dash QR. So for example, I can do Tailscale up dash dash QR. This is going to allow me

**[02:38](https://youtube.com/watch?v=k3NqliNGo6s&t=158s)** to authenticate just by using the QR code on the screen. So I can now tap the or scan

**[02:44](https://youtube.com/watch?v=k3NqliNGo6s&t=164s)** the QR code. And I can just follow the authentication flow on my phone with no typing required. And

**[02:49](https://youtube.com/watch?v=k3NqliNGo6s&t=169s)** as you can see, I can then just authenticate on my phone. I happen to have not signed into

**[02:54](https://youtube.com/watch?v=k3NqliNGo6s&t=174s)** this one all summer because it's been the summer break. And now hopefully I can just connect

**[03:00](https://youtube.com/watch?v=k3NqliNGo6s&t=180s)** this device to my tailnet that way using a QR code. You can also through Tailscale up.

**[03:07](https://youtube.com/watch?v=k3NqliNGo6s&t=187s)** You can also pass in an auth key. So for example, if I do up dash dash auth key, I would

**[03:13](https://youtube.com/watch?v=k3NqliNGo6s&t=193s)** then pass in the string of an auth key generated from my Tailscale admin console. So for example,

**[03:19](https://youtube.com/watch?v=k3NqliNGo6s&t=199s)** I would go to settings, keys, and then generate an auth key here. And then I'd pass that in.

**[03:25](https://youtube.com/watch?v=k3NqliNGo6s&t=205s)** I know I've already authenticated. So it's probably going to shout at me. But I could

**[03:29](https://youtube.com/watch?v=k3NqliNGo6s&t=209s)** do that this way and sign into my tailnet programmatically. So if you're using this as part

**[03:34](https://youtube.com/watch?v=k3NqliNGo6s&t=214s)** of a CIC, the environment, for example, this can be very useful. If you pass this into

**[03:40](https://youtube.com/watch?v=k3NqliNGo6s&t=220s)** the repository secrets or something like that on GitHub, I think it's what they call it.

**[03:44](https://youtube.com/watch?v=k3NqliNGo6s&t=224s)** Now you can see that I've already authenticated to a tailnet. So it's not actually going to do

**[03:47](https://youtube.com/watch?v=k3NqliNGo6s&t=227s)** anything. There are some other things that are exposed through Tailscale up as well, for example.

**[03:52](https://youtube.com/watch?v=k3NqliNGo6s&t=232s)** So we've got things like dash dash ssh. And this is one for me that I actually find

**[03:56](https://youtube.com/watch?v=k3NqliNGo6s&t=236s)** incredibly useful on a brand new server. If all I do is Tailscale up dash dash ssh,

**[04:03](https://youtube.com/watch?v=k3NqliNGo6s&t=243s)** I then no longer need to worry about installing ssh keys into that remote node. So for example,

**[04:08](https://youtube.com/watch?v=k3NqliNGo6s&t=248s)** I can now do ssh root at CLI demo. And I don't even need to worry about installing ssh keys

**[04:15](https://youtube.com/watch?v=k3NqliNGo6s&t=255s)** into that remote server. So the problem with Tailscale up from a configuration perspective really

**[04:21](https://youtube.com/watch?v=k3NqliNGo6s&t=261s)** comes when we do something like this. If I do dash dash advertise exit node, which would allow me

**[04:26](https://youtube.com/watch?v=k3NqliNGo6s&t=266s)** to use this CLI demo virtual machine as an exit node on the tailnet, you can see that it's going

**[04:32](https://youtube.com/watch?v=k3NqliNGo6s&t=272s)** to complain that I haven't included all of the flags that I passed last time. In this case,

**[04:37](https://youtube.com/watch?v=k3NqliNGo6s&t=277s)** only ssh, but you can imagine if there's a bunch of tags and a bunch of routes and a bunch of

**[04:42](https://youtube.com/watch?v=k3NqliNGo6s&t=282s)** exit node stuff configured, having to remember each of those things to be configured every single time

**[04:48](https://youtube.com/watch?v=k3NqliNGo6s&t=288s)** can get a little bit unwieldy, which is why we recommend that people use the Tailscale set command

**[04:53](https://youtube.com/watch?v=k3NqliNGo6s&t=293s)** instead. So for example, I would do tailscale set dash dash advertise exit node. And you'll see,

**[05:00](https://youtube.com/watch?v=k3NqliNGo6s&t=300s)** there's no complaint at all. I don't have to remember that I did the ssh flag last time.

**[05:05](https://youtube.com/watch?v=k3NqliNGo6s&t=305s)** Now you can use tailscale up to unset parameters to should you wish to so I can do advertise exit node

**[05:12](https://youtube.com/watch?v=k3NqliNGo6s&t=312s)** equals false, but then I do also need to pass the dash dash ssh flag in order for the command to be

**[05:17](https://youtube.com/watch?v=k3NqliNGo6s&t=317s)** executed successfully. So you can kind of see why we don't really push people down the tailscale

**[05:22](https://youtube.com/watch?v=k3NqliNGo6s&t=322s)** up command. We really want you to be using tailscale set, which is going to be my next command.

**[05:28](https://youtube.com/watch?v=k3NqliNGo6s&t=328s)** As we discuss the moment to go, tailscale set doesn't require the complete set of desired settings

**[05:34](https://youtube.com/watch?v=k3NqliNGo6s&t=334s)** on each invocation. Many of the same flags are supported. As you can see here, if we do a dash

**[05:39](https://youtube.com/watch?v=k3NqliNGo6s&t=339s)** dash help, there's an awful long list of things here which are supported. And we have a full list

**[05:45](https://youtube.com/watch?v=k3NqliNGo6s&t=345s)** on the documentation, of course, but we want to encourage users to use tailscale set over other

**[05:50](https://youtube.com/watch?v=k3NqliNGo6s&t=350s)** commands as it will eventually be used by a declarative configuration model. In fact, I'm going to

**[05:55](https://youtube.com/watch?v=k3NqliNGo6s&t=355s)** put a link to this GitHub issue. You can see on the screen right here in the description down below,

**[05:59](https://youtube.com/watch?v=k3NqliNGo6s&t=359s)** if you'd like to follow that progress through the open source development model that tailscale

**[06:03](https://youtube.com/watch?v=k3NqliNGo6s&t=363s)** follows. Now, some of the things you might find useful, for example, in tailscale set, you know,

**[06:09](https://youtube.com/watch?v=k3NqliNGo6s&t=369s)** we can set things like ssh. We can look at things like tailscale auto update. So let me do tailscale

**[06:14](https://youtube.com/watch?v=k3NqliNGo6s&t=374s)** set dash dash auto update. This will keep the tailscale client up to date very useful on remote

**[06:20](https://youtube.com/watch?v=k3NqliNGo6s&t=380s)** systems. Now another thing you might want to do is set the host name of this box. For example,

**[06:24](https://youtube.com/watch?v=k3NqliNGo6s&t=384s)** if I want to do dash dash host name, I can now call this Bob. And in my tailnet, for example,

**[06:31](https://youtube.com/watch?v=k3NqliNGo6s&t=391s)** let me go and look at the admin console. You can see that that's now actually renamed itself

**[06:35](https://youtube.com/watch?v=k3NqliNGo6s&t=395s)** to Bob. That could be a really handy one. If you need to ever rename a node on the command line,

**[06:40](https://youtube.com/watch?v=k3NqliNGo6s&t=400s)** I'm going to go back to the original tailscale host name of CLI demo, just to keep things simple.

**[06:47](https://youtube.com/watch?v=k3NqliNGo6s&t=407s)** Now another thing that we can do is the dash dash web client. And you'll see that this is now running

**[06:51](https://youtube.com/watch?v=k3NqliNGo6s&t=411s)** on the tailscale IP on port 52 52. So if we go to my web browser and type that in, you can see I now

**[06:58](https://youtube.com/watch?v=k3NqliNGo6s&t=418s)** get a nice little web overview of exactly what the client is doing on that node in a browser.

**[07:05](https://youtube.com/watch?v=k3NqliNGo6s&t=425s)** You can see the tailscale SSH server is running, for example. And we can learn more about that by

**[07:10](https://youtube.com/watch?v=k3NqliNGo6s&t=430s)** clicking here. There's a bunch of other stuff too. So for example, let's just click that button that

**[07:15](https://youtube.com/watch?v=k3NqliNGo6s&t=435s)** says, sign in to confirm my identity. We're not diving too deep into the web UI in this video,

**[07:20](https://youtube.com/watch?v=k3NqliNGo6s&t=440s)** but you know, just for the sake of it, we can actually turn tailscale SSH on and off

**[07:26](https://youtube.com/watch?v=k3NqliNGo6s&t=446s)** from the web client. Now you can see we've lost our SSH connection because I did that.

**[07:30](https://youtube.com/watch?v=k3NqliNGo6s&t=450s)** So let me turn that back on and then come back over here and you can see I've got SSH access again.

**[07:35](https://youtube.com/watch?v=k3NqliNGo6s&t=455s)** But just that proves to you, I suppose, just how instant when tailscale

**[07:39](https://youtube.com/watch?v=k3NqliNGo6s&t=459s)** initiates things in the policy. Just how instant things happen. In fact, let me show that again.

**[07:44](https://youtube.com/watch?v=k3NqliNGo6s&t=464s)** Let me do ping.google.com and move the window so you can see what's going on.

**[07:52](https://youtube.com/watch?v=k3NqliNGo6s&t=472s)** And if I check that box again, boom, split second. I love that when that happens.

**[07:57](https://youtube.com/watch?v=k3NqliNGo6s&t=477s)** You can see that the SSH connection is immediately terminated just through the web UI.

**[08:03](https://youtube.com/watch?v=k3NqliNGo6s&t=483s)** So that's a really cool thing. I don't think many of our users know that the web UI even exists.

**[08:08](https://youtube.com/watch?v=k3NqliNGo6s&t=488s)** So if that's you, welcome to the web UI club. The subnet router stuff is there too. So if you want

**[08:14](https://youtube.com/watch?v=k3NqliNGo6s&t=494s)** to advertise, if you want to turn it into a subnet router, so you can access non-tailscale devices,

**[08:19](https://youtube.com/watch?v=k3NqliNGo6s&t=499s)** that's in the web UI too. And again, this isn't really a deep dive on the web UI,

**[08:23](https://youtube.com/watch?v=k3NqliNGo6s&t=503s)** although it's kind of turning into one. And then there's a bunch of other information about this

**[08:27](https://youtube.com/watch?v=k3NqliNGo6s&t=507s)** node and what it looks like on your tailnet on this details page too. Now, is there anything else

**[08:34](https://youtube.com/watch?v=k3NqliNGo6s&t=514s)** in the tailscale set thing that we want to look at today? I don't know. But if you want to find out

**[08:38](https://youtube.com/watch?v=k3NqliNGo6s&t=518s)** more, you can always do dash dash help. And that will print out all of the options and all of the flags

**[08:44](https://youtube.com/watch?v=k3NqliNGo6s&t=524s)** you can set using a specific command or things you can set using set. So as you can see,

**[08:51](https://youtube.com/watch?v=k3NqliNGo6s&t=531s)** tailscale set actually exposes a great number of different configuration flags. Some of these

**[08:57](https://youtube.com/watch?v=k3NqliNGo6s&t=537s)** are definitely for the more advanced among you, things like accepting DNS to be true or false,

**[09:02](https://youtube.com/watch?v=k3NqliNGo6s&t=542s)** for example. If you need that, you know you need that probably. Things like app connectors,

**[09:08](https://youtube.com/watch?v=k3NqliNGo6s&t=548s)** exit nodes and routes and that kind of thing, it's all there. So yeah, go take a look at tailscale set.

**[09:14](https://youtube.com/watch?v=k3NqliNGo6s&t=554s)** And like I say, if you want to use tailscale up, by all means, go ahead and do that, but just be

**[09:19](https://youtube.com/watch?v=k3NqliNGo6s&t=559s)** under the full knowledge that over time we will be moving towards funneling users, no pun intended,

**[09:28](https://youtube.com/watch?v=k3NqliNGo6s&t=568s)** funneling users towards tailscale set away from tailscale up for all, but that's sort of basic

**[09:34](https://youtube.com/watch?v=k3NqliNGo6s&t=574s)** initial login flow. So we're going to move into another tailscale CLI subcommand now called

**[09:39](https://youtube.com/watch?v=k3NqliNGo6s&t=579s)** tailscale switch. This is a very straightforward one. This lets me switch tail nets. So I can do

**[09:45](https://youtube.com/watch?v=k3NqliNGo6s&t=585s)** switch dash dash list. And this will show me all of the different tail nets assigned into

**[09:50](https://youtube.com/watch?v=k3NqliNGo6s&t=590s)** this specific laptop, this specific client. So for example, right now, I'm signed in as a tailing

**[09:55](https://youtube.com/watch?v=k3NqliNGo6s&t=595s)** scales with gmail.com. I always am for these videos. But if I do tailscale switch and then do help,

**[10:02](https://youtube.com/watch?v=k3NqliNGo6s&t=602s)** you can see that the option available to me is list. But if I want to actually just switch tail

**[10:06](https://youtube.com/watch?v=k3NqliNGo6s&t=606s)** nets, all I need to do is supply a specific account ID. So in this case, Alex KTZ at gmail.com

**[10:13](https://youtube.com/watch?v=k3NqliNGo6s&t=613s)** is 30A1. So I would do tailscale switch, 30A1, and then from the command line, I can switch between

**[10:20](https://youtube.com/watch?v=k3NqliNGo6s&t=620s)** my different tailscale accounts. Now if, for example, I haven't logged into that account all summer

**[10:26](https://youtube.com/watch?v=k3NqliNGo6s&t=626s)** because I haven't really done anything on this laptop for a month because I've been out, you know,

**[10:31](https://youtube.com/watch?v=k3NqliNGo6s&t=631s)** at the beach and stuff, it will go through the authentication flow for me and ask me to log in

**[10:36](https://youtube.com/watch?v=k3NqliNGo6s&t=636s)** to my tail net. Now I'm in the wrong Chrome session for the Alex KTZ account. But that's not

**[10:40](https://youtube.com/watch?v=k3NqliNGo6s&t=640s)** important here right now. I don't actually want it to use that account moving forward. I just wanted

**[10:44](https://youtube.com/watch?v=k3NqliNGo6s&t=644s)** to show you. So let's do cce7 to switch back to my main tail and scales account. And we have

**[10:51](https://youtube.com/watch?v=k3NqliNGo6s&t=651s)** success. So you can see on the command line, this is how you do it on Linux too. Works on macOS

**[10:57](https://youtube.com/watch?v=k3NqliNGo6s&t=657s)** as well, obviously, because that's what we're using right here. But that's how you'd switch between

**[11:01](https://youtube.com/watch?v=k3NqliNGo6s&t=661s)** multiple accounts using the tailscale CLI tooling. Now, how do we know what the view of the world that

**[11:07](https://youtube.com/watch?v=k3NqliNGo6s&t=667s)** our tailscale client has is? Well, we use tailscale status, of course. And we can do tailscale status

**[11:13](https://youtube.com/watch?v=k3NqliNGo6s&t=673s)** dash dash help to get a full list of all the different options that this specific command supports.

**[11:19](https://youtube.com/watch?v=k3NqliNGo6s&t=679s)** So tailscale status in and of itself, very simply just prints the view of the world that this client

**[11:26](https://youtube.com/watch?v=k3NqliNGo6s&t=686s)** has of my tail net. Now this is really useful when you're debugging things. So if you're trying to

**[11:31](https://youtube.com/watch?v=k3NqliNGo6s&t=691s)** figure out, if you're writing a grant or a policy rule with an ACL or something, and you're trying

**[11:36](https://youtube.com/watch?v=k3NqliNGo6s&t=696s)** to figure out why or what nodes can this node see? I've just created this rule that prevents

**[11:42](https://youtube.com/watch?v=k3NqliNGo6s&t=702s)** this tag from seeing that groups, that user groups worth of devices. If I do a tailscale status

**[11:49](https://youtube.com/watch?v=k3NqliNGo6s&t=709s)** and that other node doesn't show up, I know that my rule is either doing what I want or not, for example.

**[11:55](https://youtube.com/watch?v=k3NqliNGo6s&t=715s)** So that's where tailscale status is really useful. But what I bet you didn't know is that tailscale

**[12:01](https://youtube.com/watch?v=k3NqliNGo6s&t=721s)** status has a web server built in. So if I do dash dash web and then dash dash browser,

**[12:08](https://youtube.com/watch?v=k3NqliNGo6s&t=728s)** what's what happens? So you're now going to open a web browser and showing all of the devices

**[12:12](https://youtube.com/watch?v=k3NqliNGo6s&t=732s)** in my tail net in a very pretty little web page. How about that? Including things like the

**[12:18](https://youtube.com/watch?v=k3NqliNGo6s&t=738s)** received and transmitted packets and the activity and the connections and how those connections are made

**[12:23](https://youtube.com/watch?v=k3NqliNGo6s&t=743s)** between different devices, for example, you can see that the connection between the CLI demo node

**[12:28](https://youtube.com/watch?v=k3NqliNGo6s&t=748s)** and PvE, for example, to this client is a direct connection. And that's printed out for me right

**[12:33](https://youtube.com/watch?v=k3NqliNGo6s&t=753s)** there. Pretty cool stuff. Now, of course, if you want to expose that through tailscale funnel

**[12:38](https://youtube.com/watch?v=k3NqliNGo6s&t=758s)** to a remote administrator or something, you could do that using tailscale server funnel, of course.

**[12:43](https://youtube.com/watch?v=k3NqliNGo6s&t=763s)** What else have we got? So let's do tailscale status dash dash peers. See what that gives us.

**[12:49](https://youtube.com/watch?v=k3NqliNGo6s&t=769s)** Again, that's pretty much the default view that we get when we run status anyway.

**[12:54](https://youtube.com/watch?v=k3NqliNGo6s&t=774s)** Now, for those of you who are more sort of developer minded, you can do tailscale status dash dash

**[13:00](https://youtube.com/watch?v=k3NqliNGo6s&t=780s)** JSON. I'm going to pipe that into jq so that it looks pretty. And there you go. You get to see all

**[13:06](https://youtube.com/watch?v=k3NqliNGo6s&t=786s)** of the different host keys and all of the information that gets exposed between different nodes on

**[13:11](https://youtube.com/watch?v=k3NqliNGo6s&t=791s)** your telnet. There's nothing sensitive here, particularly. If you've ever done anything with cryptography,

**[13:16](https://youtube.com/watch?v=k3NqliNGo6s&t=796s)** I'll understand that the private keys remain private on each device and all that we're looking at

**[13:20](https://youtube.com/watch?v=k3NqliNGo6s&t=800s)** here are the public keys. So again, there's nothing too sensitive going on. But for example,

**[13:23](https://youtube.com/watch?v=k3NqliNGo6s&t=803s)** if you ever needed to get a specific piece of information, like what the capability map of a

**[13:28](https://youtube.com/watch?v=k3NqliNGo6s&t=808s)** specific node is, for example, that's how you would do that. You do tailscale status dash dash JSON

**[13:34](https://youtube.com/watch?v=k3NqliNGo6s&t=814s)** and that prints out the command that you can see above. Pretty cool stuff. Let's just take a look at

**[13:41](https://youtube.com/watch?v=k3NqliNGo6s&t=821s)** the dash dash active command. This is a pretty interesting one. You can see if I run tailscale status

**[13:46](https://youtube.com/watch?v=k3NqliNGo6s&t=826s)** by default, it prints out all of the nodes on the telnet, including ones that are idle or offline.

**[13:52](https://youtube.com/watch?v=k3NqliNGo6s&t=832s)** If I don't want that, I only want to see active nodes. I can pass tailscale status

**[13:57](https://youtube.com/watch?v=k3NqliNGo6s&t=837s)** with the active flag. And boom, there you go. You can see I've only got my three active nodes,

**[14:02](https://youtube.com/watch?v=k3NqliNGo6s&t=842s)** which includes bulldric, this laptop, the Alex C container that's running the CLI demo and

**[14:07](https://youtube.com/watch?v=k3NqliNGo6s&t=847s)** the proxmox host that that's running on. So that covers tailscale status, I think. Now,

**[14:13](https://youtube.com/watch?v=k3NqliNGo6s&t=853s)** the next thing I wanted to talk about today is tailscale ping. So let's take a look at tailscale ping

**[14:19](https://youtube.com/watch?v=k3NqliNGo6s&t=859s)** for just a moment. This is a way to basically use the tailscale layer to make sure that you're

**[14:26](https://youtube.com/watch?v=k3NqliNGo6s&t=866s)** pinging packets directly between your nodes. So the tailscale ping command pings a peer node

**[14:33](https://youtube.com/watch?v=k3NqliNGo6s&t=873s)** from the tailscale layer and reports which route it took for its response. The first ping

**[14:40](https://youtube.com/watch?v=k3NqliNGo6s&t=880s)** will probably go over tailscale's DURP or relay protocol servers, whilst the natural

**[14:46](https://youtube.com/watch?v=k3NqliNGo6s&t=886s)** versatile finds a direct path through. So for example, I'm going to go back to status and just show

**[14:51](https://youtube.com/watch?v=k3NqliNGo6s&t=891s)** you all the nodes I've got here. I've got one in England in UK Norwich. I've got another one

**[14:57](https://youtube.com/watch?v=k3NqliNGo6s&t=897s)** in Canada at CADYYZ, YYZ, I suppose if it's Canada, right? And then I've got the exit node running

**[15:04](https://youtube.com/watch?v=k3NqliNGo6s&t=904s)** in, well, just running in just this rack down here behind me. Just on that little Dell one

**[15:09](https://youtube.com/watch?v=k3NqliNGo6s&t=909s)** liter PC that I did in the self-hosting series before the summer break. So if I want to use tailscale

**[15:14](https://youtube.com/watch?v=k3NqliNGo6s&t=914s)** ping to understand how the network is kind of handling the packets between different devices,

**[15:22](https://youtube.com/watch?v=k3NqliNGo6s&t=922s)** I can do tailscale ping and then type in the name of a node on my network. So tailscale ping

**[15:27](https://youtube.com/watch?v=k3NqliNGo6s&t=927s)** PvE for example is just pinging that rack behind me. So it's going via the interface of 1921681.10.

**[15:36](https://youtube.com/watch?v=k3NqliNGo6s&t=936s)** Staying within my local network, okay, it's traversing a VLAN in this case, but it basically traverses

**[15:42](https://youtube.com/watch?v=k3NqliNGo6s&t=942s)** the interface of 1921681.10. So it doesn't leave this network. I now know that because it's just

**[15:49](https://youtube.com/watch?v=k3NqliNGo6s&t=949s)** told me it did it in nine milliseconds. There's no way it's going to go to Canada in nine milliseconds

**[15:53](https://youtube.com/watch?v=k3NqliNGo6s&t=953s)** from here. So let's do that. Let's now do exit CADYYZ and see what happens. Are we going to establish

**[16:02](https://youtube.com/watch?v=k3NqliNGo6s&t=962s)** a direct connection right away? I should have noticed that particular node appears to be offline.

**[16:07](https://youtube.com/watch?v=k3NqliNGo6s&t=967s)** In fact, it told me that right here. I just didn't notice it because I was talking.

**[16:12](https://youtube.com/watch?v=k3NqliNGo6s&t=972s)** Okay, so let's do the UK node instead. Let's do UK NOR for UK Norwich. This is now going to show

**[16:17](https://youtube.com/watch?v=k3NqliNGo6s&t=977s)** me that it's ponging through the DURP node at London Heathrow LHR. I believe that's what it stands

**[16:23](https://youtube.com/watch?v=k3NqliNGo6s&t=983s)** for at least. And then it eventually established a direct connection in just a few seconds. So using

**[16:28](https://youtube.com/watch?v=k3NqliNGo6s&t=988s)** tailscale ping, I'm now able to determine that I've got a direct connection between those two

**[16:34](https://youtube.com/watch?v=k3NqliNGo6s&t=994s)** nodes on my tailnet. And indeed, just pay attention to how that changes. So this line right here shows

**[16:40](https://youtube.com/watch?v=k3NqliNGo6s&t=1000s)** me idle and offers exit node right now. But now if I do tailscale status again, it's going to show me

**[16:47](https://youtube.com/watch?v=k3NqliNGo6s&t=1007s)** that the Norwich node is now directly connected through the WALIP of that remote host, which I think

**[16:54](https://youtube.com/watch?v=k3NqliNGo6s&t=1014s)** is my mother-in-law's network. So please don't, please don't de-dos her. Otherwise, I'll get a very

**[16:59](https://youtube.com/watch?v=k3NqliNGo6s&t=1019s)** nasty phone call. Alex, why is my internet not working? Don't know. So you can see that now this line

**[17:05](https://youtube.com/watch?v=k3NqliNGo6s&t=1025s)** shows I've got a direct connection through the WALIP of that remote site. So you can see how we can

**[17:10](https://youtube.com/watch?v=k3NqliNGo6s&t=1030s)** start to use all of these commands together. So we've got tailscale status showing us what's going

**[17:14](https://youtube.com/watch?v=k3NqliNGo6s&t=1034s)** on and then ping showing us how the actual packets find the root to the remote host. And we also saw

**[17:21](https://youtube.com/watch?v=k3NqliNGo6s&t=1041s)** that the first ping here traversed a tailscale derp server, one of our reload protocol servers,

**[17:27](https://youtube.com/watch?v=k3NqliNGo6s&t=1047s)** as I talked about. And then as the natural reversal, the stateful packet filtering traversal

**[17:33](https://youtube.com/watch?v=k3NqliNGo6s&t=1053s)** magic happened behind the scenes. Eventually, after just three or four pings, we established a direct

**[17:38](https://youtube.com/watch?v=k3NqliNGo6s&t=1058s)** connection. Now, sometimes you might find that tailscale ping works, but a normal ping doesn't.

**[17:46](https://youtube.com/watch?v=k3NqliNGo6s&t=1066s)** And that can mean that one side's operating system file will might be blocking packets,

**[17:50](https://youtube.com/watch?v=k3NqliNGo6s&t=1070s)** because tailscale ping itself doesn't inject the packets into the other side's ton devices.

**[17:57](https://youtube.com/watch?v=k3NqliNGo6s&t=1077s)** By default, tailscale ping will stop after 10 pings, or once a direct connection,

**[18:02](https://youtube.com/watch?v=k3NqliNGo6s&t=1082s)** is established, whichever happens to come first. And a provided host name must resolve to a DNS name,

**[18:08](https://youtube.com/watch?v=k3NqliNGo6s&t=1088s)** or be a tailscale IP, or a subnet IP advertised by a tailscale relay node, in order for the

**[18:15](https://youtube.com/watch?v=k3NqliNGo6s&t=1095s)** routing table to know where to send those packets when it's doing the tailscale ping.

**[18:20](https://youtube.com/watch?v=k3NqliNGo6s&t=1100s)** All right, so that's tailscale ping. Is there anything else we need to look at by doing

**[18:23](https://youtube.com/watch?v=k3NqliNGo6s&t=1103s)** dash dash help? There are a few other things. You know how I talked about tailscale ping running

**[18:29](https://youtube.com/watch?v=k3NqliNGo6s&t=1109s)** at the tailscale layer. Well, if you want to do an ICMP level ping instead of a tailscale level

**[18:34](https://youtube.com/watch?v=k3NqliNGo6s&t=1114s)** ping, you can specify that here with dash dash ICMP. Now, I'm curious as to what exactly a verbose

**[18:41](https://youtube.com/watch?v=k3NqliNGo6s&t=1121s)** ping might do. So let me do tailscale ping dash dash verbose and just see what happens here.

**[18:48](https://youtube.com/watch?v=k3NqliNGo6s&t=1128s)** There you go. You can see that actually the direct connection, I guess I'd been waffling on for

**[18:52](https://youtube.com/watch?v=k3NqliNGo6s&t=1132s)** long enough that the state for firewalls would reset themselves, and we had to redo the natural

**[18:58](https://youtube.com/watch?v=k3NqliNGo6s&t=1138s)** versor in just a few minutes. You can see here that the time and date and that kind of thing.

**[19:03](https://youtube.com/watch?v=k3NqliNGo6s&t=1143s)** Yeah, I mean, the verbose isn't really that verbose, but it might be useful in some logs somewhere.

**[19:08](https://youtube.com/watch?v=k3NqliNGo6s&t=1148s)** So there you go. That's tailscale ping. Now, the next command that I want to look at today is

**[19:12](https://youtube.com/watch?v=k3NqliNGo6s&t=1152s)** tailscale DNS. Now, this one basically prints out the view of the world that this client has

**[19:19](https://youtube.com/watch?v=k3NqliNGo6s&t=1159s)** about the DNS of your network. So, for example, let me do tailscale DNS status and that's going to

**[19:26](https://youtube.com/watch?v=k3NqliNGo6s&t=1166s)** now print out all the name servers that I have. So this 1042 054 is the local DNS server in my network.

**[19:34](https://youtube.com/watch?v=k3NqliNGo6s&t=1174s)** You can see that velociraptor noodle fish. That's my tailscale TS net

**[19:39](https://youtube.com/watch?v=k3NqliNGo6s&t=1179s)** search domain. So that's the URL that we give to every tailnet. So automatically,

**[19:45](https://youtube.com/watch?v=k3NqliNGo6s&t=1185s)** that will be appended to things that don't have a fully qualified domain name as part of the

**[19:49](https://youtube.com/watch?v=k3NqliNGo6s&t=1189s)** search process. And you can see any split DNS that you've got set up here too. Now, this particular

**[19:55](https://youtube.com/watch?v=k3NqliNGo6s&t=1195s)** tailnet has quite a basic DNS setup. So let me switch to my personal one in order to show you something

**[20:03](https://youtube.com/watch?v=k3NqliNGo6s&t=1203s)** a little more contrived a little more over the top. I'm not logged into that one. So just give me

**[20:07](https://youtube.com/watch?v=k3NqliNGo6s&t=1207s)** a second to get logged in. I'll be right back. All right. Now, I'm back and you can see that I've

**[20:11](https://youtube.com/watch?v=k3NqliNGo6s&t=1211s)** logged into my personal town and there's way too many devices on here. But what I want to show you

**[20:16](https://youtube.com/watch?v=k3NqliNGo6s&t=1216s)** is the tailscale DNS status of the town that I have. So for example, I've got several search

**[20:22](https://youtube.com/watch?v=k3NqliNGo6s&t=1222s)** domains configured so that so that I can have different DNS servers in different physical locations

**[20:29](https://youtube.com/watch?v=k3NqliNGo6s&t=1229s)** be responsible for their local networks configuration. So WD, for example, is one site that I

**[20:36](https://youtube.com/watch?v=k3NqliNGo6s&t=1236s)** control NR is another one, that kind of thing. And then I've got specific websites that I want to

**[20:41](https://youtube.com/watch?v=k3NqliNGo6s&t=1241s)** make sure always go to a specific domain server as well. I kind of abuse the split DNS a little

**[20:47](https://youtube.com/watch?v=k3NqliNGo6s&t=1247s)** bit in order to make that search domain stuff work. But you can also see that I've got a bunch of

**[20:51](https://youtube.com/watch?v=k3NqliNGo6s&t=1251s)** split DNS routes in here as well. Stuff like the BBC, for example, always goes out over some

**[20:57](https://youtube.com/watch?v=k3NqliNGo6s&t=1257s)** connections I have back in the UK, let's we say about that, the better probably. I also will get

**[21:03](https://youtube.com/watch?v=k3NqliNGo6s&t=1263s)** cancelled. Let's not have that. But you can see, for example, this is all of the magic DNS information

**[21:10](https://youtube.com/watch?v=k3NqliNGo6s&t=1270s)** that this node has as a view of the world. And this, this as you can see, can get quite complex,

**[21:16](https://youtube.com/watch?v=k3NqliNGo6s&t=1276s)** quite quickly. Now, another command that's available to us as part of the tailscale DNS options

**[21:22](https://youtube.com/watch?v=k3NqliNGo6s&t=1282s)** is query. So the tailscale DNS query sub command performs a DNS query for the specified name

**[21:28](https://youtube.com/watch?v=k3NqliNGo6s&t=1288s)** using the internal DNS forwarder. Now, if you aren't familiar with how tailscale DNS works,

**[21:33](https://youtube.com/watch?v=k3NqliNGo6s&t=1293s)** every single client, which includes your phone and your Apple TV and your, you know, your Android

**[21:39](https://youtube.com/watch?v=k3NqliNGo6s&t=1299s)** TV set top box, that kind of stuff, they all have a local DNS resolver running on them. And every

**[21:45](https://youtube.com/watch?v=k3NqliNGo6s&t=1305s)** time we do an update a node joins a tailnet or we change an ACL rule or anything, those rules

**[21:52](https://youtube.com/watch?v=k3NqliNGo6s&t=1312s)** get pushed to those clients. So that's what this local internal DNS forwarder is talking about here,

**[21:58](https://youtube.com/watch?v=k3NqliNGo6s&t=1318s)** that's running on this laptop. It's mirroring the central control planes view of the world,

**[22:04](https://youtube.com/watch?v=k3NqliNGo6s&t=1324s)** but it is that, just that it's a mirror. But it does mean that DNS is a lot faster than it would

**[22:09](https://youtube.com/watch?v=k3NqliNGo6s&t=1329s)** otherwise be. So let's just look up Google.com. So my typing tailscale DNS query Google.com,

**[22:15](https://youtube.com/watch?v=k3NqliNGo6s&t=1335s)** you can see that that came back with a normal DNS name. And we can see the DNS server that was

**[22:19](https://youtube.com/watch?v=k3NqliNGo6s&t=1339s)** used in order to fetch that remote query. But let's say that I want to grab something from my

**[22:25](https://youtube.com/watch?v=k3NqliNGo6s&t=1345s)** tailnet, for example. So I'm going to do the fully qualified domain name of this exit node,

**[22:31](https://youtube.com/watch?v=k3NqliNGo6s&t=1351s)** for example. And let's just see what it comes back with. There we go. We can see that we get the 100.cg

**[22:37](https://youtube.com/watch?v=k3NqliNGo6s&t=1357s)** NAT IP address of this specific node that comes back from the resolvers IPv6 address there as well

**[22:45](https://youtube.com/watch?v=k3NqliNGo6s&t=1365s)** as an IPv4. So we can, this is probably a very similar situation as to using dig, which is a tool

**[22:53](https://youtube.com/watch?v=k3NqliNGo6s&t=1373s)** that lets me look up DNS records and things like that outside of the tailscale universe. You can see

**[23:00](https://youtube.com/watch?v=k3NqliNGo6s&t=1380s)** here that I get the same address come back here. But if you want a tailscale specific view of the

**[23:06](https://youtube.com/watch?v=k3NqliNGo6s&t=1386s)** world, because you know, you can override some things in the magic DNS section of tailscale over

**[23:11](https://youtube.com/watch?v=k3NqliNGo6s&t=1391s)** here in the admin console, sometimes we confuse ourselves as network admin. Sometimes we do things

**[23:18](https://youtube.com/watch?v=k3NqliNGo6s&t=1398s)** with the best of intentions and forget that we did it a few weeks later. And we need to just query

**[23:23](https://youtube.com/watch?v=k3NqliNGo6s&t=1403s)** what view of the world does this client have. And most of the tools I've shown you today are actually

**[23:29](https://youtube.com/watch?v=k3NqliNGo6s&t=1409s)** designed to just kind of show you that kind of stuff. Speaking of the view of the world,

**[23:34](https://youtube.com/watch?v=k3NqliNGo6s&t=1414s)** let's do a tailscale net check. Now this one's pretty interesting. This shows me the view of the

**[23:39](https://youtube.com/watch?v=k3NqliNGo6s&t=1419s)** world that this client has of the rest of the tailscale kind of public infrastructure. You can see

**[23:45](https://youtube.com/watch?v=k3NqliNGo6s&t=1425s)** all the different places that we run our relay nodes in our dirt nodes, these things here.

**[23:51](https://youtube.com/watch?v=k3NqliNGo6s&t=1431s)** You can see my nearest one. I mean, I live on the east coast of the states. And you can see my

**[23:54](https://youtube.com/watch?v=k3NqliNGo6s&t=1434s)** nearest one is in Virginia in Ashburton. That makes complete sense with New York not far behind.

**[24:00](https://youtube.com/watch?v=k3NqliNGo6s&t=1440s)** Singapore is 244 milliseconds away. That makes that makes complete sense too. The speed of light

**[24:06](https://youtube.com/watch?v=k3NqliNGo6s&t=1446s)** is only so fast. So this can be really useful if we want to know things like is UDP supported,

**[24:13](https://youtube.com/watch?v=k3NqliNGo6s&t=1453s)** for example, on this network, on this node. Where is my nearest dirt node for performance? And

**[24:24](https://youtube.com/watch?v=k3NqliNGo6s&t=1464s)** things like exit nodes and that kind of stuff. But if we do dash dash help, we'll see that net check

**[24:30](https://youtube.com/watch?v=k3NqliNGo6s&t=1470s)** has a few other options that we can do. So for example, we can do, again, like we could with

**[24:36](https://youtube.com/watch?v=k3NqliNGo6s&t=1476s)** status, we can do a dash dash json, which I'm going to pipe to jq. What did I do? Oh, it's format.

**[24:44](https://youtube.com/watch?v=k3NqliNGo6s&t=1484s)** Okay, it's format json. And then we'll pipe that to jq. And then we can use that maybe to

**[24:50](https://youtube.com/watch?v=k3NqliNGo6s&t=1490s)** dynamically route things around within within the network. Like let's say that we want to keep an

**[24:56](https://youtube.com/watch?v=k3NqliNGo6s&t=1496s)** eye on the latency between different regions and map that to a Prometheus dashboard or something

**[25:00](https://youtube.com/watch?v=k3NqliNGo6s&t=1500s)** like that. This is how you would do that, which sort of ties neatly into the tailscale metrics

**[25:06](https://youtube.com/watch?v=k3NqliNGo6s&t=1506s)** command that we have as well. So I'll show you tailscale metrics whilst we're in here and do

**[25:12](https://youtube.com/watch?v=k3NqliNGo6s&t=1512s)** dash dash help. And this really, if you're into DevOps and sort of building dashboards and

**[25:17](https://youtube.com/watch?v=k3NqliNGo6s&t=1517s)** that kind of thing, this will let you expose a bunch of client metrics. In fact, I've made a

**[25:23](https://youtube.com/watch?v=k3NqliNGo6s&t=1523s)** video about that a while back and I'll link that up here. But let's do tailscale metrics print.

**[25:30](https://youtube.com/watch?v=k3NqliNGo6s&t=1530s)** This shows you all of the different things. If you're familiar with Prometheus,

**[25:33](https://youtube.com/watch?v=k3NqliNGo6s&t=1533s)** this will look incredibly familiar to you. But this shows you all of the things of the view

**[25:38](https://youtube.com/watch?v=k3NqliNGo6s&t=1538s)** of the world that this node has. So you can see how if you start to combine the client metrics that

**[25:43](https://youtube.com/watch?v=k3NqliNGo6s&t=1543s)** we offer with the JSON output of net check and just all of these things are data points that you can

**[25:50](https://youtube.com/watch?v=k3NqliNGo6s&t=1550s)** use as an admin to make the tailscale network work for you and do what you need. So I think that's

**[25:56](https://youtube.com/watch?v=k3NqliNGo6s&t=1556s)** about all we've got time for today. You can see here that there is a huge long list of different

**[26:01](https://youtube.com/watch?v=k3NqliNGo6s&t=1561s)** things that we can look at in the tailscale CLI. This could have easily been a 10-part video series

**[26:07](https://youtube.com/watch?v=k3NqliNGo6s&t=1567s)** but I decided just to do a deep dive into the CLI of some of the less-known stuff perhaps today

**[26:13](https://youtube.com/watch?v=k3NqliNGo6s&t=1573s)** and digging into maybe some of the options that you've used but didn't know some of the other

**[26:17](https://youtube.com/watch?v=k3NqliNGo6s&t=1577s)** stuff about. So leave a comment down below and let me know what else you'd like to see from this

**[26:21](https://youtube.com/watch?v=k3NqliNGo6s&t=1581s)** list a bit more of a deep dive. For example, we didn't dig into drive, for example, or

**[26:27](https://youtube.com/watch?v=k3NqliNGo6s&t=1587s)** or bug report or file to send and receive files. There's a bunch more stuff in there. I highly

**[26:33](https://youtube.com/watch?v=k3NqliNGo6s&t=1593s)** recommend that you go and have a play. Each of these things, for example, let's just do file,

**[26:37](https://youtube.com/watch?v=k3NqliNGo6s&t=1597s)** dash dash help. Each of these things has their own help option and I would love to hear from you.

**[26:44](https://youtube.com/watch?v=k3NqliNGo6s&t=1604s)** Now if you are using any of this stuff and you get kind of lost or confused, we have a brand new

**[26:49](https://youtube.com/watch?v=k3NqliNGo6s&t=1609s)** discord server at discord.gg slash tailscale. I'd love to see you over there. I'm over there at

**[26:54](https://youtube.com/watch?v=k3NqliNGo6s&t=1614s)** AlexKTZ or maybe it's ironic bad drive, I forget which I am. Anyway, come join us on the tailscale

**[26:59](https://youtube.com/watch?v=k3NqliNGo6s&t=1619s)** discord server and as always thank you so much for watching and until next time I've been Alex

**[27:05](https://youtube.com/watch?v=k3NqliNGo6s&t=1625s)** from tailscale.

---

*Automatically generated transcript. May contain errors.*
