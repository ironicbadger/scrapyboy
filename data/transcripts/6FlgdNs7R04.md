---
video_id: "6FlgdNs7R04"
title: "Tailscale SSH Session Recording Demo"
description: "In this video, Sam Linville introduces session recording for Tailscale SSH. Session recording allows you to capture the full terminal output of each Tailscale SSH session on your tailnet. These record..."
channel_name: "Tailscale"
channel_id: "UCcdv38QxPjSMqbt5ffLhJLA"
published_at: "2023-05-11"
duration_seconds: 422
youtube_url: "https://www.youtube.com/watch?v=6FlgdNs7R04"
thumbnail_url: "https://i.ytimg.com/vi/6FlgdNs7R04/hqdefault.jpg"

# Transcription metadata
transcribed_at: "2025-10-03T16:25:51.480873"
transcription_method: "cpu"
model_used: "base"
language: "en"
word_count: 1192
transcription_time_seconds: 10.2
---

# Tailscale SSH Session Recording Demo

**[00:00](https://youtube.com/watch?v=6FlgdNs7R04&t=0s)** Hi, I'm Sam, and I'm a Product Manager at Tailscale. Today, I want to introduce you to session recording for Tailscale SSH. Session recording allows you to capture the full terminal output of each Tailscale SSH session on your tailnet. These recordings will be useful for things like security investigations, audits, and remaining compliant with your network security policies. Session recording for Tailscale SSH works by streaming session logs from the Tailscale SSH server to a special recorder

**[00:31](https://youtube.com/watch?v=6FlgdNs7R04&t=31s)** node that you deploy inside of your tailnet. These recordings are encrypted end-to-end, just like all other traffic in your tailnet, and Tailscale never sees any of this data. To get started, we'll first need to deploy a recorder node. I have a VM here called Dockerhost that I'll use for this project. As you can see, it's not a part of my tailnet. Recorder nodes are Docker containers that will join my tailnet directly, so there's no need for the underlying host to also be inside the tailnet. Though it won't cause a problem

**[01:02](https://youtube.com/watch?v=6FlgdNs7R04&t=62s)** if it is. If you haven't enabled HTTPS for your tailnet, that's the first step. You can find that setting under DNS at the very bottom. It's already on for this tailnet, so we don't need to do anything here. The next step is to go to Access Controls, because we need to create a new tag for our recorder nodes to be owned by. Under the tag owner's stanza, I'm going to add a new tag. I'm going to call it recorder, and I'm going to make myself the owner of that tag.

**[01:32](https://youtube.com/watch?v=6FlgdNs7R04&t=92s)** We'll save our policy file. The next step is to generate an off key. To do that, we go to Settings, and then Keys, and we'll generate a new off key.

**[01:45](https://youtube.com/watch?v=6FlgdNs7R04&t=105s)** I'm going to use the default settings, except I'm going to assign the recorder tag we just created to this off key. So that every time we use this off key to generate a new device, that device will automatically get the recorder tag, and I'll go ahead and generate this key.

**[02:03](https://youtube.com/watch?v=6FlgdNs7R04&t=123s)** I'm going to copy it to my clipboard, and I'm going to come back to my Docker host, and in my Docker host, I'm going to just set this as an environment variable. To do that, I'll say export TS underscore off key equals the off key.

**[02:18](https://youtube.com/watch?v=6FlgdNs7R04&t=138s)** Our recorder node is going to look for this variable to authenticate to our tailnet, and now we're ready to run the container. I'm going to copy and paste in the Docker run commands, and then we'll talk about each of the components individually.

**[02:36](https://youtube.com/watch?v=6FlgdNs7R04&t=156s)** The first thing we're doing is, as we just noted, pulling in the off key that we set as an environment variable.

**[02:44](https://youtube.com/watch?v=6FlgdNs7R04&t=164s)** The next thing that we're doing is down here, we're setting a destination for our recordings to live when they're saved to the file system. They'll be saved in a folder called recordings.

**[02:55](https://youtube.com/watch?v=6FlgdNs7R04&t=175s)** Then we have another flag for our state, our tailscale state will be stored in a subfolder called state, and then last we have the UI flag, and that specifies that we do want to run the built-in web UI for viewing session recordings.

**[03:10](https://youtube.com/watch?v=6FlgdNs7R04&t=190s)** This is optional, but we're going to turn it on for this demo. So I'm going to go ahead and run this command, and now we can see that the recorder has started.

**[03:21](https://youtube.com/watch?v=6FlgdNs7R04&t=201s)** When I go back to my admin console and go to machines, we can see there's now a recorder node that's joined our tailnet.

**[03:28](https://youtube.com/watch?v=6FlgdNs7R04&t=208s)** So now we can see the UI for our session recorder node, but it's looking pretty empty. In order to start recording, there's one more step we need to take.

**[03:35](https://youtube.com/watch?v=6FlgdNs7R04&t=215s)** In the admin console, we need to go to access controls, and in our SSH access rules, we need to add something to this first stanza, so that any session that originates from my account to a device tagged as prod

**[03:51](https://youtube.com/watch?v=6FlgdNs7R04&t=231s)** will get recorded. The reason we want to do that is because our SSH client is owned by my account, and our SSH server is tagged as prod.

**[04:01](https://youtube.com/watch?v=6FlgdNs7R04&t=241s)** To enable this for this SSH access rule, we add a new field at the bottom called recorder, and we'll specify the tag that we created and added the recorder to.

**[04:16](https://youtube.com/watch?v=6FlgdNs7R04&t=256s)** The reason we use the tag is that it's possible to deploy multiple recorder nodes and tag them all with this recorder tag.

**[04:23](https://youtube.com/watch?v=6FlgdNs7R04&t=263s)** If I do that, and one of my recorder nodes is offline, tailscale can automatically fall back to one of the other recorder nodes that is reachable.

**[04:32](https://youtube.com/watch?v=6FlgdNs7R04&t=272s)** So this is great for a higher availability of your SSH recording. We'll save this access rule, and now we're ready to test it out.

**[04:43](https://youtube.com/watch?v=6FlgdNs7R04&t=283s)** So in our SSH client VM, I'm going to type SSH and then SSH server, which is our destination, and we'll say yes, and you can see that we added this banner at the top now that says this session will be recorded, and that's something that tailscale will put into the session any time recording is on so that the user understands that everything they do will be logged.

**[05:07](https://youtube.com/watch?v=6FlgdNs7R04&t=307s)** Now, let's just quickly do some things to watch back on the recording.

**[05:11](https://youtube.com/watch?v=6FlgdNs7R04&t=311s)** We can do a really simple echo commands, if I say pseudo so that's going to ask me for a pseudo password, something interesting here is that because the password doesn't appear in the terminal output, it doesn't get logged.

**[05:24](https://youtube.com/watch?v=6FlgdNs7R04&t=324s)** So even though I typed in a pseudo password on a session that is recorded, it won't appear in the session recording.

**[05:31](https://youtube.com/watch?v=6FlgdNs7R04&t=331s)** Go back to my regular user, and I'll show you, you can also use full screen terminal UIs like text editors, so nano hello to TXT say hi, and we'll exit this session to close out.

**[05:48](https://youtube.com/watch?v=6FlgdNs7R04&t=348s)** So I've closed out my SSH session, let's go and look at the recording.

**[05:52](https://youtube.com/watch?v=6FlgdNs7R04&t=352s)** We'll go to our session recorder, and we can see that it's showing up, click on it, and you can play it back like a video file.

**[06:02](https://youtube.com/watch?v=6FlgdNs7R04&t=362s)** So we can see the actions that we took here, we can see the pseudo password isn't logged, and we can also see where we went into nano.

**[06:16](https://youtube.com/watch?v=6FlgdNs7R04&t=376s)** If we scroll down, we can see the metadata about the session as well.

**[06:20](https://youtube.com/watch?v=6FlgdNs7R04&t=380s)** I also want to quickly show you what these recordings look like as text.

**[06:25](https://youtube.com/watch?v=6FlgdNs7R04&t=385s)** This is the file that we just created, and you can see that all of our commands are represented as text here, even though we can also play it back like a video file.

**[06:36](https://youtube.com/watch?v=6FlgdNs7R04&t=396s)** So you can either view it as a video, or you can use command line tools to search the text file yourself.

**[06:43](https://youtube.com/watch?v=6FlgdNs7R04&t=403s)** You can also export this text file into a logging program like Splunk or logstash.

**[06:48](https://youtube.com/watch?v=6FlgdNs7R04&t=408s)** And that's really all that there is to it.

**[06:52](https://youtube.com/watch?v=6FlgdNs7R04&t=412s)** You can find all of the step-by-step instructions for deploying session recording in our documentation.

**[06:56](https://youtube.com/watch?v=6FlgdNs7R04&t=416s)** We hope you'll find this feature useful, and please let us know if you have any feedback.

---

*Automatically generated transcript. May contain errors.*
