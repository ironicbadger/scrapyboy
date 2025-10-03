---
video_id: "08clF9srJ2k"
title: "What is Tailscale SSH? | Tailscale Explained"
description: "At Tailscale, we're always adding new features and solving real problems for developers and infrastructure folks alike. In our \"Tailscale Explained\" series we show you all you need to know to get star..."
channel_name: "Tailscale"
channel_id: "UCcdv38QxPjSMqbt5ffLhJLA"
published_at: "2023-12-22"
duration_seconds: 549
youtube_url: "https://www.youtube.com/watch?v=08clF9srJ2k"
thumbnail_url: "https://i.ytimg.com/vi/08clF9srJ2k/maxresdefault.jpg"

# Transcription metadata
transcribed_at: "2025-10-03T15:56:22.828153"
transcription_method: "cpu"
model_used: "base"
language: "en"
word_count: 1648
transcription_time_seconds: 15.0
---

# What is Tailscale SSH? | Tailscale Explained

**[00:00](https://youtube.com/watch?v=08clF9srJ2k&t=0s)** Hey everyone, it's Alex from Tailscale here, and in today's video we're going to be talking about Tailscale SSH, one of my absolute favorite features. I use SSH all day every day to connect to devices in development and production environments, and I'm going to show you how we can use tags to isolate the identity of those connections and make things more secure across your infrastructure. So if you've been looking for the fastest way to get started with Tailscale SSH, then this is the video for you.

**[00:30](https://youtube.com/watch?v=08clF9srJ2k&t=30s)** Now the easiest way to do that is to go to the console of your system, in my case this is a digital ocean droplet, and I'm going to do Tailscale status just to double check them on the correct tailnet, and then Tailscale set dash dash SSH.

**[00:44](https://youtube.com/watch?v=08clF9srJ2k&t=44s)** What you'll notice in the console underneath here, we can see that I've got a little green button has appeared on my Tailscale admin console.

**[00:52](https://youtube.com/watch?v=08clF9srJ2k&t=52s)** So now what we can do is we can SSH into that node using the Tailscale machine name, so no IP addresses are required, I can do dev hyphen web NYC1, and that lets me SSH from my local dev VM behind a firewall, all that kind of stuff, out to a machine running on digital ocean with no SSH keys configured whatsoever.

**[01:16](https://youtube.com/watch?v=08clF9srJ2k&t=76s)** So if I just show you the SSH directory of my local Ubuntu host, there's no keys in there, I didn't have to type in any passwords, and I can SSH now as root into that cloud server.

**[01:27](https://youtube.com/watch?v=08clF9srJ2k&t=87s)** Now the paranoid amongst you might be thinking that was too easy, perhaps you'd like to add a little more friction and a couple more checks to this process.

**[01:37](https://youtube.com/watch?v=08clF9srJ2k&t=97s)** So let's jump into the Tailscale ACLs, these can be found under the admin console under the access controls panel.

**[01:45](https://youtube.com/watch?v=08clF9srJ2k&t=105s)** If we change this action from accept to check, I'm also going to change the check period to every minute, the default by the way is 12 hours on this.

**[01:54](https://youtube.com/watch?v=08clF9srJ2k&t=114s)** I'm going to change it to every minute just so that it forces another check for me for the demo is now going to say we need to verify that you are who you say you are, please log in and authenticate.

**[02:08](https://youtube.com/watch?v=08clF9srJ2k&t=128s)** And as soon as I do that, I sign in with my Google account here, we'll see that in real time, boom, we're now authenticated to that remote SSH node with another check.

**[02:18](https://youtube.com/watch?v=08clF9srJ2k&t=138s)** Now what happens if we're on call and we get paged at an inconvenient time, maybe we don't have our laptop with us, but we do have the ability to borrow a relative laptop or a friend's laptop and actually connect into a web browser.

**[02:34](https://youtube.com/watch?v=08clF9srJ2k&t=154s)** Well, we can create an ephemeral SSH session in the browser.

**[02:39](https://youtube.com/watch?v=08clF9srJ2k&t=159s)** So what this is going to do is it's going to create an ephemeral node and add it to my tailnet.

**[02:44](https://youtube.com/watch?v=08clF9srJ2k&t=164s)** In real time, I'm going to connect to this tailscale node and you can see the underneath here, I've got an SSH console an ephemeral node.

**[02:52](https://youtube.com/watch?v=08clF9srJ2k&t=172s)** So what that means is as soon as this SSH session finishes, this node is going to delete itself from my tailnet.

**[02:59](https://youtube.com/watch?v=08clF9srJ2k&t=179s)** And I can do whatever I was going to do on that node as if I was connected from a real browser or a real terminal.

**[03:07](https://youtube.com/watch?v=08clF9srJ2k&t=187s)** We do have some safety wheels in place too.

**[03:09](https://youtube.com/watch?v=08clF9srJ2k&t=189s)** So for example, if you were to do tailscale set dash dash SSH equals false, it's going to say, are you sure you want to do this because this is going to break the SSH connection for you.

**[03:20](https://youtube.com/watch?v=08clF9srJ2k&t=200s)** So what we have to do in this case is do a dash dash accept risk equals lose SSH because this is going to new car connection.

**[03:30](https://youtube.com/watch?v=08clF9srJ2k&t=210s)** You can see immediately the ephemeral connection terminated and the SSH badge was removed from our tailnet here.

**[03:38](https://youtube.com/watch?v=08clF9srJ2k&t=218s)** Now if I refresh the page in just a moment or two, this ephemeral node will disappear.

**[03:45](https://youtube.com/watch?v=08clF9srJ2k&t=225s)** The next thing I'd like to talk to you about are tags. Now these are absolutely vital for restricting access to different types of resources.

**[03:52](https://youtube.com/watch?v=08clF9srJ2k&t=232s)** So we don't necessarily want our dev machine to be able to access production.

**[03:57](https://youtube.com/watch?v=08clF9srJ2k&t=237s)** For example, you know, for the moment right now I can do dev web NYC one as root I can SSH there.

**[04:06](https://youtube.com/watch?v=08clF9srJ2k&t=246s)** I can also SSH as root to production straight from my VM.

**[04:12](https://youtube.com/watch?v=08clF9srJ2k&t=252s)** And that's because at the moment the identity is set to a tail and scales at Gmail.com these devices were added by me so they assume my identity.

**[04:21](https://youtube.com/watch?v=08clF9srJ2k&t=261s)** Now what we can go ahead and do in our access controls is define a bunch of tags.

**[04:26](https://youtube.com/watch?v=08clF9srJ2k&t=266s)** You see here I've got to I've got a tag for prod and a tag for dev.

**[04:30](https://youtube.com/watch?v=08clF9srJ2k&t=270s)** I've also got a couple of user groups. I've got a group for admins of which I am a member.

**[04:35](https://youtube.com/watch?v=08clF9srJ2k&t=275s)** So my identity gets subsumed into this group admin.

**[04:40](https://youtube.com/watch?v=08clF9srJ2k&t=280s)** I've also got a dev group this amily user for example is in the developers team.

**[04:45](https://youtube.com/watch?v=08clF9srJ2k&t=285s)** And then under SSH policy a little bit further down I've got configured a rule which allows developers to SSH into nodes tagged with the dev tag.

**[04:58](https://youtube.com/watch?v=08clF9srJ2k&t=298s)** So to do this we want to jump over to the machines page and actually on my developer machine click the three dot menu click edit ACL tags and add the tag of dev.

**[05:09](https://youtube.com/watch?v=08clF9srJ2k&t=309s)** I'm going to do the same thing for the production node I'm going to add the tag of prod and you can see that the identity of these nodes is now no longer mine.

**[05:22](https://youtube.com/watch?v=08clF9srJ2k&t=322s)** It doesn't have my username underneath and it has the tag as the owner of this instance.

**[05:28](https://youtube.com/watch?v=08clF9srJ2k&t=328s)** And so what this means is that now in fact I left the SSH connection open in the background whilst I added that tag and in real time the access was revoked by the tail scale SSH engine.

**[05:39](https://youtube.com/watch?v=08clF9srJ2k&t=339s)** So if I try and SSH back into production now from this machine it's not going to let me but it will let me connect back into my dev machine in the cloud using the accles that we provisioned underneath in the access controls.

**[05:53](https://youtube.com/watch?v=08clF9srJ2k&t=353s)** So let's go ahead and show you this in action in real time let's say I want to enable myself to SSH into production I'm going to allow anybody who's a member of the dev group to access an SSH into a production resource.

**[06:08](https://youtube.com/watch?v=08clF9srJ2k&t=368s)** Now the members of this group remember a defined at the top here so group dev is my username as well as Emily I've now added the tag prod to this rule set that's here.

**[06:20](https://youtube.com/watch?v=08clF9srJ2k&t=380s)** I click save and in real time I'm now able to connect into production using the rules I've just defined in my ACLs but where it gets really cool is these get pushed down to each client device in real time.

**[06:34](https://youtube.com/watch?v=08clF9srJ2k&t=394s)** So if I go ahead and remove that tag and click save look it's instantly instantly revoke the access to that SSH session in the other window.

**[06:49](https://youtube.com/watch?v=08clF9srJ2k&t=409s)** Now these rules are great because they let you control who can access which resources on your talent depending on source of group or a certain device based on things like device posture we recently added you can now limit things to say only users running Linux can connect to production or only running iOS 17.2 the most recent release at the time of recording can connect into certain resources and so on.

**[07:13](https://youtube.com/watch?v=08clF9srJ2k&t=433s)** Now wouldn't it be great if when we're adding a certain node to our talent we could use something like an off key to automatically define things like the tag.

**[07:23](https://youtube.com/watch?v=08clF9srJ2k&t=443s)** So when a node gets added we don't have to go and manually tag it we can automatically assign the role or the tag to that node when we create the off key.

**[07:33](https://youtube.com/watch?v=08clF9srJ2k&t=453s)** So I'm just going to go ahead and show you how to do that real quick.

**[07:35](https://youtube.com/watch?v=08clF9srJ2k&t=455s)** So up in the tail scale admin console you go to settings and then click keys down here on the left.

**[07:41](https://youtube.com/watch?v=08clF9srJ2k&t=461s)** And then when we click generate off key we've got a few options so I'm just going to call this demo 90 days is fine but down the bottom here there's an option called tags.

**[07:51](https://youtube.com/watch?v=08clF9srJ2k&t=471s)** So now any node that I add to my town it with this off key will automatically assume this tag this can be really handy for CICD instances and things like that.

**[08:01](https://youtube.com/watch?v=08clF9srJ2k&t=481s)** So you've got a Jenkins server or a GitHub action that's creating an instance with an off key it adds the nodes your town it does whatever it needs to do SSH and does a deploy to production or whatever.

**[08:13](https://youtube.com/watch?v=08clF9srJ2k&t=493s)** And then it only has permission and you limit the blast radius of what that SSH connection can do based on the off key with the automatic tagging underneath.

**[08:23](https://youtube.com/watch?v=08clF9srJ2k&t=503s)** So those are the basics of tail scale SSH I sometimes wonder how we lived without this for so long having a centralized way to manage SSH keys.

**[08:32](https://youtube.com/watch?v=08clF9srJ2k&t=512s)** I mean in previous roles I've been in I've had folks who have written complicated answer will playbooks to add and remove SSH keys and inevitably when people get off boarded those keys remain on the boxes for longer than they perhaps should.

**[08:47](https://youtube.com/watch?v=08clF9srJ2k&t=527s)** When folks are getting on boarded it takes too long there's just too much friction to get the keys on the boxes in the first place with tail scale SSH all of that becomes a complete non issue.

**[08:57](https://youtube.com/watch?v=08clF9srJ2k&t=537s)** We get started with tail scale with up to three users and a hundred devices for free at tail scale dot com until next time I've been Alex from tail scale.

---

*Automatically generated transcript. May contain errors.*
