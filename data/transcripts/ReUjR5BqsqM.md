---
video_id: "ReUjR5BqsqM"
title: "Tailscale Up: Pulumi Connecti"
description: "This talk was given by Lee Birggs at Tailscale Up in San Francisco on Wednesday, May 31, 2023...."
channel_name: "Tailscale"
channel_id: "UCcdv38QxPjSMqbt5ffLhJLA"
published_at: "2023-07-07"
duration_seconds: 249
youtube_url: "https://www.youtube.com/watch?v=ReUjR5BqsqM"
thumbnail_url: "https://i.ytimg.com/vi_webp/ReUjR5BqsqM/maxresdefault.webp"

# Transcription metadata
transcribed_at: "2025-10-03T16:20:02.275979"
transcription_method: "cpu"
model_used: "base"
language: "en"
word_count: 778
transcription_time_seconds: 6.8
---

# Tailscale Up: Pulumi Connecti

**[00:00](https://youtube.com/watch?v=ReUjR5BqsqM&t=0s)** OK, so I'm here to tell you a little bit about something I built with Tailscale and Pulumi

**[00:05](https://youtube.com/watch?v=ReUjR5BqsqM&t=5s)** that solves a problem that I have probably once a week, almost every day.

**[00:09](https://youtube.com/watch?v=ReUjR5BqsqM&t=9s)** I'm not going to waste time on introductions, but if you want to follow me on social media

**[00:12](https://youtube.com/watch?v=ReUjR5BqsqM&t=12s)** and all that kind of jazz, there it is. So, picture the scene, you have some cloud infrastructure,

**[00:18](https://youtube.com/watch?v=ReUjR5BqsqM&t=18s)** you haven't convinced your organization to buy Tailscale yet or you are a start-up

**[00:24](https://youtube.com/watch?v=ReUjR5BqsqM&t=24s)** and you haven't really thought about VPNs, and you have a bunch of infrastructure in the cloud,

**[00:29](https://youtube.com/watch?v=ReUjR5BqsqM&t=29s)** and you want to connect to it in a private network.

**[00:33](https://youtube.com/watch?v=ReUjR5BqsqM&t=33s)** Some examples of things that come up regularly when I'm helping customers with Pulumi

**[00:37](https://youtube.com/watch?v=ReUjR5BqsqM&t=37s)** and their infrastructure's code journey is they want to run a database migration.

**[00:41](https://youtube.com/watch?v=ReUjR5BqsqM&t=41s)** Or they want a debugger container that's broken.

**[00:43](https://youtube.com/watch?v=ReUjR5BqsqM&t=43s)** Or they have put their Kubernetes control plane in an AWS VPC in a private network

**[00:48](https://youtube.com/watch?v=ReUjR5BqsqM&t=48s)** and they want to actually access it to do some stuff.

**[00:51](https://youtube.com/watch?v=ReUjR5BqsqM&t=51s)** Or they want to actually log into an EC2 instance or an Azure instance and actually kill a process.

**[00:56](https://youtube.com/watch?v=ReUjR5BqsqM&t=56s)** All of those things regularly come up in our community channel and they're all a networking problem

**[01:01](https://youtube.com/watch?v=ReUjR5BqsqM&t=61s)** and they're not an infrastructure's code problem.

**[01:03](https://youtube.com/watch?v=ReUjR5BqsqM&t=63s)** So, I got tired of saying this is a network problem, not a Pulumi problem,

**[01:09](https://youtube.com/watch?v=ReUjR5BqsqM&t=69s)** and I built something that uses Pulumi's automation API to largely solve this problem.

**[01:13](https://youtube.com/watch?v=ReUjR5BqsqM&t=73s)** So, what does this look like?

**[01:15](https://youtube.com/watch?v=ReUjR5BqsqM&t=75s)** Demo gods and all that kind of stuff.

**[01:17](https://youtube.com/watch?v=ReUjR5BqsqM&t=77s)** So, I provisioned an AWS VPC, connect to supports three different cloud providers right now,

**[01:21](https://youtube.com/watch?v=ReUjR5BqsqM&t=81s)** AWS, Azure and Kubernetes.

**[01:23](https://youtube.com/watch?v=ReUjR5BqsqM&t=83s)** But I provisioned an AWS VPC and you can see here in this VPC and we bump this up a little bit.

**[01:29](https://youtube.com/watch?v=ReUjR5BqsqM&t=89s)** In this VPC, there is an RDS instance of database that I want to connect to.

**[01:35](https://youtube.com/watch?v=ReUjR5BqsqM&t=95s)** And if I try and connect to that right now, I cannot because I am not in the same network.

**[01:40](https://youtube.com/watch?v=ReUjR5BqsqM&t=100s)** So, if I run a single command to specify the routes that are in the AWS VPC

**[01:49](https://youtube.com/watch?v=ReUjR5BqsqM&t=109s)** and the subnet IDs that I want to create a tailscale subnet router in,

**[01:54](https://youtube.com/watch?v=ReUjR5BqsqM&t=114s)** it will go ahead and do all of that work for me.

**[01:57](https://youtube.com/watch?v=ReUjR5BqsqM&t=117s)** I don't have to do anything.

**[01:58](https://youtube.com/watch?v=ReUjR5BqsqM&t=118s)** I don't have to know anything about how AWS works.

**[02:00](https://youtube.com/watch?v=ReUjR5BqsqM&t=120s)** And if we take a look in the Pulumi console, you can see it is creating a bunch of infrastructure.

**[02:07](https://youtube.com/watch?v=ReUjR5BqsqM&t=127s)** We can go in here and take a look at the activity.

**[02:10](https://youtube.com/watch?v=ReUjR5BqsqM&t=130s)** It's creating a bunch of stuff in here.

**[02:13](https://youtube.com/watch?v=ReUjR5BqsqM&t=133s)** It's creating the tailnet key security group, a private EC2 instance,

**[02:18](https://youtube.com/watch?v=ReUjR5BqsqM&t=138s)** all of the stuff that you actually need to make tailscale work.

**[02:21](https://youtube.com/watch?v=ReUjR5BqsqM&t=141s)** This is essentially codifying the tailscale how to use a subnet router in AWS page

**[02:27](https://youtube.com/watch?v=ReUjR5BqsqM&t=147s)** that's in the documentation, but it's all happening with a single command

**[02:30](https://youtube.com/watch?v=ReUjR5BqsqM&t=150s)** without you having to do anything.

**[02:32](https://youtube.com/watch?v=ReUjR5BqsqM&t=152s)** So, it's going to create an auto scaling group and I'm going to wait for AWS

**[02:35](https://youtube.com/watch?v=ReUjR5BqsqM&t=155s)** to do all the things behind the scenes.

**[02:37](https://youtube.com/watch?v=ReUjR5BqsqM&t=157s)** So, it's going to boot an auto scaling group with an EC2 instance in there.

**[02:41](https://youtube.com/watch?v=ReUjR5BqsqM&t=161s)** And then it needs to run user data.

**[02:43](https://youtube.com/watch?v=ReUjR5BqsqM&t=163s)** So, this has actually created the infrastructure right now,

**[02:45](https://youtube.com/watch?v=ReUjR5BqsqM&t=165s)** and the tailscale subnet router has not appeared because user data needs to run

**[02:49](https://youtube.com/watch?v=ReUjR5BqsqM&t=169s)** and actually install tailscale and expose all the routes.

**[02:52](https://youtube.com/watch?v=ReUjR5BqsqM&t=172s)** But if we take a look in the machines here,

**[02:54](https://youtube.com/watch?v=ReUjR5BqsqM&t=174s)** you can see that I've also provisioned a tailscale,

**[02:59](https://youtube.com/watch?v=ReUjR5BqsqM&t=179s)** a connectie host in Kubernetes.

**[03:04](https://youtube.com/watch?v=ReUjR5BqsqM&t=184s)** So, if I do connectie list,

**[03:08](https://youtube.com/watch?v=ReUjR5BqsqM&t=188s)** you can see it's, I've also created a similar thing in Kubernetes.

**[03:13](https://youtube.com/watch?v=ReUjR5BqsqM&t=193s)** And this also works with Azure and GCP is coming very soon.

**[03:16](https://youtube.com/watch?v=ReUjR5BqsqM&t=196s)** So, all of the major cloud providers are spotted.

**[03:18](https://youtube.com/watch?v=ReUjR5BqsqM&t=198s)** I'm add planning on adding digital ocean as well.

**[03:21](https://youtube.com/watch?v=ReUjR5BqsqM&t=201s)** Essentially, just removing all of the pain of actually getting these things open running.

**[03:24](https://youtube.com/watch?v=ReUjR5BqsqM&t=204s)** So, now that I've filled the time a little bit,

**[03:27](https://youtube.com/watch?v=ReUjR5BqsqM&t=207s)** user data should have completed and it's created the tailscale Bastion for me.

**[03:31](https://youtube.com/watch?v=ReUjR5BqsqM&t=211s)** And I can now connect to my SQL instance,

**[03:37](https://youtube.com/watch?v=ReUjR5BqsqM&t=217s)** which I couldn't do 30 seconds ago, maybe a minute ago.

**[03:40](https://youtube.com/watch?v=ReUjR5BqsqM&t=220s)** So, this is an open source.

**[03:42](https://youtube.com/watch?v=ReUjR5BqsqM&t=222s)** It's written in Pulumi's automation API.

**[03:46](https://youtube.com/watch?v=ReUjR5BqsqM&t=226s)** Feel free to take a look.

**[03:47](https://youtube.com/watch?v=ReUjR5BqsqM&t=227s)** There are some bugs.

**[03:48](https://youtube.com/watch?v=ReUjR5BqsqM&t=228s)** It's not designed to be a production ready tool.

**[03:50](https://youtube.com/watch?v=ReUjR5BqsqM&t=230s)** It's designed to really just solve quick and easy problems.

**[03:53](https://youtube.com/watch?v=ReUjR5BqsqM&t=233s)** And I can obviously tear all of this down with a single command as well.

**[04:01](https://youtube.com/watch?v=ReUjR5BqsqM&t=241s)** So, it's a relatively straightforward operation.

**[04:03](https://youtube.com/watch?v=ReUjR5BqsqM&t=243s)** I think that just makes five minutes.

**[04:05](https://youtube.com/watch?v=ReUjR5BqsqM&t=245s)** Thank you very much for listening.

**[04:06](https://youtube.com/watch?v=ReUjR5BqsqM&t=246s)** Hope that's useful to people.

---

*Automatically generated transcript. May contain errors.*
