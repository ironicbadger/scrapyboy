---
video_id: "ASZm_HyrHIc"
title: "Tailscale's new Machine Explorer for VS Code"
description: "Tailscale for VS Code just got a major upgrade, bringing you the ability to explore, edit, and transfer the files on any of the nodes in your tailnet that you can reach through Tailscale SSH. For the ..."
channel_name: "Tailscale"
channel_id: "UCcdv38QxPjSMqbt5ffLhJLA"
published_at: "2023-08-18"
duration_seconds: 517
youtube_url: "https://www.youtube.com/watch?v=ASZm_HyrHIc"
thumbnail_url: "https://i.ytimg.com/vi/ASZm_HyrHIc/maxresdefault.jpg"

# Transcription metadata
transcribed_at: "2025-10-03T16:26:48.931116"
transcription_method: "cpu"
model_used: "base"
language: "en"
word_count: 1604
transcription_time_seconds: 18.4
---

# Tailscale's new Machine Explorer for VS Code

**[00:00](https://youtube.com/watch?v=ASZm_HyrHIc&t=0s)** Now I don't know about you, but working on multiple remote systems can just be a really frustrating experience. SSH here, SCP that file over there, go to use VIM and realize that this box only has NANO. Well, that means that none of my syntax highlighting is going to work. None of my developer creature comforts are there either. Well, that's the way it's been for the last 30 years or so. We SSH into a server, we open up an editor with a totally stock configuration.

**[00:30](https://youtube.com/watch?v=ASZm_HyrHIc&t=30s)** And we make do. Well, with the latest release of Tailscale's VS Code extension, I'm pleased to tell you that you can view and interact with all the files on any node in your tailnet, all from the comfort of your favorite editor.

**[00:44](https://youtube.com/watch?v=ASZm_HyrHIc&t=44s)** Tailscale is a mesh VPN that connects all your systems together using the WireGuard protocol, and it gives you secure access to any node in your tailnet from anywhere.

**[00:53](https://youtube.com/watch?v=ASZm_HyrHIc&t=53s)** Let's suppose I want to host a remote factory multiplayer server at a friend's house. It's behind a firewall. I have no other means to access it except via my tailnet. I'm going to use the SSH feature built into Tailscale to do that.

**[01:06](https://youtube.com/watch?v=ASZm_HyrHIc&t=66s)** Now, I want to host Factorio in a Docker container. That's the deployment method. I'm the most comfortable with to edit the configuration for a container. I'm going to put that into a Docker Compose YAML file.

**[01:18](https://youtube.com/watch?v=ASZm_HyrHIc&t=78s)** What we're going to do in today's demo is deploy that multiplayer Factorio server using Docker Compose and VS Code and make all of our configuration edits using the tailscale VS Code extension.

**[01:30](https://youtube.com/watch?v=ASZm_HyrHIc&t=90s)** So over here in VS Code, let's go ahead and install our tailscale extension. Look in the marketplace on the left hand side over here, search for tailscale and click install.

**[01:40](https://youtube.com/watch?v=ASZm_HyrHIc&t=100s)** Once installed, we can go ahead and look at some of the extension settings. Now, the only one that I really tend to customize is my SSH username.

**[01:48](https://youtube.com/watch?v=ASZm_HyrHIc&t=108s)** Under the hood, this extension is using tailscale SSH built into tailscale to make all the connections to the remote systems. And so for me on my systems, my typical default user is Alex. If yours is different, go ahead and enter that.

**[02:02](https://youtube.com/watch?v=ASZm_HyrHIc&t=122s)** Once we've entered that username, we can go ahead on the left hand side here and see that we've got a brand new icon. So if we click on tailscale on the left here, what we can see are all of the different machines that are part of my tailnet.

**[02:14](https://youtube.com/watch?v=ASZm_HyrHIc&t=134s)** So I've got a couple of machines here. I've got my OIDC server. This is my identity provider server. We're not going to touch that one today because that's not part of the script of this video.

**[02:25](https://youtube.com/watch?v=ASZm_HyrHIc&t=145s)** But we are going to look at a couple of these machines here. So on the left hand side, we've got this Nick's OS server. Now I'm SSH into this server using the extension, which is pretty cool if you think about it.

**[02:38](https://youtube.com/watch?v=ASZm_HyrHIc&t=158s)** And I'm connected directly into the home folder on that server. So if I click on this little icon up here, the terminal icon, it brings up an integrated terminal as part of the VS code experience on that remote node.

**[02:52](https://youtube.com/watch?v=ASZm_HyrHIc&t=172s)** Now what you probably didn't notice is that there was no SSH keys exchange that all happens transparently using the tailscale SSH feature built into tailscale.

**[03:03](https://youtube.com/watch?v=ASZm_HyrHIc&t=183s)** What if I wanted to use a different user though? Maybe I want to be root for some reason. Well, if I right click on the node in question, I can go ahead and change a few things on here. So I'm going to change my SSH username on this node to be root.

**[03:17](https://youtube.com/watch?v=ASZm_HyrHIc&t=197s)** And when we do that, it gives me access if I change also the root directory to be root. Suddenly I have access to every single file on this remote system.

**[03:29](https://youtube.com/watch?v=ASZm_HyrHIc&t=209s)** Now, being a Nick's box, of course, I'm going to want to go in and modify my Nick's OS config, of course. So if I click on a file on the remote system, it brings it up over here.

**[03:40](https://youtube.com/watch?v=ASZm_HyrHIc&t=220s)** And we can see that at the moment, I have no syntax highlighting. Well, that's because it's respecting all of our VS code extensions.

**[03:49](https://youtube.com/watch?v=ASZm_HyrHIc&t=229s)** So I go ahead and install Nick's into my local environment, go back to this file in the tailscale editor over here. Suddenly we have syntax highlighting available for our next file.

**[04:00](https://youtube.com/watch?v=ASZm_HyrHIc&t=240s)** Now the same is going to be true of YAML as well. So why don't we go ahead and install a YAML extension to, okay, that looks good.

**[04:08](https://youtube.com/watch?v=ASZm_HyrHIc&t=248s)** Now, the keen eye amongst you will notice that originally I'm going to go back to my home folder that there was actually a Docker compose file sat in this home directory.

**[04:19](https://youtube.com/watch?v=ASZm_HyrHIc&t=259s)** And this is my factorial server. So what I'm going to go ahead and do is just bring up this.

**[04:26](https://youtube.com/watch?v=ASZm_HyrHIc&t=266s)** Oh, well, I don't have Docker compose installed. That's a problem. How can I fix that? Well, what if I go to my Nick's OS config file that I also had open.

**[04:37](https://youtube.com/watch?v=ASZm_HyrHIc&t=277s)** And install Docker compose. Can't be that hard, right? Oh, look at this. The syntax highlighting is so nice. So if I go over here, I'm going to also make sure that my user is part of the Docker group so that I have access to do various things.

**[04:54](https://youtube.com/watch?v=ASZm_HyrHIc&t=294s)** And then you can see as part of the VS code terminal here, I don't really have to move around too much.

**[04:59](https://youtube.com/watch?v=ASZm_HyrHIc&t=299s)** I'm going to do a Nick's OS rebuild switch. So what this is going to do if we're not familiar with Nick's going to download and install Docker compose.

**[05:06](https://youtube.com/watch?v=ASZm_HyrHIc&t=306s)** It's going to add my user to the correct group and all that kind of stuff. I'm doing this all from within VS code. I just think this is super, super cool.

**[05:15](https://youtube.com/watch?v=ASZm_HyrHIc&t=315s)** So now if we go back to Alex as the as the user, I probably need to create a brand new session because I added by user to a new group.

**[05:23](https://youtube.com/watch?v=ASZm_HyrHIc&t=323s)** So I'm going to go back up to Nick's OS server over here on the left, click on the terminal button. And then, oh, yes, that's right. I'm root now on time. So I'm going to go SU Alex, change my user to Alex.

**[05:34](https://youtube.com/watch?v=ASZm_HyrHIc&t=334s)** And then I should be able to do my Docker compose. Look at that. Oh, well, now I have another error that I need to go and solve.

**[05:42](https://youtube.com/watch?v=ASZm_HyrHIc&t=342s)** So let's go and look at my Docker compose YAML file. Oh, that's right. Because I have syntax highlighting, I can see pretty quickly that I've got some indentation errors.

**[05:52](https://youtube.com/watch?v=ASZm_HyrHIc&t=352s)** In my Docker compose YAML file. So if I do this now, voila. Now what's it looking at here? Ah, yes, this is a factorial specific thing.

**[06:02](https://youtube.com/watch?v=ASZm_HyrHIc&t=362s)** So if I look in this directory here, home Alex update a factorial, I can go and modify some of the various stuff that's in there.

**[06:11](https://youtube.com/watch?v=ASZm_HyrHIc&t=371s)** But what's interesting is if we look at this, there isn't that that directory doesn't exist. So if I click on the refresh button up here in the top left hand corner, you can see that the app data directory suddenly appears as does all of the different configuration files.

**[06:28](https://youtube.com/watch?v=ASZm_HyrHIc&t=388s)** Let me go ahead and edit this server settings.json file. Notice the syntax highlighting how wonderful is that I'm going to select that my server pub visibility of my server for public use is false because this is just a little server we're messing around with.

**[06:46](https://youtube.com/watch?v=ASZm_HyrHIc&t=406s)** I also noticed that in my compose file is looking for a save named megabase. Well, that just so happens to be a zip file I have on my system here.

**[06:57](https://youtube.com/watch?v=ASZm_HyrHIc&t=417s)** And using tail scale SSH is now going to upload that zip file was about an 80 megabyte zip file to the remote system over tail scale fully encrypted and everything.

**[07:08](https://youtube.com/watch?v=ASZm_HyrHIc&t=428s)** Now if I bring that that container back up again, we can see that the logs are much happier.

**[07:14](https://youtube.com/watch?v=ASZm_HyrHIc&t=434s)** So if I go ahead and bring up factorial now on my local system and go ahead and try and connect to that remote server. Again, I'm going to use the tail scale IP for this.

**[07:29](https://youtube.com/watch?v=ASZm_HyrHIc&t=449s)** So I'm going to go into my, sadly, this is off screen for the screen capture, but I'm going to go into my Mac client for tail scale and get the IP address for that specific node, which I think is probably this one earlier from just a little pre demo testing that I did.

**[07:49](https://youtube.com/watch?v=ASZm_HyrHIc&t=469s)** Yeah, there we go. So if I go ahead and connect to that now, it's connecting 100% over tail scale using a factorial game server that we configured using the tail scale VS code extension with the YAML files and JSON files that we configured completely from VS code without leaving that single window.

**[08:08](https://youtube.com/watch?v=ASZm_HyrHIc&t=488s)** And so there we go, you know, I'm going to go ahead and play factorial all day and pretend I'm actually working.

**[08:15](https://youtube.com/watch?v=ASZm_HyrHIc&t=495s)** Now we're really curious for you to tell us how you're going to use this extension so we can make it better in the future. Let us know by dropping a comment down below.

**[08:23](https://youtube.com/watch?v=ASZm_HyrHIc&t=503s)** Also, there's going to be a link to a blog post down in the description for the various different bits that didn't fit into this short video.

**[08:30](https://youtube.com/watch?v=ASZm_HyrHIc&t=510s)** Thank you so much for watching and until next time, I've been Alex from tail scale.

---

*Automatically generated transcript. May contain errors.*
