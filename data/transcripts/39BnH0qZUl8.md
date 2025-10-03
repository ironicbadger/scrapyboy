---
video_id: "39BnH0qZUl8"
title: "Using Tailscale SSH Session Recording with Amazon S3"
description: "Sam Linville 

In this video, Sam Linville walks through the process of deploying Tailscale SSH session recording with S3 as a storage backend. Using S3 as a storage backend gives your session recordi..."
channel_name: "Tailscale"
channel_id: "UCcdv38QxPjSMqbt5ffLhJLA"
published_at: "2023-05-11"
duration_seconds: 454
youtube_url: "https://www.youtube.com/watch?v=39BnH0qZUl8"
thumbnail_url: "https://i.ytimg.com/vi/39BnH0qZUl8/hqdefault.jpg"

# Transcription metadata
transcribed_at: "2025-10-03T17:50:09.879751"
transcription_method: "cpu"
model_used: "base"
language: "en"
word_count: 1032
transcription_time_seconds: 9.4
---

# Using Tailscale SSH Session Recording with Amazon S3

**[00:00](https://youtube.com/watch?v=39BnH0qZUl8&t=0s)** Hi, I'm Sam and I'm a Product Manager at Tailscale. In this video, I want to show you how to enable session recording for Tailscale SSH using Amazon S3 as the storage background. By default, the session recorder nodes that you deploy in your tailnet will save recordings to their file system. This is a great way to get started, but using Amazon S3 as a storage backend adds even more scalability and resiliency to your session recording and configuration. What I'm going to demo today uses

**[00:31](https://youtube.com/watch?v=39BnH0qZUl8&t=31s)** S3 on AWS, but you can also configure session recording with other S3 compatible object storage services like Wasabi or Minayo. To get started, we'll go to the AWS console and set up a few things. We need an S3 bucket, an IAM policy and roll, and a VM on EC2. First, we'll go to S3 and we'll create our bucket. I'm going to call my bucket session recording bucket and we're going to keep ACLs disabled and

**[01:06](https://youtube.com/watch?v=39BnH0qZUl8&t=66s)** block all public access. You can keep all of the default settings here. Now that we've created our bucket, we're going to go to the IAM management console and create a policy. So we'll go to policies and create new policy. We're going to use the JSON editor and I'm going to paste in the correct policy. The policy is available in documentation and I'll quickly walk through the basic anatomy of this policy. The first thing that we'll do is specify

**[01:44](https://youtube.com/watch?v=39BnH0qZUl8&t=104s)** which actions roles with this policy are allowed to take. They're allowed to add objects to our S3 bucket. They're allowed to get the region of our bucket. They're allowed to retrieve objects out of our bucket and list all of the objects in the bucket. And we are constraining that policy only to our bucket that we're using for this demo.

**[02:09](https://youtube.com/watch?v=39BnH0qZUl8&t=129s)** So we need to replace bucket name with session recording bucket and we'll do the same thing on the next line. This policy is constrained to the minimum actions that are required to run the session recorder nodes with S3 of the storage backend with the web UI enabled.

**[02:31](https://youtube.com/watch?v=39BnH0qZUl8&t=151s)** If you choose not to use the web UI, you can emit the get object and list bucket actions.

**[02:40](https://youtube.com/watch?v=39BnH0qZUl8&t=160s)** Click next. We'll name this policy session recording policy and we will create the policy.

**[02:48](https://youtube.com/watch?v=39BnH0qZUl8&t=168s)** The next thing we need to do is attach this policy to a role. We'll go to roles and create a new role. We're going to create this role for an AWS service, specifically EC2, and we're going to attach our session recording policy.

**[03:10](https://youtube.com/watch?v=39BnH0qZUl8&t=190s)** We're going to call this role session recording role and we're going to create the role. The last thing that we need to do is create a virtual machine on EC2 to host our recorder node.

**[03:29](https://youtube.com/watch?v=39BnH0qZUl8&t=209s)** We'll go to EC2 and we'll launch a new instance. We'll call our instance session recording host leaves the default Amazon Linux AMI will attach our key pair, choose our default security group.

**[03:54](https://youtube.com/watch?v=39BnH0qZUl8&t=234s)** And under advanced details, we're going to select the session recording role for IAM instance profile. Now, what this does is give our EC2 instance the ability to access that S3 bucket that we created according to the policy we wrote.

**[04:10](https://youtube.com/watch?v=39BnH0qZUl8&t=250s)** And now we can launch the instance. We fast forwarded just a bit here. Our EC2 instance is up and running. I've connected to it over SSH and installed Docker.

**[04:22](https://youtube.com/watch?v=39BnH0qZUl8&t=262s)** The next thing that we need to do is get it off key for tail scale for our recorder node to do that. I'll go to the admin console settings keys and I'll generate an off key.

**[04:34](https://youtube.com/watch?v=39BnH0qZUl8&t=274s)** I'm going to apply a tag to it. I've already created this recorder tag. This will be familiar from our prior demo. We'll generate that key and I'll copy it to the clipboard.

**[04:46](https://youtube.com/watch?v=39BnH0qZUl8&t=286s)** And just like in the standard session recorder deployment, we want to export this to an environment variable.

**[04:59](https://youtube.com/watch?v=39BnH0qZUl8&t=299s)** Now that we've done that, we can paste in our Docker run command. This will be available in documentation for you to copy.

**[05:07](https://youtube.com/watch?v=39BnH0qZUl8&t=307s)** Let's quickly review what's going on here. First, we are passing the TS off key into our container.

**[05:15](https://youtube.com/watch?v=39BnH0qZUl8&t=315s)** And then we're specifying in the destination flag instead of a file path, the S3 regional URL.

**[05:22](https://youtube.com/watch?v=39BnH0qZUl8&t=322s)** Make sure that you replace USB 1 with whichever region it is that you are working in.

**[05:27](https://youtube.com/watch?v=39BnH0qZUl8&t=327s)** Our state directory is the same as a normal deployment. And we have a new flag called bucket where you specify the name of the S3 bucket you want to place your recordings in.

**[05:37](https://youtube.com/watch?v=39BnH0qZUl8&t=337s)** Lastly, we do have our UI flag because we want our web UI to be activated. I'll go ahead and run this command.

**[05:50](https://youtube.com/watch?v=39BnH0qZUl8&t=350s)** So now you can see that our recorder is running. One thing you'll notice is it says it's missing values for the access and secret key, but it is attempting to use the local credentials.

**[06:01](https://youtube.com/watch?v=39BnH0qZUl8&t=361s)** And that should be working for us. As always, we can access our UI by going to this URL.

**[06:12](https://youtube.com/watch?v=39BnH0qZUl8&t=372s)** And we can see our session recorder with no recordings yet.

**[06:16](https://youtube.com/watch?v=39BnH0qZUl8&t=376s)** So let's go to our SSH client and let's start a session that we can record.

**[06:22](https://youtube.com/watch?v=39BnH0qZUl8&t=382s)** Say SSH and then SSH server, which is going to be our destination.

**[06:29](https://youtube.com/watch?v=39BnH0qZUl8&t=389s)** And we see that our session is recorded. It's just to a few things here and we'll close out the session.

**[06:47](https://youtube.com/watch?v=39BnH0qZUl8&t=407s)** Now, if we refresh this recorder, we see that there is a session now, just like with the default file system storage.

**[06:54](https://youtube.com/watch?v=39BnH0qZUl8&t=414s)** But if we go back to our Amazon console and we go to S3, let's take a look in the bucket and we see that that session is being stored in our S3 bucket.

**[07:09](https://youtube.com/watch?v=39BnH0qZUl8&t=429s)** And we still have the ability to click into the session and view it from the S3 bucket in the web UI.

**[07:20](https://youtube.com/watch?v=39BnH0qZUl8&t=440s)** We're thrilled to be able to offer increased resiliency and scalability with S3 as a storage backend for session recording.

**[07:27](https://youtube.com/watch?v=39BnH0qZUl8&t=447s)** We hope that you'll give it a try in the free or enterprise plans and let us know what you think.

**[07:32](https://youtube.com/watch?v=39BnH0qZUl8&t=452s)** Thank you.

---

*Automatically generated transcript. May contain errors.*
