---
video_id: "MZu_T5YgW5c"
title: "Ask A Tailscale Engineer: What is Tailscale SSH? (full)"
description: "This video walks through Tailscale SSH in beta and details how it works with Tailscale engineers, Brad Fitzpatrick and Maisem Ali.

Many organizations already use Tailscale to protect their SSH sessio..."
channel_name: "Tailscale"
channel_id: "UCcdv38QxPjSMqbt5ffLhJLA"
published_at: "2022-06-22"
duration_seconds: 418
youtube_url: "https://www.youtube.com/watch?v=MZu_T5YgW5c"
thumbnail_url: "https://i.ytimg.com/vi/MZu_T5YgW5c/maxresdefault.jpg"

# Transcription metadata
transcribed_at: "2025-10-03T18:18:33.308202"
transcription_method: "cpu"
model_used: "base"
language: "en"
word_count: 1394
transcription_time_seconds: 11.9
---

# Ask A Tailscale Engineer: What is Tailscale SSH? (full)

**[00:04](https://youtube.com/watch?v=MZu_T5YgW5c&t=4s)** Hi there, I'm Jessica Kennedy from the Tailscale Marketing Team, and today I'm joined by Brad and Messim, who are here to tell us a bit more about a new feature they've been working on. Tailscale SSH. Brad and Messim, can you tell us a bit more about yourselves and what you've been working on here? I am an engineer at Tailscale, working on code things and like the tailscale shared client code that runs on people's machines, but also like the back end and the data plane and the control plane servers that coordinate everything.

**[00:34](https://youtube.com/watch?v=MZu_T5YgW5c&t=34s)** That doesn't involve the web or Swift. Basically the same, I'm also an engineer at Tailscale and I also work on all the things that do not involve me designing stuff.

**[00:45](https://youtube.com/watch?v=MZu_T5YgW5c&t=45s)** So what is Tailscale SSH? Basically we wrote a SSH server that is kind of nicely integrated with Tailscale. It knows your SSH identity so you don't need to have SSH keys or certs and Bastion hosts and all that sort of stuff.

**[01:00](https://youtube.com/watch?v=MZu_T5YgW5c&t=60s)** That sounds great, but does this mean that I have to uninstall open SSH?

**[01:04](https://youtube.com/watch?v=MZu_T5YgW5c&t=64s)** No, Tailscale SSH does not care about open SSH at all, you can run those alongside, you can regain all of your access that does not work Tailscale and everything should just keep working as is.

**[01:14](https://youtube.com/watch?v=MZu_T5YgW5c&t=74s)** That's great, but do I have to use a different port or something?

**[01:18](https://youtube.com/watch?v=MZu_T5YgW5c&t=78s)** No, it's actually pretty interesting. Tailscale SSH only listens on the Tailscale IP, so it will listen on the Tailscale IP for on port 22.

**[01:26](https://youtube.com/watch?v=MZu_T5YgW5c&t=86s)** But the system does not really know about it, so you can run whatever else you want on port 22.

**[01:31](https://youtube.com/watch?v=MZu_T5YgW5c&t=91s)** Very nice, but how does that work?

**[01:34](https://youtube.com/watch?v=MZu_T5YgW5c&t=94s)** We never give it to the operating system. So if you're open SSH or whatever is listening on port 22 on like the unspecified address or you have IP tables rules or something blocking it, it doesn't matter because as long as it makes it to tail scale, the encrypted wire guard packets.

**[01:47](https://youtube.com/watch?v=MZu_T5YgW5c&t=107s)** We decrypt the wire guard stuff and then we see that it's a TCP port 22 connection.

**[01:52](https://youtube.com/watch?v=MZu_T5YgW5c&t=112s)** We just handle it directly inside Tailscale D and it never goes into the kernel and never goes to another user space process on the machine.

**[02:00](https://youtube.com/watch?v=MZu_T5YgW5c&t=120s)** So we could just basically intercept anything that looks like SSH going to ourselves as long as it came over tail scale.

**[02:07](https://youtube.com/watch?v=MZu_T5YgW5c&t=127s)** That's great. So what was the motivation to build tail scale SSH?

**[02:11](https://youtube.com/watch?v=MZu_T5YgW5c&t=131s)** Primarily, we got tired of like sshq distribution.

**[02:15](https://youtube.com/watch?v=MZu_T5YgW5c&t=135s)** Sshq distribution is such a pain.

**[02:18](https://youtube.com/watch?v=MZu_T5YgW5c&t=138s)** The more employees you have, the more complex it gets, the more service you have, the more complex it gets auditing, trying to figure out who has access to what who should have access to what is a pain.

**[02:30](https://youtube.com/watch?v=MZu_T5YgW5c&t=150s)** And then like sshqs go out to think and then you have really build this entire system to distribute sshqs, which we thought we don't really need to because we have a wire guard.

**[02:40](https://youtube.com/watch?v=MZu_T5YgW5c&t=160s)** And it tells us we were.

**[02:42](https://youtube.com/watch?v=MZu_T5YgW5c&t=162s)** Yeah, so I actually have built like the first prototype of this in a like early 2020, like right after I joined tailscale because everyone's early questions was, well, I want to make sshq only accessible over tail scale.

**[02:54](https://youtube.com/watch?v=MZu_T5YgW5c&t=174s)** We've since been doing that tail scale off thing for more things like we have a blog post about our graphana off proxy.

**[02:59](https://youtube.com/watch?v=MZu_T5YgW5c&t=179s)** So internally when we look at our graphana instance, we don't have to log into graphana. It just knows who we are from our tail scale identity.

**[03:05](https://youtube.com/watch?v=MZu_T5YgW5c&t=185s)** We have like an engine X off proxy basically that does the same thing that it passes on the identity information to engine X which can pass it on to your backend application.

**[03:13](https://youtube.com/watch?v=MZu_T5YgW5c&t=193s)** So we're probably going to be doing more and more of this like protocol specific integration with tail scale off for more things because just so convenient.

**[03:22](https://youtube.com/watch?v=MZu_T5YgW5c&t=202s)** So this is really full circle.

**[03:24](https://youtube.com/watch?v=MZu_T5YgW5c&t=204s)** So how do people turn on tail scale ssh?

**[03:27](https://youtube.com/watch?v=MZu_T5YgW5c&t=207s)** So most of the most important you should only have to go to your client that you want to station to under on like tail scale up dash as ssh.

**[03:35](https://youtube.com/watch?v=MZu_T5YgW5c&t=215s)** And that should just enable for the client and if it requires like you to change policies to let a guide you on what to do next.

**[03:40](https://youtube.com/watch?v=MZu_T5YgW5c&t=220s)** And just like we have ACLs today, we can also define ssh policies or instead ssh rules, but like who can.

**[03:47](https://youtube.com/watch?v=MZu_T5YgW5c&t=227s)** You want devices at what as what user.

**[03:50](https://youtube.com/watch?v=MZu_T5YgW5c&t=230s)** One distinction that they'll scale puts in is that you can only a station to your own devices or fact devices.

**[03:57](https://youtube.com/watch?v=MZu_T5YgW5c&t=237s)** So you will not be able to station to like someone else's devices. And that's by design, for example, like I don't want Brad to be able to decide into my machines and to run weird malware.

**[04:08](https://youtube.com/watch?v=MZu_T5YgW5c&t=248s)** So how do you use tail scale ssh and how is it different from what users might expect.

**[04:13](https://youtube.com/watch?v=MZu_T5YgW5c&t=253s)** From like a client side, it's no different. You just use your normal ssh client.

**[04:17](https://youtube.com/watch?v=MZu_T5YgW5c&t=257s)** Either it will just work because you configured it to like not have any double checks, but you can also configure in your policy something called check mode where it like verifies again that you're still present and you know do whatever your author provider wants you to do again.

**[04:29](https://youtube.com/watch?v=MZu_T5YgW5c&t=269s)** So in that case, when you connect, you'll get a little message saying like you have to like do some extra authentication step to prove that you know you're still who you are whatever.

**[04:37](https://youtube.com/watch?v=MZu_T5YgW5c&t=277s)** And people can configure this to be like, you know, once a day. So the beginning of your work day, the first time you ssh you get a little prompt.

**[04:43](https://youtube.com/watch?v=MZu_T5YgW5c&t=283s)** And you can go to a URL to finish it. But instead of having copy paste that if you're already running tail scale on your machine, we just pop your browser up to where you want to go in addition to the message.

**[04:52](https://youtube.com/watch?v=MZu_T5YgW5c&t=292s)** And so then once you go through the web off flow your ssh session just unblocks and your ssh to wherever you need to be.

**[04:59](https://youtube.com/watch?v=MZu_T5YgW5c&t=299s)** But then if you do it again, like throughout the rest of the day or whatever the configured period is, then it just works.

**[05:04](https://youtube.com/watch?v=MZu_T5YgW5c&t=304s)** And without a prompt. And the tail scale control plane is out of the loop at that point.

**[05:09](https://youtube.com/watch?v=MZu_T5YgW5c&t=309s)** That sounds great. So we don't have ssh keys and ssh certs anymore. But what does it mean for my bastion?

**[05:16](https://youtube.com/watch?v=MZu_T5YgW5c&t=316s)** For one, you shouldn't really need a bastion anymore. If you're using tails for ssh, you're you should really consider it just installing tails.

**[05:23](https://youtube.com/watch?v=MZu_T5YgW5c&t=323s)** It's around the machine that you want to ssh into directly. And that way you'll from your client to the server that you want to ssh into it will create a direct connection between them.

**[05:32](https://youtube.com/watch?v=MZu_T5YgW5c&t=332s)** And you're not going through like a bashing on like the east coast while you trying to access a machine on the west coast.

**[05:37](https://youtube.com/watch?v=MZu_T5YgW5c&t=337s)** So it should really help reduce your latency on that.

**[05:40](https://youtube.com/watch?v=MZu_T5YgW5c&t=340s)** That sounds great. So is there anything else you'd like to share about the process of building tail scale ssh as an edge team, wouldn't you learn?

**[05:49](https://youtube.com/watch?v=MZu_T5YgW5c&t=349s)** Learned I guess a lot of things about term caps and the login process on Linux and all the things that open ssh and Pam and system D and all these all these weird things.

**[06:01](https://youtube.com/watch?v=MZu_T5YgW5c&t=361s)** So the lesson and I ended up buying these like Linux internals books that are like this thick and yeah, that was fun.

**[06:09](https://youtube.com/watch?v=MZu_T5YgW5c&t=369s)** Yeah, figuring out like what BT wise do and what TT wise do and what controlling journals do and why they matter was a great learning experience.

**[06:20](https://youtube.com/watch?v=MZu_T5YgW5c&t=380s)** That's wonderful. Well, I feel like you gave a great kind of overview of tail scale ssh and I'm sure people are wondering when is it available?

**[06:29](https://youtube.com/watch?v=MZu_T5YgW5c&t=389s)** It's now available in beta for everyone.

**[06:32](https://youtube.com/watch?v=MZu_T5YgW5c&t=392s)** That's great. And who can use it? Do you have to be on a paid plan?

**[06:36](https://youtube.com/watch?v=MZu_T5YgW5c&t=396s)** Nope, it's included. So it's free for everyone.

**[06:41](https://youtube.com/watch?v=MZu_T5YgW5c&t=401s)** Even better. Well, thank you so much, Brad and messim tail scale ssh is now available for all tail scale plans and we can't wait for you to go try it.

**[06:50](https://youtube.com/watch?v=MZu_T5YgW5c&t=410s)** Thanks guys.

**[06:51](https://youtube.com/watch?v=MZu_T5YgW5c&t=411s)** Go. See you.

**[06:53](https://youtube.com/watch?v=MZu_T5YgW5c&t=413s)** Yeah.

---

*Automatically generated transcript. May contain errors.*
