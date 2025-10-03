---
video_id: "HnhgmRDiBFo"
title: "Put a link shortener app right on your Tailnet with golink"
description: "golink is a private shortlink service for your tailnet. It lets you create short, memorable links for the websites you and your team use most.

In today's video Alex shows you the ropes and guides you..."
channel_name: "Tailscale"
channel_id: "UCcdv38QxPjSMqbt5ffLhJLA"
published_at: "2025-07-25"
duration_seconds: 565
youtube_url: "https://www.youtube.com/watch?v=HnhgmRDiBFo"
thumbnail_url: "https://i.ytimg.com/vi/HnhgmRDiBFo/maxresdefault.jpg"

# Transcription metadata
transcribed_at: "2025-10-03T15:54:21.065641"
transcription_method: "cpu"
model_used: "base"
language: "en"
word_count: 1804
transcription_time_seconds: 15.8
---

# Put a link shortener app right on your Tailnet with golink

**[00:00](https://youtube.com/watch?v=HnhgmRDiBFo&t=0s)** Are you fed up with typing long, complicated URLs into your browser? Well, let me introduce

**[00:05](https://youtube.com/watch?v=HnhgmRDiBFo&t=5s)** you to GoLink, an open source, private URL shortening service for your tailnet, written

**[00:12](https://youtube.com/watch?v=HnhgmRDiBFo&t=12s)** by the nerds here at Tailscale. Using GoLink, you can create and share simple, go-slash-name

**[00:18](https://youtube.com/watch?v=HnhgmRDiBFo&t=18s)** links for commonly accessed websites so that anyone in your tailnet can access them no

**[00:23](https://youtube.com/watch?v=HnhgmRDiBFo&t=23s)** matter to the device they're on, without requiring any browser extensions or fiddling with

**[00:28](https://youtube.com/watch?v=HnhgmRDiBFo&t=28s)** any DNS settings either. For example, let's say you want to get to your Tailscale admin console.

**[00:33](https://youtube.com/watch?v=HnhgmRDiBFo&t=33s)** You can typically find this at tailscale.com slash admin, which then redirects you to where you

**[00:39](https://youtube.com/watch?v=HnhgmRDiBFo&t=39s)** need to go. But with GoLink, we can just type in go slash admin and boom, we are at our tailscale

**[00:48](https://youtube.com/watch?v=HnhgmRDiBFo&t=48s)** admin console with no further typing required. Now, GoLink can do more than just simple name

**[00:54](https://youtube.com/watch?v=HnhgmRDiBFo&t=54s)** expansion. It also supports templated links. Because GoLink is written in Go, it supports using Go

**[01:02](https://youtube.com/watch?v=HnhgmRDiBFo&t=62s)** templates for all destination links as well. The launch blog post linked down below has plenty

**[01:08](https://youtube.com/watch?v=HnhgmRDiBFo&t=68s)** of examples for you here. One such example, though, is you can do go slash search and then you

**[01:13](https://youtube.com/watch?v=HnhgmRDiBFo&t=73s)** can put your query after another slash. So, Tailscale here, for example, searches Google for tailscale.

**[01:20](https://youtube.com/watch?v=HnhgmRDiBFo&t=80s)** Now, you can probably think about ways you can pass those parameters into other services

**[01:25](https://youtube.com/watch?v=HnhgmRDiBFo&t=85s)** on your own time. Now, this is a tailnet first app so it is designed, built and distributed

**[01:31](https://youtube.com/watch?v=HnhgmRDiBFo&t=91s)** with tailscale in mind. No docker side cars are required here and deploying it will probably take

**[01:37](https://youtube.com/watch?v=HnhgmRDiBFo&t=97s)** you less than a minute as I'll show you after the break. So, let's see how we go about deploying

**[01:44](https://youtube.com/watch?v=HnhgmRDiBFo&t=104s)** GoLink. The concept of tailscale, or more specifically your tailnet as an app platform,

**[01:51](https://youtube.com/watch?v=HnhgmRDiBFo&t=111s)** can take a moment for you to get your head around at first. But when you realize that you can run

**[01:56](https://youtube.com/watch?v=HnhgmRDiBFo&t=116s)** an app anywhere and then also access that app from anywhere, you start to see your infrastructure

**[02:03](https://youtube.com/watch?v=HnhgmRDiBFo&t=123s)** a bit differently. Now, here at Tailscale we use GoLink internally and before we made it an integral

**[02:09](https://youtube.com/watch?v=HnhgmRDiBFo&t=129s)** part of our company's workflow, it was running off a single developer's laptop. Nobody even noticed

**[02:15](https://youtube.com/watch?v=HnhgmRDiBFo&t=135s)** when we moved it into a production host because the app was available from anywhere within the tailnet,

**[02:20](https://youtube.com/watch?v=HnhgmRDiBFo&t=140s)** exactly the same as before. All that changed was we made our sys admins happy on the back end

**[02:26](https://youtube.com/watch?v=HnhgmRDiBFo&t=146s)** because there were backups and that kind of thing. Now, deployment, as I promised, is really straight

**[02:31](https://youtube.com/watch?v=HnhgmRDiBFo&t=151s)** forward via docker compose. And as usual, in the description down below, I have a link to the source

**[02:37](https://youtube.com/watch?v=HnhgmRDiBFo&t=157s)** code that you're going to need. It's also in the linked blog post there too. But essentially,

**[02:42](https://youtube.com/watch?v=HnhgmRDiBFo&t=162s)** all you need is this very straight forward docker compose YAML files. So, I already have a host with

**[02:47](https://youtube.com/watch?v=HnhgmRDiBFo&t=167s)** tailscale installed on it. In fact, it's my proxmox host over here at pve.philociraptor. And we

**[02:54](https://youtube.com/watch?v=HnhgmRDiBFo&t=174s)** set this up a few weeks ago in the self-hosted starter guide, which I'll put a link to the playlist

**[02:59](https://youtube.com/watch?v=HnhgmRDiBFo&t=179s)** for that up here. But all I want to do is create a YAML file here of called compose.yaml. I'm going

**[03:05](https://youtube.com/watch?v=HnhgmRDiBFo&t=185s)** to delete the contents of this file and then just paste in the contents of my docker compose

**[03:11](https://youtube.com/watch?v=HnhgmRDiBFo&t=191s)** YAML file from the gettub repo. Now, all you need to do, dear user, dear viewer, is go to tailscale.com,

**[03:19](https://youtube.com/watch?v=HnhgmRDiBFo&t=199s)** go to your admin console. I suppose I could have gone to go slash admin, couldn't I? And save myself

**[03:24](https://youtube.com/watch?v=HnhgmRDiBFo&t=204s)** a few keystrokes there, but maybe next time muscle memory will get me. So, we need to get ourselves

**[03:31](https://youtube.com/watch?v=HnhgmRDiBFo&t=211s)** an auth key. So, to do that, we go to our admin console, as I say, go to settings and then keys,

**[03:36](https://youtube.com/watch?v=HnhgmRDiBFo&t=216s)** generate an auth key here. I'm going to make mine reusable. I'm just going to call this go link,

**[03:43](https://youtube.com/watch?v=HnhgmRDiBFo&t=223s)** I think, glink. I kind of wish the project was called glink now. And you can actually put this

**[03:50](https://youtube.com/watch?v=HnhgmRDiBFo&t=230s)** behind a tag and you can do some filtering based on tags with go link as well. If you'd like to,

**[03:55](https://youtube.com/watch?v=HnhgmRDiBFo&t=235s)** we're not going to do that today, but it's certainly possible with an ACL grant, which again,

**[04:00](https://youtube.com/watch?v=HnhgmRDiBFo&t=240s)** is discussed in the linked blog post down below. All right. So, I've got my auth key right here.

**[04:05](https://youtube.com/watch?v=HnhgmRDiBFo&t=245s)** I'm going to paste this in. I'm going to press save. In fact, I need to edit the file on the

**[04:11](https://youtube.com/watch?v=HnhgmRDiBFo&t=251s)** proxmox host. Don't sign not the one in the get repo. I'm going to find the part of the file I

**[04:16](https://youtube.com/watch?v=HnhgmRDiBFo&t=256s)** want to edit with a forward slash TS key. It's going to take me right to where I want to go.

**[04:21](https://youtube.com/watch?v=HnhgmRDiBFo&t=261s)** And then I'm going to do see and then dollar signs take me until the end of the file.

**[04:26](https://youtube.com/watch?v=HnhgmRDiBFo&t=266s)** Make sure that I've got this value on my clipboard. And then just paste it. And you'll see that

**[04:30](https://youtube.com/watch?v=HnhgmRDiBFo&t=270s)** it overwrites the contents of that file. I'll then press escape and then WQ for right quit.

**[04:36](https://youtube.com/watch?v=HnhgmRDiBFo&t=276s)** By the way, if you want to get into VIM, VIMTUTE is an amazing thing. Obviously, I don't have

**[04:40](https://youtube.com/watch?v=HnhgmRDiBFo&t=280s)** it installed here, but take a look at it. You'll probably lose an evening to it, but it's a lot

**[04:44](https://youtube.com/watch?v=HnhgmRDiBFo&t=284s)** of fun. Okay, so we've got our compose file here ready to go. I actually already set this up

**[04:49](https://youtube.com/watch?v=HnhgmRDiBFo&t=289s)** a few minutes ago. So, Docker compose up here won't do an awful lot. But if we do Docker compose

**[04:55](https://youtube.com/watch?v=HnhgmRDiBFo&t=295s)** up minus D, that will start the app and then logs minus F will show us the logs of the running

**[05:01](https://youtube.com/watch?v=HnhgmRDiBFo&t=301s)** application. And all that's happened is we've now got ourselves a brand new app on our tailnet.

**[05:06](https://youtube.com/watch?v=HnhgmRDiBFo&t=306s)** This is running at go.valosiraptorhyphenoodlefish. And much like any other node on our tailnet,

**[05:13](https://youtube.com/watch?v=HnhgmRDiBFo&t=313s)** this just appears as a node right here. You can see that I've got an IP address. I've got an IPv6

**[05:19](https://youtube.com/watch?v=HnhgmRDiBFo&t=319s)** address. I've got a fully qualified domain name as well as a short one. So if I literally do

**[05:23](https://youtube.com/watch?v=HnhgmRDiBFo&t=323s)** HTTP slash go, this takes me to the private short link service for my tailnet. So I can just call

**[05:32](https://youtube.com/watch?v=HnhgmRDiBFo&t=332s)** this go slash cats. And then I can search for a cat website. Absolutely no idea what we're about to see.

**[05:39](https://youtube.com/watch?v=HnhgmRDiBFo&t=339s)** Let's go to the cat site.com. Yeah, there we go. That's perfect. So the cat site.com,

**[05:45](https://youtube.com/watch?v=HnhgmRDiBFo&t=345s)** I can now do go slash cats. And that's going to redirect me to whenever I go to go slash cats.

**[05:51](https://youtube.com/watch?v=HnhgmRDiBFo&t=351s)** Now that's now going to redirect me to the cat site.com. And there is the gist of a very simple

**[05:57](https://youtube.com/watch?v=HnhgmRDiBFo&t=357s)** URL shortener. Okay, now what else can I show you? You'll see here that we've got some very basic

**[06:03](https://youtube.com/watch?v=HnhgmRDiBFo&t=363s)** telemetry. So you can see, for example, at my PR link has been clicked on five times. Search for

**[06:09](https://youtube.com/watch?v=HnhgmRDiBFo&t=369s)** cats, just the one time. Here is where we can see all of the different links, including what they're

**[06:15](https://youtube.com/watch?v=HnhgmRDiBFo&t=375s)** actually referencing underneath who owns them. And because this is a tailnet first application,

**[06:20](https://youtube.com/watch?v=HnhgmRDiBFo&t=380s)** you can also manage the ownership of these links using the tail scale identity that's baked into your

**[06:25](https://youtube.com/watch?v=HnhgmRDiBFo&t=385s)** tailnet as well. Now, one thing I should point out as part of that deployment that we just did

**[06:31](https://youtube.com/watch?v=HnhgmRDiBFo&t=391s)** is that we have a user set here as root. And this is because of some weirdness around

**[06:36](https://youtube.com/watch?v=HnhgmRDiBFo&t=396s)** local directory ownership and the user 65 532. There'll be a link to a GitHub issue explaining

**[06:43](https://youtube.com/watch?v=HnhgmRDiBFo&t=403s)** that down below if you want to get into the details there. The short version is if you want to put

**[06:48](https://youtube.com/watch?v=HnhgmRDiBFo&t=408s)** a bind mount directory to persist the go link data, just put user root and everything will be fine.

**[06:55](https://youtube.com/watch?v=HnhgmRDiBFo&t=415s)** This is like a proper hand wave. This is all you need to know droids are not these are not the

**[06:59](https://youtube.com/watch?v=HnhgmRDiBFo&t=419s)** droids you're looking for type moment. I'm aware of that. But just pop in user root and you should

**[07:05](https://youtube.com/watch?v=HnhgmRDiBFo&t=425s)** be good to go. Now, I want to show you some of the stuff going on with the templated links here

**[07:09](https://youtube.com/watch?v=HnhgmRDiBFo&t=429s)** because this is where things can get quite advanced quite quickly. If you're familiar with go templates,

**[07:14](https://youtube.com/watch?v=HnhgmRDiBFo&t=434s)** then obviously this will be second nature to you. And it can look a little bit weird to see

**[07:18](https://youtube.com/watch?v=HnhgmRDiBFo&t=438s)** kind of go code in the browser, but eventually you kind of get used to a bit like ginger templating

**[07:24](https://youtube.com/watch?v=HnhgmRDiBFo&t=444s)** and stuff like that. So you can see here, this is how we did our Google search query. So if you wanted

**[07:28](https://youtube.com/watch?v=HnhgmRDiBFo&t=448s)** to make this a Gira search, for example, or some kind of a other tool that you're using on a regular

**[07:33](https://youtube.com/watch?v=HnhgmRDiBFo&t=453s)** basis, you can pass parameters into the query that you're doing here and then have them come out

**[07:39](https://youtube.com/watch?v=HnhgmRDiBFo&t=459s)** the other side, which is pretty cool as well. In the linked blog post down below, there is a whole

**[07:44](https://youtube.com/watch?v=HnhgmRDiBFo&t=464s)** section here discussing some of the more advanced things you can do. Well, my favorite things that we

**[07:49](https://youtube.com/watch?v=HnhgmRDiBFo&t=469s)** do internally is we want to make a quick meeting. We just have a go slash meet thing here at tailscar.

**[07:55](https://youtube.com/watch?v=HnhgmRDiBFo&t=475s)** We do go slash meet. We have a link put on our clipboard and everybody can just join a very quick

**[08:00](https://youtube.com/watch?v=HnhgmRDiBFo&t=480s)** meet room. Now the other thing that I need to talk to you about is that this is an open source

**[08:04](https://youtube.com/watch?v=HnhgmRDiBFo&t=484s)** application. The week of August 4th, we're doing an internal hackathon week here at tailscale.

**[08:09](https://youtube.com/watch?v=HnhgmRDiBFo&t=489s)** Now internally, many of us will be looking at repos just like this, looking into ways to improve

**[08:14](https://youtube.com/watch?v=HnhgmRDiBFo&t=494s)** our open source projects. If you'd like to get involved, I can promise you that there will be folks

**[08:19](https://youtube.com/watch?v=HnhgmRDiBFo&t=499s)** and eyeballs looking at your PRs on these repos over the coming weeks. So do please get involved

**[08:26](https://youtube.com/watch?v=HnhgmRDiBFo&t=506s)** if you see a feature you want to add a feature to this project. Go ahead, open a PR and

**[08:30](https://youtube.com/watch?v=HnhgmRDiBFo&t=510s)** somebody at tailscale will take a look. You can also head over to the tailscale community projects

**[08:34](https://youtube.com/watch?v=HnhgmRDiBFo&t=514s)** page. So let's take a look at that, the community projects, where there are a whole bunch of other

**[08:39](https://youtube.com/watch?v=HnhgmRDiBFo&t=519s)** projects here at tailscale that we've we've featured from across the tailscale community.

**[08:46](https://youtube.com/watch?v=HnhgmRDiBFo&t=526s)** And indeed, go link is one of those projects. So you see there's a bunch of other projects on this

**[08:51](https://youtube.com/watch?v=HnhgmRDiBFo&t=531s)** page too. And if you'd like to get involved and open a PR, like I say, over the next week,

**[08:56](https://youtube.com/watch?v=HnhgmRDiBFo&t=536s)** so August 4th or so, there will be a bunch of people internally at tailscale looking at those

**[09:02](https://youtube.com/watch?v=HnhgmRDiBFo&t=542s)** repos. Now, may you go fourth and your links be short and your tailnet filled with apps.

**[09:07](https://youtube.com/watch?v=HnhgmRDiBFo&t=547s)** Thank you so much for watching and until next time, I've been Alex from tailscale.

---

*Automatically generated transcript. May contain errors.*
