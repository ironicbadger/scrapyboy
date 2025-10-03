---
video_id: "PEoMmZOj6Cg"
title: "Automate your Tailscale cloud deployments with Terraform | Infrastructure as Code Series Part 2"
description: "In today's video Alex walks you through the process of automating the deployment of a Digitalocean droplet cloud instance with Terraform, and pre-configuring it to be a tailnet node using cloud-init.
..."
channel_name: "Tailscale"
channel_id: "UCcdv38QxPjSMqbt5ffLhJLA"
published_at: "2024-08-14"
duration_seconds: 879
youtube_url: "https://www.youtube.com/watch?v=PEoMmZOj6Cg"
thumbnail_url: "https://i.ytimg.com/vi/PEoMmZOj6Cg/maxresdefault.jpg"

# Transcription metadata
transcribed_at: "2025-10-03T16:11:38.104629"
transcription_method: "cpu"
model_used: "base"
language: "en"
word_count: 2907
transcription_time_seconds: 25.8
---

# Automate your Tailscale cloud deployments with Terraform | Infrastructure as Code Series Part 2

**[00:00](https://youtube.com/watch?v=PEoMmZOj6Cg&t=0s)** Hi everyone, I'm Alex from Tailscale and welcome into part two of our Infrastructure as Code Video Series. In part one, we covered the basics of cloud units. They'll be a link to the playlist down below. But in today's video, we're going to cover the basics of Terraform. Specifically, we're going to deploy a digital ocean droplet using Terraform. So automatically, we're going to spin up a virtual machine in the cloud, pre-configure it with tailscale, and add that node to your tailnet in today's video. Alright, so let's make a start by talking about what Terraform

**[00:31](https://youtube.com/watch?v=PEoMmZOj6Cg&t=31s)** is, first of all. Terraform was developed by the HashieCorp company, and the idea behind it is it's one tool that can speak many different languages. So what do I mean by that? Well, in the old days, when we wanted to automate the provisioning of infrastructure, we had to be aware of all the different APIs, of all the different cloud providers, and all the different things that they offered. So for example, let's say I wanted to spin up a virtual machine on Amazon Web Services, and I wanted to create an S3 bucket and some

**[01:01](https://youtube.com/watch?v=PEoMmZOj6Cg&t=61s)** low balancers and some ingress, that kind of thing. I could learn the Amazon's domain-specific cloud formation language, so that's a way of writing your virtual machine definitions as templates using cloud formation. Or I could just learn how to do it in Terraform. And the way that Terraform does this is it uses what's called a provider, and this provider is like a connector. So it takes the Terraform code that I write and translates it into a domain-specific language for each cloud provider. So in Amazon's case, it conveys

**[01:31](https://youtube.com/watch?v=PEoMmZOj6Cg&t=91s)** that it into API calls, Amazon can understand. Today, we're going to use digital oceans provider. Now this provider speaks the language that digital ocean needs to know, but I only ever had to learn one language, which was the Terraform markup language known as HCL or HashieCorp configuration language. Now all the documentation for every provider is over on the Terraform registry. I'll put a link to that in the description down below. But let's just take a quick look at my screen over here, and don't forget all

**[02:01](https://youtube.com/watch?v=PEoMmZOj6Cg&t=121s)** these sources, all the technical code snippets and everything that I'm showing you in today's video will be available in a link in the description down below, link to a GitHub repo accompanying this video.

**[02:11](https://youtube.com/watch?v=PEoMmZOj6Cg&t=131s)** So first of all, we have to define a set of providers. This is non-negotiable. This is just a basic way that Terraform knows which provider to use. So if I were speaking to Amazon, I would define the Amazon resource provider. If I were speaking to Proxmox, I would define the Proxmox one here as well.

**[02:29](https://youtube.com/watch?v=PEoMmZOj6Cg&t=149s)** But today, we're just focusing on digital ocean. Next up, I specify a couple of variables, and we'll come on to the variables in a moment because they're quite important.

**[02:38](https://youtube.com/watch?v=PEoMmZOj6Cg&t=158s)** Next up, the digital ocean provider actually needs to know what token to use. So we set a variable here of token equals var.do token.

**[02:47](https://youtube.com/watch?v=PEoMmZOj6Cg&t=167s)** And then finally, we start specifying our resources. Now, these resources can be anything from a simple as just configuring a droplet all the way to configuring firewall rules, S3 buckets, you name it, pretty much any resource that digital ocean make available can be configured through their Terraform provider.

**[03:05](https://youtube.com/watch?v=PEoMmZOj6Cg&t=185s)** These resources require a number of arguments to be passed to them. In our case, the image name is defined by digital ocean upstream. So we can use the doctl command, which is a command line interface utility to connect a digital ocean, which will come on to later to generate a list of these names.

**[03:23](https://youtube.com/watch?v=PEoMmZOj6Cg&t=203s)** Next, we're going to give the virtual machine that we create an actual name in this case NYC one Terraform caddy. Next, we're going to specify the data center or the region that we want to put this resource into.

**[03:35](https://youtube.com/watch?v=PEoMmZOj6Cg&t=215s)** And after that is the sizing. So we're going to pick the small, this is just the $6 a month droplet for this demo that's perfectly fine. But again, you can use doctl to generate a list of all the variables that you could put all the values you could put into this variable down here.

**[03:50](https://youtube.com/watch?v=PEoMmZOj6Cg&t=230s)** Next, we're going to specify the SSH key that we want to install into our virtual machine. And again, we generate this number using the doctl command.

**[03:59](https://youtube.com/watch?v=PEoMmZOj6Cg&t=239s)** And then finally, this is where the magic happens for this video, at least. We're going to inject our cloud init file directly using the Terraform resource.

**[04:07](https://youtube.com/watch?v=PEoMmZOj6Cg&t=247s)** We're going to do this using the template file module that's built into Terraform. You can see here I've got a digital ocean TFTPL file.

**[04:15](https://youtube.com/watch?v=PEoMmZOj6Cg&t=255s)** Now if I jump into that file, which is this one over here on the left, you can see that this is just a cloud init file.

**[04:21](https://youtube.com/watch?v=PEoMmZOj6Cg&t=261s)** There's not really anything special going on for it to be a hashie corp or Terraform specific file, except for where we inject our tail scale or key.

**[04:32](https://youtube.com/watch?v=PEoMmZOj6Cg&t=272s)** So because this is a templated file, when this gets injected from Terraform into the digital ocean virtual machine, that process does some variable interpolation and injects the variable value of our tokens and API keys into the cloud init file.

**[04:48](https://youtube.com/watch?v=PEoMmZOj6Cg&t=288s)** So that we can actually pre-authenticate this node programmatically to our tail net.

**[04:53](https://youtube.com/watch?v=PEoMmZOj6Cg&t=293s)** And if you watch part one of this video series, this file should look very familiar to you. You might notice at the top, I've added a couple of extra things.

**[05:00](https://youtube.com/watch?v=PEoMmZOj6Cg&t=300s)** This is all to do with Ansible, which will come onto in part three of this video series. But you can see we're just configuring a user that Ansible can use via SSH.

**[05:09](https://youtube.com/watch?v=PEoMmZOj6Cg&t=309s)** We'll come onto that in part three.

**[05:12](https://youtube.com/watch?v=PEoMmZOj6Cg&t=312s)** So let's take a look at what's required to actually configure the variable side of this.

**[05:16](https://youtube.com/watch?v=PEoMmZOj6Cg&t=316s)** You can see I've got a couple of extra files here in my directory structure on the left hand side.

**[05:21](https://youtube.com/watch?v=PEoMmZOj6Cg&t=321s)** I've got an example file, so this is one actually gets committed to Git.

**[05:25](https://youtube.com/watch?v=PEoMmZOj6Cg&t=325s)** Now one of the issues when dealing with secrets is we don't want to commit secrets to Git.

**[05:30](https://youtube.com/watch?v=PEoMmZOj6Cg&t=330s)** Otherwise, you could authenticate to my tail net because essentially a token is as good or sometimes it's better than a password to give me API level access to your account.

**[05:41](https://youtube.com/watch?v=PEoMmZOj6Cg&t=341s)** So what we have to do is put these things into a dot Git ignore file, which is over here on the left hand side.

**[05:47](https://youtube.com/watch?v=PEoMmZOj6Cg&t=347s)** And you can see I've got a few things in this direct. I love, by the way, I love the website Git Ignore dot IO.

**[05:54](https://youtube.com/watch?v=PEoMmZOj6Cg&t=354s)** I'm just going to jump to that. And that was a bit of a tangent for this video. But if you have, you know, VS code, was it Visual Studio code?

**[06:02](https://youtube.com/watch?v=PEoMmZOj6Cg&t=362s)** There we go. And then Terraform, and then Ansible, there's a bunch of files for these specific things that you need to put in your Git Ignore file.

**[06:12](https://youtube.com/watch?v=PEoMmZOj6Cg&t=372s)** This website Git Ignore dot IO generates that file for you automatically. Anyway, I digress.

**[06:18](https://youtube.com/watch?v=PEoMmZOj6Cg&t=378s)** So jumping back to VS code for a second, we can see that I've added my TF Vars files here to my Git Ignore file.

**[06:25](https://youtube.com/watch?v=PEoMmZOj6Cg&t=385s)** That means that these files will not end up in source control. That's by design.

**[06:30](https://youtube.com/watch?v=PEoMmZOj6Cg&t=390s)** So the example file here, just rename it to dot TF Vars, change the values, and you should be good to go.

**[06:36](https://youtube.com/watch?v=PEoMmZOj6Cg&t=396s)** The reason we do that is because, as I say, we don't want to commit those secrets to Git.

**[06:41](https://youtube.com/watch?v=PEoMmZOj6Cg&t=401s)** Again, I don't want to leak my auth key, nor do I want to leak my digital ocean API token that gets specified over here.

**[06:49](https://youtube.com/watch?v=PEoMmZOj6Cg&t=409s)** So that's that's one of the real benefits of using this template file.

**[06:52](https://youtube.com/watch?v=PEoMmZOj6Cg&t=412s)** So we could specify the cloud init stuff in line in this file, but by using the templating stuff built into Terraform,

**[06:59](https://youtube.com/watch?v=PEoMmZOj6Cg&t=419s)** we're able to define those secrets opaquely in a variables file, so they don't get exposed through Git.

**[07:05](https://youtube.com/watch?v=PEoMmZOj6Cg&t=425s)** So in order to proceed with Terraform, we're going to have to generate our API tokens for digital ocean,

**[07:10](https://youtube.com/watch?v=PEoMmZOj6Cg&t=430s)** and also generate a tail scale auth key so that that can get injected into our cloud init file.

**[07:15](https://youtube.com/watch?v=PEoMmZOj6Cg&t=435s)** So let's make a start by jumping over to the digital ocean web interface.

**[07:19](https://youtube.com/watch?v=PEoMmZOj6Cg&t=439s)** Over here on the left hand side, they have an API section, and then we're going to want to generate a new token.

**[07:25](https://youtube.com/watch?v=PEoMmZOj6Cg&t=445s)** For the purposes of this video, I'm just going to generate a full access token just to make it easier.

**[07:30](https://youtube.com/watch?v=PEoMmZOj6Cg&t=450s)** But if you want to generate a custom scope where it can only do certain things, you would do that using the custom scopes option.

**[07:37](https://youtube.com/watch?v=PEoMmZOj6Cg&t=457s)** If you're doing this in production, this is absolutely what you should be doing.

**[07:40](https://youtube.com/watch?v=PEoMmZOj6Cg&t=460s)** But for a quick and easy demo like this, I'm just going to do the full access option down here.

**[07:45](https://youtube.com/watch?v=PEoMmZOj6Cg&t=465s)** Now, my API token is only shown once on this screen, so you must copy it here and now, otherwise you'll lose it forever.

**[07:53](https://youtube.com/watch?v=PEoMmZOj6Cg&t=473s)** But treat this like a password, like I say, it's a very sensitive piece of information.

**[07:58](https://youtube.com/watch?v=PEoMmZOj6Cg&t=478s)** Don't worry, I'll rotate the token after I finish recording the video.

**[08:02](https://youtube.com/watch?v=PEoMmZOj6Cg&t=482s)** Now, we've done the digital ocean side of things.

**[08:05](https://youtube.com/watch?v=PEoMmZOj6Cg&t=485s)** Time to jump into tail scale.

**[08:07](https://youtube.com/watch?v=PEoMmZOj6Cg&t=487s)** Now, I want to go into my admin console over on tailscale.com, make sure I'm authenticated into my tail net.

**[08:13](https://youtube.com/watch?v=PEoMmZOj6Cg&t=493s)** Up here on the top right hand side, I go to settings, keys, and then I'm going to generate a new auth key.

**[08:19](https://youtube.com/watch?v=PEoMmZOj6Cg&t=499s)** I'm going to make this one reusable because we're going to be spinning up and destroying this droplet several times, probably during the recording process.

**[08:27](https://youtube.com/watch?v=PEoMmZOj6Cg&t=507s)** I'm going to just generate the key for today. I'm not going to worry about any of the other stuff.

**[08:31](https://youtube.com/watch?v=PEoMmZOj6Cg&t=511s)** I'm going to generate that and copy that and put that into my TF Vars file over here.

**[08:36](https://youtube.com/watch?v=PEoMmZOj6Cg&t=516s)** Okay, we should be pretty much good to go at this point.

**[08:39](https://youtube.com/watch?v=PEoMmZOj6Cg&t=519s)** I'm going to open the integrated terminal in VS code and type terraform init.

**[08:45](https://youtube.com/watch?v=PEoMmZOj6Cg&t=525s)** This is going to configure the basics of the terraform digital ocean provider.

**[08:49](https://youtube.com/watch?v=PEoMmZOj6Cg&t=529s)** Download it and make sure it's got all the runtimes it needs, that kind of thing.

**[08:53](https://youtube.com/watch?v=PEoMmZOj6Cg&t=533s)** And then we can just hopefully do a terraform apply at this point.

**[08:57](https://youtube.com/watch?v=PEoMmZOj6Cg&t=537s)** And it's going to say, right, I've authenticated to the API. Do you want to perform these changes?

**[09:02](https://youtube.com/watch?v=PEoMmZOj6Cg&t=542s)** Yes, and it's going to go ahead and create the droplet for us.

**[09:05](https://youtube.com/watch?v=PEoMmZOj6Cg&t=545s)** Now, if I jump back to my digital ocean interface, we should be able to see under my main tail scale dev project over here, we should be able to see that a new droplet is being created programmatically for us.

**[09:17](https://youtube.com/watch?v=PEoMmZOj6Cg&t=557s)** Now, this can take 20 to 30 seconds to create the droplet and then another 20 to 30, maybe sometimes even 60 seconds to actually boot the VM up and finish running the cloud init scripts to install the packages and create the users and authenticate it to our tail net.

**[09:33](https://youtube.com/watch?v=PEoMmZOj6Cg&t=573s)** All right, so after you've given it a minute or two, I'm just going to jump straight into the console and just see if I can check whether it's booted or not.

**[09:39](https://youtube.com/watch?v=PEoMmZOj6Cg&t=579s)** And yes, we have shell access through the digital ocean console. Excellent.

**[09:45](https://youtube.com/watch?v=PEoMmZOj6Cg&t=585s)** Now, if I type tail scale status, we should see that this node has been authenticated to my tail net, haven't done anything.

**[09:51](https://youtube.com/watch?v=PEoMmZOj6Cg&t=591s)** The only commands I've run you can see is tail scale status and history.

**[09:55](https://youtube.com/watch?v=PEoMmZOj6Cg&t=595s)** This is a brand new virtual machine that's been up for literally one minute.

**[09:59](https://youtube.com/watch?v=PEoMmZOj6Cg&t=599s)** So just in case cloud init's misbehaving or taking too long or doing something you don't quite expect, we want to be able to look at the log files and digital ocean storm under slash var log cloud init dot log.

**[10:11](https://youtube.com/watch?v=PEoMmZOj6Cg&t=611s)** And you can see here there's a huge amount of stuff going on. There's also another one of cloud init output and these two things tell you everything that's been going on.

**[10:20](https://youtube.com/watch?v=PEoMmZOj6Cg&t=620s)** So we can see we've not only installed tail scale, we've also installed docker as part of our cloud init configuration.

**[10:27](https://youtube.com/watch?v=PEoMmZOj6Cg&t=627s)** So if you remember in my cloud init file, let's just jump back to that for a second.

**[10:31](https://youtube.com/watch?v=PEoMmZOj6Cg&t=631s)** I actually created a user called ZFOD.

**[10:34](https://youtube.com/watch?v=PEoMmZOj6Cg&t=634s)** I also enabled tail scale SSH as part of my up command in my cloud init configuration.

**[10:39](https://youtube.com/watch?v=PEoMmZOj6Cg&t=639s)** So what this is going to let me do is jump back to a terminal window.

**[10:44](https://youtube.com/watch?v=PEoMmZOj6Cg&t=644s)** And without doing any special configuration, I can do SSH ZFOD at the DNS hostname that tail scale gives this node.

**[10:52](https://youtube.com/watch?v=PEoMmZOj6Cg&t=652s)** And I'm not installing any SSH keys in that remote box. I'm not configuring port forwarding and I'm just doing any of that.

**[10:59](https://youtube.com/watch?v=PEoMmZOj6Cg&t=659s)** Just using tail scale SSH, I'm able to connect directly into that remote node.

**[11:03](https://youtube.com/watch?v=PEoMmZOj6Cg&t=663s)** So if you're doing this terraform stuff programmatically as part of a CI job or you're doing, you know, some just some automated way of doing this.

**[11:12](https://youtube.com/watch?v=PEoMmZOj6Cg&t=672s)** You can start to put Ansible in the background and have Ansible SSH into this node and now configure it after it's been created.

**[11:19](https://youtube.com/watch?v=PEoMmZOj6Cg&t=679s)** And so that's exactly what we're going to do in part three of this video series.

**[11:22](https://youtube.com/watch?v=PEoMmZOj6Cg&t=682s)** We're going to create a node which is going to be running a reverse proxy called caddy.

**[11:27](https://youtube.com/watch?v=PEoMmZOj6Cg&t=687s)** And that's going to be configured using Ansible via tail scale SSH.

**[11:31](https://youtube.com/watch?v=PEoMmZOj6Cg&t=691s)** So we're going to piece all of these three things together.

**[11:33](https://youtube.com/watch?v=PEoMmZOj6Cg&t=693s)** We're going to create the virtual machine using cloud init as we showed you in part one.

**[11:37](https://youtube.com/watch?v=PEoMmZOj6Cg&t=697s)** We're then going to do it automatically and create it under the solution automatically as we just showed you in this part two.

**[11:44](https://youtube.com/watch?v=PEoMmZOj6Cg&t=704s)** And in part three, we're going to automatically configure that thing as part of a CI workflow on something like GitHub actions or some other CI workflow engine.

**[11:53](https://youtube.com/watch?v=PEoMmZOj6Cg&t=713s)** Now, before we get out of here, I need to show you a couple of things with DOCTL.

**[11:58](https://youtube.com/watch?v=PEoMmZOj6Cg&t=718s)** So jumping back to my terminal window over here, DOCTL is a tool that lets us interface with the digital ocean API

**[12:06](https://youtube.com/watch?v=PEoMmZOj6Cg&t=726s)** without doing anything related to terraform whatsoever.

**[12:09](https://youtube.com/watch?v=PEoMmZOj6Cg&t=729s)** Now, this gives us a bunch of information around our digital ocean account.

**[12:13](https://youtube.com/watch?v=PEoMmZOj6Cg&t=733s)** We do need a token and luckily, we happen to have one stored in the autovars over here.

**[12:19](https://youtube.com/watch?v=PEoMmZOj6Cg&t=739s)** So, and so if I copy this value, what I can do is a DOCTL hyphen T and then paste in my token value.

**[12:27](https://youtube.com/watch?v=PEoMmZOj6Cg&t=747s)** What I want to get here is the list of SSH keys that are assigned to my digital ocean account.

**[12:33](https://youtube.com/watch?v=PEoMmZOj6Cg&t=753s)** That's because when I create a virtual machine resource and that's I specify an SSH key on the first login of the console in digital oceans web interface, I'm going to be prompted to create a password, which I think is a little bit draconian in this day and age.

**[12:49](https://youtube.com/watch?v=PEoMmZOj6Cg&t=769s)** So I always like to try and use SSH keys wherever possible.

**[12:52](https://youtube.com/watch?v=PEoMmZOj6Cg&t=772s)** Now, the command that we need here is under the compute key option under the DOCTL syntax.

**[12:59](https://youtube.com/watch?v=PEoMmZOj6Cg&t=779s)** So if we simply type compute, we're going to get a bunch of options here.

**[13:02](https://youtube.com/watch?v=PEoMmZOj6Cg&t=782s)** We can create droplets, we can manage them, all that kind of thing.

**[13:05](https://youtube.com/watch?v=PEoMmZOj6Cg&t=785s)** What we're after here is actually displaying the SSH keys linked to my account.

**[13:09](https://youtube.com/watch?v=PEoMmZOj6Cg&t=789s)** So I'm going to do a compute SSH key and then list.

**[13:13](https://youtube.com/watch?v=PEoMmZOj6Cg&t=793s)** And that's just going to list out all the SSH keys assigned and attached to my DO account.

**[13:19](https://youtube.com/watch?v=PEoMmZOj6Cg&t=799s)** And so once we have that number, what we want to do is copy that onto our clipboards and just take it back and put it in our main terraform configuration.

**[13:26](https://youtube.com/watch?v=PEoMmZOj6Cg&t=806s)** This wants to be specified as a list and you could of you could of course put this as a variable and then obfuscate it into the variables file.

**[13:33](https://youtube.com/watch?v=PEoMmZOj6Cg&t=813s)** If you don't to expose this number, but I don't think it's a particularly sensitive value.

**[13:37](https://youtube.com/watch?v=PEoMmZOj6Cg&t=817s)** So your mileage may vary and it's up to you to how to proceed here.

**[13:41](https://youtube.com/watch?v=PEoMmZOj6Cg&t=821s)** So another command you might find useful is this DOCTL compute image list command.

**[13:46](https://youtube.com/watch?v=PEoMmZOj6Cg&t=826s)** This is how we get the slug value that goes into this image inside the resource definition in terraform.

**[13:52](https://youtube.com/watch?v=PEoMmZOj6Cg&t=832s)** So in my case, if I do DOCTL compute image list, I then get a whole long list of all the different various images that are available.

**[14:00](https://youtube.com/watch?v=PEoMmZOj6Cg&t=840s)** And then I get the slug over here on the right hand side.

**[14:03](https://youtube.com/watch?v=PEoMmZOj6Cg&t=843s)** So in my case, I know that the slug is a Ubuntu 2404.

**[14:07](https://youtube.com/watch?v=PEoMmZOj6Cg&t=847s)** But if you have a different image you want to use or even a custom image that you've created in DO, this is where you would specify it in terraform.

**[14:14](https://youtube.com/watch?v=PEoMmZOj6Cg&t=854s)** And so I think that will cover us for the basics of getting started with terraform, cloud in it and tail scale all at once.

**[14:20](https://youtube.com/watch?v=PEoMmZOj6Cg&t=860s)** In part three, don't forget we're going to be moving on to configuring that infrastructure using Ansible programmatically as well.

**[14:26](https://youtube.com/watch?v=PEoMmZOj6Cg&t=866s)** So thank you so much for watching and until next time I've been Alex from tail scale.

---

*Automatically generated transcript. May contain errors.*
