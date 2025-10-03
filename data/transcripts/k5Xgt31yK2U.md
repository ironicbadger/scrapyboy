---
video_id: "k5Xgt31yK2U"
title: "An Ansible primer for Devops | Infrastructure as Code Series Part 3"
description: "Ansible is a fundamental Devops technology and relies heavily on SSH under the covers to connect from one place to another. In today's video, Alex discusses what Ansible is and why you might want to u..."
channel_name: "Tailscale"
channel_id: "UCcdv38QxPjSMqbt5ffLhJLA"
published_at: "2024-08-26"
duration_seconds: 2180
youtube_url: "https://www.youtube.com/watch?v=k5Xgt31yK2U"
thumbnail_url: "https://i.ytimg.com/vi_webp/k5Xgt31yK2U/maxresdefault.webp"

# Transcription metadata
transcribed_at: "2025-10-03T17:58:16.592210"
transcription_method: "cpu"
model_used: "base"
language: "en"
word_count: 7012
transcription_time_seconds: 58.0
---

# An Ansible primer for Devops | Infrastructure as Code Series Part 3

**[00:00](https://youtube.com/watch?v=k5Xgt31yK2U&t=0s)** I am Alex from Tailscale, and welcome into part three of our Infrastructure as CodePlaylist.

**[00:05](https://youtube.com/watch?v=k5Xgt31yK2U&t=5s)** In part one, we covered Cloud init. That's a technology that lets you configure a completely

**[00:10](https://youtube.com/watch?v=k5Xgt31yK2U&t=10s)** blank virtual machine, just by providing a few lines of text. You can do things like

**[00:15](https://youtube.com/watch?v=k5Xgt31yK2U&t=15s)** Create Users, configure the network, install packages, but it has its limitations.

**[00:20](https://youtube.com/watch?v=k5Xgt31yK2U&t=20s)** In part two, we took Cloud init a step further, and automated the creation of a cloud resource

**[00:26](https://youtube.com/watch?v=k5Xgt31yK2U&t=26s)** in our case a digital ocean droplet using Terraform. Terraforms great for creating infrastructure,

**[00:32](https://youtube.com/watch?v=k5Xgt31yK2U&t=32s)** but it's not so hot at actually configuring the nuts and bolts of those virtual machines

**[00:37](https://youtube.com/watch?v=k5Xgt31yK2U&t=37s)** and some of the other stuff that Ansible can do. So that's what we're going to do in part

**[00:41](https://youtube.com/watch?v=k5Xgt31yK2U&t=41s)** three today. We're going to use Ansible to configure that blank virtual machine that we created

**[00:46](https://youtube.com/watch?v=k5Xgt31yK2U&t=46s)** using Terraform. Back when I was a fledgling university student, Ansible was one of the very

**[00:53](https://youtube.com/watch?v=k5Xgt31yK2U&t=53s)** first DevOps technologies I ever learned, and indeed I still believe today that Ansible is one

**[00:58](https://youtube.com/watch?v=k5Xgt31yK2U&t=58s)** of those foundational DevOps technologies that is fundamental in the day-to-day life of an

**[01:04](https://youtube.com/watch?v=k5Xgt31yK2U&t=64s)** infrastructure engineer. It's one of the most approachable technologies in the space as it uses

**[01:09](https://youtube.com/watch?v=k5Xgt31yK2U&t=69s)** simple YAML configuration syntax to describe exactly what it's doing. In the infrastructure

**[01:14](https://youtube.com/watch?v=k5Xgt31yK2U&t=74s)** as CodeWorld, we love to declaratively describe our systems, and Ansible lets us do just that.

**[01:21](https://youtube.com/watch?v=k5Xgt31yK2U&t=81s)** We define a series of tasks in a specific order and group those tasks together into playbooks.

**[01:27](https://youtube.com/watch?v=k5Xgt31yK2U&t=87s)** Those playbooks get executed against remote systems, and we bring them in line by doing so

**[01:32](https://youtube.com/watch?v=k5Xgt31yK2U&t=92s)** with our desired state of the world. I should also add you can run Ansible against your local system,

**[01:38](https://youtube.com/watch?v=k5Xgt31yK2U&t=98s)** and in fact I know many folks who use that as a learning opportunity when they're first getting

**[01:42](https://youtube.com/watch?v=k5Xgt31yK2U&t=102s)** started with Ansible. So let's take a moment and just look at what Ansible is in its most

**[01:47](https://youtube.com/watch?v=k5Xgt31yK2U&t=107s)** simple form. Really it's just a way to configure systems. It does this by taking a series of inputs,

**[01:55](https://youtube.com/watch?v=k5Xgt31yK2U&t=115s)** YAML files, with variables and tasks, and it gathers a bunch of facts about a remote system,

**[02:01](https://youtube.com/watch?v=k5Xgt31yK2U&t=121s)** and ensures that there isn't a delta between these two states. It connects to these remote systems

**[02:06](https://youtube.com/watch?v=k5Xgt31yK2U&t=126s)** via SSH in what's called a push model, so it pushes its configuration to a remote host.

**[02:12](https://youtube.com/watch?v=k5Xgt31yK2U&t=132s)** This is in contrast to a tool like Puppet, which is running on a pull model,

**[02:16](https://youtube.com/watch?v=k5Xgt31yK2U&t=136s)** so it has an agent running on the remote host, phoning home, and asking for configuration changes.

**[02:22](https://youtube.com/watch?v=k5Xgt31yK2U&t=142s)** So what this means in practice is that you must be able to connect from your Ansible control

**[02:27](https://youtube.com/watch?v=k5Xgt31yK2U&t=147s)** system to push the configuration out to the system that you want to remotely configure via SSH.

**[02:34](https://youtube.com/watch?v=k5Xgt31yK2U&t=154s)** So this is where tailscale comes in. We already added our remote system to our tailnet using

**[02:40](https://youtube.com/watch?v=k5Xgt31yK2U&t=160s)** cloud init in part one and two of this video series, and in doing so we removed that initial

**[02:45](https://youtube.com/watch?v=k5Xgt31yK2U&t=165s)** dance of creating a bootstrap SSH key, creating a temporary bootstrap user, and all that kind of

**[02:51](https://youtube.com/watch?v=k5Xgt31yK2U&t=171s)** stuff. Simply by virtue of being on our tailnet, tailscale is able to provide your identity to the

**[02:56](https://youtube.com/watch?v=k5Xgt31yK2U&t=176s)** remote system's SSH service to validate its you and let you in. Now because Ansible connects via

**[03:03](https://youtube.com/watch?v=k5Xgt31yK2U&t=183s)** SSH remember, so long as we use a tailscale node name to connect, we never need to worry about

**[03:08](https://youtube.com/watch?v=k5Xgt31yK2U&t=188s)** SSH keys ever again. It's really cool, and I'll show you this later in the video. Ansible is

**[03:14](https://youtube.com/watch?v=k5Xgt31yK2U&t=194s)** written in Python, but we don't need to know any Python to use it. In fact, all we need to know

**[03:19](https://youtube.com/watch?v=k5Xgt31yK2U&t=199s)** is how to use the Ansible module system. So there's a huge long list, as you can see on the screen

**[03:24](https://youtube.com/watch?v=k5Xgt31yK2U&t=204s)** right here. Things from line in file, so if you want to modify just one or two characters in a

**[03:30](https://youtube.com/watch?v=k5Xgt31yK2U&t=210s)** specific file or change a value, you can do it that way. There's a file copy module. If you want

**[03:35](https://youtube.com/watch?v=k5Xgt31yK2U&t=215s)** a copy files to the remote host, there's packages, there's user modules, there's honestly, there are

**[03:42](https://youtube.com/watch?v=k5Xgt31yK2U&t=222s)** so many modules for Ansible, not just for Linux systems, but for networking appliances and all sorts

**[03:48](https://youtube.com/watch?v=k5Xgt31yK2U&t=228s)** of other stuff as well. It's kind of overwhelming to start with, but in reality, you're only ever

**[03:53](https://youtube.com/watch?v=k5Xgt31yK2U&t=233s)** going to need a handful of modules to get started. But where I really found it most useful was managing

**[03:59](https://youtube.com/watch?v=k5Xgt31yK2U&t=239s)** configuration files using the ginger templating language. Now, of course, your mileage may vary.

**[04:04](https://youtube.com/watch?v=k5Xgt31yK2U&t=244s)** You might want to just use Ansible to install a few packages and create a few users that you

**[04:09](https://youtube.com/watch?v=k5Xgt31yK2U&t=249s)** didn't do in the previous cloud init configuration, or maybe you want to bring a virtual machine up

**[04:13](https://youtube.com/watch?v=k5Xgt31yK2U&t=253s)** to some policy inside your organization, or whatever you want to do with it. Ansible is a fantastic

**[04:18](https://youtube.com/watch?v=k5Xgt31yK2U&t=258s)** tool that executes a bunch of tasks in a sequential order. It's almost like a bash script, but a

**[04:23](https://youtube.com/watch?v=k5Xgt31yK2U&t=263s)** bash script is actually smart. One of the separating things between just a bash script and Ansible

**[04:30](https://youtube.com/watch?v=k5Xgt31yK2U&t=270s)** is this concept of something called idempotency. An idempotency is something that is

**[04:35](https://youtube.com/watch?v=k5Xgt31yK2U&t=275s)** contextually aware of what the target host is going to be doing. So from my laptop here, I will run

**[04:41](https://youtube.com/watch?v=k5Xgt31yK2U&t=281s)** an Ansible command. I'll run a what's called a playbook, which is a series of tasks in a specific

**[04:46](https://youtube.com/watch?v=k5Xgt31yK2U&t=286s)** order against a certain remote host. Ansible is smart enough to gather a bunch of facts and a bunch

**[04:52](https://youtube.com/watch?v=k5Xgt31yK2U&t=292s)** of information about that remote host and decide whether it needs to execute a certain task or not.

**[04:58](https://youtube.com/watch?v=k5Xgt31yK2U&t=298s)** So it's not going to go ahead and install 20 copies of the same package over and over again,

**[05:03](https://youtube.com/watch?v=k5Xgt31yK2U&t=303s)** for example, it knows I've already got git installed on this computer. Well, I don't need to go

**[05:08](https://youtube.com/watch?v=k5Xgt31yK2U&t=308s)** and install git again. I've already got it. But there's a bunch of other configuration flags you

**[05:13](https://youtube.com/watch?v=k5Xgt31yK2U&t=313s)** can pass to Ansible as well to actually update those packages. So if you wanted to say just verify

**[05:18](https://youtube.com/watch?v=k5Xgt31yK2U&t=318s)** that something is present on the system, you can do that. Or if you'd like to say give me the latest

**[05:23](https://youtube.com/watch?v=k5Xgt31yK2U&t=323s)** version of something, you can do that too. And every single Ansible module has this concept of

**[05:29](https://youtube.com/watch?v=k5Xgt31yK2U&t=329s)** configuration flags that you pass to it at runtime. Ansible is configured using the YAML.

**[05:36](https://youtube.com/watch?v=k5Xgt31yK2U&t=336s)** I don't want to say programming language because that's going to set a few people. But I mean,

**[05:40](https://youtube.com/watch?v=k5Xgt31yK2U&t=340s)** essentially at this point, YAML, particularly once you get into the Kubernetes space,

**[05:44](https://youtube.com/watch?v=k5Xgt31yK2U&t=344s)** it kind of is a programming language at this point. And we do make it do things that perhaps

**[05:49](https://youtube.com/watch?v=k5Xgt31yK2U&t=349s)** it possibly shouldn't. But essentially what we do with YAML is we specify each module we want to run

**[05:55](https://youtube.com/watch?v=k5Xgt31yK2U&t=355s)** and then the parameters and then the Python code that Ansible executes under the hood,

**[05:59](https://youtube.com/watch?v=k5Xgt31yK2U&t=359s)** which we don't actually see. Ansible is written in Python, but we never have to write any Python.

**[06:04](https://youtube.com/watch?v=k5Xgt31yK2U&t=364s)** Unless you want to get into custom filters, but that's way beyond the scope of today's video.

**[06:09](https://youtube.com/watch?v=k5Xgt31yK2U&t=369s)** What you want to do is just write these YAML playbooks, which execute a certain set of tasks

**[06:13](https://youtube.com/watch?v=k5Xgt31yK2U&t=373s)** in a specific order, as I say, against a remote host. So what we're going to do today is I have

**[06:20](https://youtube.com/watch?v=k5Xgt31yK2U&t=380s)** the Terraform code linked in a description down below, along with all the Ansible code and everything

**[06:25](https://youtube.com/watch?v=k5Xgt31yK2U&t=385s)** I'm going to show you in today's video too. So what I'm going to do is just jump over here to my

**[06:29](https://youtube.com/watch?v=k5Xgt31yK2U&t=389s)** tail net. Now, you can see that I have a machine over here called fake NAS. And on fake NAS,

**[06:35](https://youtube.com/watch?v=k5Xgt31yK2U&t=395s)** I'm running a jellyfin server. I've got to get my Michael Portillo in every now and again.

**[06:40](https://youtube.com/watch?v=k5Xgt31yK2U&t=400s)** Something comforting about Great British Railway journeys. It's one of my favorite go-to comfort food

**[06:45](https://youtube.com/watch?v=k5Xgt31yK2U&t=405s)** TVs. Anyway, I digress. So what I want to do is take this jellyfin instance, which is currently

**[06:52](https://youtube.com/watch?v=k5Xgt31yK2U&t=412s)** running on fake NAS, Port 2285, and expose that to the public internet. Now, I could do this using

**[06:59](https://youtube.com/watch?v=k5Xgt31yK2U&t=419s)** tailscale funnel, but it's probably a bad idea because of some of the quality of service stuff

**[07:04](https://youtube.com/watch?v=k5Xgt31yK2U&t=424s)** for streaming videos specifically. Same is true with something like Cloudflare tunnels. I mean,

**[07:09](https://youtube.com/watch?v=k5Xgt31yK2U&t=429s)** they have a specific line, I think, in their terms of service that say, please don't stream video via

**[07:14](https://youtube.com/watch?v=k5Xgt31yK2U&t=434s)** this. It's not what it's meant for. So if we want to actually go ahead and configure something to

**[07:19](https://youtube.com/watch?v=k5Xgt31yK2U&t=439s)** stream video, we probably want to spin up a VPS. Well, that's what we're going to do today.

**[07:24](https://youtube.com/watch?v=k5Xgt31yK2U&t=444s)** We're going to spin up a VPS on digital ocean using the Terraform and Cloud init code that we

**[07:29](https://youtube.com/watch?v=k5Xgt31yK2U&t=449s)** already showed you in parts one and two. And then we're going to use Ansible to configure

**[07:33](https://youtube.com/watch?v=k5Xgt31yK2U&t=453s)** caddy, which is a reverse proxy. Now, all a reverse proxy does is it sits out on the public internet

**[07:39](https://youtube.com/watch?v=k5Xgt31yK2U&t=459s)** and waits for somebody to connect to a certain URL. In our case, it's going to be jellyfin.something.com.

**[07:46](https://youtube.com/watch?v=k5Xgt31yK2U&t=466s)** It then takes that request and tunnels it back to my server that's running in my LAN safely over

**[07:53](https://youtube.com/watch?v=k5Xgt31yK2U&t=473s)** a tailscale encrypted tunnel. Now, if you think about the ramifications of what this means,

**[07:58](https://youtube.com/watch?v=k5Xgt31yK2U&t=478s)** you can have one VPS reverse proxy in any node and any service on your tailnet anywhere in the world.

**[08:05](https://youtube.com/watch?v=k5Xgt31yK2U&t=485s)** It's an incredibly powerful realization once you have it. Okay, let's jump in.

**[08:11](https://youtube.com/watch?v=k5Xgt31yK2U&t=491s)** In my Vs code instance over here, I have a couple of folders and again, link into the description

**[08:16](https://youtube.com/watch?v=k5Xgt31yK2U&t=496s)** down below to all this code. But I have an Ansible directory here, which has a few files in it.

**[08:22](https://youtube.com/watch?v=k5Xgt31yK2U&t=502s)** And if you're brand new to Ansible, I'm going to go through everything step by step,

**[08:25](https://youtube.com/watch?v=k5Xgt31yK2U&t=505s)** and there'll be chapters if you want to skip past a certain piece. So bear with me. Okay,

**[08:30](https://youtube.com/watch?v=k5Xgt31yK2U&t=510s)** so first of all, we are going to look at this Ansible config file here. This is just a bunch

**[08:34](https://youtube.com/watch?v=k5Xgt31yK2U&t=514s)** of Ansible specific stuff. If you are new, don't worry too much about it. Essentially,

**[08:39](https://youtube.com/watch?v=k5Xgt31yK2U&t=519s)** she's just configuring a bunch of stuff like where the hosts file lives, where the encryption

**[08:45](https://youtube.com/watch?v=k5Xgt31yK2U&t=525s)** password lives for our vault password file, that kind of stuff. And also where we import any third

**[08:50](https://youtube.com/watch?v=k5Xgt31yK2U&t=530s)** party roles that we're going to use. So remember when I was talking about how Ansible is a bunch

**[08:54](https://youtube.com/watch?v=k5Xgt31yK2U&t=534s)** of tasks that get executed in a specific order, well, that grouping of tasks is called a role.

**[09:00](https://youtube.com/watch?v=k5Xgt31yK2U&t=540s)** And the idea would be that you have a web server and you want to configure a bunch of different

**[09:05](https://youtube.com/watch?v=k5Xgt31yK2U&t=545s)** roles. You want it to have a certain set of packages, a certain set of users. And in our case,

**[09:09](https://youtube.com/watch?v=k5Xgt31yK2U&t=549s)** a certain reverse proxy configuration, when you give it a role configures the server to perform

**[09:15](https://youtube.com/watch?v=k5Xgt31yK2U&t=555s)** that role. The grouping of roles, so you can have multiple roles. So you've got it's a little bit

**[09:21](https://youtube.com/watch?v=k5Xgt31yK2U&t=561s)** confusing. You've got a grouping of multiple tasks is a role. And then a grouping of multiple roles

**[09:26](https://youtube.com/watch?v=k5Xgt31yK2U&t=566s)** is called a playbook. And the playbook gets executed in a specific order. Now the playbook we're

**[09:32](https://youtube.com/watch?v=k5Xgt31yK2U&t=572s)** going to run today is this run dot yaml playbook. And currently there's only one role in it.

**[09:38](https://youtube.com/watch?v=k5Xgt31yK2U&t=578s)** It's going to run against this host, which is NYC terraform caddy. And then there is a secret

**[09:44](https://youtube.com/watch?v=k5Xgt31yK2U&t=584s)** yaml file that lives over here in vars slash secrets dot yaml. This role is configured in the

**[09:50](https://youtube.com/watch?v=k5Xgt31yK2U&t=590s)** requirements dot yaml over here. Now Ansible has the concept a bit like Docker Hub where you can

**[09:55](https://youtube.com/watch?v=k5Xgt31yK2U&t=595s)** import third party roles and repose and that kind of thing. So all I'm doing here is specifying

**[10:01](https://youtube.com/watch?v=k5Xgt31yK2U&t=601s)** that I want this git repo ironic badger Ansible role caddy to appear as ironic badger dot caddy

**[10:08](https://youtube.com/watch?v=k5Xgt31yK2U&t=608s)** in my playbook. So that's where that code comes from here to install that role. What we need to do

**[10:14](https://youtube.com/watch?v=k5Xgt31yK2U&t=614s)** is an Ansible galaxy install. There is a just file, which if you've ever worked in infrastructure

**[10:21](https://youtube.com/watch?v=k5Xgt31yK2U&t=621s)** roles, you might see make files or scripts to do a bunch of commands. I'm using this one called

**[10:26](https://youtube.com/watch?v=k5Xgt31yK2U&t=626s)** just, which is I think on GitHub by Casey slash just if you want to Google it. The

**[10:30](https://youtube.com/watch?v=k5Xgt31yK2U&t=630s)** be a link down below of course. This just file here is executing this command Ansible galaxy

**[10:37](https://youtube.com/watch?v=k5Xgt31yK2U&t=637s)** install minus our requirements dot yaml. But all I need to do to execute that command is type

**[10:44](https://youtube.com/watch?v=k5Xgt31yK2U&t=644s)** just rex and you can see that just here. These commands, this isn't Ansible specific but it

**[10:50](https://youtube.com/watch?v=k5Xgt31yK2U&t=650s)** really helps you organize the commands you've got to run. You can see that sometimes they start

**[10:55](https://youtube.com/watch?v=k5Xgt31yK2U&t=655s)** to get a little bit long in the tooth these commands and there's a lot of stuff to remember in

**[10:58](https://youtube.com/watch?v=k5Xgt31yK2U&t=658s)** tags and hosts and yada yada yada. So the rex thing here is my shorthand in my mind for requirements.

**[11:05](https://youtube.com/watch?v=k5Xgt31yK2U&t=665s)** So when I type just rex into the terminal down below, you can see the Ansible goes out to GitHub

**[11:12](https://youtube.com/watch?v=k5Xgt31yK2U&t=672s)** pulls in the latest version of that role and installs it into this galaxy roles directory over here.

**[11:18](https://youtube.com/watch?v=k5Xgt31yK2U&t=678s)** That's configured in our Ansible config directory up here. See this roles path. We can see under

**[11:24](https://youtube.com/watch?v=k5Xgt31yK2U&t=684s)** print working directory. So current working directory is this one O2 cloud init DO Terraform.

**[11:29](https://youtube.com/watch?v=k5Xgt31yK2U&t=689s)** You can see that over here. That's why that gets installed to this directory here is because of

**[11:34](https://youtube.com/watch?v=k5Xgt31yK2U&t=694s)** this galaxy roles option that's right here. So you can see it created that galaxy roles directory

**[11:39](https://youtube.com/watch?v=k5Xgt31yK2U&t=699s)** and in it is now the ironic badger caddy role. Now remember a role is a grouping of tasks. So let's

**[11:46](https://youtube.com/watch?v=k5Xgt31yK2U&t=706s)** jump inside this role and take a very quick look at what it's going to do for us. The main dot yaml

**[11:52](https://youtube.com/watch?v=k5Xgt31yK2U&t=712s)** is almost always where you want to start with a third party role to try and understand what it's

**[11:56](https://youtube.com/watch?v=k5Xgt31yK2U&t=716s)** doing. Beyond the read me of course which I definitely put some many long hours into for this one.

**[12:05](https://youtube.com/watch?v=k5Xgt31yK2U&t=725s)** So under main dot yaml we can see the very first thing that this role is going to do is check to see

**[12:10](https://youtube.com/watch?v=k5Xgt31yK2U&t=730s)** if the caddy binary is present. This registers what's called a fact and then Ansible uses that to

**[12:16](https://youtube.com/watch?v=k5Xgt31yK2U&t=736s)** decide whether to actually execute the next entire grouping of tasks. So by doing this include tasks

**[12:25](https://youtube.com/watch?v=k5Xgt31yK2U&t=745s)** section down here. We're able to conditionally include and decide how to do so I can if then else

**[12:29](https://youtube.com/watch?v=k5Xgt31yK2U&t=749s)** statement effectively when true by default and obviously when this is false I want to install caddy

**[12:37](https://youtube.com/watch?v=k5Xgt31yK2U&t=757s)** and when it's true I'm not going to okay. Now when I jump into the install yaml file what we're

**[12:43](https://youtube.com/watch?v=k5Xgt31yK2U&t=763s)** going to do is download the latest release of caddy add the users add the groups make sure that

**[12:49](https://youtube.com/watch?v=k5Xgt31yK2U&t=769s)** the system D service gets installed and then call a system D module. Now if this is the first time

**[12:54](https://youtube.com/watch?v=k5Xgt31yK2U&t=774s)** you've ever seen an Ansible playbook forgive me for rushing through that a little bit and let me

**[12:58](https://youtube.com/watch?v=k5Xgt31yK2U&t=778s)** just explain what's going on here. This is the structure of how an Ansible module always works.

**[13:04](https://youtube.com/watch?v=k5Xgt31yK2U&t=784s)** So we are using yaml of course and each block here is defined by this little dash at the beginning

**[13:12](https://youtube.com/watch?v=k5Xgt31yK2U&t=792s)** and what we do for good practice is we give each task that happens here a name and then we call

**[13:18](https://youtube.com/watch?v=k5Xgt31yK2U&t=798s)** the module so in this case this is the get url module. Now if we want to look up the documentation

**[13:23](https://youtube.com/watch?v=k5Xgt31yK2U&t=803s)** for that specific module we can go to Google and type in Ansible and then the name of the module

**[13:28](https://youtube.com/watch?v=k5Xgt31yK2U&t=808s)** and over here on the Ansible website is a bunch of information about how to actually use and

**[13:34](https://youtube.com/watch?v=k5Xgt31yK2U&t=814s)** configure this specific module right at the bottom I never know why this isn't at the top but whatever

**[13:41](https://youtube.com/watch?v=k5Xgt31yK2U&t=821s)** it's always at the bottom you can see there are a bunch of examples of how to actually use this

**[13:46](https://youtube.com/watch?v=k5Xgt31yK2U&t=826s)** specific module. So I noticed there's a small typo in my code it's not really a typo because a

**[13:53](https://youtube.com/watch?v=k5Xgt31yK2U&t=833s)** few years ago Ansible introduced the idea of collections that's a topic for an entirely separate

**[13:58](https://youtube.com/watch?v=k5Xgt31yK2U&t=838s)** video. What we're going to do is just use the Ansible built-in module of get url to fetch the caddy

**[14:04](https://youtube.com/watch?v=k5Xgt31yK2U&t=844s)** binary this is the reverse proxy remember caddy and install it into a specific destination or path

**[14:11](https://youtube.com/watch?v=k5Xgt31yK2U&t=851s)** on our host system. Now where is the where are these variables defined? So if we look at the parameters

**[14:16](https://youtube.com/watch?v=k5Xgt31yK2U&t=856s)** that are configured in this module in this task right here we can see we've got two things being

**[14:21](https://youtube.com/watch?v=k5Xgt31yK2U&t=861s)** substituted in and out. So we've got the caddy AMD 64 linux binary url this is where the caddy

**[14:28](https://youtube.com/watch?v=k5Xgt31yK2U&t=868s)** project publish a cloud flare compatible version of caddy if you want to use caddy with any other

**[14:34](https://youtube.com/watch?v=k5Xgt31yK2U&t=874s)** providers like cloud flare or duck DNS or pork bun or name cheap or whoever you need to download

**[14:41](https://youtube.com/watch?v=k5Xgt31yK2U&t=881s)** the specific version of caddy for those DNS providers for the DNS challenge to work properly and

**[14:47](https://youtube.com/watch?v=k5Xgt31yK2U&t=887s)** get your TLS certificate. In my case I'm doing everything with cloud flare today so if I look in the

**[14:52](https://youtube.com/watch?v=k5Xgt31yK2U&t=892s)** defaults folder over here we can take a quick look and see that the linux binary url includes the

**[14:59](https://youtube.com/watch?v=k5Xgt31yK2U&t=899s)** caddy DNS cloud flare plugin this is all open source all this code is in github and there'll be

**[15:05](https://youtube.com/watch?v=k5Xgt31yK2U&t=905s)** links to it down in the description down below. The next thing that gets included is the caddy

**[15:09](https://youtube.com/watch?v=k5Xgt31yK2U&t=909s)** binary path so if we take a quick look at the install page again we can see the destination this is

**[15:15](https://youtube.com/watch?v=k5Xgt31yK2U&t=915s)** where it's going to actually install that binary and then it's going to make it executable and owned

**[15:19](https://youtube.com/watch?v=k5Xgt31yK2U&t=919s)** by root and also by the group root. And so it continues throughout this file you can see we create

**[15:25](https://youtube.com/watch?v=k5Xgt31yK2U&t=925s)** the group we create the user we create the system D service this is a really interesting one

**[15:30](https://youtube.com/watch?v=k5Xgt31yK2U&t=930s)** remember I talked about ginger templating this is where it starts to get really pretty cool in my

**[15:35](https://youtube.com/watch?v=k5Xgt31yK2U&t=935s)** opinion as a massive nerd so if we take a quick look at line 22 we can see we're calling the template

**[15:42](https://youtube.com/watch?v=k5Xgt31yK2U&t=942s)** module now if we go back to the Ansible documentation and have a quick look at the template module

**[15:48](https://youtube.com/watch?v=k5Xgt31yK2U&t=948s)** you can see there's a bunch of other stuff that we can do with this module but one of my favorite

**[15:52](https://youtube.com/watch?v=k5Xgt31yK2U&t=952s)** things to do is sometimes just to use it to configure some very basic parameters so what

**[15:57](https://youtube.com/watch?v=k5Xgt31yK2U&t=957s)** it's going to do is it's going to take this caddy dot service dot J2 ginger to file from the

**[16:02](https://youtube.com/watch?v=k5Xgt31yK2U&t=962s)** templates directory and install it into slash Etsy system D system caddy dot service so let's take a

**[16:09](https://youtube.com/watch?v=k5Xgt31yK2U&t=969s)** very quick look at the system D unit file that's going to be installed and you'll notice there are

**[16:14](https://youtube.com/watch?v=k5Xgt31yK2U&t=974s)** some variables here so in the main this is such a confusing thing about Ansible but in the main

**[16:20](https://youtube.com/watch?v=k5Xgt31yK2U&t=980s)** file you need to use these quote marks and the double curly braces to have a variable substituted

**[16:26](https://youtube.com/watch?v=k5Xgt31yK2U&t=986s)** by Ansible but in a downstream ginger to substitution because of the interpreter that ginger to

**[16:32](https://youtube.com/watch?v=k5Xgt31yK2U&t=992s)** uses versus the Ansible Python interpreter it's all about string quoting and honestly very

**[16:38](https://youtube.com/watch?v=k5Xgt31yK2U&t=998s)** confusing it's just one of those things you have to learn and once you get it you're like okay that

**[16:42](https://youtube.com/watch?v=k5Xgt31yK2U&t=1002s)** makes sort of kind of sense in the ginger to file you notice there are no quotation marks so

**[16:49](https://youtube.com/watch?v=k5Xgt31yK2U&t=1009s)** I should put these two side by side real quick you can see that the caddy user here is in quotes but

**[16:54](https://youtube.com/watch?v=k5Xgt31yK2U&t=1014s)** in the actual ginger to file it isn't it's not a mistake that is just the way it's supposed to be

**[17:00](https://youtube.com/watch?v=k5Xgt31yK2U&t=1020s)** now here we've also got the exec start and the exec reload this is pointing at the specific binary

**[17:05](https://youtube.com/watch?v=k5Xgt31yK2U&t=1025s)** path where caddy's binary got installed to by the previous task in the playbook and then that's

**[17:11](https://youtube.com/watch?v=k5Xgt31yK2U&t=1031s)** it the caddy binary is installed and the system D service is also installed but at this point

**[17:16](https://youtube.com/watch?v=k5Xgt31yK2U&t=1036s)** it doesn't have a configuration so what we need to do is actually install that configuration

**[17:21](https://youtube.com/watch?v=k5Xgt31yK2U&t=1041s)** if we jump back to our main.yaml file we can see we've got a bunch of tasks here that get executed

**[17:26](https://youtube.com/watch?v=k5Xgt31yK2U&t=1046s)** in order the last one is configure so taking a look at configure you can see the first task here

**[17:32](https://youtube.com/watch?v=k5Xgt31yK2U&t=1052s)** just essentially make sure that the target directory for the configuration file exists which

**[17:37](https://youtube.com/watch?v=k5Xgt31yK2U&t=1057s)** is the caddy file path which gets defined in the defaults file over here caddy file path in this

**[17:43](https://youtube.com/watch?v=k5Xgt31yK2U&t=1063s)** case is slash Etsy slash caddy now back to the configure yaml file over here we're going to write

**[17:50](https://youtube.com/watch?v=k5Xgt31yK2U&t=1070s)** out the caddy file and if you are a ginger nerd like I am you're going to love this so take a

**[17:56](https://youtube.com/watch?v=k5Xgt31yK2U&t=1076s)** quick look at the caddy file right here we can do loops we can do for loops we can iterate over this

**[18:02](https://youtube.com/watch?v=k5Xgt31yK2U&t=1082s)** file and start doing all sorts of ifs and fors and it's it's really cool so what we're going to do

**[18:09](https://youtube.com/watch?v=k5Xgt31yK2U&t=1089s)** now is provide the ginger templating module the Ansible is calling with a bunch of variables

**[18:14](https://youtube.com/watch?v=k5Xgt31yK2U&t=1094s)** and we're going to present these in this folder here called groupfars so take a quick look at

**[18:18](https://youtube.com/watch?v=k5Xgt31yK2U&t=1098s)** this caddy file here this is a list of dictionaries in yaml parlance and you can see here that each

**[18:25](https://youtube.com/watch?v=k5Xgt31yK2U&t=1105s)** grouping is again denoted by this little hash this line at the beginning of the grouping

**[18:30](https://youtube.com/watch?v=k5Xgt31yK2U&t=1110s)** of dictionary within yaml and under this data structure here of caddy underscore end points

**[18:37](https://youtube.com/watch?v=k5Xgt31yK2U&t=1117s)** we can see we've got a bunch of information so friendly name fully qualified domain name upstream

**[18:43](https://youtube.com/watch?v=k5Xgt31yK2U&t=1123s)** TLS insecure provider etc okay so let's step through the templating process that's going to happen

**[18:50](https://youtube.com/watch?v=k5Xgt31yK2U&t=1130s)** with ginger on the left hand side we can see that if caddy TLS providers is defined well up here yes

**[18:57](https://youtube.com/watch?v=k5Xgt31yK2U&t=1137s)** it is defined for item in this list of dictionaries what I want to do is iterate over each group so

**[19:04](https://youtube.com/watch?v=k5Xgt31yK2U&t=1144s)** I could have multiple providers here for example if I wanted to remember caddy itself only supports

**[19:10](https://youtube.com/watch?v=k5Xgt31yK2U&t=1150s)** cloud flare for now with how the role is configured but this is an exercise for the reader if they

**[19:14](https://youtube.com/watch?v=k5Xgt31yK2U&t=1154s)** want to configure it themselves so taking a quick look at this um dictionary here we can see we've

**[19:20](https://youtube.com/watch?v=k5Xgt31yK2U&t=1160s)** now got two dictionaries within side this list okay I'm going to go back to one because we don't

**[19:25](https://youtube.com/watch?v=k5Xgt31yK2U&t=1165s)** need to because they'll be the same um we're going to iterate so four item in caddy TLS providers we're

**[19:32](https://youtube.com/watch?v=k5Xgt31yK2U&t=1172s)** going to take each item from each provider so item dot provider now is referring to the value

**[19:39](https://youtube.com/watch?v=k5Xgt31yK2U&t=1179s)** cloud flare but essentially what it's going to do is just output a caddy file formatted in the way

**[19:45](https://youtube.com/watch?v=k5Xgt31yK2U&t=1185s)** that caddy is expecting to call a DNS challenge so we need to provide a few things to do that and

**[19:50](https://youtube.com/watch?v=k5Xgt31yK2U&t=1190s)** one of them is an API token and this really is the magic of why I love this method so much I've

**[19:57](https://youtube.com/watch?v=k5Xgt31yK2U&t=1197s)** used it for my Docker compose files for years at this point six or seven years at this point

**[20:02](https://youtube.com/watch?v=k5Xgt31yK2U&t=1202s)** and I lost I love to roll this out whenever I can and show this off to people because I just think

**[20:06](https://youtube.com/watch?v=k5Xgt31yK2U&t=1206s)** it's the coolest implementation of taking a plain text secret and actually making it somewhat secure

**[20:13](https://youtube.com/watch?v=k5Xgt31yK2U&t=1213s)** and being able to commit it to source control so this value here of cloud flare API token actually

**[20:19](https://youtube.com/watch?v=k5Xgt31yK2U&t=1219s)** gets stored on disk as an encrypted value so under this vast directory here remember I'm going

**[20:25](https://youtube.com/watch?v=k5Xgt31yK2U&t=1225s)** right back to the beginning now so just bear with me on the directory structure on the left hand

**[20:31](https://youtube.com/watch?v=k5Xgt31yK2U&t=1231s)** side where it says run dot yaml remember we can figure this secrets dot yaml to be pulled in at

**[20:35](https://youtube.com/watch?v=k5Xgt31yK2U&t=1235s)** runtime this is what that file looks like right now so you can see there are two tokens here we've

**[20:42](https://youtube.com/watch?v=k5Xgt31yK2U&t=1242s)** got an API token well actually should only be one I think that was me testing earlier so we've got one

**[20:48](https://youtube.com/watch?v=k5Xgt31yK2U&t=1248s)** token here okay just one and in this cloud flare API token is is the value that I generated in my

**[20:56](https://youtube.com/watch?v=k5Xgt31yK2U&t=1256s)** cloud flare dashboard so let me show you how I did that real quick just so you have it on record

**[21:00](https://youtube.com/watch?v=k5Xgt31yK2U&t=1260s)** get logged in to your cloud flare dashboard make sure your domain is activated and registered

**[21:05](https://youtube.com/watch?v=k5Xgt31yK2U&t=1265s)** and then go over to your account where it says my profile up in the top right hand corner

**[21:10](https://youtube.com/watch?v=k5Xgt31yK2U&t=1270s)** and click on API tokens next we want to just go over and make sure we've got

**[21:16](https://youtube.com/watch?v=k5Xgt31yK2U&t=1276s)** this specific thing configured so if we go to the summary we want to make sure we've got the

**[21:21](https://youtube.com/watch?v=k5Xgt31yK2U&t=1281s)** following things enabled zone read and DNS edit now I'm going to roll this token just so that I

**[21:27](https://youtube.com/watch?v=k5Xgt31yK2U&t=1287s)** get a fresh one for this video I'm going to paste that in and we should be good to go now remember

**[21:32](https://youtube.com/watch?v=k5Xgt31yK2U&t=1292s)** how I'm using just as an aid memoir for all of my various commands one of the things that's in my

**[21:37](https://youtube.com/watch?v=k5Xgt31yK2U&t=1297s)** just file is a way to encrypt this value so there is a vault option down here on line 22 so what I

**[21:44](https://youtube.com/watch?v=k5Xgt31yK2U&t=1304s)** can do is do just vault encrypt what that's going to do is call Ansible Vaults encryption tool

**[21:51](https://youtube.com/watch?v=k5Xgt31yK2U&t=1311s)** to encrypt this file is going to do that using a password that's configured in Ansible config so

**[21:58](https://youtube.com/watch?v=k5Xgt31yK2U&t=1318s)** Ansible dot config over here has a file for the vault password file at dot vault password now

**[22:06](https://youtube.com/watch?v=k5Xgt31yK2U&t=1326s)** this is such a secure password oh my goodness I don't know how anybody's going to break that with

**[22:12](https://youtube.com/watch?v=k5Xgt31yK2U&t=1332s)** a quantum computer but the idea is rather than me typing it on the command line this happens

**[22:17](https://youtube.com/watch?v=k5Xgt31yK2U&t=1337s)** automatically and this kind of detail is really important when you want to start using Ansible

**[22:22](https://youtube.com/watch?v=k5Xgt31yK2U&t=1342s)** in a CI environment okay so I'm going to do just vault encrypt and you'll see that underneath now

**[22:28](https://youtube.com/watch?v=k5Xgt31yK2U&t=1348s)** my secrets file this happens in real time by the way if I type decrypt now you'll see that it's

**[22:33](https://youtube.com/watch?v=k5Xgt31yK2U&t=1353s)** now decrypted and I'm going to just encrypt it again and voila we now have a completely safe

**[22:40](https://youtube.com/watch?v=k5Xgt31yK2U&t=1360s)** apart from the passwords kind of rubbish we have a completely safe file that we can commit to

**[22:46](https://youtube.com/watch?v=k5Xgt31yK2U&t=1366s)** source control here and so this means we can provide sensitive information securely or at least

**[22:51](https://youtube.com/watch?v=k5Xgt31yK2U&t=1371s)** relatively securely because it still ends up in plain text on the disk of the remote host remember

**[22:56](https://youtube.com/watch?v=k5Xgt31yK2U&t=1376s)** but it's not going to end up in source control on the public internet as a clear text secret at least

**[23:02](https://youtube.com/watch?v=k5Xgt31yK2U&t=1382s)** this is now going to be substituted into our caddy file using Ansible ginger to templating engine

**[23:08](https://youtube.com/watch?v=k5Xgt31yK2U&t=1388s)** so let's jump back to the configure tasks that are happening and just take another look at the caddy

**[23:13](https://youtube.com/watch?v=k5Xgt31yK2U&t=1393s)** file that's being configured right here so we've jumped through the first few hoops we've

**[23:18](https://youtube.com/watch?v=k5Xgt31yK2U&t=1398s)** got our provider configured this is what's going to tell caddy how to actually talk to cloud flare

**[23:24](https://youtube.com/watch?v=k5Xgt31yK2U&t=1404s)** and configure the DNS challenge side of getting our TLS certificate and then the final part here is

**[23:29](https://youtube.com/watch?v=k5Xgt31yK2U&t=1409s)** the caddy endpoints this is where it's going to loop over the list of dictionaries defined in my

**[23:34](https://youtube.com/watch?v=k5Xgt31yK2U&t=1414s)** group vars so in this specific role i've only got one one host configured but i can very easily

**[23:41](https://youtube.com/watch?v=k5Xgt31yK2U&t=1421s)** configure two three four twenty a thousand different hosts to be reversed proxied by this instance

**[23:47](https://youtube.com/watch?v=k5Xgt31yK2U&t=1427s)** and all i would have to do is add these three or four lines here and you could probably make this

**[23:52](https://youtube.com/watch?v=k5Xgt31yK2U&t=1432s)** a lot cleaner if you're so inclined but i didn't think four or five lines was too bad

**[23:59](https://youtube.com/watch?v=k5Xgt31yK2U&t=1439s)** so the idea is that once this is done we run one command against our remote host

**[24:03](https://youtube.com/watch?v=k5Xgt31yK2U&t=1443s)** and our caddy file gets configured caddy gets started and the system d service also gets started

**[24:09](https://youtube.com/watch?v=k5Xgt31yK2U&t=1449s)** in that process caddy will handle the automated TLS of getting us a lecture certificate

**[24:15](https://youtube.com/watch?v=k5Xgt31yK2U&t=1455s)** for our own custom domain we're not relying on ts.net here or cloud flare tunnels as i mentioned

**[24:21](https://youtube.com/watch?v=k5Xgt31yK2U&t=1461s)** or any other kind of proxying it's just connecting the caddy reverse proxy over tail scale with a

**[24:27](https://youtube.com/watch?v=k5Xgt31yK2U&t=1467s)** direct connection almost certainly back to your local instance of jelly fin running in your house

**[24:33](https://youtube.com/watch?v=k5Xgt31yK2U&t=1473s)** in in in my basement in my case so let's go ahead and actually configure and and show you how this

**[24:38](https://youtube.com/watch?v=k5Xgt31yK2U&t=1478s)** is doing i'm going to try and upset the demo gods right now and do this in real time i don't know

**[24:44](https://youtube.com/watch?v=k5Xgt31yK2U&t=1484s)** what i'm thinking but here we go so what i want to do is uh to start with i'm going to use my

**[24:50](https://youtube.com/watch?v=k5Xgt31yK2U&t=1490s)** just file to actually create the terraform resource which in my case is a digital ocean droplet

**[24:58](https://youtube.com/watch?v=k5Xgt31yK2U&t=1498s)** now you can see that already this virtual machine is being created in front of our very eyes

**[25:03](https://youtube.com/watch?v=k5Xgt31yK2U&t=1503s)** once that's created and we have an IP address a public IP address for this host we do need to

**[25:08](https://youtube.com/watch?v=k5Xgt31yK2U&t=1508s)** create the DNS record in cloud flare so that when you're out and about on the public internet

**[25:12](https://youtube.com/watch?v=k5Xgt31yK2U&t=1512s)** you can actually resolve the reverse proxy you're not exposing well you are kind of exposing

**[25:18](https://youtube.com/watch?v=k5Xgt31yK2U&t=1518s)** your land to the internet but not directly it's all over tail scale once it gets to the reverse proxy

**[25:23](https://youtube.com/watch?v=k5Xgt31yK2U&t=1523s)** but you are putting this on the public internet in so much as that this domain name will be

**[25:27](https://youtube.com/watch?v=k5Xgt31yK2U&t=1527s)** rootable from anybody anywhere on the internet so just bear that in mind set up some firewall rules

**[25:33](https://youtube.com/watch?v=k5Xgt31yK2U&t=1533s)** to geo block certain countries you're not in so once i have this IP address i'm just going to copy

**[25:37](https://youtube.com/watch?v=k5Xgt31yK2U&t=1537s)** this into my cloud flare DNS profile for my domain so the cloud flare dashboard always confuses me

**[25:45](https://youtube.com/watch?v=k5Xgt31yK2U&t=1545s)** a little bit but over here on the right hand side i've got in a tech labs dot dev and then on the

**[25:50](https://youtube.com/watch?v=k5Xgt31yK2U&t=1550s)** left hand side i've got my DNS records over here i'm just going to add a very simple a record

**[25:56](https://youtube.com/watch?v=k5Xgt31yK2U&t=1556s)** i'm then going to give it a name in my case of jf for jellyfin and then i'm going to give it the

**[26:01](https://youtube.com/watch?v=k5Xgt31yK2U&t=1561s)** IP v4 address of the digital ocean droplet i'm going to uncheck the proxy status thing because i

**[26:07](https://youtube.com/watch?v=k5Xgt31yK2U&t=1567s)** don't want cloud flare proxying all of my video traffic in this case and then i'm going to click save

**[26:12](https://youtube.com/watch?v=k5Xgt31yK2U&t=1572s)** now this DNS piece potentially is the bit that will take the longest to propagate

**[26:17](https://youtube.com/watch?v=k5Xgt31yK2U&t=1577s)** so what i want to do whilst that's propagating is just check that the vm got added to my

**[26:22](https://youtube.com/watch?v=k5Xgt31yK2U&t=1582s)** talent correctly i'm going to jump into my tail scale machines page and hey look at that

**[26:27](https://youtube.com/watch?v=k5Xgt31yK2U&t=1587s)** NYC one terraform caddy is now on my tail net i'm going to click on the ssh button because i also

**[26:33](https://youtube.com/watch?v=k5Xgt31yK2U&t=1593s)** enable ssh change the username to zafod and this is going to open a brand new ssh session in the browser

**[26:41](https://youtube.com/watch?v=k5Xgt31yK2U&t=1601s)** by the way you don't need to use a terminal sometimes and i'm just going to connect to the console

**[26:46](https://youtube.com/watch?v=k5Xgt31yK2U&t=1606s)** of this virtual machine over tail scale ssh with a quick ephemeral session that we set up

**[26:51](https://youtube.com/watch?v=k5Xgt31yK2U&t=1611s)** in the browser voila there we go look at that isn't that fantastic and you can even see in the

**[26:56](https://youtube.com/watch?v=k5Xgt31yK2U&t=1616s)** background that the ssh console is ephemeral so that means once i disconnect it's going to automatically

**[27:02](https://youtube.com/watch?v=k5Xgt31yK2U&t=1622s)** remove itself from my tail net so this just proves to me that tail scale ssh is working exactly

**[27:07](https://youtube.com/watch?v=k5Xgt31yK2U&t=1627s)** as it should the virtual machine is up and stable and it's been up for two minutes

**[27:12](https://youtube.com/watch?v=k5Xgt31yK2U&t=1632s)** okay so now it is time to go ahead and actually try and run the Ansible role against this machine

**[27:18](https://youtube.com/watch?v=k5Xgt31yK2U&t=1638s)** so we can see that terraform completed successfully we know that our machine is on tail scale ssh

**[27:24](https://youtube.com/watch?v=k5Xgt31yK2U&t=1644s)** it's on our tail net all right demo gods be kind to me i'm going to do just run caddy remember i

**[27:31](https://youtube.com/watch?v=k5Xgt31yK2U&t=1651s)** already did the just rex to get the prerequisites if you forget what that looks like

**[27:36](https://youtube.com/watch?v=k5Xgt31yK2U&t=1656s)** just rex looks like this that installs the caddy role from github that i wrote to configure my caddy

**[27:43](https://youtube.com/watch?v=k5Xgt31yK2U&t=1663s)** virtual machine i've got my fully qualified domain name here of jf.initeclabs.dev

**[27:49](https://youtube.com/watch?v=k5Xgt31yK2U&t=1669s)** proxying to the upstream location of fake nas colon 2285 so it really is time to actually run

**[27:56](https://youtube.com/watch?v=k5Xgt31yK2U&t=1676s)** the Ansible now so i'm going to do just run caddy which is if we take a quick look at my

**[28:01](https://youtube.com/watch?v=k5Xgt31yK2U&t=1681s)** just file over here just run is the shorthand for Ansible playbook dash b for become or root

**[28:09](https://youtube.com/watch?v=k5Xgt31yK2U&t=1689s)** user and then we're going to run the run.yaml playbook and limit it to a specific host which in my case

**[28:15](https://youtube.com/watch?v=k5Xgt31yK2U&t=1695s)** is caddy now i didn't talk you through the hosts file i really should do that before i press go

**[28:20](https://youtube.com/watch?v=k5Xgt31yK2U&t=1700s)** if we look at the hosts file this is where it starts to get pretty interesting so there's a few

**[28:25](https://youtube.com/watch?v=k5Xgt31yK2U&t=1705s)** things going on here that you need to be aware of first of all line one this is the grouping of hosts

**[28:31](https://youtube.com/watch?v=k5Xgt31yK2U&t=1711s)** now i could have multiple hosts here i could have NYC2 which i think co-pilot was trying to do for me

**[28:37](https://youtube.com/watch?v=k5Xgt31yK2U&t=1717s)** yes there we go you know i could have multiple hosts in here i could have you know web servers i could

**[28:44](https://youtube.com/watch?v=k5Xgt31yK2U&t=1724s)** have you know web one i could have database right that's the idea of these groups is you you can

**[28:50](https://youtube.com/watch?v=k5Xgt31yK2U&t=1730s)** start to group hosts in specific groups and then you can use group files to apply specific variables

**[28:57](https://youtube.com/watch?v=k5Xgt31yK2U&t=1737s)** to all of those hosts that live within a specific group around into some weirdness with host

**[29:03](https://youtube.com/watch?v=k5Xgt31yK2U&t=1743s)** files a few years ago i can't remember the specifics but i always just use group files and then i

**[29:07](https://youtube.com/watch?v=k5Xgt31yK2U&t=1747s)** put maybe one host in that specific group and it works for me so up to you your mileage may vary if

**[29:13](https://youtube.com/watch?v=k5Xgt31yK2U&t=1753s)** you get confused reading your documentation about host files versus group files just tell them

**[29:18](https://youtube.com/watch?v=k5Xgt31yK2U&t=1758s)** Alex sent you and then it all be fine okay hand wave time so the next thing we need to look at is

**[29:25](https://youtube.com/watch?v=k5Xgt31yK2U&t=1765s)** the host name or the IP address that we're connecting to in our case NYC one terraform caddy

**[29:30](https://youtube.com/watch?v=k5Xgt31yK2U&t=1770s)** is the DNS hostname that gets applied to that specific host by tail scale so if we take a quick

**[29:35](https://youtube.com/watch?v=k5Xgt31yK2U&t=1775s)** look at the addresses that are here we could if we wanted to substitute this for the fully qualified

**[29:40](https://youtube.com/watch?v=k5Xgt31yK2U&t=1780s)** domain name of our tailnet if we want to get really fancy but this is going to work just fine as well

**[29:46](https://youtube.com/watch?v=k5Xgt31yK2U&t=1786s)** this could also be the public IP address of the server if you have ssh keys installed manually

**[29:51](https://youtube.com/watch?v=k5Xgt31yK2U&t=1791s)** but we don't i didn't install any ssh keys for this is a ford user i'm simply relying on the tail

**[29:57](https://youtube.com/watch?v=k5Xgt31yK2U&t=1797s)** scale tailnet just by virtue of being on my tailnet for authentication with the remote node to say

**[30:04](https://youtube.com/watch?v=k5Xgt31yK2U&t=1804s)** hey this is definitely Alex you can you can allow him to ssh into this node as a z ford user

**[30:10](https://youtube.com/watch?v=k5Xgt31yK2U&t=1810s)** so in order for tailscale ssh to work and in order for this whole thing to work this name here

**[30:15](https://youtube.com/watch?v=k5Xgt31yK2U&t=1815s)** must match the name that's in your tailscale admin console all right with all of that said it's time

**[30:21](https://youtube.com/watch?v=k5Xgt31yK2U&t=1821s)** to actually push go at the bottom here i'm going to type just run caddy at last and if this is

**[30:26](https://youtube.com/watch?v=k5Xgt31yK2U&t=1826s)** the first time you've ever seen antibles output it can seem a little daunting sometimes with all

**[30:31](https://youtube.com/watch?v=k5Xgt31yK2U&t=1831s)** these stars going across the screen and stuff but if you actually take a moment to look at it

**[30:36](https://youtube.com/watch?v=k5Xgt31yK2U&t=1836s)** we're just running stuff we've we've looked through in the code manually we're running the is caddy

**[30:41](https://youtube.com/watch?v=k5Xgt31yK2U&t=1841s)** binary present check and then we're installing caddy and including certain files and installing

**[30:48](https://youtube.com/watch?v=k5Xgt31yK2U&t=1848s)** system d servers we're not doing anything that isn't already named in the playbooks and the roles

**[30:53](https://youtube.com/watch?v=k5Xgt31yK2U&t=1853s)** and the tasks uh once we get right and drill right down into it and you can see that we've finally

**[30:59](https://youtube.com/watch?v=k5Xgt31yK2U&t=1859s)** actually gotten to the point where caddy is installed and configured at least i hope so anyway so

**[31:05](https://youtube.com/watch?v=k5Xgt31yK2U&t=1865s)** now it's time to ssh into that host as z ford so again we can use tailscale ssh to ssh into that remote

**[31:14](https://youtube.com/watch?v=k5Xgt31yK2U&t=1874s)** host and hopefully if i do a system ctl status caddy we can see that caddy is running and again

**[31:22](https://youtube.com/watch?v=k5Xgt31yK2U&t=1882s)** even more hopefully this is all happening in real time we can do jf dot in a tech labs dot dev oh please

**[31:32](https://youtube.com/watch?v=k5Xgt31yK2U&t=1892s)** work array it actually seems to have worked first time in a demo that's actually a first for me

**[31:42](https://youtube.com/watch?v=k5Xgt31yK2U&t=1902s)** okay cool there was no even any movie magic going on about this demo for once so what we can see now

**[31:48](https://youtube.com/watch?v=k5Xgt31yK2U&t=1908s)** is that my jelly fin is now on the public internet with a tls certificate on a domain i own using

**[31:56](https://youtube.com/watch?v=k5Xgt31yK2U&t=1916s)** nothing but cloud init terraform and answer ball how easy was that there's so much technology

**[32:04](https://youtube.com/watch?v=k5Xgt31yK2U&t=1924s)** gone into what you've just seen there and i'm aware that that took a long time to explain on video

**[32:09](https://youtube.com/watch?v=k5Xgt31yK2U&t=1929s)** but the reality is we can actually destroy this virtual machine and spin it up in under five

**[32:13](https://youtube.com/watch?v=k5Xgt31yK2U&t=1933s)** minutes and get this caddy stuff configured automatically so let's say hypothetically you travel

**[32:21](https://youtube.com/watch?v=k5Xgt31yK2U&t=1941s)** for work i don't know a few times a year you don't necessarily need to access your jelly fin all the

**[32:28](https://youtube.com/watch?v=k5Xgt31yK2U&t=1948s)** time but when you're away from the house maybe you want to so you could set this up as a github action

**[32:34](https://youtube.com/watch?v=k5Xgt31yK2U&t=1954s)** or have some kind of home assistant automation that would configure and start off some CI jobs

**[32:39](https://youtube.com/watch?v=k5Xgt31yK2U&t=1959s)** somewhere to deploy this reverse proxy automatically in less than five minutes using cloud init to

**[32:45](https://youtube.com/watch?v=k5Xgt31yK2U&t=1965s)** automatically add it to tailnet and then using terraform to automatically provision that infrastructure

**[32:51](https://youtube.com/watch?v=k5Xgt31yK2U&t=1971s)** on digital ocean you could even take that a step further and add the DNS record automatically using

**[32:56](https://youtube.com/watch?v=k5Xgt31yK2U&t=1976s)** terraform or actually could probably do that using answer ball as it has modules for almost everything

**[33:01](https://youtube.com/watch?v=k5Xgt31yK2U&t=1981s)** in the entire known universe as well so and then finally you can configure the caddy reverse proxy

**[33:08](https://youtube.com/watch?v=k5Xgt31yK2U&t=1988s)** using answer ball automatically as well and remember that this caddy node is just another node

**[33:14](https://youtube.com/watch?v=k5Xgt31yK2U&t=1994s)** on your tailnet so i'm going to just jump back to the console of this digital ocean droplet right here

**[33:21](https://youtube.com/watch?v=k5Xgt31yK2U&t=2001s)** and do a tailscale status just a kind of hammer at home for you this laptop right here is the one i'm

**[33:26](https://youtube.com/watch?v=k5Xgt31yK2U&t=2006s)** using to record this video it's behind a residential firewall there are no ports open there's no

**[33:32](https://youtube.com/watch?v=k5Xgt31yK2U&t=2012s)** you know UP and P or whatever that's that you know going on the games consoles like to try and punch

**[33:38](https://youtube.com/watch?v=k5Xgt31yK2U&t=2018s)** through firewalls with this is all happening over what tailscale calls natural versus so if I do

**[33:44](https://youtube.com/watch?v=k5Xgt31yK2U&t=2024s)** tailscale ping and then put in the name of MVP ball trick which is the name of this computer

**[33:50](https://youtube.com/watch?v=k5Xgt31yK2U&t=2030s)** you can see i've got a direct connection it's not even going through a bounce server which we'd

**[33:54](https://youtube.com/watch?v=k5Xgt31yK2U&t=2034s)** call a dirt server a relay proxy this is just a direct connection from that host where caddy is

**[34:01](https://youtube.com/watch?v=k5Xgt31yK2U&t=2041s)** running in the cloud straight back to this local laptop direct connection there's no middleman

**[34:07](https://youtube.com/watch?v=k5Xgt31yK2U&t=2047s)** whatsoever so you could start spinning up stuff at friends houses parent houses if you have the joy

**[34:14](https://youtube.com/watch?v=k5Xgt31yK2U&t=2054s)** of having colo in your life for a collocated server or something that too firewalls become kind of

**[34:21](https://youtube.com/watch?v=k5Xgt31yK2U&t=2061s)** invisible with tailscale and that really is one of the magical parts of using it and then when

**[34:26](https://youtube.com/watch?v=k5Xgt31yK2U&t=2066s)** you're done of course we are just using infrastructure as code it's just one command to clean it all

**[34:32](https://youtube.com/watch?v=k5Xgt31yK2U&t=2072s)** up again if I type just destroy it's going to do the terraform thing of saying are you sure you

**[34:37](https://youtube.com/watch?v=k5Xgt31yK2U&t=2077s)** want to do this and if I go back to my web browser and back to digital ocean in just a few seconds

**[34:44](https://youtube.com/watch?v=k5Xgt31yK2U&t=2084s)** we'll see the NYC one terraform caddy disappears ceases to be becomes an ex-parat a droplet I mean

**[34:53](https://youtube.com/watch?v=k5Xgt31yK2U&t=2093s)** there you go it's gone so in the background you can see terraform still doing its thing but

**[34:57](https://youtube.com/watch?v=k5Xgt31yK2U&t=2097s)** so far as DO is concerned the node is gone now you'll also notice on our tailnet as well that this

**[35:03](https://youtube.com/watch?v=k5Xgt31yK2U&t=2103s)** is an ephemeral node so because I set ephemeral when I generated my auth key which I covered in part

**[35:10](https://youtube.com/watch?v=k5Xgt31yK2U&t=2110s)** two but I'll just show you real quick just in case you got this far settings keys and then generate

**[35:16](https://youtube.com/watch?v=k5Xgt31yK2U&t=2116s)** auth key over here I set this to be ephemeral and what that means is that when the device is removed

**[35:23](https://youtube.com/watch?v=k5Xgt31yK2U&t=2123s)** from my tailnet and goes offline eventually after a few minutes tailscale will automatically go

**[35:29](https://youtube.com/watch?v=k5Xgt31yK2U&t=2129s)** ahead and clean up those ephemeral nodes on the regular for you so I'm not sure if this will be

**[35:33](https://youtube.com/watch?v=k5Xgt31yK2U&t=2133s)** the end of the infrastructure as code playlist forever but it's certainly the end for right now

**[35:38](https://youtube.com/watch?v=k5Xgt31yK2U&t=2138s)** we've looked at three really core DevOps technologies in the last few weeks cloud in it terraform

**[35:43](https://youtube.com/watch?v=k5Xgt31yK2U&t=2143s)** and answerable if there's another technology that you would love to hear about and how you could

**[35:47](https://youtube.com/watch?v=k5Xgt31yK2U&t=2147s)** use it with tailscale maybe something like pelumi or you want to see this with a different cloud

**[35:51](https://youtube.com/watch?v=k5Xgt31yK2U&t=2151s)** provider maybe AWS or I don't know who you guys are using let me know in the comments down below

**[35:56](https://youtube.com/watch?v=k5Xgt31yK2U&t=2156s)** so I hope you found today's video useful and I hope I introduced a few of you to some new concepts

**[36:01](https://youtube.com/watch?v=k5Xgt31yK2U&t=2161s)** and of course introduced some of you to Michael Portillo and his great British railway journeys

**[36:06](https://youtube.com/watch?v=k5Xgt31yK2U&t=2166s)** wow they are fantastic until next time thank you so much for watching I've been Alex from tailscale

---

*Automatically generated transcript. May contain errors.*
