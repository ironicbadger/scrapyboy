---
video_id: "JcrcbkDGJuk"
title: "Own Your Code Forever - A Private Git Server Setup Guide with Tailscale and Forgejo"
description: "In this comprehensive tutorial, learn how to set up your own private Git server using Forgejo (a self-hostable code forge) running in an LXC container on Proxmox. 

Alex walks through the entire proce..."
channel_name: "Tailscale"
channel_id: "UCcdv38QxPjSMqbt5ffLhJLA"
published_at: "2025-09-12"
duration_seconds: 1656
youtube_url: "https://www.youtube.com/watch?v=JcrcbkDGJuk"
thumbnail_url: "https://i.ytimg.com/vi_webp/JcrcbkDGJuk/maxresdefault.webp"

# Transcription metadata
transcribed_at: "2025-10-03T18:15:57.562778"
transcription_method: "cpu"
model_used: "base"
language: "en"
word_count: 5164
transcription_time_seconds: 46.4
---

# Own Your Code Forever - A Private Git Server Setup Guide with Tailscale and Forgejo

**[00:00](https://youtube.com/watch?v=JcrcbkDGJuk&t=0s)** If you've ever thought, wouldn't it be cool to host my own GitHub-like service? Well, you've come to the right place. Today, we're setting up a project called For YeHo in an LXC running on top of Proxmox. I'll show you how to connect it to your tailnet so that you can access your repositories from anywhere in the world, including a seamless way to expose SSH for clone operations using just a couple of lines of code in your tailscale configuration. Now, let me get this out of the way upfront.

**[00:30](https://youtube.com/watch?v=JcrcbkDGJuk&t=30s)** The pronunciation of the word for YeHo is probably excruciating the obvious to those of you who do speak Spanish that I do not. Part of me wonders, couldn't we just call this thing Cody McStore, my codeface, or something just to make Alex's life easier? Anyway, one of the reasons I decided to feature for YeHo today,

**[00:51](https://youtube.com/watch?v=JcrcbkDGJuk&t=51s)** is that the parent company of For YeHo codeberg is a self-described democratic non-profit organization building a trusted, exclusively free software code forge.

**[01:07](https://youtube.com/watch?v=JcrcbkDGJuk&t=67s)** You can broadly speaking think about For YeHo as a self-hostible clone of GitHub. Of course, a self-hostible code forge means that you're issuing the 150 million or so strong developer community that GitHub has and going it alone.

**[01:22](https://youtube.com/watch?v=JcrcbkDGJuk&t=82s)** That can be a bug or a feature depending on your point of view, because that community makes GitHub what it is, that collaborative aspect, both a treasure and a potential long-term problem

**[01:35](https://youtube.com/watch?v=JcrcbkDGJuk&t=95s)** through homogenization of the developer ecosystem. But if what you are looking for is a private, secure, and locally hosted place to put your Git repos, not to mention something that lives on your own infrastructure to boot, then For YeHo may just be a great solution for you.

**[01:54](https://youtube.com/watch?v=JcrcbkDGJuk&t=114s)** Equally, it's really useful for small teams who want to collaborate privately. Now, For YeHo can do almost everything that GitHub itself can do, issues, workflows, of course storing your code and a whole lot more besides,

**[02:09](https://youtube.com/watch?v=JcrcbkDGJuk&t=129s)** but it also has some often overlooked nifty little features like automatic repository mirroring. This is really useful if you want to use this instance of For YeHo to back up a public repository every few hours

**[02:22](https://youtube.com/watch?v=JcrcbkDGJuk&t=142s)** in case it gets taken down through a DMCA request or whatever and or otherwise removed from the internet. It's really useful to back up your code as well. So I use this to actually mirror all of my GitHub repositories locally just in case.

**[02:37](https://youtube.com/watch?v=JcrcbkDGJuk&t=157s)** So let's begin by spinning up an LXC on top of Proxmox. In fact, we've done this many times on the channel and I'll put a link to a dedicated video I've made about this before up there.

**[02:47](https://youtube.com/watch?v=JcrcbkDGJuk&t=167s)** And you can find as always all the code snippets and everything that we need to actually deploy this project in the description down below along with timestamps and chapters for you to find the bit of this video that makes the most sense for you.

**[03:00](https://youtube.com/watch?v=JcrcbkDGJuk&t=180s)** We can find the For YeHo project over at For YeHo.org. And again, I apologize for the pronunciation there. I hope I'm getting it right. For YeHo. For YeHo. Maybe we'll see. I'm sure the comments will tell me. Okay, so what we're going to do first of all, you can see I've already got an instance here running on an LXC one thousand and one.

**[03:22](https://youtube.com/watch?v=JcrcbkDGJuk&t=202s)** Indeed, that's running on my tailnet at for YeHo.volosiraptor hyphen needlefish. And you can see I've started to use it for a few things even. So let's say I want to back up a GitHub repository.

**[03:33](https://youtube.com/watch?v=JcrcbkDGJuk&t=213s)** Let's in fact use the one we're doing for this video. I'm going to come in here and grab the HTTPS URL that I have for this repo.

**[03:42](https://youtube.com/watch?v=JcrcbkDGJuk&t=222s)** Go across to, I mean, it said get the Freudian slip there for YeHo and do a new migration. You see all the options I've got here and actually going to just select GitHub.

**[03:54](https://youtube.com/watch?v=JcrcbkDGJuk&t=234s)** It supports not only GitHub.com, but also the self hosted on premise GitHub enterprise version. So this that could be useful if you're doing this at work potentially. And all you want to do is paste the URL in here for the clone URL.

**[04:07](https://youtube.com/watch?v=JcrcbkDGJuk&t=247s)** Sometimes you need to put an access token here for reasons. You can see right here. Now I want to select this repository will be a mirror. I'm not, I don't have a wiki over here.

**[04:19](https://youtube.com/watch?v=JcrcbkDGJuk&t=259s)** And indeed, if I want to migrate all these other items to issues, pull requests, what have you, I need an access token. I'm not going to bother with that today.

**[04:27](https://youtube.com/watch?v=JcrcbkDGJuk&t=267s)** But the local clone of that repository in this instance is going to live under the user's a pod, which is the main user I've created in this local instance of for YeHo.

**[04:38](https://youtube.com/watch?v=JcrcbkDGJuk&t=278s)** I'm just going to come migrate repository. And before my very eyes, essentially what this does is it just does a supposed to get pull fetch like clone every I think the default is every eight hours or so.

**[04:50](https://youtube.com/watch?v=JcrcbkDGJuk&t=290s)** And if you want to change that, well, first of all, let's just take a moment and realize that we now have a fully local clone of this tail scale dev repo on infrastructure that I own and I control and you can see it broadly speaking looks like a code for like it like suppose a self hosted GitHub, right.

**[05:09](https://youtube.com/watch?v=JcrcbkDGJuk&t=309s)** And we can see in here you've got all this stuff. We've got all the branches. So for today's video as I record video for YeHo is in here and there are all the different files we're going to get to in just a minute.

**[05:21](https://youtube.com/watch?v=JcrcbkDGJuk&t=321s)** But I mentioned a moment ago that you can configure the mirror setting so you can configure how frequently this thing checks for updates, I suppose. And you can see that the default time here is every eight hours.

**[05:34](https://youtube.com/watch?v=JcrcbkDGJuk&t=334s)** And of course, you can do a manual sync just here. So lots of things you can poke around with under the hood here and I will also add that for YeHo supports self hosted runners.

**[05:46](https://youtube.com/watch?v=JcrcbkDGJuk&t=346s)** So if you want to integrate this into a locally self hosted CICD pipeline, you can absolutely do that using for YeHo. In fact, next weeks or certainly a video coming soon to the channel will be part two of for YeHo how to spin up self hosted runners and connect them to your tail net.

**[06:03](https://youtube.com/watch?v=JcrcbkDGJuk&t=363s)** So you can have fully offline CICD pipeline running across. Well, it doesn't matter where the infrastructure is. It could be under my desk. It could be literally under your desk and tail scale will make a connection between the two.

**[06:16](https://youtube.com/watch?v=JcrcbkDGJuk&t=376s)** So that's a basic overview. I suppose of for YeHo. It's basically a local GitHub. Right. We're all familiar. I think at this point if you're watching this video at least with the idea of a code forge.

**[06:29](https://youtube.com/watch?v=JcrcbkDGJuk&t=389s)** Now what we want to do is spin up a brand new version and show you how to go about doing that. So like most projects on this channel. I'm going to reach for Docker to deploy this software.

**[06:40](https://youtube.com/watch?v=JcrcbkDGJuk&t=400s)** Mostly because we can just use the tail scale sidecar container method here to forward our SSH packets later on in order to have transparent SSH cloning working without having to specify a port number.

**[06:53](https://youtube.com/watch?v=JcrcbkDGJuk&t=413s)** It's a really nice little feature which we'll get to in just a minute. But you can see here as part of my standard Docker compose file. I have the tail scale standard. Right. This is just deploying the tail scale slash tail scale image.

**[07:05](https://youtube.com/watch?v=JcrcbkDGJuk&t=425s)** And we are then deploying for YeHo itself next. So here you can see we're actually cloning it from the Docker repository that lives at codeberg dot org.

**[07:16](https://youtube.com/watch?v=JcrcbkDGJuk&t=436s)** Codeberg of course are the company behind the nonprofit behind for YeHo. So we're pulling that Docker image down from codeberg directly.

**[07:24](https://youtube.com/watch?v=JcrcbkDGJuk&t=444s)** And then we're just linking it directly to the tail scale container up here. So you see where it says service for YeHo TS. That's where this links together. So essentially behind the scenes where we're merging the Linux networking name space of these two containers together.

**[07:40](https://youtube.com/watch?v=JcrcbkDGJuk&t=460s)** But they still maintain entirely separate user spaces so the package sets and everything else about the containers is entirely separate but they're basically inside the same networking name space. They have the same view of the network of the world inside the Linux kernel.

**[07:54](https://youtube.com/watch?v=JcrcbkDGJuk&t=474s)** You can see there's a few other things configured in here to like the root URL. Well, I'm going to show you how we can figure that in just a second. And then you've got some things like volumes to persist data outside the containers.

**[08:04](https://youtube.com/watch?v=JcrcbkDGJuk&t=484s)** And in our case, we don't actually need these ports because we're going to be using tail scale serve to expose this container.

**[08:11](https://youtube.com/watch?v=JcrcbkDGJuk&t=491s)** So let's take a look first of all at how we configure things like the environment variables. That's these things here. The four YeHo host name that word is going to trip me up all video. I'm sorry.

**[08:22](https://youtube.com/watch?v=JcrcbkDGJuk&t=502s)** And also how we configure the tail scale off key. So in this file here, the dot end file, this is where we configure the off key now to generate an

**[08:33](https://youtube.com/watch?v=JcrcbkDGJuk&t=513s)** off key. We have done this many times on the channel before but I will not assume anything. Let's go over to our tail scale admin console right here. You want to go to settings.

**[08:43](https://youtube.com/watch?v=JcrcbkDGJuk&t=523s)** I'm assuming you've already created a town and you're already logged in, of course, you go to settings and then keys and then generate an off key. I'm going to make mine reusable just in case I tell this up and down a few times in the purposes of making this video.

**[08:57](https://youtube.com/watch?v=JcrcbkDGJuk&t=537s)** You can add a tag if you want to. So if you want this for YeHo instance to only be available with a certain set of rules and parameters in your ACLs or your grants.

**[09:07](https://youtube.com/watch?v=JcrcbkDGJuk&t=547s)** This is where you would configure tags or you could even just make it an ephemeral node so that devices authenticated with this key get automatically removed when they go offline.

**[09:18](https://youtube.com/watch?v=JcrcbkDGJuk&t=558s)** I'm just going to leave this as the default except for reusable generate this key and then copy it to my clipboard. Once I put it on my clipboard, I will go back to VS code and replace the value of TS or key in my dot end file.

**[09:34](https://youtube.com/watch?v=JcrcbkDGJuk&t=574s)** Now you'll also want to make sure that your tail scale suffix is updated and how we do that is we go across to the app and console once again and we go to DNS.

**[09:44](https://youtube.com/watch?v=JcrcbkDGJuk&t=584s)** We need to do a couple of things at this point. We have to make sure that magic DNS is turned on number one and HTTPS certificates are turned on number two.

**[09:53](https://youtube.com/watch?v=JcrcbkDGJuk&t=593s)** And then from here, we can roll a new name for our tailnet by default. Every tailnet comes with a default name that looks something like this like tail six e blah blah blah.

**[10:03](https://youtube.com/watch?v=JcrcbkDGJuk&t=603s)** It's not very pretty but we provide a list of tailnets. You can roll like a randomized roll to pick something that has both a tail and scale.

**[10:12](https://youtube.com/watch?v=JcrcbkDGJuk&t=612s)** So in my case, a velociraptor and a noodle fish. Okay, so that's how we get that value right there. We've copied that to our clipboard, paste that in here and we are good to go.

**[10:23](https://youtube.com/watch?v=JcrcbkDGJuk&t=623s)** Now the only thing you've got left to change now is this option right here. So in my case, I've already got for YeHo on my tailnet and I want to deploy another one just for demo.

**[10:32](https://youtube.com/watch?v=JcrcbkDGJuk&t=632s)** So I'm just going to call this Git. You call it whatever you want but whatever it does, you have to make sure it matches the name that is specified here.

**[10:40](https://youtube.com/watch?v=JcrcbkDGJuk&t=640s)** So this online five is the name that the service will get when it is instantiated onto your tailnet. So this will be Git dot velociraptor high for noodle fish dot TS dot net.

**[10:53](https://youtube.com/watch?v=JcrcbkDGJuk&t=653s)** Because we specify that in the end file in just one spot, we don't then need to update it in two spots in this file later on.

**[11:01](https://youtube.com/watch?v=JcrcbkDGJuk&t=661s)** Now typically I issue the dot end option, the file option for it specifying environment variables.

**[11:08](https://youtube.com/watch?v=JcrcbkDGJuk&t=668s)** Because I don't find it makes a ton of sense to have one declarative file that is then dependent on another file elsewhere and I know there are varying schools of thought on this particular topic.

**[11:20](https://youtube.com/watch?v=JcrcbkDGJuk&t=680s)** But for me, at least I like to just keep everything in the compose YAML file because for YeHo itself has a huge number of environment variables that you can configure.

**[11:29](https://youtube.com/watch?v=JcrcbkDGJuk&t=689s)** And these all get passed through to the container underneath. So if you want to do a custom database, for example, you configure it through environment variables.

**[11:36](https://youtube.com/watch?v=JcrcbkDGJuk&t=696s)** If you want to change the app name, for example, you can change that in the environment variables to when it starts to get beyond sort of four or five or six lines of this stanza here.

**[11:47](https://youtube.com/watch?v=JcrcbkDGJuk&t=707s)** That for me is when it starts to make sense to break it out into a separate file and particularly if you're going to start reusing those values across multiple containers, like you would do if you had the four YeHo app and a separate database.

**[11:59](https://youtube.com/watch?v=JcrcbkDGJuk&t=719s)** For me, this is a single user instance. So I'm just going to use the default SQL light database that for YeHo ships with.

**[12:06](https://youtube.com/watch?v=JcrcbkDGJuk&t=726s)** But it supports, I believe, Postgres and a bunch of other stuff too.

**[12:09](https://youtube.com/watch?v=JcrcbkDGJuk&t=729s)** Okay, so I think we're good to go with the compose YAML file.

**[12:13](https://youtube.com/watch?v=JcrcbkDGJuk&t=733s)** Next thing I want to do is explain to you how we're going to expose not only port 3000, but also port 22 securely to our tailnet transparently so that folks can do get clone using for YeHo TS.net URL that we've created.

**[12:30](https://youtube.com/watch?v=JcrcbkDGJuk&t=750s)** So you'd have to specify a specific port.

**[12:33](https://youtube.com/watch?v=JcrcbkDGJuk&t=753s)** The magic source here today is this light of these three lines here, lines three, four, and five.

**[12:39](https://youtube.com/watch?v=JcrcbkDGJuk&t=759s)** We're going to use TCP forward to forward from the local host inside the container.

**[12:44](https://youtube.com/watch?v=JcrcbkDGJuk&t=764s)** Remember, it's all sort of merged in the Linux kernel underneath in the name, the networking namespace.

**[12:50](https://youtube.com/watch?v=JcrcbkDGJuk&t=770s)** So we're going to forward local host port 22 using TCP forwarding to the local host port 22.

**[12:58](https://youtube.com/watch?v=JcrcbkDGJuk&t=778s)** I know it's kind of confusing, but the traffic comes in over your tailnet and then gets redirected to local host inside that container, which is also the same networking namespace in which for YeHo lives.

**[13:09](https://youtube.com/watch?v=JcrcbkDGJuk&t=789s)** So essentially all that happens is the traffic comes in over tailscale lands inside that container and goes immediately to port 22 inside that networking namespace and it just works.

**[13:19](https://youtube.com/watch?v=JcrcbkDGJuk&t=799s)** We then do the same thing with port 3000 to expose on the root of the subdomain, the TS domain that you have.

**[13:27](https://youtube.com/watch?v=JcrcbkDGJuk&t=807s)** So what did we say get a velociraptor hyphen newtlefish.ts.net.

**[13:32](https://youtube.com/watch?v=JcrcbkDGJuk&t=812s)** This really is the magic source. I've seen for many years in compose files.

**[13:37](https://youtube.com/watch?v=JcrcbkDGJuk&t=817s)** I've had to expose ports like this and then when I do get clone, I have to do get clone get at get.com and then put port like this

**[13:48](https://youtube.com/watch?v=JcrcbkDGJuk&t=828s)** and then repository and then was it user and then repo dot get.

**[13:53](https://youtube.com/watch?v=JcrcbkDGJuk&t=833s)** Well, it might seem like a small detail to remove these few characters here.

**[13:58](https://youtube.com/watch?v=JcrcbkDGJuk&t=838s)** But what this means now is that by default all the SSH traffic traverses port 22, which is exactly where it should be as part of a get clone operation.

**[14:07](https://youtube.com/watch?v=JcrcbkDGJuk&t=847s)** So it really makes the overall user experience much much smoother.

**[14:13](https://youtube.com/watch?v=JcrcbkDGJuk&t=853s)** And now the final file I have to show you today is the LXC configuration. This is a pretty standard tailscale LXC configuration.

**[14:20](https://youtube.com/watch?v=JcrcbkDGJuk&t=860s)** All we really add to this file are these three lines right here.

**[14:24](https://youtube.com/watch?v=JcrcbkDGJuk&t=864s)** So let's make a start. Let's actually create ourselves a brand new LXC container at last.

**[14:30](https://youtube.com/watch?v=JcrcbkDGJuk&t=870s)** Let's do 10, 10 or something and we're going to call this get.

**[14:35](https://youtube.com/watch?v=JcrcbkDGJuk&t=875s)** It doesn't really matter what you call it so long as it makes sense to you.

**[14:40](https://youtube.com/watch?v=JcrcbkDGJuk&t=880s)** And I'm going to go through next. I'm going to speedrun this because I've done it many times on the channel before.

**[14:45](https://youtube.com/watch?v=JcrcbkDGJuk&t=885s)** 8 gig should be fine. Although actually this is going to be hosting all of our get data. Isn't it?

**[14:50](https://youtube.com/watch?v=JcrcbkDGJuk&t=890s)** So let's make it 50 gig just in case couple of CPUs. Yeah, that should be fine.

**[14:55](https://youtube.com/watch?v=JcrcbkDGJuk&t=895s)** Anything intensive. Remember, we're going to be doing with runners, which will have a hot.

**[14:59](https://youtube.com/watch?v=JcrcbkDGJuk&t=899s)** I suppose you could run the runners inside this LXC if he wanted to, but separation of concerns it might make sense to run the runners in a separate LXC.

**[15:08](https://youtube.com/watch?v=JcrcbkDGJuk&t=908s)** We'll get on to that later. Don't worry about that in a future video. Not this one.

**[15:12](https://youtube.com/watch?v=JcrcbkDGJuk&t=912s)** Memory 2 gig totally fine. Mem network network. Yet we'll do DHCP DNS.

**[15:21](https://youtube.com/watch?v=JcrcbkDGJuk&t=921s)** We're going to use the host settings and then I'm not going to click start after created because I want to copy in these three lines into the configuration of the LXC that just got created.

**[15:32](https://youtube.com/watch?v=JcrcbkDGJuk&t=932s)** So back in Proxmox, I'm going to go to the node itself in question. PvE is the name of the node in question.

**[15:39](https://youtube.com/watch?v=JcrcbkDGJuk&t=939s)** By the way, this is just running on one of those little one liter Dell PCs that I use for the self hosting series a few weeks ago.

**[15:44](https://youtube.com/watch?v=JcrcbkDGJuk&t=944s)** It's just running on that rack just out of shot down there. So you really don't need much in the way of resources to do this.

**[15:50](https://youtube.com/watch?v=JcrcbkDGJuk&t=950s)** You know, you could do this on the Raspberry Pi if you wanted to.

**[15:53](https://youtube.com/watch?v=JcrcbkDGJuk&t=953s)** But we need to put these lines into our LXC configuration.

**[15:56](https://youtube.com/watch?v=JcrcbkDGJuk&t=956s)** So we go to ETC slash PvE LXC and then we do 1010.conf.

**[16:03](https://youtube.com/watch?v=JcrcbkDGJuk&t=963s)** Jump to the bottom of the file with shift G press O to insert or going to insert mode at the bottom and then just paste these two lines in.

**[16:12](https://youtube.com/watch?v=JcrcbkDGJuk&t=972s)** This is so that tailscale can run and bind to the DevNet Tun device.

**[16:16](https://youtube.com/watch?v=JcrcbkDGJuk&t=976s)** So now we can do PCT start 1010 followed swiftly by PCT exec 1010 and then I'm going to jump into bash inside that container.

**[16:27](https://youtube.com/watch?v=JcrcbkDGJuk&t=987s)** So we're now we are now inside look you see the host name change to get we are now inside the LXC container.

**[16:35](https://youtube.com/watch?v=JcrcbkDGJuk&t=995s)** So you want to think of it like a true route or something like that you can if that helps you understand it better.

**[16:39](https://youtube.com/watch?v=JcrcbkDGJuk&t=999s)** But we are now inside the physical constraints of the LXC container get with the ID 1010.

**[16:46](https://youtube.com/watch?v=JcrcbkDGJuk&t=1006s)** So I want to do a few things now I'm not on the host anymore remember.

**[16:49](https://youtube.com/watch?v=JcrcbkDGJuk&t=1009s)** So I've got to make sure that my package sets are all up to date with at update and at upgrade.

**[16:54](https://youtube.com/watch?v=JcrcbkDGJuk&t=1014s)** The next thing you're going to want to do is go to tailscale.com slash download and download tailscale from our website.

**[17:03](https://youtube.com/watch?v=JcrcbkDGJuk&t=1023s)** Click on Linux and then copy this command to your clipboard and change back to the correct tab.

**[17:09](https://youtube.com/watch?v=JcrcbkDGJuk&t=1029s)** When this is finished updating the packages the next thing we're going to want to do is to install tailscale.

**[17:14](https://youtube.com/watch?v=JcrcbkDGJuk&t=1034s)** Now I know for a fact that Debbie and doesn't come out of the box with curl installed.

**[17:18](https://youtube.com/watch?v=JcrcbkDGJuk&t=1038s)** So I'm going to install curl manually first with an apt install curl.

**[17:22](https://youtube.com/watch?v=JcrcbkDGJuk&t=1042s)** And then I'm going to paste in the one line tailscale install script.

**[17:26](https://youtube.com/watch?v=JcrcbkDGJuk&t=1046s)** I then want to do the same thing with docker.

**[17:29](https://youtube.com/watch?v=JcrcbkDGJuk&t=1049s)** So I'm going to go to get docker.com and verify that this script is what I think it is the docker install script.

**[17:36](https://youtube.com/watch?v=JcrcbkDGJuk&t=1056s)** I'm just going to grab this URL right here.

**[17:39](https://youtube.com/watch?v=JcrcbkDGJuk&t=1059s)** And I'm going to then modify the tailscale install command because I kind of like just piping it to root like this.

**[17:47](https://youtube.com/watch?v=JcrcbkDGJuk&t=1067s)** Now remember there are some security concerns about piping things to root scripts from the random scripts from the internet.

**[17:55](https://youtube.com/watch?v=JcrcbkDGJuk&t=1075s)** But we've literally just verified the contents of the get docker script.

**[18:00](https://youtube.com/watch?v=JcrcbkDGJuk&t=1080s)** So I think we're good to go.

**[18:02](https://youtube.com/watch?v=JcrcbkDGJuk&t=1082s)** So we've installed tailscale now and we're going to install docker next.

**[18:07](https://youtube.com/watch?v=JcrcbkDGJuk&t=1087s)** Before we reboot I want to get this node onto my tailnet.

**[18:11](https://youtube.com/watch?v=JcrcbkDGJuk&t=1091s)** Now I already had an off key remember which I set to reusable.

**[18:15](https://youtube.com/watch?v=JcrcbkDGJuk&t=1095s)** So I'm going to go back to my VS code and go back to my end file and just grab this off key right here.

**[18:22](https://youtube.com/watch?v=JcrcbkDGJuk&t=1102s)** Because I'm going to do tailscale up and last week I made a video about seven things you can do with the tailscale command line.

**[18:29](https://youtube.com/watch?v=JcrcbkDGJuk&t=1109s)** I put a link to that one right up here and I'm going to tailscale up dash dash SSH and then dash dash off key.

**[18:37](https://youtube.com/watch?v=JcrcbkDGJuk&t=1117s)** I think it's I think it's that and then paste that in like that.

**[18:40](https://youtube.com/watch?v=JcrcbkDGJuk&t=1120s)** And this is going to authenticate this node to my tailnet with no QR codes with no clicking links and signing into things.

**[18:47](https://youtube.com/watch?v=JcrcbkDGJuk&t=1127s)** Just using my off key to authenticate this node to tailscale as you can see.

**[18:52](https://youtube.com/watch?v=JcrcbkDGJuk&t=1132s)** I can now do tailscale status and I'm connected to my tailnet how cool is that.

**[18:58](https://youtube.com/watch?v=JcrcbkDGJuk&t=1138s)** Okay before we go any further I want to reboot the LXC to make sure any of the package changes that we made stick.

**[19:04](https://youtube.com/watch?v=JcrcbkDGJuk&t=1144s)** And then just to make it a little clearer for you watching.

**[19:07](https://youtube.com/watch?v=JcrcbkDGJuk&t=1147s)** I'm going to log in to the container in its own separate shell rather than doing the exact kind of thing.

**[19:12](https://youtube.com/watch?v=JcrcbkDGJuk&t=1152s)** So now the next thing I'm going to do is just verify that docker is installed and working.

**[19:17](https://youtube.com/watch?v=JcrcbkDGJuk&t=1157s)** Yes hello from docker so we have tailscale installed.

**[19:22](https://youtube.com/watch?v=JcrcbkDGJuk&t=1162s)** We have docker installed and running.

**[19:25](https://youtube.com/watch?v=JcrcbkDGJuk&t=1165s)** We are now ready to go and not only do we have tailscale installed we've got tailscale with tailscale SSH ready to go.

**[19:31](https://youtube.com/watch?v=JcrcbkDGJuk&t=1171s)** Which brings me to my grand reveal.

**[19:34](https://youtube.com/watch?v=JcrcbkDGJuk&t=1174s)** I have spent countless hours with Claude writing a little script here to make the deployment of this container as easy as I possibly could.

**[19:45](https://youtube.com/watch?v=JcrcbkDGJuk&t=1185s)** So you want to change into the 2025 09 for yeHo directory.

**[19:50](https://youtube.com/watch?v=JcrcbkDGJuk&t=1190s)** I'm already in that directory as you can see.

**[19:53](https://youtube.com/watch?v=JcrcbkDGJuk&t=1193s)** And then you really want to just run setup.sh and then get or whatever the name of the node that you put in your tailnet was.

**[20:02](https://youtube.com/watch?v=JcrcbkDGJuk&t=1202s)** So in my case the name here of the machine is get so I should let me just test that by doing pseudo root at get.

**[20:11](https://youtube.com/watch?v=JcrcbkDGJuk&t=1211s)** So if I now do dot slash setup dot sh and then do get this is going to go out over SSH and target the node on your tailnet named get.

**[20:22](https://youtube.com/watch?v=JcrcbkDGJuk&t=1222s)** It's going to copy across the compose.yaml and the serve.json file as well as the dot end file.

**[20:29](https://youtube.com/watch?v=JcrcbkDGJuk&t=1229s)** And now if we SSH to that remote node with SSH root at get we can see that I can get in here.

**[20:36](https://youtube.com/watch?v=JcrcbkDGJuk&t=1236s)** But also if I do ID for yeHo there's now a brand new user created on this host too.

**[20:42](https://youtube.com/watch?v=JcrcbkDGJuk&t=1242s)** Because one of the things that for yeHo doesn't like is trying to run as root.

**[20:46](https://youtube.com/watch?v=JcrcbkDGJuk&t=1246s)** So we create inside the LXC a non root user.

**[20:49](https://youtube.com/watch?v=JcrcbkDGJuk&t=1249s)** And in fact we can go there by doing SU for yeHo.

**[20:53](https://youtube.com/watch?v=JcrcbkDGJuk&t=1253s)** We also add this user to the docker group as far I can show you that here.

**[20:57](https://youtube.com/watch?v=JcrcbkDGJuk&t=1257s)** This uses part of the docker group.

**[20:59](https://youtube.com/watch?v=JcrcbkDGJuk&t=1259s)** So we can just go into the container structure that gets created into the for yeHo directory that gets created.

**[21:05](https://youtube.com/watch?v=JcrcbkDGJuk&t=1265s)** And do a docker compose up.

**[21:08](https://youtube.com/watch?v=JcrcbkDGJuk&t=1268s)** This is going to pull down the tail scale for yeHo container.

**[21:11](https://youtube.com/watch?v=JcrcbkDGJuk&t=1271s)** And also the for yeHo app server container.

**[21:15](https://youtube.com/watch?v=JcrcbkDGJuk&t=1275s)** It's going to instantiate the tail scale one and put that container onto townnet.

**[21:20](https://youtube.com/watch?v=JcrcbkDGJuk&t=1280s)** And then make the for yeHo container available on your townnet by virtue of being merged together

**[21:26](https://youtube.com/watch?v=JcrcbkDGJuk&t=1286s)** with the network mode standard as part of your compose file.

**[21:29](https://youtube.com/watch?v=JcrcbkDGJuk&t=1289s)** That really is all there is to it.

**[21:31](https://youtube.com/watch?v=JcrcbkDGJuk&t=1291s)** You can see the app root URL here is set to get at the velociraptor high for noodle fish.

**[21:36](https://youtube.com/watch?v=JcrcbkDGJuk&t=1296s)** We can see it doesn't work.

**[21:37](https://youtube.com/watch?v=JcrcbkDGJuk&t=1297s)** And that's because I made a bit of an error earlier on.

**[21:40](https://youtube.com/watch?v=JcrcbkDGJuk&t=1300s)** So I've accidentally ended up with two nodes here with kind of the same name.

**[21:45](https://youtube.com/watch?v=JcrcbkDGJuk&t=1305s)** And I confused myself a little bit and probably you in the process.

**[21:49](https://youtube.com/watch?v=JcrcbkDGJuk&t=1309s)** So I'm going to leave this what in the video because you've told me in the past.

**[21:53](https://youtube.com/watch?v=JcrcbkDGJuk&t=1313s)** You like it when I show my working and show my mistakes like my third grade math teacher did.

**[21:59](https://youtube.com/watch?v=JcrcbkDGJuk&t=1319s)** And I've named the LXC container Git.

**[22:03](https://youtube.com/watch?v=JcrcbkDGJuk&t=1323s)** I've also named the for yeHo container Git.

**[22:06](https://youtube.com/watch?v=JcrcbkDGJuk&t=1326s)** And when tail scale detects that it puts two nodes on the tail net.

**[22:10](https://youtube.com/watch?v=JcrcbkDGJuk&t=1330s)** But it's sort of numbers one of them.

**[22:12](https://youtube.com/watch?v=JcrcbkDGJuk&t=1332s)** So I'm literally just going to rename the LXC to LXC Git.

**[22:17](https://youtube.com/watch?v=JcrcbkDGJuk&t=1337s)** So that I know that this is kind of like the host.

**[22:20](https://youtube.com/watch?v=JcrcbkDGJuk&t=1340s)** And then I'm going to rename the node that is the container that's running for yeHo just to Git.

**[22:28](https://youtube.com/watch?v=JcrcbkDGJuk&t=1348s)** And now I need to restart the applications underneath so that they pick up everything properly

**[22:34](https://youtube.com/watch?v=JcrcbkDGJuk&t=1354s)** in terms of rooting for tail scale server and what have you.

**[22:38](https://youtube.com/watch?v=JcrcbkDGJuk&t=1358s)** And so now that I've renamed that node, what I want to do is go and click on the drop down here.

**[22:42](https://youtube.com/watch?v=JcrcbkDGJuk&t=1362s)** Click on this Git.Volosser Raptor, high for noodle fish.

**[22:45](https://youtube.com/watch?v=JcrcbkDGJuk&t=1365s)** It's just known as your fully qualified domain name.

**[22:48](https://youtube.com/watch?v=JcrcbkDGJuk&t=1368s)** And paste that into my browser.

**[22:50](https://youtube.com/watch?v=JcrcbkDGJuk&t=1370s)** And you can see I'm greeted with the default welcome script.

**[22:53](https://youtube.com/watch?v=JcrcbkDGJuk&t=1373s)** Now in the background, this may take a minute or two for the first time as it loads up the search.

**[22:57](https://youtube.com/watch?v=JcrcbkDGJuk&t=1377s)** You can see that it actually goes out and automatically does all the TLS stuff.

**[23:02](https://youtube.com/watch?v=JcrcbkDGJuk&t=1382s)** So it goes out to let's encrypt, generate the required certificates and make sure that you don't have to worry about any of that stuff.

**[23:09](https://youtube.com/watch?v=JcrcbkDGJuk&t=1389s)** This just works magically in the background.

**[23:12](https://youtube.com/watch?v=JcrcbkDGJuk&t=1392s)** And you can see here that this is currently going to be titled for yeHo.

**[23:15](https://youtube.com/watch?v=JcrcbkDGJuk&t=1395s)** Let's call this tailscales awesome Git server.

**[23:19](https://youtube.com/watch?v=JcrcbkDGJuk&t=1399s)** And then we'll just leave all of this other stuff alone except for where it says to create an administrator account.

**[23:26](https://youtube.com/watch?v=JcrcbkDGJuk&t=1406s)** So username, I was going to pick z4d and I don't think this is a real username.

**[23:32](https://youtube.com/watch?v=JcrcbkDGJuk&t=1412s)** Though if if I if I ever meet anybody called z4d, I'll be like your parents had good taste.

**[23:38](https://youtube.com/watch?v=JcrcbkDGJuk&t=1418s)** And then I'm going to click on install for yeHo.

**[23:41](https://youtube.com/watch?v=JcrcbkDGJuk&t=1421s)** And the application underneath is going to go away and do its thing.

**[23:45](https://youtube.com/watch?v=JcrcbkDGJuk&t=1425s)** And you know, you might see in the logs it goes through and does a bunch of stuff in the background.

**[23:49](https://youtube.com/watch?v=JcrcbkDGJuk&t=1429s)** That's good.

**[23:51](https://youtube.com/watch?v=JcrcbkDGJuk&t=1431s)** Before before too long you'll be presented with a brand new completely empty instance of for yeHo.

**[23:58](https://youtube.com/watch?v=JcrcbkDGJuk&t=1438s)** So let's create a new repository and just call this one.

**[24:01](https://youtube.com/watch?v=JcrcbkDGJuk&t=1441s)** I don't know.

**[24:02](https://youtube.com/watch?v=JcrcbkDGJuk&t=1442s)** One, two, three, four.

**[24:04](https://youtube.com/watch?v=JcrcbkDGJuk&t=1444s)** I'm going to initialize it with a blank file and MIT license because it's very important to have a license on an empty repo.

**[24:11](https://youtube.com/watch?v=JcrcbkDGJuk&t=1451s)** And then I want to show you how here because of the environment variables that we've set up in our compose file, namely

**[24:20](https://youtube.com/watch?v=JcrcbkDGJuk&t=1460s)** the root URL and the SSH domain, we get the correct stuff here.

**[24:26](https://youtube.com/watch?v=JcrcbkDGJuk&t=1466s)** And there's no extra ports have to be declared at all.

**[24:28](https://youtube.com/watch?v=JcrcbkDGJuk&t=1468s)** So if I want to clone this repo now, I'm going to show you this will fail to start with.

**[24:33](https://youtube.com/watch?v=JcrcbkDGJuk&t=1473s)** And that's by design.

**[24:35](https://youtube.com/watch?v=JcrcbkDGJuk&t=1475s)** I'm going to go into this temp directory here where I clone all sorts of junk and put this in here.

**[24:41](https://youtube.com/watch?v=JcrcbkDGJuk&t=1481s)** And it's going to fail because I haven't set up the SSH keys.

**[24:44](https://youtube.com/watch?v=JcrcbkDGJuk&t=1484s)** Now one of the one of the things I was hoping to be able to do as part of this video was reuse the tail scale identity

**[24:49](https://youtube.com/watch?v=JcrcbkDGJuk&t=1489s)** and tail scale SSH to do that as part of SSH clones.

**[24:53](https://youtube.com/watch?v=JcrcbkDGJuk&t=1493s)** Unfortunately, that would have involved some upstreaming of a bunch of stuff.

**[24:57](https://youtube.com/watch?v=JcrcbkDGJuk&t=1497s)** And I just didn't have the time to do that as part of this video.

**[25:00](https://youtube.com/watch?v=JcrcbkDGJuk&t=1500s)** So for now, I suppose it's still not that terrible of a situation.

**[25:04](https://youtube.com/watch?v=JcrcbkDGJuk&t=1504s)** We're just going to have to use the existing SSH keys that we have for our nodes.

**[25:08](https://youtube.com/watch?v=JcrcbkDGJuk&t=1508s)** Now you can see this is my public SSH key.

**[25:11](https://youtube.com/watch?v=JcrcbkDGJuk&t=1511s)** And I'm going to put this on my clipboard on macOS by piping it to PB copy.

**[25:16](https://youtube.com/watch?v=JcrcbkDGJuk&t=1516s)** Much like you would do on GitHub, I'm going to go to the user zafod and settings and then SSH keys.

**[25:23](https://youtube.com/watch?v=JcrcbkDGJuk&t=1523s)** When I put that in here, it's going to detect that it's for ball trick which is this laptop on the desk in front of me.

**[25:29](https://youtube.com/watch?v=JcrcbkDGJuk&t=1529s)** I'm going to add this key.

**[25:31](https://youtube.com/watch?v=JcrcbkDGJuk&t=1531s)** Now when I go back and try and clone this repo again, you'll see that it just works.

**[25:35](https://youtube.com/watch?v=JcrcbkDGJuk&t=1535s)** So what's happening there is the SSH stuff comes from this laptop, goes out over tail scale,

**[25:41](https://youtube.com/watch?v=JcrcbkDGJuk&t=1541s)** admittedly just to the computer behind me and this rack just behind me.

**[25:45](https://youtube.com/watch?v=JcrcbkDGJuk&t=1545s)** But I could take this laptop anywhere in the world right now and then still clone with no extra port configuration,

**[25:52](https://youtube.com/watch?v=JcrcbkDGJuk&t=1552s)** no reverse proxies, no ports open in my firewall, none of that.

**[25:56](https://youtube.com/watch?v=JcrcbkDGJuk&t=1556s)** And I can just clone stuff over tail scale from my locally self hosted for YeHo instance.

**[26:03](https://youtube.com/watch?v=JcrcbkDGJuk&t=1563s)** It is wonderful and it's a really simple thing to have your own self hosted GitForge.

**[26:10](https://youtube.com/watch?v=JcrcbkDGJuk&t=1570s)** But why not? We can, self hosting's never been easier to get into and I hope today's video

**[26:16](https://youtube.com/watch?v=JcrcbkDGJuk&t=1576s)** a little bit involved as it was with some of the stuff with spinning up the Alexi and renaming things.

**[26:22](https://youtube.com/watch?v=JcrcbkDGJuk&t=1582s)** I hope today's video gave you another taste of some of the things you can do with tail scale

**[26:27](https://youtube.com/watch?v=JcrcbkDGJuk&t=1587s)** and how you can own your own data and be in full control of everything that's going on.

**[26:31](https://youtube.com/watch?v=JcrcbkDGJuk&t=1591s)** There's no business model at play here other than for YeHo and code bugs,

**[26:36](https://youtube.com/watch?v=JcrcbkDGJuk&t=1596s)** non-profit business model. It's you own it, right?

**[26:40](https://youtube.com/watch?v=JcrcbkDGJuk&t=1600s)** This, ostensibly you can continue to run this piece of software until the end of time in its current guys.

**[26:46](https://youtube.com/watch?v=JcrcbkDGJuk&t=1606s)** I mean, the world around it would move on and eventually it would become a problem.

**[26:50](https://youtube.com/watch?v=JcrcbkDGJuk&t=1610s)** But certainly for many, many years you can standardize around self hosted software

**[26:54](https://youtube.com/watch?v=JcrcbkDGJuk&t=1614s)** and it will just keep trucking, it will just keep working.

**[26:57](https://youtube.com/watch?v=JcrcbkDGJuk&t=1617s)** So if you haven't already, by the way, I highly encourage you to go over to our brand new Discord server

**[27:03](https://youtube.com/watch?v=JcrcbkDGJuk&t=1623s)** at discord.gg slash tail scale.

**[27:06](https://youtube.com/watch?v=JcrcbkDGJuk&t=1626s)** Our wonderful community over there is growing by the day.

**[27:09](https://youtube.com/watch?v=JcrcbkDGJuk&t=1629s)** We're going to have live streams and all sorts of community hangouts over the coming weeks.

**[27:13](https://youtube.com/watch?v=JcrcbkDGJuk&t=1633s)** So please go over there, join discord.gg slash tail scale.

**[27:17](https://youtube.com/watch?v=JcrcbkDGJuk&t=1637s)** Now thank you so much for watching and until next time, I've been Alex from tail scale.

---

*Automatically generated transcript. May contain errors.*
