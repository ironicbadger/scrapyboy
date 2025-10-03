---
video_id: "5bxU3Kltd1g"
title: "Ask a Tailscale Engineer: What is User & Group Provisioning for Okta?"
description: "This video walks through User & Group Provisioning for Okta in beta in Tailscale, and details how it works with Tailscale engineer, Ramya Nagarajan.

https://tailscale.com/blog/sync-okta-groups/
https..."
channel_name: "Tailscale"
channel_id: "UCcdv38QxPjSMqbt5ffLhJLA"
published_at: "2022-04-19"
duration_seconds: 333
youtube_url: "https://www.youtube.com/watch?v=5bxU3Kltd1g"
thumbnail_url: "https://i.ytimg.com/vi/5bxU3Kltd1g/hqdefault.jpg"

# Transcription metadata
transcribed_at: "2025-10-03T18:03:15.195934"
transcription_method: "cpu"
model_used: "base"
language: "en"
word_count: 897
transcription_time_seconds: 8.5
---

# Ask a Tailscale Engineer: What is User & Group Provisioning for Okta?

**[00:04](https://youtube.com/watch?v=5bxU3Kltd1g&t=4s)** Hi there, I'm Jessica Kennedy from the Tailscale Marketing Team, and today I'm joined by Ramiya, who is here to tell us a bit more about a new feature in Tailscale, user and group provisioning for Octa. Ramiya, can you tell us a bit more about yourself and what you're working on here? Sure. Hi, I'm Ramiya Nagarajan, an engineer at Tailscale, and I work on features to do with the control plane in Tailscale. The control plane, roughly speaking, manages weather and how nodes can connect to each other on the network. Got it.

**[00:34](https://youtube.com/watch?v=5bxU3Kltd1g&t=34s)** So one of the ways to determine whether devices can connect to each other is through the access control lists or ACLs. In Tailscale, ACLs are a set of rules that specify which groups of users have access to which endpoints. So what's the best way to limit access for many users who may have the same role?

**[01:04](https://youtube.com/watch?v=5bxU3Kltd1g&t=64s)** And limit access for that group with an accol. Okay, so if I work at a big organization, how can I authenticate to Tailscale? Large organizations typically use an identity and access management system like Octa or Azure Active Directory, and with these identity providers or IDPs, enterprises can easily manage changes to their organization, such as employees joining, leaving, or changing teams.

**[01:31](https://youtube.com/watch?v=5bxU3Kltd1g&t=91s)** So when you set up Tailscale for the first time, you'll have to select which IDP you want to authenticate with.

**[01:36](https://youtube.com/watch?v=5bxU3Kltd1g&t=96s)** Okay, so what are other ways I can authenticate to Tailscale for an individual project or at work?

**[01:42](https://youtube.com/watch?v=5bxU3Kltd1g&t=102s)** And Tailscale also supports authentication through GitHub, Google Off, and Microsoft accounts, as well as others. The full list is available on the Tailscale site.

**[01:52](https://youtube.com/watch?v=5bxU3Kltd1g&t=112s)** Okay, so what is user and group provisioning?

**[01:55](https://youtube.com/watch?v=5bxU3Kltd1g&t=115s)** So provisioning is the process of making user and group information available for SSO integrated applications like Tailscale.

**[02:03](https://youtube.com/watch?v=5bxU3Kltd1g&t=123s)** When users and groups are provisioned through an identity provider that supports synchronization, changes to group membership and user status are automatically updated with connected applications.

**[02:14](https://youtube.com/watch?v=5bxU3Kltd1g&t=134s)** Sounds very convenient. So what is skin?

**[02:17](https://youtube.com/watch?v=5bxU3Kltd1g&t=137s)** Skin is the system for cross-domain identity management, and it's a specification that is designed to make identity management in cloud-based applications easier.

**[02:27](https://youtube.com/watch?v=5bxU3Kltd1g&t=147s)** It lays out a schema and a protocol for communication between identity providers like Octa and applications like Tailscale to make user and group provisioning possible.

**[02:37](https://youtube.com/watch?v=5bxU3Kltd1g&t=157s)** So why did you decide to build this? What is this enable and what problems does this solve?

**[02:43](https://youtube.com/watch?v=5bxU3Kltd1g&t=163s)** So this is a feature that a lot of our enterprise customers have been asking for as a way to simplify management of Tailscale.

**[02:50](https://youtube.com/watch?v=5bxU3Kltd1g&t=170s)** And there's a couple of key features that have been enabled.

**[02:53](https://youtube.com/watch?v=5bxU3Kltd1g&t=173s)** The first is group sync and they're used in ACLs. So with group sync and administrator can select groups within their IDP to push to Tailscale.

**[03:02](https://youtube.com/watch?v=5bxU3Kltd1g&t=182s)** And this includes changes to the group name and membership as and when they happen.

**[03:06](https://youtube.com/watch?v=5bxU3Kltd1g&t=186s)** The group defined in the IDP can be directly referenced in the Tailscale ACL and stay up to date with changes to the organization.

**[03:14](https://youtube.com/watch?v=5bxU3Kltd1g&t=194s)** So there's no intervention required when individuals change teams, which is great.

**[03:19](https://youtube.com/watch?v=5bxU3Kltd1g&t=199s)** The second key feature is user sync for suspension. So when an employee goes on leave or exits the organization, an administrator typically deactivates them in the IDP.

**[03:29](https://youtube.com/watch?v=5bxU3Kltd1g&t=209s)** With user sync, that status gets automatically sent to Tailscale. So they lose access to those resources too.

**[03:36](https://youtube.com/watch?v=5bxU3Kltd1g&t=216s)** Wonderful. Sounds like that would be really helpful.

**[03:39](https://youtube.com/watch?v=5bxU3Kltd1g&t=219s)** So how do I refer to sync groups in ACLs and why would I need to do this?

**[03:44](https://youtube.com/watch?v=5bxU3Kltd1g&t=224s)** So Tailscale actually already supports creation of groups within the ACL file.

**[03:49](https://youtube.com/watch?v=5bxU3Kltd1g&t=229s)** And these natively defined groups list the membership within the ACL.

**[03:54](https://youtube.com/watch?v=5bxU3Kltd1g&t=234s)** So big old list of users in the ACL. But if you use a sync group, you can skip maintaining that user list within the ACL file.

**[04:03](https://youtube.com/watch?v=5bxU3Kltd1g&t=243s)** In order to differentiate between a sync group from a natively defined one, we've introduced a new naming convention that includes the group name from the IDP along with the name of your tailman.

**[04:14](https://youtube.com/watch?v=5bxU3Kltd1g&t=254s)** So instead of using group colon engineering, you might use group colon engineering act exactly about calm in your ACL file.

**[04:24](https://youtube.com/watch?v=5bxU3Kltd1g&t=264s)** Okay. So what do you think I should do if I have a reorg or change group memberships?

**[04:29](https://youtube.com/watch?v=5bxU3Kltd1g&t=269s)** So with provisioning enabled, you'd make changes to the group in your IDP.

**[04:34](https://youtube.com/watch?v=5bxU3Kltd1g&t=274s)** And if there's no change to the group name, you're done.

**[04:38](https://youtube.com/watch?v=5bxU3Kltd1g&t=278s)** There is a change to the group name. You just need to go into the tailscale ACL file and update it with that new name, and then you're done.

**[04:47](https://youtube.com/watch?v=5bxU3Kltd1g&t=287s)** Nice. So when should I use user and group provisioning?

**[04:50](https://youtube.com/watch?v=5bxU3Kltd1g&t=290s)** So I'd recommend this if you spend a lot of time managing user and group life cycles, and you're looking for a simpler centralized way of doing all of that.

**[04:59](https://youtube.com/watch?v=5bxU3Kltd1g&t=299s)** All right. And how do I use user and group provisioning? Where do I go to learn more about it?

**[05:04](https://youtube.com/watch?v=5bxU3Kltd1g&t=304s)** So I'd recommend talking about the tailscale site for information on which IDP currently have support for user and group provisioning.

**[05:12](https://youtube.com/watch?v=5bxU3Kltd1g&t=312s)** And you can also check out some guides to help you get started while you're there.

**[05:17](https://youtube.com/watch?v=5bxU3Kltd1g&t=317s)** Great. Well, thank you so much, Ramia.

**[05:19](https://youtube.com/watch?v=5bxU3Kltd1g&t=319s)** User and group provisioning is now available for Opta in beta and it's in tailscales business plan.

**[05:25](https://youtube.com/watch?v=5bxU3Kltd1g&t=325s)** Thank you so much for your time today.

**[05:27](https://youtube.com/watch?v=5bxU3Kltd1g&t=327s)** Thank you.

---

*Automatically generated transcript. May contain errors.*
