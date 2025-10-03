---
video_id: "e-X5FJwrkaA"
title: "How to use cloud-init and Tailscale | Infrastructure as Code Series Part 1"
description: "In today's video Alex walks you through the process of creating a Digitalocean droplet cloud instance and pre-configuring it to be a tailnet node using cloud-init.

This is part 1 in a series examinin..."
channel_name: "Tailscale"
channel_id: "UCcdv38QxPjSMqbt5ffLhJLA"
published_at: "2024-08-02"
duration_seconds: 563
youtube_url: "https://www.youtube.com/watch?v=e-X5FJwrkaA"
thumbnail_url: "https://i.ytimg.com/vi/e-X5FJwrkaA/maxresdefault.jpg"

# Transcription metadata
transcribed_at: "2025-10-03T16:07:57.615596"
transcription_method: "cpu"
model_used: "base"
language: "en"
word_count: 1867
transcription_time_seconds: 15.8
---

# How to use cloud-init and Tailscale | Infrastructure as Code Series Part 1

**[00:00](https://youtube.com/watch?v=e-X5FJwrkaA&t=0s)** Hi, I'm Alex from Tailscale, and welcome into today's video, where we're going to talk about cloud in it. This is a technology that lets you pre-configure virtual machines that are going to spin up in the cloud just by providing a few lines of text. In this video, which is the first in a series that we're going to put together over the next few weeks, we're going to manually configure a virtual machine on digital ocean. In the next video, we're going to cover deploying that machine with Terraform, and after that, we'll move on to Ansible.

**[00:30](https://youtube.com/watch?v=e-X5FJwrkaA&t=30s)** So let's take a moment just to talk about what cloud in it is first. It's a tool used mostly by folks in the sort of DevOps space who want to automate the creation of infrastructure, specifically virtual machines that they want to create certain users or perform or run certain scripts when the machines created as part of the initial boot process.

**[01:00](https://youtube.com/watch?v=e-X5FJwrkaA&t=60s)** Cloud in it was originally a canonical project, the company behind Ubuntu, but more recently, it's now a fully open source project and distribution agnostic. So in today's video, I'm going to walk you through the process of creating a virtual machine or a droplets as they call it on digital ocean. These droplets support the injection of cloud in it configuration in what's called the user data field.

**[01:21](https://youtube.com/watch?v=e-X5FJwrkaA&t=81s)** You can provide this text just by copying and pasting it into the digital ocean interface. So let's jump in and take a look. Now, I've already gone ahead and got logged into my digital ocean account over here. And I'm going to click on the green create button up in the top right hand corner and create a droplet.

**[01:37](https://youtube.com/watch?v=e-X5FJwrkaA&t=97s)** Now, there's a few things to pay attention to here. First of all, I should note, we're going to do everything in this next few minutes manually.

**[01:44](https://youtube.com/watch?v=e-X5FJwrkaA&t=104s)** I'm going to do automation with terraform and Ansible later on in this video series, but today everything is manual. So we'll need to pick a region. I'm just going to pick New York because that happens to be closest to my geographic location, but where you put this.

**[01:57](https://youtube.com/watch?v=e-X5FJwrkaA&t=117s)** Kind of matters a little bit like I don't want to put it in Sydney if I live in the northern hemisphere, for example, but any of these US data centers or a European one, if you're in, you know, Europe or the UK or something should suffice in terms of latency.

**[02:10](https://youtube.com/watch?v=e-X5FJwrkaA&t=130s)** So just pick something that makes sense to you in this list. Next, we're going to want to go ahead and pick an OS. I almost always just pick Ubuntu's latest LTS, which in this case is 24.04.

**[02:21](https://youtube.com/watch?v=e-X5FJwrkaA&t=141s)** Then I'm going to go ahead and select the type of droplet that I want to create. In my case, we don't need the $32 a month one. All we're going to need is a basic $6 a month droplet down here. That also fights for our needs today.

**[02:35](https://youtube.com/watch?v=e-X5FJwrkaA&t=155s)** Next up, I've already created an SSH key on my digital ocean accounts, although this is entirely unnecessary if you're using tail scale SSH.

**[02:44](https://youtube.com/watch?v=e-X5FJwrkaA&t=164s)** What I will say is if you don't select an SSH key here and you go and try and connect to the virtual machine in the digital ocean console, you'll be asked to create a password.

**[02:53](https://youtube.com/watch?v=e-X5FJwrkaA&t=173s)** So it is advisable probably to just have an SSH key there because creating a root password manually feels a little bit draconian.

**[03:02](https://youtube.com/watch?v=e-X5FJwrkaA&t=182s)** Next, we're going to give this one a name. I'm just going to call this one banana and then under the advanced options just up here.

**[03:09](https://youtube.com/watch?v=e-X5FJwrkaA&t=189s)** This is where the magic happens. So if we click on this ad initialization scripts option, we want to paste in our cloud init stanza into this text box.

**[03:18](https://youtube.com/watch?v=e-X5FJwrkaA&t=198s)** So I'm going to jump back over to the tail scale knowledge base article, scroll down a little bit and then just literally copy and paste this entire cloud config block here.

**[03:28](https://youtube.com/watch?v=e-X5FJwrkaA&t=208s)** You should note that this header here, the hashtag cloud config must remain intact.

**[03:35](https://youtube.com/watch?v=e-X5FJwrkaA&t=215s)** This is the keyword that must appear as part of the beginning of a cloud init stanza.

**[03:40](https://youtube.com/watch?v=e-X5FJwrkaA&t=220s)** Next, we're going to need to go over to tailscale.com and generate our auth key. This is the case of just going to tailscale.com, our admin console, click on settings, click on personal settings down here in keys.

**[03:52](https://youtube.com/watch?v=e-X5FJwrkaA&t=232s)** I am going to generate an auth key. I'm just going to call this one banana, but the name is not important reusable. Yes, why not? Because it's a demo.

**[04:01](https://youtube.com/watch?v=e-X5FJwrkaA&t=241s)** If emeral, no, I don't really care about that for this and tags. If you want to, you can go ahead and set up a tag. This is defined in your ACLs.

**[04:08](https://youtube.com/watch?v=e-X5FJwrkaA&t=248s)** By the way, if you don't see these tags, you need to go ahead and create them in your ACLs as it tells you down here.

**[04:14](https://youtube.com/watch?v=e-X5FJwrkaA&t=254s)** You do that by clicking on the access controls tab here and defining the tags in your ACLs just here.

**[04:21](https://youtube.com/watch?v=e-X5FJwrkaA&t=261s)** That isn't important for this demo, so I'm just going to leave that alone. Then 90 days, that's plenty for what we want to do today.

**[04:28](https://youtube.com/watch?v=e-X5FJwrkaA&t=268s)** So generate the key, copy that to my clipboard, go back to my digital ocean tab, and then just paste in this line just here.

**[04:38](https://youtube.com/watch?v=e-X5FJwrkaA&t=278s)** Nope, I need to leave the auth key equals, don't I? There we go.

**[04:44](https://youtube.com/watch?v=e-X5FJwrkaA&t=284s)** Now, there's a few things going on in this cloud config file, but we are largely done at this point.

**[04:49](https://youtube.com/watch?v=e-X5FJwrkaA&t=289s)** You can see that, first of all, this cloud config file under this run command option here. It's downloading and installing tail scale.

**[04:57](https://youtube.com/watch?v=e-X5FJwrkaA&t=297s)** Then it's setting up IPv forwarding using ctl. This is so that if you want to use this node as an exit node or do some kind of subnet routing,

**[05:05](https://youtube.com/watch?v=e-X5FJwrkaA&t=305s)** the Linux kernel is able to forward TCP packets.

**[05:09](https://youtube.com/watch?v=e-X5FJwrkaA&t=309s)** Next up, we're going to authenticate this node to our tail net and then enable tail scale SSH.

**[05:14](https://youtube.com/watch?v=e-X5FJwrkaA&t=314s)** And finally, request to advertise this node as an exit node.

**[05:18](https://youtube.com/watch?v=e-X5FJwrkaA&t=318s)** Now, I'm going to go ahead and click on create droplet. And I'll be back in just a second when it's finished provisioning.

**[05:23](https://youtube.com/watch?v=e-X5FJwrkaA&t=323s)** Now, on the right hand side over here, I just want to click on console.

**[05:26](https://youtube.com/watch?v=e-X5FJwrkaA&t=326s)** And this can take a couple of minutes for the VM to kind of boot up and warm up.

**[05:30](https://youtube.com/watch?v=e-X5FJwrkaA&t=330s)** And once that has happened, I can click on that console button and be dropped into a shell in my browser for this remote virtual machine.

**[05:38](https://youtube.com/watch?v=e-X5FJwrkaA&t=338s)** And we should be able to see that tail scale is actually already installed on this VM because of the cloud init stuff that we set up earlier.

**[05:45](https://youtube.com/watch?v=e-X5FJwrkaA&t=345s)** And as you can see, banana is now a member of my tail net.

**[05:49](https://youtube.com/watch?v=e-X5FJwrkaA&t=349s)** So if we go over here back to my tail scale console, go to machines, we can indeed see that banana has been set up.

**[05:56](https://youtube.com/watch?v=e-X5FJwrkaA&t=356s)** Also note that SSH has been requested and also has the exit node functionality as well.

**[06:02](https://youtube.com/watch?v=e-X5FJwrkaA&t=362s)** So we could now use this virtual machine. We didn't have to type anything.

**[06:06](https://youtube.com/watch?v=e-X5FJwrkaA&t=366s)** Well, we had to copy and paste our auth key, but we didn't have to do any apt-get install or curling scripts or what have you.

**[06:12](https://youtube.com/watch?v=e-X5FJwrkaA&t=372s)** It was all handled by that cloud init stuff that we copied and pasted from the knowledge base for tail scale earlier.

**[06:19](https://youtube.com/watch?v=e-X5FJwrkaA&t=379s)** You could append any other arguments that you would like here.

**[06:21](https://youtube.com/watch?v=e-X5FJwrkaA&t=381s)** Anything else that you would pass to the tail scale set command, you can string these together into just one line if you would like to.

**[06:28](https://youtube.com/watch?v=e-X5FJwrkaA&t=388s)** And it's worth noting that I'll put a link to this documentation down in the description down below.

**[06:32](https://youtube.com/watch?v=e-X5FJwrkaA&t=392s)** Now doing things manually isn't really the point of cloud init.

**[06:36](https://youtube.com/watch?v=e-X5FJwrkaA&t=396s)** We want to start automating this stuff.

**[06:38](https://youtube.com/watch?v=e-X5FJwrkaA&t=398s)** And so in the next couple of videos, we're going to show you how to do this using Terraform and Ansible as well.

**[06:43](https://youtube.com/watch?v=e-X5FJwrkaA&t=403s)** But here's a quick sneak peek at the Terraform stuff.

**[06:46](https://youtube.com/watch?v=e-X5FJwrkaA&t=406s)** So one of the key principles of infrastructure as code is that we can define our entire infrastructure in a text file or something that we can commit to a Git repo somewhere.

**[06:56](https://youtube.com/watch?v=e-X5FJwrkaA&t=416s)** I'll put it in source control. I'll put a link in the description down below if you'd like to get started with Terraform and also keep an eye out for the video that's coming in the next week or two.

**[07:05](https://youtube.com/watch?v=e-X5FJwrkaA&t=425s)** To deploy a machine with tail scale pre-installed and Docker pre-installed in my case to digital ocean is just as simple as typing Terraform apply and then enter a value.

**[07:17](https://youtube.com/watch?v=e-X5FJwrkaA&t=437s)** Yes, in order to actually go ahead and have Terraform perform those steps.

**[07:21](https://youtube.com/watch?v=e-X5FJwrkaA&t=441s)** And so what we'll see if we jump back to digital ocean is we will see in my main dev project over here.

**[07:28](https://youtube.com/watch?v=e-X5FJwrkaA&t=448s)** We will see that now there is a new virtual machine being created by Terraform noting the background down here.

**[07:34](https://youtube.com/watch?v=e-X5FJwrkaA&t=454s)** It's still creating it says 10 seconds elapsed.

**[07:37](https://youtube.com/watch?v=e-X5FJwrkaA&t=457s)** This is creating via the API Terraform is creating on digital ocean a new virtual machine automatically with the cloud init stuff pre-populated,

**[07:47](https://youtube.com/watch?v=e-X5FJwrkaA&t=467s)** with my off key with my digital ocean API token is able to go and create those resources for me in the cloud.

**[07:55](https://youtube.com/watch?v=e-X5FJwrkaA&t=475s)** So what we could start to do with this is in part of CI environment, we could actually start to sprinkle this stuff into GitHub actions or Jenkins workflows or whatever you're using for CI these days.

**[08:07](https://youtube.com/watch?v=e-X5FJwrkaA&t=487s)** We can do this stuff programmatically.

**[08:09](https://youtube.com/watch?v=e-X5FJwrkaA&t=489s)** And so I just like to double check that everything went okay with my automation.

**[08:13](https://youtube.com/watch?v=e-X5FJwrkaA&t=493s)** One of the easiest ways to do this is to jump into the console of the virtual machine and just try and execute a couple of commands.

**[08:18](https://youtube.com/watch?v=e-X5FJwrkaA&t=498s)** So I'm going to jump back to the console of the digital ocean droplet type tail scale status and we will see that this node is now already on my tailnet.

**[08:27](https://youtube.com/watch?v=e-X5FJwrkaA&t=507s)** And what this means is that this node that's in a data center in New York somewhere can now talk to any other node on my tailnet as if it was in the same land.

**[08:36](https://youtube.com/watch?v=e-X5FJwrkaA&t=516s)** So I'm just going to do a ping MVP ball trick that's the laptop I'm using to record this demo for example.

**[08:43](https://youtube.com/watch?v=e-X5FJwrkaA&t=523s)** So that digital ocean droplet is now talking directly to my laptop over tail scale even though there's a residential file wall in the way with no ports open or anything.

**[08:54](https://youtube.com/watch?v=e-X5FJwrkaA&t=534s)** I just love this stuff.

**[08:56](https://youtube.com/watch?v=e-X5FJwrkaA&t=536s)** Okay, I also snuck into this cloud in it file a docker install script as well.

**[09:01](https://youtube.com/watch?v=e-X5FJwrkaA&t=541s)** So this node not only has tail scale pre installed and pre authenticated to my tail net.

**[09:06](https://youtube.com/watch?v=e-X5FJwrkaA&t=546s)** It's also ready to run docker containers out the box as well.

**[09:09](https://youtube.com/watch?v=e-X5FJwrkaA&t=549s)** So I hope you you can see that terraform is incredibly powerful and we will dig into that in the next video.

**[09:14](https://youtube.com/watch?v=e-X5FJwrkaA&t=554s)** But for now, thank you so much for watching.

**[09:16](https://youtube.com/watch?v=e-X5FJwrkaA&t=556s)** I've been Alex from tail scale.

---

*Automatically generated transcript. May contain errors.*
