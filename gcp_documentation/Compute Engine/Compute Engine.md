## Compute Engine overview

Compute Engine is an infrastructure as a service (IaaS) product that offers self-managed virtual machine (VM) instances and bare metal instances. Compute Engine offers VMs with a KVM hypervisor, operating systems for both Linux and Windows, and durable storage options. You can configure and control Compute Engine resources using the Google Cloud console, the Google Cloud CLI, or using a REST-based API. You can also use a variety of programming languages available with Google's [Cloud Client Libraries](https://docs.cloud.google.com/apis/docs/cloud-client-libraries).

<br />

Here are some of the benefits of using Compute Engine:

- **Extensibility:** Compute Engine integrates with Google Cloud technologies such as Cloud Storage, Google Kubernetes Engine, and BigQuery, to extend beyond the basic computational capability to create more complex and sophisticated applications.
- **Scalability:** Scale the number of compute resources as needed without having to manage your own infrastructure. This is useful for businesses that experience sudden increases in traffic, because you can quickly add more instances to handle the increase and remove the instances after they are no longer needed.

- **Reliability:** The minimum uptime SLO for Compute Engine is 99.5%. The uptime SLO varies depending on the regions and Network Service Tiers that you choose and the deployment configurations. For more information, see [Compute Engine Service Level Agreement (SLA)](https://cloud.google.com/compute/sla).

- **Cost-effectiveness:** Compute Engine offers a variety of pricing options to fit your budget. Also, you only pay for the resources that you use, and there are no up-front costs.

## What Compute Engine provides

Compute Engine provides flexibility so that you can run a wide-range of applications and workloads that support your needs. From batch processing to webserving or high performance computing you can configure Compute Engine to meet your needs.

### Location selection

Google offers worldwide regions for you to deploy Compute Engine resources. You can choose a region that best fits the requirements of your workload:

- Region-specific restrictions
- User latency by region
- Latency requirements of your application
- Amount of control over latency
- Balance between low latency and simplicity

For more information about regions and zones, see [About regions and zones](https://docs.cloud.google.com/compute/docs/regions-zones).

### Compute Engine machine types

Compute Engine provides a comprehensive set of machine families, each containing machine types to choose from when you create a compute instance. Each machine family is comprised of machine series and predefined machine types within each series.
Compute Engine offers general-purpose, compute-optimized, network-optimized, storage-optimized, memory-optimized, and accelerator-optimized machine families.

<br />

If a preconfigured, general-purpose machine type doesn't meet your needs, then you can create a custom machine type with customized CPU and memory resources for some of the machine series.

For more information, see the [Machine families resource guide](https://docs.cloud.google.com/compute/docs/machine-resource).

### Operating systems

Compute Engine provides many preconfigured public operating system images for both Linux and Windows.
Most public images are provided for no additional cost, but there are some [premium images](https://docs.cloud.google.com/compute/disks-image-pricing#premiumimages) for which you are billed. You are not billed for importing custom images, but you will incur an [image storage charge](https://docs.cloud.google.com/compute/disks-image-pricing#imagestorage) while you keep the custom image in your project.

### Storage options

You can choose from several block storage options, including Google Cloud Hyperdisk, Local SSD, and Persistent Disk.

- **Local SSD:** Physical drives that offer the best performance, but are not durable. If you stop the instance, the data on the Local SSD disks that are attached to the instance is lost. Local SSD disks are attached directly to the same server as the compute instance.

- **Hyperdisk:** The fastest durable storage for Compute Engine. Data on Hyperdisk volumes is preserved even if you stop the instance. Hyperdisk volumes offer configurable performance and can be resized dynamically. You can also reduce costs and disk management complexity by purchasing capacity and performance in advance with Hyperdisk Storage Pools.

- **Persistent Disk:** If you need durable storage for a machine series that doesn't support Hyperdisk, then use Persistent Disk. Persistent Disk provides fast durable block storage that is preserved even if you stop the instance.

Each option has unique pricing and performance. For more information about disks in Compute Engine, see [Choose a disk type](https://docs.cloud.google.com/compute/docs/disks).
For cost comparisons, see [Disk pricing](https://docs.cloud.google.com/compute/disks-image-pricing#disk).

## What's next

- See the [CPU platforms](https://docs.cloud.google.com/compute/docs/cpu-platforms) and [GPUs](https://docs.cloud.google.com/compute/docs/gpus) that are available for your use.
- Read an [overview of networking capabilities](https://docs.cloud.google.com/compute/docs/networking/network-overview).
- Learn about the various [deployment strategies](https://docs.cloud.google.com/compute/docs/choose-compute-deployment-option).

## Compute Engine instances

This page provides an overview of Compute Engine instances. A Compute Engine instance can be either a virtual machine (VM) or bare metal instance that is hosted on Google's infrastructure. You can [create an instance](https://docs.cloud.google.com/compute/docs/instances/create-start-instance) or [create a group of managed instances (MIG)](https://docs.cloud.google.com/compute/docs/instance-groups/creating-groups-of-managed-instances) by using the Google Cloud console, the Google Cloud CLI, or the Compute Engine API.

<br />

## Introduction

The terms *Compute Engine instance*, *compute instance* or *instance* are synonymous. Based on the [machine type](https://docs.cloud.google.com/compute/docs/machine-resource) that you specify, an instance can be either a bare metal instance or a virtual machine (VM) instance, as follows:

- If the name of its machine type ends in `-metal`, an instance is a [bare metal instance](https://docs.cloud.google.com/compute/docs/machine-resource#bare-metal-types), which does not have a hypervisor installed.
- Otherwise, an instance is a VM instance. The terms *virtual machine instance*, *VM instance*, and *VM* are synonymous.

Synonymous terms are used interchangeably across the documentation and Google Cloud interfaces such as the [Google Cloud console](https://console.cloud.google.com/), the [gcloud](https://docs.cloud.google.com/compute/docs/gcloud-compute) command-line tool, and the [REST API](https://docs.cloud.google.com/compute/docs/reference/latest).

<br />

Compute Engine instances can run the [public images](https://docs.cloud.google.com/compute/docs/images) for Linux and Windows Server that Google provides as well as private custom images that you can [create](https://docs.cloud.google.com/compute/docs/images/create-delete-deprecate-private-images) or [import from your existing systems](https://docs.cloud.google.com/compute/docs/import/importing-virtual-disks). You can also [deploy Docker containers](https://docs.cloud.google.com/compute/docs/containers/deploying-containers), which are automatically launched on instances running the [Container-Optimized OS](https://docs.cloud.google.com/container-optimized-os/docs) public image.

You can choose the machine properties of your instances, such as the number of virtual CPUs and the amount of memory, by using a set of [predefined machine types](https://docs.cloud.google.com/compute/docs/machine-resource) or by creating your own [custom machine types](https://docs.cloud.google.com/compute/docs/instances/creating-instance-with-custom-machine-type).

## Instances and projects

Each instance belongs to a [Google Cloud console](https://console.cloud.google.com/) project, and a project can have one or more instances. When you create an instance in a project, you specify the zone, operating system, and machine type of that instance. When you delete an instance, it is removed from the project.

## Instances and storage options

By default, each Compute Engine instance has a small boot disk that contains the operating system. You can add more disks to the instance when you create it, and you can add disks to an instance while the instance is running. For more information about disks in Compute Engine, see [Choose a disk type](https://docs.cloud.google.com/compute/docs/disks).

## Instances and networks

Each network interface of a Compute Engine instance is associated with a subnet of a unique VPC network. For more information about VPCs, see [Network overview](https://docs.cloud.google.com/compute/docs/networking/network-overview) and [VPC quotas](https://docs.cloud.google.com/vpc/docs/quota).

## Instances and containers

Compute Engine instances support a declarative method for launching your applications using [containers](https://cloud.google.com/containers). When creating an instance or an instance template, you can provide a Docker image name and launch configuration. Compute Engine takes care of the rest including supplying an up-to-date [Container-Optimized OS](https://docs.cloud.google.com/container-optimized-os/docs) image with Docker installed and launching your container when the instance starts. For more information, see [Deploying containers on instances and MIGs](https://docs.cloud.google.com/compute/docs/containers/deploying-containers).

## Tools to manage instances

To create and manage instances, you can use a variety of tools, including the [Google Cloud console](https://console.cloud.google.com/), the [`gcloud`](https://docs.cloud.google.com/compute/docs/gcloud-compute) command-line tool, and the [REST API](https://docs.cloud.google.com/compute/docs/reference/latest). To configure applications on your instances, [connect to the instance](https://docs.cloud.google.com/compute/docs/instances/connecting-to-instance) using Secure Shell (SSH) for Linux instances or Remote Desktop Protocol (RDP) for Windows Server instances.

## Managing access to your instances

You can manage access to your instances using one of the following methods:

- Linux instances:
  - [Managing instance access using OS Login](https://docs.cloud.google.com/compute/docs/instances/managing-instance-access), which allows you to associate SSH keys with your Google Account or Google Workspace account and manage admin or non-admin access to your instance through IAM roles.
  - [Manage your SSH keys in project or instance metadata](https://docs.cloud.google.com/compute/docs/connect/add-ssh-keys#metadata), which uses public SSH keys stored in Compute Engine metadata to grant access to the instance. You can use SSH keys stored in project metadata to access all instances in a project. You can use SSH keys stored in instance metadata to access individual instances.
  - If you [connect to your instances](https://docs.cloud.google.com/compute/docs/instances/connecting-to-instance#gcetools) using the Google Cloud CLI or SSH from the console, Compute Engine automatically generates SSH keys for you.
- Windows Server instances:
  - [Generate credentials for Windows instances](https://docs.cloud.google.com/compute/docs/instances/windows/generating-credentials), which associates a password with a Windows user. Windows instances use this information to authenticate access to the instance.

## Accessing your instances

After you configure access to your instances, you can use one of many options to [connect to your Linux instances](https://docs.cloud.google.com/compute/docs/instances/connecting-to-instance) or [connect to your Windows instances](https://docs.cloud.google.com/compute/docs/instances/connecting-to-windows).

## Default time zone for compute instances

Regardless of the [region](https://docs.cloud.google.com/compute/docs/regions-zones) where you create your instance, the default time for your instance is Coordinated Universal Time (UTC).

## What's next

- If you are new to Compute Engine, see [Create a Linux instance in Compute Engine](https://docs.cloud.google.com/compute/docs/create-linux-vm-instance) to learn how to create an instance using the Google Cloud console.

- For a more detailed guide to create an instance, see [Create and start an instance](https://docs.cloud.google.com/compute/docs/instances/create-start-instance).

- For more information about the features of Compute Engine instances, see the following:

  - [Machine families resource and comparison guide](https://docs.cloud.google.com/compute/docs/machine-resource)

  - [Operating system images](https://docs.cloud.google.com/compute/docs/images)

  - [Networking overview for instances](https://docs.cloud.google.com/compute/docs/networking/network-overview)

  - [Choose a deployment strategy for your workload](https://docs.cloud.google.com/compute/docs/choose-compute-deployment-option)

- Learn how to [create a MIG from an existing instance](https://docs.cloud.google.com/compute/docs/instance-groups/create-mig-from-vm).

## Regions and zones

Compute Engine resources are hosted in multiple locations worldwide. These locations are composed of regions and zones.

*Regions* are independent geographic areas that consist of *zones*. Zones and regions are logical abstractions of underlying physical resources. For more information about region-specific considerations, see [Geography and regions](https://docs.cloud.google.com/docs/geography-and-regions#regions_and_zones).

Resources that live in a zone, such as [Compute Engine instances](https://docs.cloud.google.com/compute/docs/instances) or zonal [disks](https://docs.cloud.google.com/compute/docs/disks), are referred to as zonal resources. Other resources, like [static external IP addresses](https://docs.cloud.google.com/compute/docs/ip-addresses#reservedaddress), are regional. Regional resources can be used by any resource in that region, regardless of zone, while zonal resources can only be used by other resources in the same zone. For example, to attach a zonal persistent disk to an instance, both resources must be in the same zone. Similarly, if you want to assign a static IP address to an instance, the instance must be in the same region as the static IP address.

Putting resources in different zones in a region reduces the risk of an infrastructure outage affecting all resources simultaneously. Putting resources in different regions provides an even higher degree of failure independence. This lets you design robust systems with resources spread across different failure domains.

Only certain resources are region- or zone-specific. Other resources, such as images, are global resources that can be used by any other resources across any location. For information on global, regional, and zonal Compute Engine resources, see [Global, Regional, and Zonal Resources](https://docs.cloud.google.com/compute/docs/regions-zones/global-regional-zonal-resources).

Google Cloud also offers specialized AI zones that provide high-capacity GPUs and TPUs for AI and ML workloads. These zones have unique characteristics, including specific network latency requirements and shared fate with a parent zone. For more information, see [AI zones](https://docs.cloud.google.com/compute/docs/regions-zones/ai-zones).

## Identifying a region or zone

Each region in Compute Engine contains a number of zones. Each zone name contains two parts that describe each zone in detail. The first part of the zone name is the **region** and the second part of the name describes the **zone** in the region:

- **Region**

  Regions are collections of zones. Zones have high-bandwidth, low-latency network connections to other zones in the same region. In order to deploy fault-tolerant applications that have high availability, Google recommends deploying applications across multiple zones and multiple regions. This helps protect against unexpected failures of components, up to and including a single zone or region.

  Choose regions that make sense for your scenario. For example, if you only have customers in the US, or if you have specific needs that require your data to live in the US, it makes sense to store your resources in zones in the `us-central1` region or zones in the `us-east1` region.
- **Zone**

  A zone is a deployment area within a region. Zones which are specialized for AI and ML workloads are called AI zones. Non-AI zones are referred to as standard zones or just zones. Depending on how widely you want to distribute your resources, create compute instances across multiple zones in multiple regions for redundancy.
  - **Standard zone**

    A standard zone name contains two parts: the **region** and the **zone** in the region. For example, the fully qualified name for zone `a` in region `us-central1` is `us-central1-a`.
  - **AI zone**

    AI zones follow an extended naming convention to differentiate them from non-AI zones. For an AI zone, the `<zone>` variable consists of three parts: the string ai (to identify it as an AI zone), a number (indicating its deployment group), and a letter (indicating the shared software update schedule). For example, the fully qualified name for AI zone `ai2b` in region `us-west4` is `us-west4-ai2b`. This AI zone shares its deployment rollout wave with the standard `us-west4-b` zone.

## Resource quotas

Certain resources, such as static IPs, images, firewall rules, and VPC networks, have defined project-wide quota limits and per-region quota limits. When you create these resources, it counts towards your total project-wide quota or your per-region quota, if applicable. If any of the affected quota limits are exceeded, you won't be able to add more resources of the same type in that project or region.

To see a comprehensive list of quotas that apply to your project, visit the [Quotas](https://console.cloud.google.com/iam-admin/quotas) page in the Google Cloud console.

For example, if your global target pools quota is 50 and you create 25 target pools in example-region-1 and 25 target pools in example-region-2, you reach your project-wide quota and won't be able to create more target pools in any region within your project until you free up space. Similarly, if you have a per-region quota of 7 reserved IP addresses, you can only reserve up to 7 IP addresses in a single region. After you reach that limit, you will either need to reserve IP addresses in a new region or release some IP addresses.

## Transparent maintenance

Google regularly maintains its infrastructure by patching systems with the latest software, performing routine tests and preventative maintenance, and generally ensuring that Google infrastructure is as fast and efficient as Google knows how to make it.

By default, all compute instances are configured so that these maintenance events are transparent to your applications and workloads. Google uses a combination of datacenter innovations, operational best practices, and live migration technology to move running virtual machine instances out of the way of maintenance that is being performed. Your instance continues to run within the same zone with no action on your part.

By default, most virtual machines are set to live migrate, but you can also set your virtual machines to stop and reboot. Some machine series support only stop and reboot for maintenance operations. The two options differ in the following ways:

- **Live migrate**

  Compute Engine automatically migrates your running instance. The migration process will impact guest performance to some degree but your instance remains online throughout the migration process. The exact guest performance impact and duration depends on many factors, but it is expected most applications and workloads will not notice. For more information, see [Live Migration](https://docs.cloud.google.com/compute/docs/instances/live-migration-process).
- **Stop and reboot**

  Compute Engine automatically signals your instance to shut down, waits a short time for it to shut down cleanly, and then restarts it away from the maintenance event.

For more information on how to set the options above for your instances, see [Set VM host maintenance policy](https://docs.cloud.google.com/compute/docs/instances/setting-vm-host-options).

## Choosing a region and zone

You choose which region or zone hosts your resources, which controls where your data is stored and used. Choosing a region and zone is important for several reasons:


Handling failures
:
    Distribute your resources across multiple zones and regions to tolerate outages. Google designs zones to minimize the risk of correlated failures caused by physical infrastructure outages like power, cooling, or networking. Thus, if a zone becomes unavailable, you can transfer traffic to another zone in the same region to keep your services running. Similarly, you can mitigate the impact of a region outage on your application by running backup services in a different region. For more information about distributing your resources and designing a robust system, see [Designing resilient systems](https://docs.cloud.google.com/compute/docs/tutorials/robustsystems).


Decreased network latency
:
    To decrease network latency, you might want to choose a region or zone that is close to your point of service. For example, if you mostly have customers on the East coast of the United States of America, then you might want to choose a primary region and zone that is close to that area and a backup region and zone that is also close by.


Optimized AI and ML acceleration
:
    For workloads that require high-capacity AI accelerators, AI zones are available in select regions. These specialized zones provide GPU and TPU resources for AI and ML training and inference. You can select an AI zone to use infrastructure that is optimized for maximizing AI and ML throughput. See the [AI zones](https://docs.cloud.google.com/compute/docs/regions-zones/ai-zones) section for details.

For more information about how to choose a region and zone for your Compute Engine resources, see [Best practices for Compute Engine regions selection](https://cloud.google.com/solutions/best-practices-compute-engine-region-selection).

## Location selection tips

During compute instance creation, Compute Engine can automatically select zones for your instances based on capacity and availability using the following methods:

- The [bulk instance creation API](https://docs.cloud.google.com/compute/docs/instances/multiple/about-bulk-creation) can automatically choose the zone in which to create instances.
- A regional managed instance group (MIG) can be configured with a [target distribution shape](https://docs.cloud.google.com/compute/docs/instance-groups/regional-mig-set-target-distribution-shape), which can automatically create instances in zones where resources are available.
- If you are creating an instance in the Google Cloud console and you know the machine type and region that you want but you aren't sure which zone to select, you can select **Any** and Google will choose a zone for you based on the machine type and availability.

When selecting zones yourself, here are some things to keep in mind:

- **Communication within and across regions will incur different costs.**

  Generally, communication within regions will always be cheaper and faster than communication across different regions.
- **Design important systems with redundancy across multiple zones or regions.**

  At some point in time, your instances might experience an unexpected failure. To mitigate the effects of these possible events, you should duplicate important systems in multiple zones and regions.

  For example, by hosting instances in zones `europe-west1-b` and `europe-west1-c`, if `europe-west1-b` fails unexpectedly, your instances in zone `europe-west1-c` will still be available. However, if you host all your instances in `europe-west1-b`, you will not be able to access any instances if `europe-west1-b` goes offline. Also, consider hosting your resources across regions. For example, to plan for continued availability of your workload in the unlikely scenario that the `europe-west1` region experiences a failure, consider deploying the workload on backup instances in the `europe-west3` region. For more tips on how to design systems for availability, see [Designing resilient systems](https://docs.cloud.google.com/compute/docs/tutorials/robustsystems).

## Available regions and zones

You can use the Google Cloud console, the Google Cloud CLI, or REST to [see available regions and zones](https://docs.cloud.google.com/compute/docs/regions-zones/viewing-regions-zones). You can also get the complete list of available machine types in all regions and zones by using the [`gcloud compute machine-types list` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/machine-types/list). For example, running the following command displays all the regions and zones where you can use `c4d-standard-4` machine types.

    gcloud compute machine-types list --filter="name=c4d-standard-4"

Each zone offers a variety of processors. When you create an instance in a zone, your instance uses the default processor supported in that zone. For example, if you create an instance in the `us-central1-a` zone, your instance by default uses an Intel Haswell processor, unless you specify another option.

Alternatively, you can choose your desired CPU platform. For more information, read [Specifying a minimum CPU platform for VM instances](https://docs.cloud.google.com/compute/docs/instances/specify-min-cpu-platform).

Consider the following information about resource availability before you select the regions and zones where you create your instances:

- Local SSD and Titanium SSD storage is available in all regions and zones for supported machine series and machine types. See [About Local SSD disks](https://docs.cloud.google.com/compute/docs/disks/local-ssd) to learn more.
- [GPUs](https://docs.cloud.google.com/compute/docs/regions-zones/gpu-regions-zones) and [TPUs](https://docs.cloud.google.com/compute/docs/regions-zones/tpu-regions-zones) are available only in specific zones.
- [Sole-tenancy](https://docs.cloud.google.com/compute/docs/nodes/sole-tenant-nodes) is available in regions and zones where machine series with [sole-tenant node types](https://docs.cloud.google.com/compute/docs/nodes/sole-tenant-nodes#node_types) are available.
- [Confidential VM](https://docs.cloud.google.com/confidential-computing/confidential-vm/docs/supported-configurations) is available only with certain machine series in specific zones.

For information about hardware and feature support for all machine series, see [Machine series comparison](https://docs.cloud.google.com/compute/docs/machine-resource#machine_type_comparison). For example, to see which machine series support both Intel TDX and sole tenancy, in the **Choose instance properties to compare** field, select both **Confidential Computing** and **Sole tenancy**.

For zonal availability of bare metal machine types, see [Regional availability of bare metal instances](https://docs.cloud.google.com/compute/docs/instances/bare-metal-instances#regions-zones).
APAC North America South America Europe Middle East Africa A4X Max (NVIDIA GB300 Ultra Superchips) A4X (NVIDIA GB200 Superchips) {# Trailing hair space added to exclude A4X Max # } A4 (NVIDIA B200) A3 (NVIDIA H200/H100) A2 (NVIDIA A100) C4 C4A C4D C4N C3 C3D C2 C2D E2 G4 (NVIDIA RTX PRO 6000) G2 (NVIDIA L4) H4D H3 M4N M4 M3 M2 M1 N4A N4D N4 N2 N2D N1 T2D T2A X4 Z3 NVIDIA Grace Granite Rapids Google Axion Emerald Rapids Sapphire Rapids Ice Lake Cascade Lake Skylake AMD EPYC Turin AMD EPYC Genoa AMD EPYC Milan Ampere Altra Broadwell Haswell Sandy Bridge Ivy Bridge GPUs AMD SEV  AMD SEV-SNP Intel TDX NVIDIA Confidential Computing <button class="clear-all">Clear all</button>

| Zones | Location | Machine types | CPUs | Options | CO~2~ emissions |
|---|---|---|---|---|---|
| `africa-south1-a` | Johannesburg, South Africa | E2, N4 , N2 , N2D, C4 , C4A, C4D, T2D, M3, C2D | Intel Cascade Lake, Ice Lake, Emerald Rapids, Granite Rapids, AMD EPYC Milan, AMD EPYC Turin, Google Axion | [AMD SEV ](https://docs.cloud.google.com/confidential-computing/confidential-vm/docs/supported-configurations?tab=amd-sev) |   |
| `africa-south1-b` | Johannesburg, South Africa | E2, N4 , N2 , N2D, C4 , T2D, C2D | Intel Cascade Lake, Ice Lake, Emerald Rapids, Granite Rapids, AMD EPYC Milan | [AMD SEV ](https://docs.cloud.google.com/confidential-computing/confidential-vm/docs/supported-configurations?tab=amd-sev) |   |
| `africa-south1-c` | Johannesburg, South Africa | E2, N4 , N2 , N2D, C4 , C4D, T2D, M3, C2D | Intel Cascade Lake, Ice Lake, Emerald Rapids, Granite Rapids, AMD EPYC Milan, AMD EPYC Turin | [AMD SEV ](https://docs.cloud.google.com/confidential-computing/confidential-vm/docs/supported-configurations?tab=amd-sev) |   |
| `asia-east1-a` | Changhua County, Taiwan, APAC | E2, N4 , N2 , N2D, N1, C4 , C4A, C3 , C3D, T2D, Z3-metal, M1, C2 , C2D, G4, G2 | Intel Ivy Bridge, Sandy Bridge, Haswell, Broadwell, Skylake, Cascade Lake, Ice Lake, Sapphire Rapids, Emerald Rapids, Granite Rapids, AMD EPYC Milan, AMD EPYC Genoa, AMD EPYC Turin, Google Axion | GPUs, [AMD SEV ](https://docs.cloud.google.com/confidential-computing/confidential-vm/docs/supported-configurations?tab=amd-sev) |   |
| `asia-east1-b` | Changhua County, Taiwan, APAC | E2, N4 , N2 , N2D, N1, C4 , C4A, C3 , C3D, T2D, M3, M1, C2 , C2D, G2 | Intel Ivy Bridge, Sandy Bridge, Haswell, Broadwell, Skylake, Cascade Lake, Ice Lake, Sapphire Rapids, Emerald Rapids, Granite Rapids, AMD EPYC Milan, AMD EPYC Genoa, Google Axion | GPUs, [AMD SEV ](https://docs.cloud.google.com/confidential-computing/confidential-vm/docs/supported-configurations?tab=amd-sev) |   |
| `asia-east1-c` | Changhua County, Taiwan, APAC | E2, N4 , N2 , N2D, N1, C4 , C4A, C3 , C3D, T2D, Z3-metal, M3, M1, C2 , C2D, G2 | Intel Ivy Bridge, Sandy Bridge, Haswell, Broadwell, Skylake, Cascade Lake, Ice Lake, Emerald Rapids, Granite Rapids, AMD EPYC Milan, AMD EPYC Genoa, Google Axion | GPUs, [AMD SEV ](https://docs.cloud.google.com/confidential-computing/confidential-vm/docs/supported-configurations?tab=amd-sev) |   |
| `asia-east2-a` | Hong Kong, APAC | E2, N4 , N2 , N2D, N1, C4 , C3 , T2D, C2  | Intel Ivy Bridge, Sandy Bridge, Haswell, Broadwell, Skylake, Cascade Lake, Sapphire Rapids, Emerald Rapids, Granite Rapids, AMD EPYC Milan | GPUs, [AMD SEV ](https://docs.cloud.google.com/confidential-computing/confidential-vm/docs/supported-configurations?tab=amd-sev) |   |
| `asia-east2-b` | Hong Kong, APAC | E2, N2 , N2D, N1, T2D, C4 , C2  | Intel Ivy Bridge, Sandy Bridge, Haswell, Broadwell, Skylake, Cascade Lake, Ice Lake, Emerald Rapids, AMD EPYC Milan | [AMD SEV ](https://docs.cloud.google.com/confidential-computing/confidential-vm/docs/supported-configurations?tab=amd-sev) |   |
| `asia-east2-c` | Hong Kong, APAC | E2, N4 , N2 , N2D, N1, T2D, C4 , C2 , C2D | Intel Ivy Bridge, Sandy Bridge, Haswell, Broadwell, Skylake, Cascade Lake, Ice Lake, Emerald Rapids, Granite Rapids, AMD EPYC Milan | GPUs, [AMD SEV ](https://docs.cloud.google.com/confidential-computing/confidential-vm/docs/supported-configurations?tab=amd-sev) |   |
| `asia-northeast1-a` | Tokyo, Japan, APAC | E2, C4A, N4 , N2 , N2D, N1, T2D, Z3, M4, M3, M2, M1, C2 , A2, G2 | Intel Ivy Bridge, Sandy Bridge, Haswell, Broadwell, Skylake, Cascade Lake, Ice Lake, Emerald Rapids, AMD EPYC Milan, Google Axion | GPUs, [AMD SEV ](https://docs.cloud.google.com/confidential-computing/confidential-vm/docs/supported-configurations?tab=amd-sev) |   |
| `asia-northeast1-b` | Tokyo, Japan, APAC | E2, N4 , N2 , N2D, N1, C4 , C4A, C4D, C3 , T2D, Z3, M3, M2, M1, C2 , C2D, A4 , A3, G2 | Intel Ivy Bridge, Sandy Bridge, Haswell, Broadwell, Skylake, Cascade Lake, Ice Lake, Sapphire Rapids, Emerald Rapids, Granite Rapids, AMD EPYC Milan, AMD EPYC Turin, Google Axion | GPUs, [AMD SEV ](https://docs.cloud.google.com/confidential-computing/confidential-vm/docs/supported-configurations?tab=amd-sev), [Intel TDX](https://docs.cloud.google.com/confidential-computing/confidential-vm/docs/supported-configurations?tab=intel-tdx) |   |
| `asia-northeast1-c` | Tokyo, Japan, APAC | E2, N4 , N2 , N2D, N1, C4 , C4A, C4D, C3 , T2D, Z3, M3, M1, C2 , A2, G2 | Intel Ivy Bridge, Sandy Bridge, Haswell, Broadwell, Skylake, Cascade Lake, Ice Lake, Sapphire Rapids, Emerald Rapids, Granite Rapids, AMD EPYC Milan, AMD EPYC Turin, Google Axion | GPUs, [AMD SEV ](https://docs.cloud.google.com/confidential-computing/confidential-vm/docs/supported-configurations?tab=amd-sev) |   |
| `asia-northeast2-a` | Osaka, Japan, APAC | E2, N4 , N2 , N2D, N1, C4 , C3 , T2D, M3, M1, C2 , C2D | Intel Ivy Bridge, Sandy Bridge, Broadwell, Skylake, Cascade Lake, Ice Lake, Sapphire Rapids, Emerald Rapids, AMD EPYC Milan | [AMD SEV ](https://docs.cloud.google.com/confidential-computing/confidential-vm/docs/supported-configurations?tab=amd-sev) |   |
| `asia-northeast2-b` | Osaka, Japan, APAC | E2, N2 , N2D, N1, T2D, M3, M2, M1, C2  | Intel Ivy Bridge, Sandy Bridge, Broadwell, Skylake, Cascade Lake, Ice Lake, AMD EPYC Milan | [AMD SEV ](https://docs.cloud.google.com/confidential-computing/confidential-vm/docs/supported-configurations?tab=amd-sev) |   |
| `asia-northeast2-c` | Osaka, Japan, APAC | E2, N4 , N2 , N2D, N1, C4 , C3 , T2D, M3, M2, M1, C2 , C2D | Intel Ivy Bridge, Sandy Bridge, Broadwell, Skylake, Cascade Lake, Ice Lake, Sapphire Rapids, Emerald Rapids, AMD EPYC Milan | [AMD SEV ](https://docs.cloud.google.com/confidential-computing/confidential-vm/docs/supported-configurations?tab=amd-sev) |   |
| `asia-northeast3-a` | Seoul, South Korea, APAC | E2, N4 , N2 , N2D, N1, C4 , C3 , M3, M2, M1, C2 , C2D, G2 | Intel Ivy Bridge, Sandy Bridge, Haswell, Broadwell, Skylake, Cascade Lake, Ice Lake, Emerald Rapids, Granite Rapids, AMD EPYC Milan | GPUs, [AMD SEV ](https://docs.cloud.google.com/confidential-computing/confidential-vm/docs/supported-configurations?tab=amd-sev) |   |
| `asia-northeast3-b` | Seoul, South Korea, APAC | E2, N4 , N2 , N2D, N1, C4 , C3 , M3, M2, M1, C2 , C2D, A2, G2 | Intel Ivy Bridge, Sandy Bridge, Haswell, Broadwell, Skylake, Cascade Lake, Ice Lake, Emerald Rapids, Granite Rapids, AMD EPYC Milan | GPUs, [AMD SEV ](https://docs.cloud.google.com/confidential-computing/confidential-vm/docs/supported-configurations?tab=amd-sev) |   |
| `asia-northeast3-c` | Seoul, South Korea, APAC | E2, N4 , N2 , N2D, N1, C4 , M3, C2 , C2D, A3 | Intel Ivy Bridge, Sandy Bridge, Broadwell, Skylake, Cascade Lake, Ice Lake, Emerald Rapids, Granite Rapids, AMD EPYC Milan | GPUs, [AMD SEV ](https://docs.cloud.google.com/confidential-computing/confidential-vm/docs/supported-configurations?tab=amd-sev) |   |
| `asia-south1-a` | Mumbai, India, APAC | E2, N4 , N4D, N2 , N2D, C4 , C4A, C3 , C3D, T2D, N1, M2, M1, C2 , C2D, G2 | Intel Ivy Bridge, Sandy Bridge, Haswell, Broadwell, Skylake, Cascade Lake, Ice Lake, Sapphire Rapids, Emerald Rapids, Granite Rapids, AMD EPYC Milan, AMD EPYC Genoa, AMD EPYC Turin, Google Axion | GPUs, [AMD SEV ](https://docs.cloud.google.com/confidential-computing/confidential-vm/docs/supported-configurations?tab=amd-sev) |   |
| `asia-south1-b` | Mumbai, India, APAC | E2, N4 , N4D, N2 , N2D, N1, C4 , C4A, C4D, C3 , C3D, T2D, Z3, X4, M4 , M3, M2, M1, C2 , C2D, G2, A3 | Intel Ivy Bridge, Sandy Bridge, Haswell, Broadwell, Skylake, Cascade Lake, Ice Lake, Sapphire Rapids, Emerald Rapids, Granite Rapids, AMD EPYC Milan, AMD EPYC Genoa, AMD EPYC Turin, Google Axion | GPUs, [AMD SEV ](https://docs.cloud.google.com/confidential-computing/confidential-vm/docs/supported-configurations?tab=amd-sev), [Intel TDX](https://docs.cloud.google.com/confidential-computing/confidential-vm/docs/supported-configurations?tab=intel-tdx) |   |
| `asia-south1-c` | Mumbai, India, APAC | E2, N4 , N4A, N4D, N2 , N2D, N1, C4 , C4A, C4D, C3 , C3D, T2D, Z3, H4D, X4, M4 , M3, M1, C2 , C2D, A3, G4, G2 | Intel Ivy Bridge, Sandy Bridge, Haswell, Broadwell, Skylake, Cascade Lake, Ice Lake, Sapphire Rapids, Emerald Rapids, Granite Rapids, AMD EPYC Milan, AMD EPYC Genoa, AMD EPYC Turin, Google Axion | GPUs, [AMD SEV ](https://docs.cloud.google.com/confidential-computing/confidential-vm/docs/supported-configurations?tab=amd-sev) |   |
| `asia-south2-a` | Delhi, India, APAC | E2, N4 , N2 , N2D, N1, C4 , C3, T2D, X4, M4 , M3, M2, M1, C2 , C2D, G4 | Intel Ivy Bridge, Haswell, Broadwell, Skylake, Cascade Lake, Ice Lake, Sapphire Rapids, Emerald Rapids, Granite Rapids, AMD EPYC Milan, AMD EPYC Turin | GPUs, [AMD SEV ](https://docs.cloud.google.com/confidential-computing/confidential-vm/docs/supported-configurations?tab=amd-sev) |   |
| `asia-south2-b` | Delhi, India, APAC | E2, N4 , N2 , N2D, N1, C4 , C3 ,T2D, M4 , M3, M2, M1, C2 , C2D | Intel Ivy Bridge, Haswell, Broadwell, Skylake, Cascade Lake, Ice Lake, Sapphire Rapids, Emerald Rapids, Granite Rapids, AMD EPYC Milan | [AMD SEV ](https://docs.cloud.google.com/confidential-computing/confidential-vm/docs/supported-configurations?tab=amd-sev) |   |
| `asia-south2-c` | Delhi, India, APAC | E2, N4 , N2 , N2D, N1, C4 , C3 , T2D, C2 , A3, G4 | Intel Ivy Bridge, Haswell, Broadwell, Skylake, Cascade Lake, Emerald Rapids, Granite Rapids, AMD EPYC Milan, AMD EPYC Turin | GPUs, [AMD SEV ](https://docs.cloud.google.com/confidential-computing/confidential-vm/docs/supported-configurations?tab=amd-sev) |   |
| `asia-southeast1-a` | Jurong West, Singapore, APAC | E2, N4 , N4A, N4D, N2 , N2D, N1, C4 , C4A, C4D, C3 , C3D, C2 , C2D, T2D, Z3, H4D, M4 , M3, M2, M1, A2, G4, G2 | Intel Ivy Bridge, Sandy Bridge, Haswell, Broadwell, Skylake, Cascade Lake, Ice Lake, Sapphire Rapids, Emerald Rapids, Granite Rapids, AMD EPYC Milan, AMD EPYC Genoa, AMD EPYC Turin, Google Axion | GPUs, [AMD SEV ](https://docs.cloud.google.com/confidential-computing/confidential-vm/docs/supported-configurations?tab=amd-sev), [AMD SEV-SNP](https://docs.cloud.google.com/confidential-computing/confidential-vm/docs/supported-configurations?tab=amd-sev-snp), [Intel TDX](https://docs.cloud.google.com/confidential-computing/confidential-vm/docs/supported-configurations?tab=intel-tdx) |   |
| `asia-southeast1-b` | Jurong West, Singapore, APAC | E2, N4 , N4A, N4D, N2 , N2D, N1, C4 , C4A, C4D, C3 , C3D, C2 , C2D, T2D, T2A, Z3, M4 , M3, M2, M1, A4 , A3, G4, G2 | Intel Ivy Bridge, Sandy Bridge, Haswell, Broadwell, Skylake, Cascade Lake, Ice Lake, Sapphire Rapids, Emerald Rapids, Granite Rapids, AMD EPYC Milan, AMD EPYC Genoa, AMD EPYC Turin, Ampere Altra Arm, Google Axion | GPUs, [AMD SEV ](https://docs.cloud.google.com/confidential-computing/confidential-vm/docs/supported-configurations?tab=amd-sev), [AMD SEV-SNP](https://docs.cloud.google.com/confidential-computing/confidential-vm/docs/supported-configurations?tab=amd-sev-snp), [Intel TDX](https://docs.cloud.google.com/confidential-computing/confidential-vm/docs/supported-configurations?tab=intel-tdx) |   |
| `asia-southeast1-c` | Jurong West, Singapore, APAC | E2, N4 , N4A, N4D, N2 , N2D, N1, C4 , C4A, C4D, C3 , C3D, T2D, T2A, Z3, M1, C2 , C2D, A2, A3, G4, G2 | Intel Ivy Bridge, Sandy Bridge, Haswell, Broadwell, Skylake, Cascade Lake, Ice Lake, Sapphire Rapids, Emerald Rapids, Granite Rapids, AMD EPYC Milan, AMD EPYC Genoa, AMD EPYC Turin, Ampere Altra Arm, Google Axion | GPUs, [AMD SEV ](https://docs.cloud.google.com/confidential-computing/confidential-vm/docs/supported-configurations?tab=amd-sev), [AMD SEV-SNP](https://docs.cloud.google.com/confidential-computing/confidential-vm/docs/supported-configurations?tab=amd-sev-snp), [Intel TDX](https://docs.cloud.google.com/confidential-computing/confidential-vm/docs/supported-configurations?tab=intel-tdx) |   |
| `asia-southeast2-a` | Jakarta, Indonesia, APAC | E2, N4 , N2 , N2D, N1, C4 , C4A, C3 , T2D, M1 | Intel Ivy Bridge, Haswell, Broadwell, Skylake, Cascade Lake, Ice Lake, Sapphire Rapids, Emerald Rapids, Granite Rapids, AMD EPYC Milan | GPUs, [AMD SEV ](https://docs.cloud.google.com/confidential-computing/confidential-vm/docs/supported-configurations?tab=amd-sev) |   |
| `asia-southeast2-b` | Jakarta, Indonesia, APAC | E2, N4 , N2 , N2D, N1, C4 , C4A, T2D, G4 | Intel Ivy Bridge, Haswell, Broadwell, Skylake, Cascade Lake, Ice Lake, Emerald Rapids, Granite Rapids, AMD EPYC Milan, Google Axion AMD EPYC Turin | GPUs, [AMD SEV ](https://docs.cloud.google.com/confidential-computing/confidential-vm/docs/supported-configurations?tab=amd-sev) |   |
| `asia-southeast2-c` | Jakarta, Indonesia, APAC | E2, N4 , N2 , N2D, N1, C4 , C4A, T2D, M1, G4 | Intel Ivy Bridge, Haswell, Broadwell, Skylake, Cascade Lake, Ice Lake, Emerald Rapids, Granite Rapids, AMD EPYC Milan, AMD EPYC Turin, Google Axion | GPUs, [AMD SEV ](https://docs.cloud.google.com/confidential-computing/confidential-vm/docs/supported-configurations?tab=amd-sev) |   |
| `asia-southeast3-a` | Bangkok, Thailand, APAC | N4 , C4 , C3D, M4 , M3 | Intel Emerald Rapids, Granite Rapids, AMD EPYC Milan |   |   |
| `asia-southeast3-b` | Bangkok, Thailand, APAC | N4 , C4 , C3D, M4 , M3 | Intel Emerald Rapids, Granite Rapids, AMD EPYC Milan |   |   |
| `asia-southeast3-c` | Bangkok, Thailand, APAC | N4 , C4 , C3D, M4 , M3 | Intel Emerald Rapids, Granite Rapids, AMD EPYC Milan |   |   |
| `australia-southeast1-a` | Sydney, Australia, APAC | E2, N4 , N2 , N2D, N1, C3 , T2D, C2 , M3, M2, M1 | Intel Ivy Bridge, Sandy Bridge, Haswell, Broadwell, Skylake, Cascade Lake, Ice Lake, Sapphire Rapids, Emerald Rapids, AMD EPYC Milan | GPUs, [AMD SEV ](https://docs.cloud.google.com/confidential-computing/confidential-vm/docs/supported-configurations?tab=amd-sev) |   |
| `australia-southeast1-b` | Sydney, Australia, APAC | E2, N4 , N2 , N2D, N1, C4, C3 , C3D, T2D, Z3, C2 , M2, M1 | Intel Ivy Bridge, Sandy Bridge, Haswell, Broadwell, Skylake, Cascade Lake, Ice Lake, Sapphire Rapids, Emerald Rapids, Granite Rapids, AMD EPYC Milan, AMD EPYC Genoa | GPUs, [AMD SEV ](https://docs.cloud.google.com/confidential-computing/confidential-vm/docs/supported-configurations?tab=amd-sev) |   |
| `australia-southeast1-c` | Sydney, Australia, APAC | E2, N4 , N2 , N2D, N1, C4 , C4A, C4D, C3 , C3D, T2D, C2 , M4, M3, M1, A3, Z3 | Intel Ivy Bridge, Sandy Bridge, Haswell, Broadwell, Skylake, Cascade Lake, Ice Lake, Sapphire Rapids, Emerald Rapids, Granite Rapids, AMD EPYC Milan, AMD EPYC Genoa, AMD EPYC Turin, Google Axion | GPUs, [AMD SEV ](https://docs.cloud.google.com/confidential-computing/confidential-vm/docs/supported-configurations?tab=amd-sev) |   |
| `australia-southeast2-a` | Melbourne, Australia, APAC | E2, N4 , N2 , N2D, N1, C4 , C4A, C3 , C3D, T2D, Z3-metal, C2D | Intel Ivy Bridge, Haswell, Broadwell, Skylake, Cascade Lake, Ice Lake, Sapphire Rapids, Emerald Rapids, AMD EPYC Milan, Google Axion | [AMD SEV ](https://docs.cloud.google.com/confidential-computing/confidential-vm/docs/supported-configurations?tab=amd-sev) |   |
| `australia-southeast2-b` | Melbourne, Australia, APAC | E2, N4 , N2 , N2D, N1, C4 , C4A, T2D, C3 , Z3-metal, M3, M1 | Intel Ivy Bridge, Haswell, Broadwell, Skylake, Cascade Lake, Ice Lake, Sapphire Rapids, Emerald Rapids, Granite Rapids, AMD EPYC Milan, Google Axion |   |   |
| `australia-southeast2-c` | Melbourne, Australia, APAC | E2, N4 , N2 , N2D, C4 , C4A, T2D, N1, M3, M1 | Intel Ivy Bridge, Haswell, Broadwell, Skylake, Cascade Lake, Ice Lake, Emerald Rapids, Granite Rapids, AMD EPYC Milan, Google Axion | [AMD SEV ](https://docs.cloud.google.com/confidential-computing/confidential-vm/docs/supported-configurations?tab=amd-sev) |   |
| `europe-north1-a` | Hamina, Finland, Europe | E2, N4 , N2 , N2D, N1, C4 , C4A, C3D, T2D, C2 , M3, G4 | Intel Ivy Bridge, Sandy Bridge, Broadwell, Skylake, Cascade Lake, Ice Lake, Emerald Rapids, AMD EPYC Milan, AMD EPYC Turin, Google Axion | GPUs, [AMD SEV ](https://docs.cloud.google.com/confidential-computing/confidential-vm/docs/supported-configurations?tab=amd-sev) | ![leaf icon](https://cloud.google.com/sustainability/region-carbon/gleaf.svg) [Low CO~2~](https://cloud.google.com/sustainability/region-carbon#region-picker) |
| `europe-north1-b` | Hamina, Finland, Europe | E2, N4 , N2 , N2D, N1, C4A, C4 , C3 , T2D, C2 , A4 , G4 | Intel Ivy Bridge, Sandy Bridge, Broadwell, Skylake, Cascade Lake, Emerald Rapids, Granite Rapids, AMD EPYC Milan, AMD EPYC Turin, Google Axion | GPUs, [AMD SEV ](https://docs.cloud.google.com/confidential-computing/confidential-vm/docs/supported-configurations?tab=amd-sev) | ![leaf icon](https://cloud.google.com/sustainability/region-carbon/gleaf.svg) [Low CO~2~](https://cloud.google.com/sustainability/region-carbon#region-picker) |
| `europe-north1-c` | Hamina, Finland, Europe | E2, N4 , N2 , N2D, N1, T2D, C4 , C4A, C2 , M3 | Intel Ivy Bridge, Sandy Bridge, Broadwell, Skylake, Cascade Lake, Ice Lake, Emerald Rapids, Granite Rapids, AMD EPYC Milan, Google Axion | [AMD SEV ](https://docs.cloud.google.com/confidential-computing/confidential-vm/docs/supported-configurations?tab=amd-sev) | ![leaf icon](https://cloud.google.com/sustainability/region-carbon/gleaf.svg) [Low CO~2~](https://cloud.google.com/sustainability/region-carbon#region-picker) |
| `europe-north2-a` | Stockholm, Sweden, Europe | E2, N4 , C4 , C4A, C3 , C3D, Z3 | Intel Ivy Bridge, Broadwell, Haswell, Cascade Lake, Ice Lake, Sapphire Rapids, Emerald Rapids, Granite Rapids, AMD EPYC Milan, AMD EPYC Genoa, Google Axion | [AMD SEV ](https://docs.cloud.google.com/confidential-computing/confidential-vm/docs/supported-configurations?tab=amd-sev) | ![leaf icon](https://cloud.google.com/sustainability/region-carbon/gleaf.svg) [Low CO~2~](https://cloud.google.com/sustainability/region-carbon#region-picker) |
| `europe-north2-b` | Stockholm, Sweden, Europe | E2, N4 , C4 , C4A, C3 , C3D, Z3, C2D | Intel Ivy Bridge, Broadwell, Haswell, Cascade Lake, Ice Lake, Sapphire Rapids, Emerald Rapids, Granite Rapids, AMD EPYC Milan, AMD EPYC Genoa, Google Axion | [AMD SEV ](https://docs.cloud.google.com/confidential-computing/confidential-vm/docs/supported-configurations?tab=amd-sev) | ![leaf icon](https://cloud.google.com/sustainability/region-carbon/gleaf.svg) [Low CO~2~](https://cloud.google.com/sustainability/region-carbon#region-picker) |
| `europe-north2-c` | Stockholm, Sweden, Europe | E2, N4 , C4  | Intel Ivy Bridge, Broadwell, Haswell, Cascade Lake, Ice Lake, Emerald Rapids, AMD EPYC Milan | [AMD SEV ](https://docs.cloud.google.com/confidential-computing/confidential-vm/docs/supported-configurations?tab=amd-sev) | ![leaf icon](https://cloud.google.com/sustainability/region-carbon/gleaf.svg) [Low CO~2~](https://cloud.google.com/sustainability/region-carbon#region-picker) |
| `europe-central2-a` | Warsaw, Poland, Europe | E2, N4 , N2 , N2D, N1, C4 , C4A, T2D, M4, M3, M1, C2D | Intel Ivy Bridge, Haswell, Broadwell, Skylake, Cascade Lake, Ice Lake, Emerald Rapids, Granite Rapids, AMD EPYC Milan, Google Axion | [AMD SEV ](https://docs.cloud.google.com/confidential-computing/confidential-vm/docs/supported-configurations?tab=amd-sev) |   |
| `europe-central2-b` | Warsaw, Poland, Europe | E2, N2 , N2D, N1, T2D, M1, C2D | Intel Ivy Bridge, Haswell, Broadwell, Skylake, Cascade Lake, Ice Lake, AMD EPYC Milan | GPUs, [AMD SEV ](https://docs.cloud.google.com/confidential-computing/confidential-vm/docs/supported-configurations?tab=amd-sev) |   |
| `europe-central2-c` | Warsaw, Poland, Europe | E2, N4 , N2 , N2D, N1, C4 , T2D | Intel Ivy Bridge, Haswell, Broadwell, Skylake, Cascade Lake, Ice Lake, Emerald Rapids, AMD EPYC Milan | GPUs, [AMD SEV ](https://docs.cloud.google.com/confidential-computing/confidential-vm/docs/supported-configurations?tab=amd-sev) |   |
| `europe-southwest1-a` | Madrid, Spain, Europe | E2, N4 , N2 , N2D, C4 , C4A, T2D, M4, M3, M2, M1 | Intel Broadwell, Skylake, Cascade Lake, Ice Lake, Emerald Rapids, AMD EPYC Milan, Google Axion | [AMD SEV ](https://docs.cloud.google.com/confidential-computing/confidential-vm/docs/supported-configurations?tab=amd-sev) | ![leaf icon](https://cloud.google.com/sustainability/region-carbon/gleaf.svg) [Low CO~2~](https://cloud.google.com/sustainability/region-carbon#region-picker) |
| `europe-southwest1-b` | Madrid, Spain, Europe | E2, N4 , N2 , N2D, C4 , C4A, T2D, C2D | Intel Broadwell, Skylake, Cascade Lake, Ice Lake, Emerald Rapids, Granite Rapids, AMD EPYC Milan, Google Axion | [AMD SEV ](https://docs.cloud.google.com/confidential-computing/confidential-vm/docs/supported-configurations?tab=amd-sev) | ![leaf icon](https://cloud.google.com/sustainability/region-carbon/gleaf.svg) [Low CO~2~](https://cloud.google.com/sustainability/region-carbon#region-picker) |
| `europe-southwest1-c` | Madrid, Spain, Europe | E2, N4 , N2 , N2D, C4 , C4A, T2D, M4 , M3, M2, M1 | Intel Broadwell, Skylake, Cascade Lake, Ice Lake, Emerald Rapids, Granite Rapids, AMD EPYC Milan, Google Axion | [AMD SEV ](https://docs.cloud.google.com/confidential-computing/confidential-vm/docs/supported-configurations?tab=amd-sev) | ![leaf icon](https://cloud.google.com/sustainability/region-carbon/gleaf.svg) [Low CO~2~](https://cloud.google.com/sustainability/region-carbon#region-picker) |
| `europe-west1-b` | St. Ghislain, Belgium, Europe | E2, N4 , N4A, N4D, N2 , N2D, N1, C4 , C4A, C4D, C3 , C3D, T2D, Z3, X4, M4 , M3, M2, M1, C2 , C2D, A3, G2 | Intel Ivy Bridge, Sandy Bridge, Haswell, Broadwell, Skylake, Cascade Lake, Ice Lake, Sapphire Rapids, Emerald Rapids, Granite Rapids, AMD EPYC Milan, AMD EPYC Genoa, AMD EPYC Turin, Google Axion | GPUs, [AMD SEV ](https://docs.cloud.google.com/confidential-computing/confidential-vm/docs/supported-configurations?tab=amd-sev) | ![leaf icon](https://cloud.google.com/sustainability/region-carbon/gleaf.svg) [Low CO~2~](https://cloud.google.com/sustainability/region-carbon#region-picker) |
| `europe-west1-c` | St. Ghislain, Belgium, Europe | E2, N4 , N4A, N4D, N2 , N2D, N1, C4 , C4A, C4D, C3 , C3D, T2D, Z3, X4, M4N, M4, M2, C2 , C2D, A3, G4, G2 | Intel Ivy Bridge, Sandy Bridge, Haswell, Broadwell, Skylake, Cascade Lake, Ice Lake, Sapphire Rapids, Emerald Rapids, Granite Rapids, AMD EPYC Milan, AMD EPYC Genoa, AMD EPYC Turin, Google Axion | GPUs, [AMD SEV ](https://docs.cloud.google.com/confidential-computing/confidential-vm/docs/supported-configurations?tab=amd-sev) | ![leaf icon](https://cloud.google.com/sustainability/region-carbon/gleaf.svg) [Low CO~2~](https://cloud.google.com/sustainability/region-carbon#region-picker) |
| `europe-west1-d` | St. Ghislain, Belgium, Europe | E2, N4 , N4D, N2 , N2D, N1, C4 , C4A, C4D, C3 , C3D, T2D, Z3, M4 , M3, M2, M1, C2 , C2D | Intel Ivy Bridge, Sandy Bridge, Haswell, Broadwell, Skylake, Cascade Lake, Ice Lake, Sapphire Rapids, Emerald Rapids, Granite Rapids, AMD EPYC Milan, AMD EPYC Genoa, AMD EPYC Turin, Google Axion | GPUs, [AMD SEV ](https://docs.cloud.google.com/confidential-computing/confidential-vm/docs/supported-configurations?tab=amd-sev) | ![leaf icon](https://cloud.google.com/sustainability/region-carbon/gleaf.svg) [Low CO~2~](https://cloud.google.com/sustainability/region-carbon#region-picker) |
| `europe-west2-a` | London, England, Europe | E2, N4 , N4A, N4D, N2 , N2D, N1, C4 , C4A, C4D, C4N, C3 , C3D, C2 , C2D, T2D, Z3, M3, M2, M1, G2 | Intel Ivy Bridge, Sandy Bridge, Haswell, Broadwell, Skylake, Cascade Lake, Ice Lake, Sapphire Rapids, Emerald Rapids, Granite Rapids, AMD EPYC Milan, AMD EPYC Genoa, AMD EPYC Turin, Google Axion | GPUs, [AMD SEV ](https://docs.cloud.google.com/confidential-computing/confidential-vm/docs/supported-configurations?tab=amd-sev) | ![leaf icon](https://cloud.google.com/sustainability/region-carbon/gleaf.svg) [Low CO~2~](https://cloud.google.com/sustainability/region-carbon#region-picker) |
| `europe-west2-b` | London, England, Europe | E2, N4 , N4A, N2 , N2D, N1, C4 , C4A, C4D, C3 , C3D, C2 , C2D, T2D, Z3, M3, M2, M1, G4, G2 | Intel Ivy Bridge, Sandy Bridge, Haswell, Broadwell, Skylake, Cascade Lake, Ice Lake, Sapphire Rapids, Emerald Rapids, Granite Rapids, AMD EPYC Milan, AMD EPYC Genoa, AMD EPYC Turin, Google Axion | GPUs, [AMD SEV ](https://docs.cloud.google.com/confidential-computing/confidential-vm/docs/supported-configurations?tab=amd-sev) | ![leaf icon](https://cloud.google.com/sustainability/region-carbon/gleaf.svg) [Low CO~2~](https://cloud.google.com/sustainability/region-carbon#region-picker) |
| `europe-west2-c` | London, England, Europe | E2, N4 , N4A, N4D, N2 , N2D, N1, C4 , C4A, C4D, C3 , C2 , C2D, T2D, Z3, M4N, M4, M3, M1, G4 | Intel Ivy Bridge, Sandy Bridge, Haswell, Broadwell, Skylake, Cascade Lake, Ice Lake, Sapphire Rapids, Emerald Rapids, Granite Rapids, AMD EPYC Milan, AMD EPYC Turin, Google Axion | GPUs, [AMD SEV ](https://docs.cloud.google.com/confidential-computing/confidential-vm/docs/supported-configurations?tab=amd-sev) | ![leaf icon](https://cloud.google.com/sustainability/region-carbon/gleaf.svg) [Low CO~2~](https://cloud.google.com/sustainability/region-carbon#region-picker) |
| `europe-west3-a` | Frankfurt, Germany, Europe | E2, N4 , N4A, N4D, N2 , N2D, N1, C4 , C4A, C4D, C3 , C3D, T2D, Z3, X4, M4 , M3, M2, M1, C2 , C2D, G2 | Intel Ivy Bridge, Sandy Bridge, Haswell, Broadwell, Skylake, Cascade Lake, Ice Lake, Sapphire Rapids, Emerald Rapids, Granite Rapids, AMD EPYC Milan, AMD EPYC Genoa, AMD EPYC Turin, Google Axion | GPUs, [AMD SEV ](https://docs.cloud.google.com/confidential-computing/confidential-vm/docs/supported-configurations?tab=amd-sev), [AMD SEV-SNP](https://docs.cloud.google.com/confidential-computing/confidential-vm/docs/supported-configurations?tab=amd-sev-snp) |   |
| `europe-west3-b` | Frankfurt, Germany, Europe | E2, N4 , N4A, N2 , N2D, N1, C4 , C4A, C4D, C3 , C3D, T2D, Z3, X4, M4 , M3, M2, M1, C2 , C2D, G2 | Intel Ivy Bridge, Sandy Bridge, Haswell, Broadwell, Skylake, Cascade Lake, Ice Lake, Sapphire Rapids, Emerald Rapids, Granite Rapids, AMD EPYC Milan, AMD EPYC Genoa, AMD EPYC Turin, Google Axion | GPUs, [AMD SEV ](https://docs.cloud.google.com/confidential-computing/confidential-vm/docs/supported-configurations?tab=amd-sev), [AMD SEV-SNP](https://docs.cloud.google.com/confidential-computing/confidential-vm/docs/supported-configurations?tab=amd-sev-snp) |   |
| `europe-west3-c` | Frankfurt, Germany, Europe | E2, N4 , N4A, N2 , N2D, N1, C4 , C4A, C4D, C3 , C3D, T2D, Z3, M3, M1, C2 , C2D, A3 | Intel Ivy Bridge, Sandy Bridge, Haswell, Broadwell, Skylake, Cascade Lake, Ice Lake, Sapphire Rapids, Emerald Rapids, Granite Rapids, AMD EPYC Milan, AMD EPYC Genoa, AMD EPYC Turin, Google Axion | GPUs, [AMD SEV ](https://docs.cloud.google.com/confidential-computing/confidential-vm/docs/supported-configurations?tab=amd-sev), [AMD SEV-SNP](https://docs.cloud.google.com/confidential-computing/confidential-vm/docs/supported-configurations?tab=amd-sev-snp) |   |
| `europe-west4-a` | Eemshaven, Netherlands, Europe | E2, N4 , N4A, N4D, N2 , N2D, N1, C4 , C4A, C4D, C3 , C3D, T2D, T2A, Z3, X4, M4 , M3, M2, M1, C2 , C2D, A3, A2, G4, G2 | Intel Ivy Bridge, Sandy Bridge, Haswell, Broadwell, Skylake, Cascade Lake, Ice Lake, Sapphire Rapids, Emerald Rapids, Granite Rapids, AMD EPYC Milan, AMD EPYC Genoa, AMD EPYC Turin, Ampere Altra Arm, Google Axion | GPUs, [AMD SEV ](https://docs.cloud.google.com/confidential-computing/confidential-vm/docs/supported-configurations?tab=amd-sev), [AMD SEV-SNP](https://docs.cloud.google.com/confidential-computing/confidential-vm/docs/supported-configurations?tab=amd-sev-snp), [Intel TDX](https://docs.cloud.google.com/confidential-computing/confidential-vm/docs/supported-configurations?tab=intel-tdx) | ![leaf icon](https://cloud.google.com/sustainability/region-carbon/gleaf.svg) [Low CO~2~](https://cloud.google.com/sustainability/region-carbon#region-picker) |
| `europe-west4-b` | Eemshaven, Netherlands, Europe | E2, N4 , N4A, N4D, N2 , N2D, N1, C4 , C4A, C4D, C3 , C3D, T2D, T2A, Z3, X4, M4 , M3, M2, M1, H4D, H3, C2 , C2D, A4X , A4 , A3, A2, G4, G2 | Intel Ivy Bridge, Sandy Bridge, Haswell, Broadwell, Skylake, Cascade Lake, Ice Lake, Sapphire Rapids, Emerald Rapids, Granite Rapids, AMD EPYC Milan, AMD EPYC Genoa, AMD EPYC Turin, Ampere Altra Arm, Google Axion | GPUs, [AMD SEV ](https://docs.cloud.google.com/confidential-computing/confidential-vm/docs/supported-configurations?tab=amd-sev), [AMD SEV-SNP](https://docs.cloud.google.com/confidential-computing/confidential-vm/docs/supported-configurations?tab=amd-sev-snp), [Intel TDX](https://docs.cloud.google.com/confidential-computing/confidential-vm/docs/supported-configurations?tab=intel-tdx) | ![leaf icon](https://cloud.google.com/sustainability/region-carbon/gleaf.svg) [Low CO~2~](https://cloud.google.com/sustainability/region-carbon#region-picker) |
| `europe-west4-c` | Eemshaven, Netherlands, Europe | E2, N4 , N4A, N4D, N2 , N2D, N1, C4 , C4A, C4D, C3 , C3D, T2D, T2A, Z3, X4, M2, M1, H4D, H3, C2 , C2D, A3, G2 | Intel Ivy Bridge, Sandy Bridge, Haswell, Broadwell, Skylake, Cascade Lake, Ice Lake, Sapphire Rapids, Emerald Rapids, Granite Rapids, AMD EPYC Milan, AMD EPYC Genoa, AMD EPYC Turin, Ampere Altra Arm, Google Axion | GPUs, [AMD SEV ](https://docs.cloud.google.com/confidential-computing/confidential-vm/docs/supported-configurations?tab=amd-sev), [AMD SEV-SNP](https://docs.cloud.google.com/confidential-computing/confidential-vm/docs/supported-configurations?tab=amd-sev-snp), [Intel TDX](https://docs.cloud.google.com/confidential-computing/confidential-vm/docs/supported-configurations?tab=intel-tdx), [NVIDIA Confidential Computing](https://docs.cloud.google.com/confidential-computing/confidential-vm/docs/supported-configurations?tab=nvidia-confidential-computing) | ![leaf icon](https://cloud.google.com/sustainability/region-carbon/gleaf.svg) [Low CO~2~](https://cloud.google.com/sustainability/region-carbon#region-picker) |
| `europe-west6-a` | Zurich, Switzerland, Europe | E2, N4 , N2 , N2D, N1, C2 , T2D | Intel Ivy Bridge, Sandy Bridge, Haswell, Broadwell, Skylake, Cascade Lake, Ice Lake, Emerald Rapids, AMD EPYC Milan |   | ![leaf icon](https://cloud.google.com/sustainability/region-carbon/gleaf.svg) [Low CO~2~](https://cloud.google.com/sustainability/region-carbon#region-picker) |
| `europe-west6-b` | Zurich, Switzerland, Europe | E2, N4 , N2 , N2D, N1, C4 , C4A, T2D, M3, M1, C2 , G2, Z3 | Intel Ivy Bridge, Sandy Bridge, Haswell, Broadwell, Skylake, Cascade Lake, Ice Lake, Sapphire Rapids, Emerald Rapids, Granite Rapids, AMD EPYC Milan, Google Axion | GPUs, [AMD SEV ](https://docs.cloud.google.com/confidential-computing/confidential-vm/docs/supported-configurations?tab=amd-sev) | ![leaf icon](https://cloud.google.com/sustainability/region-carbon/gleaf.svg) [Low CO~2~](https://cloud.google.com/sustainability/region-carbon#region-picker) |
| `europe-west6-c` | Zurich, Switzerland, Europe | E2, N4 , N2 , N2D, N1, C4 , T2D, M3, M1, C2 , G2 | Intel Ivy Bridge, Sandy Bridge, Haswell, Broadwell, Skylake, Cascade Lake, Ice Lake, Emerald Rapids, Granite Rapids, AMD EPYC Milan | GPUs, [AMD SEV ](https://docs.cloud.google.com/confidential-computing/confidential-vm/docs/supported-configurations?tab=amd-sev) | ![leaf icon](https://cloud.google.com/sustainability/region-carbon/gleaf.svg) [Low CO~2~](https://cloud.google.com/sustainability/region-carbon#region-picker) |
| `europe-west8-a` | Milan, Italy, Europe | E2, N4 , N2 , N2D, T2D, X4, M3, M2, M1 | Intel Broadwell, Skylake, Cascade Lake, Ice Lake, Sapphire Rapids, Emerald Rapids, AMD EPYC Milan | [AMD SEV ](https://docs.cloud.google.com/confidential-computing/confidential-vm/docs/supported-configurations?tab=amd-sev) |   |
| `europe-west8-b` | Milan, Italy, Europe | E2, N4 , N2 , N2D, C4 , T2D, Z3-metal, M2, G4 | Intel Broadwell, Skylake, Cascade Lake, Sapphire Rapids, Emerald Rapids, Granite Rapids, AMD EPYC Milan, AMD EPYC Turin | GPUs, [AMD SEV ](https://docs.cloud.google.com/confidential-computing/confidential-vm/docs/supported-configurations?tab=amd-sev) |   |
| `europe-west8-c` | Milan, Italy, Europe | E2, N4 , N2 , N2D, C4 , C2D, T2D, Z3-metal, X4, M3, M2, M1 | Intel Broadwell, Skylake, Cascade Lake, Ice Lake, Sapphire Rapids, Emerald Rapids, Granite Rapids, AMD EPYC Milan | [AMD SEV ](https://docs.cloud.google.com/confidential-computing/confidential-vm/docs/supported-configurations?tab=amd-sev) |   |
| `europe-west9-a` | Paris, France, Europe | E2, N4 , N2 , N2D, C4 , C3 , T2D, M3 | Intel Broadwell, Skylake, Cascade Lake, Ice Lake, Sapphire Rapids, Emerald Rapids, AMD EPYC Milan | [AMD SEV ](https://docs.cloud.google.com/confidential-computing/confidential-vm/docs/supported-configurations?tab=amd-sev), [Intel TDX](https://docs.cloud.google.com/confidential-computing/confidential-vm/docs/supported-configurations?tab=intel-tdx) | ![leaf icon](https://cloud.google.com/sustainability/region-carbon/gleaf.svg) [Low CO~2~](https://cloud.google.com/sustainability/region-carbon#region-picker) |
| `europe-west9-b` | Paris, France, Europe | E2, N4 , N2 , N2D, C4 , C4D, C3 , T2D, M3, M1 | Intel Broadwell, Haswell, Skylake, Cascade Lake, Ice Lake, Sapphire Rapids, Emerald Rapids, Granite Rapids, AMD EPYC Milan, AMD EPYC Turin | [AMD SEV ](https://docs.cloud.google.com/confidential-computing/confidential-vm/docs/supported-configurations?tab=amd-sev), [Intel TDX](https://docs.cloud.google.com/confidential-computing/confidential-vm/docs/supported-configurations?tab=intel-tdx) | ![leaf icon](https://cloud.google.com/sustainability/region-carbon/gleaf.svg) [Low CO~2~](https://cloud.google.com/sustainability/region-carbon#region-picker) |
| `europe-west9-c` | Paris, France, Europe | E2, N4 , N2 , N2D, C4 , C3 , T2D, M1 | Intel Broadwell, Haswell, Skylake, Cascade Lake, Ice Lake, Sapphire Rapids, Emerald Rapids, Granite Rapids, AMD EPYC Milan | [AMD SEV ](https://docs.cloud.google.com/confidential-computing/confidential-vm/docs/supported-configurations?tab=amd-sev) | ![leaf icon](https://cloud.google.com/sustainability/region-carbon/gleaf.svg) [Low CO~2~](https://cloud.google.com/sustainability/region-carbon#region-picker) |
| `europe-west10-a` | Berlin, Germany, Europe | E2, N4 , N2 , N2D, C4D, C3 , T2D, Z3 | Intel Broadwell, Skylake, Cascade Lake, Ice Lake, Sapphire Rapids, Emerald Rapids, AMD EPYC Milan, AMD EPYC Turin | [AMD SEV ](https://docs.cloud.google.com/confidential-computing/confidential-vm/docs/supported-configurations?tab=amd-sev) |   |
| `europe-west10-b` | Berlin, Germany, Europe | E2, N2 , N2D, C4D, Z3, G4 | Intel Cascade Lake, Ice Lake, Sapphire Rapids, AMD EPYC Milan, AMD EPYC Turin | [AMD SEV ](https://docs.cloud.google.com/confidential-computing/confidential-vm/docs/supported-configurations?tab=amd-sev) |   |
| `europe-west10-c` | Berlin, Germany, Europe | E2, N4 , N2 , N2D, C4 , C4D, T2D, Z3 | Intel Broadwell, Skylake, Cascade Lake, Ice Lake, Sapphire Rapids, Emerald Rapids, AMD EPYC Milan, AMD EPYC Turin | [AMD SEV ](https://docs.cloud.google.com/confidential-computing/confidential-vm/docs/supported-configurations?tab=amd-sev) |   |
| `europe-west12-a` | Turin, Italy, Europe | E2, N2 , N2D, T2D, M4, M3 | Intel Broadwell, Skylake, Cascade Lake, Ice Lake, Emerald Rapids, AMD EPYC Milan | [AMD SEV ](https://docs.cloud.google.com/confidential-computing/confidential-vm/docs/supported-configurations?tab=amd-sev) |   |
| `europe-west12-b` | Turin, Italy, Europe | E2, N2 , N2D, T2D, M3, C2D | Intel Broadwell, Skylake, Cascade Lake, Ice Lake, AMD EPYC Milan | [AMD SEV ](https://docs.cloud.google.com/confidential-computing/confidential-vm/docs/supported-configurations?tab=amd-sev) |   |
| `europe-west12-c` | Turin, Italy, Europe | E2, N4 , N2 , N2D, C4 , T2D | Intel Broadwell, Skylake, Cascade Lake, Emerald Rapids, AMD EPYC Milan | [AMD SEV ](https://docs.cloud.google.com/confidential-computing/confidential-vm/docs/supported-configurations?tab=amd-sev) |   |
| `me-central1-a` | Doha, Qatar, Middle East | E2, N2 , N2D, C4 , C3 , T2D, Z3-metal | Intel Broadwell, Haswell, Ivy Bridge, Skylake, Cascade Lake, Ice Lake, Sapphire Rapids, AMD EPYC Milan |   |   |
| `me-central1-b` | Doha, Qatar, Middle East | E2, N4 , N2 , N2D, C4 , T2D, M3 | Intel Broadwell, Haswell, Ivy Bridge, Skylake, Cascade Lake, Ice Lake, Emerald Rapids, AMD EPYC Milan | [AMD SEV ](https://docs.cloud.google.com/confidential-computing/confidential-vm/docs/supported-configurations?tab=amd-sev) |   |
| `me-central1-c` | Doha, Qatar, Middle East | E2, N4 , N2 , N2D, C4 , C4A, C3 , T2D, Z3-metal, M3 | Intel Broadwell, Haswell, Ivy Bridge, Skylake, Cascade Lake, Ice Lake, Sapphire Rapids, Emerald Rapids, Granite Rapids, AMD EPYC Milan, Google Axion | [AMD SEV ](https://docs.cloud.google.com/confidential-computing/confidential-vm/docs/supported-configurations?tab=amd-sev) |   |
| `me-central2-a` | Dammam, Saudi Arabia, Middle East | E2, N4 , N2 , N2D, C4 , C4A, C3 , C3D, T2D, C2  M3, M2, G2 | Intel Broadwell, Haswell, Cascade Lake, Ice Lake, Sapphire Rapids, Emerald Rapids, Granite Rapids, EPYC Milan, AMD EPYC Genoa, Google Axion | GPUs, [AMD SEV ](https://docs.cloud.google.com/confidential-computing/confidential-vm/docs/supported-configurations?tab=amd-sev) |   |
| `me-central2-b` | Dammam, Saudi Arabia, Middle East | E2, N2 , N2D, C3 , T2D, M3, M2, C2  | Intel Broadwell, Haswell, Ivy Bridge, Cascade Lake, Ice Lake, Sapphire Rapids, AMD EPYC Milan | [AMD SEV ](https://docs.cloud.google.com/confidential-computing/confidential-vm/docs/supported-configurations?tab=amd-sev) |   |
| `me-central2-c` | Dammam, Saudi Arabia, Middle East | E2, N4 , N2 , N2D, C4 , C3 , C3D, T2D, M4 , M3, M2, C2 , G2 | Intel Broadwell, Haswell, Ivy Bridge, Cascade Lake, Ice Lake, Sapphire Rapids, Emerald Rapids, Granite Rapids, AMD EPYC Milan | GPUs, [AMD SEV ](https://docs.cloud.google.com/confidential-computing/confidential-vm/docs/supported-configurations?tab=amd-sev) |   |
| `me-west1-a` | Tel Aviv, Israel, Middle East | E2, N4 , N2 , N2D, C4 , C3 , T2D, M3, M1, C2 , A2 | Intel Broadwell, Haswell, Skylake, Cascade Lake, Ice Lake, Sapphire Rapids, Emerald Rapids, AMD EPYC Milan | GPUs, [AMD SEV ](https://docs.cloud.google.com/confidential-computing/confidential-vm/docs/supported-configurations?tab=amd-sev) |   |
| `me-west1-b` | Tel Aviv, Israel, Middle East | E2, N4 , N2 , N2D, N1^[GPU required](https://docs.cloud.google.com/compute/docs/regions-zones#n1-footnote)^, C4 , C4A, C3 , C3D, T2D, C2  | Intel Broadwell, Haswell, Ivy Bridge, Skylake, Cascade Lake, Ice Lake, Sapphire Rapids, Emerald Rapids, Granite Rapids, AMD EPYC Milan, Google Axion | GPUs, [AMD SEV ](https://docs.cloud.google.com/confidential-computing/confidential-vm/docs/supported-configurations?tab=amd-sev) |   |
| `me-west1-c` | Tel Aviv, Israel, Middle East | E2, N2 , N2D, N1^[GPU required](https://docs.cloud.google.com/compute/docs/regions-zones#n1-footnote)^, C3 , T2D, M3, M1, C2 , C2D, A2 | Intel Broadwell, Haswell, Ivy Bridge, Skylake, Cascade Lake, Ice Lake, Sapphire Rapids, AMD EPYC Milan | GPUs, [AMD SEV ](https://docs.cloud.google.com/confidential-computing/confidential-vm/docs/supported-configurations?tab=amd-sev) |   |
| `northamerica-northeast1-a` | Montréal, Québec, North America | E2, N4 , N2 , N2D, N1, C4 , C4A, C3 , T2D, M4, C2 , C2D | Intel Ivy Bridge, Sandy Bridge, Haswell, Broadwell, Skylake, Cascade Lake, Ice Lake, Sapphire Rapids, Emerald Rapids, Granite Rapids, AMD EPYC Milan, Google Axion | [AMD SEV ](https://docs.cloud.google.com/confidential-computing/confidential-vm/docs/supported-configurations?tab=amd-sev) | ![leaf icon](https://cloud.google.com/sustainability/region-carbon/gleaf.svg) [Low CO~2~](https://cloud.google.com/sustainability/region-carbon#region-picker) |
| `northamerica-northeast1-b` | Montréal, Québec, North America | E2, N4 , C4 , C4A, C4D, C3 , N2 , N2D, N1, T2D, M4, M3, M2, M1, H3, C2 , G2 | Intel Ivy Bridge, Sandy Bridge, Haswell, Broadwell, Skylake, Cascade Lake, Ice Lake, Sapphire Rapids, Emerald Rapids, Granite Rapids, AMD EPYC Milan, AMD EPYC Turin, Google Axion | GPUs, [AMD SEV ](https://docs.cloud.google.com/confidential-computing/confidential-vm/docs/supported-configurations?tab=amd-sev) | ![leaf icon](https://cloud.google.com/sustainability/region-carbon/gleaf.svg) [Low CO~2~](https://cloud.google.com/sustainability/region-carbon#region-picker) |
| `northamerica-northeast1-c` | Montréal, Québec, North America | E2, N2 , N2D, N1, T2D, M3, M2, M1, C2 , G2 | Intel Ivy Bridge, Sandy Bridge, Haswell, Broadwell, Skylake, Cascade Lake, Ice Lake, AMD EPYC Milan | GPUs, [AMD SEV ](https://docs.cloud.google.com/confidential-computing/confidential-vm/docs/supported-configurations?tab=amd-sev) | ![leaf icon](https://cloud.google.com/sustainability/region-carbon/gleaf.svg) [Low CO~2~](https://cloud.google.com/sustainability/region-carbon#region-picker) |
| `northamerica-northeast2-a` | Toronto, Ontario, North America | E2, N2 , N2D, N1, C4 , T2D, M3, M2, M1, G2 | Intel Ivy Bridge, Haswell, Broadwell, Skylake, Cascade Lake, Ice Lake, Emerald Rapids, AMD EPYC Milan | GPUs, [AMD SEV ](https://docs.cloud.google.com/confidential-computing/confidential-vm/docs/supported-configurations?tab=amd-sev) | ![leaf icon](https://cloud.google.com/sustainability/region-carbon/gleaf.svg) [Low CO~2~](https://cloud.google.com/sustainability/region-carbon#region-picker) |
| `northamerica-northeast2-b` | Toronto, Ontario, North America | E2, N4 , N2 , N2D, N1, C4 , C4A, C4D, C2D, T2D, Z3-metal, M3, M2, M1, G2 | Intel Ivy Bridge, Haswell, Broadwell, Skylake, Cascade Lake, Ice Lake, Sapphire Rapids, Emerald Rapids, Granite Rapids, AMD EPYC Milan, AMD EPYC Turin, Google Axion | GPUs, [AMD SEV ](https://docs.cloud.google.com/confidential-computing/confidential-vm/docs/supported-configurations?tab=amd-sev) | ![leaf icon](https://cloud.google.com/sustainability/region-carbon/gleaf.svg) [Low CO~2~](https://cloud.google.com/sustainability/region-carbon#region-picker) |
| `northamerica-northeast2-c` | Toronto, Ontario, North America | E2, N4 , N2 , N2D, N1, C4 , C2D, T2D, Z3-metal, M4, M3, M2, A3 | Intel Ivy Bridge, Haswell, Broadwell, Skylake, Cascade Lake, Ice Lake, Sapphire Rapids, Emerald Rapids, Granite Rapids, AMD EPYC Milan | GPUs, [AMD SEV ](https://docs.cloud.google.com/confidential-computing/confidential-vm/docs/supported-configurations?tab=amd-sev) | ![leaf icon](https://cloud.google.com/sustainability/region-carbon/gleaf.svg) [Low CO~2~](https://cloud.google.com/sustainability/region-carbon#region-picker) |
| `northamerica-south1-a` | Queretaro, Mexico, North America | E2, N4 , C4 , C4A, C3D, Z3 | Intel Ivy Bridge, Haswell, Broadwell, Cascade Lake, Ice Lake, Emerald Rapids, Granite Rapids, AMD EPYC Milan, AMD EPYC Genoa, Google Axion | [AMD SEV ](https://docs.cloud.google.com/confidential-computing/confidential-vm/docs/supported-configurations?tab=amd-sev) |   |
| `northamerica-south1-b` | Queretaro, Mexico, North America | E2, N4 , C4 , C4A, C3D, Z3 | Intel Ivy Bridge, Haswell, Broadwell, Cascade Lake, Ice Lake, Emerald Rapids, Granite Rapids, AMD EPYC Milan, AMD EPYC Genoa, Google Axion | [AMD SEV ](https://docs.cloud.google.com/confidential-computing/confidential-vm/docs/supported-configurations?tab=amd-sev) |   |
| `northamerica-south1-c` | Queretaro, Mexico, North America | E2, N4 , C4 , C4A, C3D, Z3 | Intel Ivy Bridge, Haswell, Broadwell, Cascade Lake, Ice Lake, Emerald Rapids, Granite Rapids, AMD EPYC Milan, AMD EPYC Genoa, Google Axion | [AMD SEV ](https://docs.cloud.google.com/confidential-computing/confidential-vm/docs/supported-configurations?tab=amd-sev) |   |
| `southamerica-east1-a` | Osasco, São Paulo, Brazil, South America | E2, N4 , N2 , N2D, N1, C4 , C3 , T2D, Z3-metal, C2 , C2D | Intel Ivy Bridge, Sandy Bridge, Haswell, Broadwell, Skylake, Cascade Lake, Ice Lake, Sapphire Rapids, Emerald Rapids, Granite Rapids, AMD EPYC Milan | GPUs, [AMD SEV ](https://docs.cloud.google.com/confidential-computing/confidential-vm/docs/supported-configurations?tab=amd-sev) | ![leaf icon](https://cloud.google.com/sustainability/region-carbon/gleaf.svg) [Low CO~2~](https://cloud.google.com/sustainability/region-carbon#region-picker) |
| `southamerica-east1-b` | Osasco, São Paulo, Brazil, South America | E2, N4 , N2 , N2D, N1, C4 , C3 , T2D, M3, M2, M1, C2 , C2D | Intel Ivy Bridge, Sandy Bridge, Haswell, Broadwell, Skylake, Cascade Lake, Ice Lake, Sapphire Rapids, Emerald Rapids, Granite Rapids, AMD EPYC Milan | GPUs, [AMD SEV ](https://docs.cloud.google.com/confidential-computing/confidential-vm/docs/supported-configurations?tab=amd-sev) | ![leaf icon](https://cloud.google.com/sustainability/region-carbon/gleaf.svg) [Low CO~2~](https://cloud.google.com/sustainability/region-carbon#region-picker) |
| `southamerica-east1-c` | Osasco, São Paulo, Brazil, South America | E2, N4 , N2 , N2D, N1, C4 , C4A, C3 , T2D, M4 , M3, M2, M1, C2 , C2D | Intel Ivy Bridge, Sandy Bridge, Haswell, Broadwell, Skylake, Cascade Lake, Ice Lake, Sapphire Rapids, Emerald Rapids, Granite Rapids, AMD EPYC Milan, Google Axion | GPUs, [AMD SEV ](https://docs.cloud.google.com/confidential-computing/confidential-vm/docs/supported-configurations?tab=amd-sev) | ![leaf icon](https://cloud.google.com/sustainability/region-carbon/gleaf.svg) [Low CO~2~](https://cloud.google.com/sustainability/region-carbon#region-picker) |
| `southamerica-west1-a` | Santiago, Chile, South America | E2, N4 , N2 , N2D, C4 , C4A, C2 , T2D, Z3 | Intel Broadwell, Haswell, Skylake, Cascade Lake, Sapphire Rapids, Emerald Rapids, Granite Rapids, AMD EPYC Milan, Google Axion |   | ![leaf icon](https://cloud.google.com/sustainability/region-carbon/gleaf.svg) [Low CO~2~](https://cloud.google.com/sustainability/region-carbon#region-picker) |
| `southamerica-west1-b` | Santiago, Chile, South America | E2, N4 , N2 , N2D, C4 , C4A, C2 , T2D, M4 , M3, M2, M1 | Intel Broadwell, Haswell, Skylake, Cascade Lake, Ice Lake, Emerald Rapids, Granite Rapids, AMD EPYC Milan, Google Axion | [AMD SEV ](https://docs.cloud.google.com/confidential-computing/confidential-vm/docs/supported-configurations?tab=amd-sev) | ![leaf icon](https://cloud.google.com/sustainability/region-carbon/gleaf.svg) [Low CO~2~](https://cloud.google.com/sustainability/region-carbon#region-picker) |
| `southamerica-west1-c` | Santiago, Chile, South America | E2, N4 , N2 , N2D, C4 , T2D, M4 , M3, M2, M1, C2  | Intel Broadwell, Haswell, Skylake, Cascade Lake, Ice Lake, Emerald Rapids, Granite Rapids, AMD EPYC Milan |   | ![leaf icon](https://cloud.google.com/sustainability/region-carbon/gleaf.svg) [Low CO~2~](https://cloud.google.com/sustainability/region-carbon#region-picker) |
| `us-central1-a` | Council Bluffs, Iowa, North America | E2, N4 , N4A, N4D, N2 , N2D, N1, C4 , C4A, C4D, C4N, C3 , C3D, T2D, T2A, Z3, X4, M4 , M3, M2, M1, H3, C2 , C2D, H4D, A4X , A3, A2, G2 | Intel Ivy Bridge, Sandy Bridge, Haswell, Broadwell, Skylake, Cascade Lake, Ice Lake, Sapphire Rapids, Emerald Rapids, Granite Rapids, AMD EPYC Milan, AMD EPYC Genoa, AMD EPYC Turin, Ampere Altra Arm, Google Axion, NVIDIA Grace | GPUs, [AMD SEV ](https://docs.cloud.google.com/confidential-computing/confidential-vm/docs/supported-configurations?tab=amd-sev), [AMD SEV-SNP](https://docs.cloud.google.com/confidential-computing/confidential-vm/docs/supported-configurations?tab=amd-sev-snp), [Intel TDX](https://docs.cloud.google.com/confidential-computing/confidential-vm/docs/supported-configurations?tab=intel-tdx), [NVIDIA Confidential Computing](https://docs.cloud.google.com/confidential-computing/confidential-vm/docs/supported-configurations?tab=nvidia-confidential-computing) | ![leaf icon](https://cloud.google.com/sustainability/region-carbon/gleaf.svg) [Low CO~2~](https://cloud.google.com/sustainability/region-carbon#region-picker) |
| `us-central1-b` | Council Bluffs, Iowa, North America | E2, N4 , N4D, N4A, N2 , N2D, N1, C4 , C4A, C4D, C4N, C3 , C3D, T2D, T2A, Z3, X4, M4 , M3, M2, M1, C2 , C2D, A4X Max, A4 , A3, A2, G4, G2, H4D | Intel Ivy Bridge, Sandy Bridge, Haswell, Broadwell, Skylake, Cascade Lake, Ice Lake, Sapphire Rapids, Emerald Rapids, Granite Rapids, AMD EPYC Milan, AMD EPYC Genoa, AMD EPYC Turin, Ampere Altra Arm, Google Axion, NVIDIA Grace | GPUs, [AMD SEV ](https://docs.cloud.google.com/confidential-computing/confidential-vm/docs/supported-configurations?tab=amd-sev), [AMD SEV-SNP](https://docs.cloud.google.com/confidential-computing/confidential-vm/docs/supported-configurations?tab=amd-sev-snp), [Intel TDX](https://docs.cloud.google.com/confidential-computing/confidential-vm/docs/supported-configurations?tab=intel-tdx) | ![leaf icon](https://cloud.google.com/sustainability/region-carbon/gleaf.svg) [Low CO~2~](https://cloud.google.com/sustainability/region-carbon#region-picker) |
| `us-central1-c` | Council Bluffs, Iowa, North America | E2, N4 , N4D, N4A, N2 , N2D, N1, C4 , C4A, C4D, C4N, C3 , C3D, T2D, Z3, X4, M4 , M3, M2, M1, C2 , C2D, A3, A2, G2 | Intel Ivy Bridge, Sandy Bridge, Haswell, Broadwell, Skylake, Cascade Lake, Ice Lake, Sapphire Rapids, Emerald Rapids, Granite Rapids, AMD EPYC Milan, AMD EPYC Genoa, AMD EPYC Turin, Google Axion | GPUs, [AMD SEV ](https://docs.cloud.google.com/confidential-computing/confidential-vm/docs/supported-configurations?tab=amd-sev), [AMD SEV-SNP](https://docs.cloud.google.com/confidential-computing/confidential-vm/docs/supported-configurations?tab=amd-sev-snp), [Intel TDX](https://docs.cloud.google.com/confidential-computing/confidential-vm/docs/supported-configurations?tab=intel-tdx) | ![leaf icon](https://cloud.google.com/sustainability/region-carbon/gleaf.svg) [Low CO~2~](https://cloud.google.com/sustainability/region-carbon#region-picker) |
| `us-central1-f` | Council Bluffs, Iowa, North America | E2, N4 , N4A, N4D, N2 , N2D, N1, C4 , C4A, C4D, C3 , C3D, T2D, T2A, Z3, M1, C2 , C2D, A2, G4 | Intel Ivy Bridge, Sandy Bridge, Haswell, Broadwell, Skylake, Cascade Lake, Ice Lake, Sapphire Rapids, Emerald Rapids, Granite Rapids, AMD EPYC Milan, AMD EPYC Genoa, AMD EPYC Turin, Ampere Altra Arm, Google Axion | GPUs, [AMD SEV ](https://docs.cloud.google.com/confidential-computing/confidential-vm/docs/supported-configurations?tab=amd-sev) | ![leaf icon](https://cloud.google.com/sustainability/region-carbon/gleaf.svg) [Low CO~2~](https://cloud.google.com/sustainability/region-carbon#region-picker) |
| `us-east1-b` | Moncks Corner, South Carolina, North America | E2, N4 , N4A, N4D, N2 , N2D, N1, C4 , C4A, C4D, C3 , C3D, T2D, Z3, M4 , M3, M1, H4D, C2 , C2D, A4 , A2, G4, G2 | Intel Ivy Bridge, Sandy Bridge, Haswell, Broadwell, Skylake, Cascade Lake, Ice Lake, Sapphire Rapids, Emerald Rapids, Granite Rapids, AMD EPYC Milan, AMD EPYC Genoa, AMD EPYC Turin, Google Axion | GPUs, [AMD SEV ](https://docs.cloud.google.com/confidential-computing/confidential-vm/docs/supported-configurations?tab=amd-sev) |   |
| `us-east1-c` | Moncks Corner, South Carolina, North America | E2, N4 , N4A, N4D, N2 , N2D, N1, C4 , C4A, C4D, C4N, C3 , C3D, T2D, Z3, M1, C2 , C2D, G2 | Intel Ivy Bridge, Sandy Bridge, Haswell, Broadwell, Skylake, Cascade Lake, Ice Lake, Sapphire Rapids, Emerald Rapids, Granite Rapids, AMD EPYC Milan, AMD EPYC Genoa, AMD EPYC Turin, Google Axion | GPUs, [AMD SEV ](https://docs.cloud.google.com/confidential-computing/confidential-vm/docs/supported-configurations?tab=amd-sev), [Intel TDX](https://docs.cloud.google.com/confidential-computing/confidential-vm/docs/supported-configurations?tab=intel-tdx) |   |
| `us-east1-d` | Moncks Corner, South Carolina, North America | E2, N4 , N4A, N4D, N2 , N2D, N1, C4 , C4A, C4D, C3 , C3D, T2D, Z3, M4, M3, M1, C2 , C2D, G2 | Intel Ivy Bridge, Sandy Bridge, Haswell, Broadwell, Skylake, Cascade Lake, Ice Lake, Sapphire Rapids, Emerald Rapids, Granite Rapids, AMD EPYC Milan, AMD EPYC Genoa, AMD EPYC Turin, Google Axion | GPUs, [AMD SEV ](https://docs.cloud.google.com/confidential-computing/confidential-vm/docs/supported-configurations?tab=amd-sev), [Intel TDX](https://docs.cloud.google.com/confidential-computing/confidential-vm/docs/supported-configurations?tab=intel-tdx) |   |
| `us-east4-a` | Ashburn, Virginia, North America | E2, N4 , N4A, N4D, N2 , N2D, N1, C4 , C4A, C4D, C3 , C3D, T2D, Z3, X4, M4 , M3, M2, M1, C2 , C2D, A3, G2 | Intel Ivy Bridge, Sandy Bridge, Haswell, Broadwell, Skylake, Cascade Lake, Ice Lake, Sapphire Rapids, Emerald Rapids, Granite Rapids, AMD EPYC Milan, AMD EPYC Genoa, AMD EPYC Turin, Google Axion | GPUs, [AMD SEV ](https://docs.cloud.google.com/confidential-computing/confidential-vm/docs/supported-configurations?tab=amd-sev), [Intel TDX](https://docs.cloud.google.com/confidential-computing/confidential-vm/docs/supported-configurations?tab=intel-tdx) |   |
| `us-east4-b` | Ashburn, Virginia, North America | E2, N4 , N4A, N4D, N2 , N2D, N1, C4 , C4A, C4D, C3 , C3D, T2D, Z3, X4, M4 , M3, M2, M1, C2 , C2D, A4X Max, A4X , A4 , A3, G4 | Intel Ivy Bridge, Sandy Bridge, Haswell, Broadwell, Skylake, Cascade Lake, Ice Lake, Sapphire Rapids, Emerald Rapids, Granite Rapids, AMD EPYC Milan, AMD EPYC Genoa, AMD EPYC Turin, Google Axion, NVIDIA Grace | GPUs, [AMD SEV ](https://docs.cloud.google.com/confidential-computing/confidential-vm/docs/supported-configurations?tab=amd-sev) |   |
| `us-east4-c` | Ashburn, Virginia, North America | E2, N4 , N4A, N4D, N2 , N2D, N1, C4 , C4A, C4D, C3 , C3D, T2D, Z3, X4, M4 , M3, M1, C2 , C2D, A3, A2, G4, G2 | Intel Ivy Bridge, Sandy Bridge, Haswell, Broadwell, Skylake, Cascade Lake, Ice Lake, Sapphire Rapids, Emerald Rapids, Granite Rapids, AMD EPYC Milan, AMD EPYC Genoa, AMD EPYC Turin, Google Axion | GPUs, [AMD SEV ](https://docs.cloud.google.com/confidential-computing/confidential-vm/docs/supported-configurations?tab=amd-sev), [Intel TDX](https://docs.cloud.google.com/confidential-computing/confidential-vm/docs/supported-configurations?tab=intel-tdx) |   |
| `us-east5-a` | Columbus, Ohio, North America | E2, N4 , N4D, N2 , N2D, C4 , C4A, C4D, C3 , C3D, T2D, Z3, M4 , C2 , A3, A2, G4 | Intel Broadwell, Haswell, Skylake, Cascade Lake, Ice Lake, Sapphire Rapids, Emerald Rapids, Granite Rapids, AMD EPYC Milan, AMD EPYC Turin, Google Axion | GPUs, [AMD SEV ](https://docs.cloud.google.com/confidential-computing/confidential-vm/docs/supported-configurations?tab=amd-sev), [NVIDIA Confidential Computing](https://docs.cloud.google.com/confidential-computing/confidential-vm/docs/supported-configurations?tab=nvidia-confidential-computing) |   |
| `us-east5-b` | Columbus, Ohio, North America | E2, N4 , N4D , N2 , N2D, C4 , C4A, C4D, C4N, C3 , C3D, T2D, Z3, M4 , C2 , A4X Max, G4 | Intel Broadwell, Haswell, Skylake, Cascade Lake, Sapphire Rapids, Emerald Rapids, Granite Rapids, AMD EPYC Milan, AMD EPYC Genoa, AMD EPYC Turin, Google Axion | GPUs, [AMD SEV ](https://docs.cloud.google.com/confidential-computing/confidential-vm/docs/supported-configurations?tab=amd-sev), [Intel TDX](https://docs.cloud.google.com/confidential-computing/confidential-vm/docs/supported-configurations?tab=intel-tdx) |   |
| `us-east5-c` | Columbus, Ohio, North America | E2, N4 , N4D , N2 , N2D, C4 , C4A, C4D, C4N, C3 , C3D, T2D, M4 , Z3, C2 , A4X Max, G4 | Intel Broadwell, Haswell, Skylake, Cascade Lake, Sapphire Rapids, Emerald Rapids, Granite Rapids, AMD EPYC Milan, AMD EPYC Turin, NVIDIA Grace, Google Axion | GPUs, [AMD SEV ](https://docs.cloud.google.com/confidential-computing/confidential-vm/docs/supported-configurations?tab=amd-sev), [Intel TDX](https://docs.cloud.google.com/confidential-computing/confidential-vm/docs/supported-configurations?tab=intel-tdx) |   |
| `us-south1-a` | Dallas, Texas, North America | E2, N4 , N2 , N2D, C4 , C4A, C3 , T2D, Z3, G4 | Intel Broadwell, Haswell, Skylake, Cascade Lake, Ice Lake, Sapphire Rapids, Emerald Rapids, Granite Rapids, AMD EPYC Milan, AMD EPYC Turin, Google Axion | GPUs, [AMD SEV ](https://docs.cloud.google.com/confidential-computing/confidential-vm/docs/supported-configurations?tab=amd-sev) | ![leaf icon](https://cloud.google.com/sustainability/region-carbon/gleaf.svg) [Low CO~2~](https://cloud.google.com/sustainability/region-carbon#region-picker) |
| `us-south1-b` | Dallas, Texas, North America | E2, N4 , N2 , N2D, C4 , C4A, C3 , T2D, A4 , A3, Z3, G4 | Intel Broadwell, Haswell, Skylake, Cascade Lake, Sapphire Rapids, Emerald Rapids, Granite Rapids, AMD EPYC Milan, AMD EPYC Turin, Google Axion | GPUs | ![leaf icon](https://cloud.google.com/sustainability/region-carbon/gleaf.svg) [Low CO~2~](https://cloud.google.com/sustainability/region-carbon#region-picker) |
| `us-south1-c` | Dallas, Texas, North America | E2, N2 , N2D, C3 , T2D, Z3 | Intel Broadwell, Haswell, Skylake, Cascade Lake, Ice Lake, Sapphire Rapids, AMD EPYC Milan | [AMD SEV ](https://docs.cloud.google.com/confidential-computing/confidential-vm/docs/supported-configurations?tab=amd-sev) | ![leaf icon](https://cloud.google.com/sustainability/region-carbon/gleaf.svg) [Low CO~2~](https://cloud.google.com/sustainability/region-carbon#region-picker) |
| `us-west1-a` | The Dalles, Oregon, North America | E2, N4 , N4A, N4D, N2 , N2D, N1, C4 , C4A, C4D, C3 , C3D, T2D, Z3, M4 , M3, M1, C2 , C2D, A3, G4, G2 | Intel Ivy Bridge, Sandy Bridge, Haswell, Broadwell, Skylake, Cascade Lake, Ice Lake, Sapphire Rapids, Emerald Rapids, Granite Rapids, AMD EPYC Milan, AMD EPYC Genoa, AMD EPYC Turin Google Axion | GPUs, [AMD SEV ](https://docs.cloud.google.com/confidential-computing/confidential-vm/docs/supported-configurations?tab=amd-sev), [Intel TDX](https://docs.cloud.google.com/confidential-computing/confidential-vm/docs/supported-configurations?tab=intel-tdx) | ![leaf icon](https://cloud.google.com/sustainability/region-carbon/gleaf.svg) [Low CO~2~](https://cloud.google.com/sustainability/region-carbon#region-picker) |
| `us-west1-b` | The Dalles, Oregon, North America | E2, N4 , N4A, N4D, N2 , N2D, N1, C4 , C4D, C4N, C3 , C3D, T2D, Z3, C2 , C2D, M4 , M3, M1, A3, A2, G4, G2 | Intel Ivy Bridge, Sandy Bridge, Haswell, Broadwell, Skylake, Cascade Lake, Ice Lake, Sapphire Rapids, Emerald Rapids, Granite Rapids, AMD EPYC Milan, AMD EPYC Genoa, AMD EPYC Turin, Google Axion | GPUs, [AMD SEV ](https://docs.cloud.google.com/confidential-computing/confidential-vm/docs/supported-configurations?tab=amd-sev), [Intel TDX](https://docs.cloud.google.com/confidential-computing/confidential-vm/docs/supported-configurations?tab=intel-tdx) | ![leaf icon](https://cloud.google.com/sustainability/region-carbon/gleaf.svg) [Low CO~2~](https://cloud.google.com/sustainability/region-carbon#region-picker) |
| `us-west1-c` | The Dalles, Oregon, North America | E2, N4 , N4A, N4D, N2 , N2D, N1, C4 , C4A, C4D, C3D, T2D, C3 , C2 , C2D, M4, M3, A3 | Intel Ivy Bridge, Sandy Bridge, Haswell, Broadwell, Skylake, Cascade Lake, Ice Lake, Sapphire Rapids, Emerald Rapids, Granite Rapids, AMD EPYC Milan, AMD EPYC Turin, Google Axion | GPUs, [AMD SEV ](https://docs.cloud.google.com/confidential-computing/confidential-vm/docs/supported-configurations?tab=amd-sev) | ![leaf icon](https://cloud.google.com/sustainability/region-carbon/gleaf.svg) [Low CO~2~](https://cloud.google.com/sustainability/region-carbon#region-picker) |
| `us-west2-a` | Los Angeles, California, North America | E2, N4 , N2 , N2D, N1, C4 , C4A, C3 , C3D, T2D, C2 , C2D, Z3 | Intel Ivy Bridge, Sandy Bridge, Haswell, Broadwell, Skylake, Cascade Lake, Ice Lake, Sapphire Rapids, Emerald Rapids, AMD EPYC Milan, AMD EPYC Genoa, Google Axion | [AMD SEV ](https://docs.cloud.google.com/confidential-computing/confidential-vm/docs/supported-configurations?tab=amd-sev) |   |
| `us-west2-b` | Los Angeles, California, North America | E2, N4 , N2 , N2D, N1, C4 , C4A, C3 , C3D, T2D, M1, C2  | Intel Ivy Bridge, Sandy Bridge, Haswell, Broadwell, Skylake, Cascade Lake, Ice Lake, Sapphire Rapids, Emerald Rapids, Granite Rapids, AMD EPYC Milan, Google Axion | GPUs, [AMD SEV ](https://docs.cloud.google.com/confidential-computing/confidential-vm/docs/supported-configurations?tab=amd-sev) |   |
| `us-west2-c` | Los Angeles, California, North America | E2, N4 , N2 , N2D, N1, T2D, C4 , C4A, C3 , C3D, M1, C2 , C2D, A4  | Intel Ivy Bridge, Sandy Bridge, Haswell, Broadwell, Skylake, Cascade Lake, Ice Lake, Sapphire Rapids, Emerald Rapids, Granite Rapids, AMD EPYC Milan, Google Axion | GPUs, [AMD SEV ](https://docs.cloud.google.com/confidential-computing/confidential-vm/docs/supported-configurations?tab=amd-sev) |   |
| `us-west3-a` | Salt Lake City, Utah, North America | E2, N4 , N4D , N2 , N2D, N1, C4 , C4D, C3 , T2D, C2 , M3, G4 | Intel Ivy Bridge, Sandy Bridge, Broadwell, Skylake, Cascade Lake, Ice Lake, Sapphire Rapids, Emerald Rapids, Granite Rapids, AMD EPYC Milan, AMD EPYC Turin | GPUs, [AMD SEV ](https://docs.cloud.google.com/confidential-computing/confidential-vm/docs/supported-configurations?tab=amd-sev) |   |
| `us-west3-b` | Salt Lake City, Utah, North America | E2, N4 , N2 , N2D, N1, C4 , C3 , T2D, C2 , A4 , A2 | Intel Ivy Bridge, Sandy Bridge, Broadwell, Skylake, Cascade Lake, Ice Lake, Sapphire Rapids, Emerald Rapids, Granite Rapids, AMD EPYC Milan | GPUs, [AMD SEV ](https://docs.cloud.google.com/confidential-computing/confidential-vm/docs/supported-configurations?tab=amd-sev) |   |
| `us-west3-c` | Salt Lake City, Utah, North America | E2, N4 , N2 , N2D, N1, C4 , C3 , T2D, C2 , C2D, A4  | Intel Ivy Bridge, Sandy Bridge, Broadwell, Skylake, Cascade Lake, Ice Lake, Sapphire Rapids, Emerald Rapids, Granite Rapids, AMD EPYC Milan | GPUs, [AMD SEV ](https://docs.cloud.google.com/confidential-computing/confidential-vm/docs/supported-configurations?tab=amd-sev) |   |
| `us-west4-a` | Las Vegas, Nevada, North America | E2, N4 , N4D, N2 , N2D, N1, C4 , C4A, C4D, C3 , C3D, T2D, C2 , C2D, X4, M4, M3, M2, M1, A3, G4, G2, H4D | Intel Ivy Bridge, Broadwell, Skylake, Cascade Lake, Ice Lake, Sapphire Rapids, Emerald Rapids, Granite Rapids, AMD EPYC Milan, AMD EPYC Genoa, AMD EPYC Turin, Google Axion | GPUs, [AMD SEV ](https://docs.cloud.google.com/confidential-computing/confidential-vm/docs/supported-configurations?tab=amd-sev) |   |
| `us-west4-b` | Las Vegas, Nevada, North America | E2, N4 , N4D, N2 , N2D, N1, C4 , C4A, C4D, C3 , C3D, T2D, C2 , C2D, X4, M4, M3, M2, M1, A2 | Intel Ivy Bridge, Broadwell, Skylake, Cascade Lake, Ice Lake, Sapphire Rapids, Emerald Rapids, Granite Rapids, AMD EPYC Milan, AMD EPYC Turin, Google Axion | GPUs, [AMD SEV ](https://docs.cloud.google.com/confidential-computing/confidential-vm/docs/supported-configurations?tab=amd-sev) |   |
| `us-west4-c` | Las Vegas, Nevada, North America | E2, N4 , N4D, N2 , N2D, N1, C4A, C4 , C4D, C3 , T2D, C2 , C2D, G4, G2 | Intel Ivy Bridge, Broadwell, Skylake, Cascade Lake, Ice Lake, Sapphire Rapids, Emerald Rapids, Granite Rapids, AMD EPYC Milan, AMD EPYC Turin, Google Axion | GPUs, [AMD SEV ](https://docs.cloud.google.com/confidential-computing/confidential-vm/docs/supported-configurations?tab=amd-sev) |   |

<br />

^\*^**GPU required** : To use an N1 machine type in any of the supported `me-west1` zones, you must attach at least one NVIDIA T4 GPU to the VM.

<br />

## What's next

- Learn more about [geography and regions](https://docs.cloud.google.com/docs/geography-and-regions).
- Learn how to [view available regions and zones](https://docs.cloud.google.com/compute/docs/regions-zones/viewing-regions-zones).
- Learn how to [change your default zone or region](https://docs.cloud.google.com/compute/docs/regions-zones/changing-default-zone-region).
- Learn more about the [global, regional, and zonal resources](https://docs.cloud.google.com/compute/docs/regions-zones/global-regional-zonal-resources).

## Global, regional, and zonal resources

This document describes global, regional, and zonal Compute Engine
resources.

Google Cloud resources are hosted in
[multiple locations](https://docs.cloud.google.com/docs/geography-and-regions#regions_and_zones) worldwide.
These locations are composed of regions with zones within those regions. Putting
resources in different zones in a region provides isolation from many types of
infrastructure, hardware, and software failures. Putting resources in different
regions provides an even higher degree of failure independence. You can design
robust systems by spreading resources across different failure domains.

All Compute Engine resources are either global, regional, or zonal in scope.
For example, images are a global resource, but regional static IPs are regional,
and Persistent Disks can be either regional or zonal resources.

The scope of the resource determines how accessible the resource is to other
resources:

**Global resources** are accessible by resources in any
region or zone, For example, virtual machine (VM) instances from different zones can use
the same global image.

**Regional resources** are accessible only to resources within the same region.
For example, a regional static external IP address is accessible only by
resources within the same region. For a VM instance to use a specific static
external IP, the VM must be in a zone that is in the same region as the address.

**Zonal resources** are accessible only to resources within the same zone. Zonal
resources can also access regional and global resources. For example, a VM
instance can access a global image and regional network resources.

| Scope | Accessibility | Naming uniqueness | Examples |
|---|---|---|---|
| Global | Any region or zone in the project | Project-wide | Images, VPC networks, instance templates |
| Regional | Any zone within the same region | Region-wide | Subnets, regional static IPs, regional disks, instance templates |
| Zonal | Same zone only | Zone-wide | VM instances, zonal disks and |
| Hyperdisk Storage Pools, machine types |   |   |   |

Within a project, a zonal resource must have a unique name within its
zone. For example, you can have a VM named `my-instance` in zone
`us-central1-a` and another VM named `my-instance` in zone `us-central1-b`
within the same project.

## Global resources

Global resources are accessible by any resource in any zone within the same
project. When you create a global resource, you don't need to provide a scope
specification.

> [!NOTE]
> **Note:** Although all Compute Engine resources are classified as global, regional, or zonal in scope, some global resources, like custom images, disk snapshots, and machine images, allow you to choose a **multi-region** or **region** storage location for their underlying data. Even when stored in a multi-region, the resource itself behaves as a global resource.

Global resources include:

Addresses
:   The Addresses collection contains any global static external IP addresses that
    you have reserved for your project. Global static external IP addresses are a
    global resource and are used for global load balancers.

Images
:   Images are used by any instance or disk resource in the same project as the
    image. Google provides preconfigured images that you can use to boot your
    instance. You can customize one of these images, or you can build your own
    image. Optionally, you can
    [share images across projects](https://docs.cloud.google.com/compute/docs/images/sharing-images-across-projects).

Snapshots
:   Hyperdisk and Persistent Disk standard and archive snapshots are
    global resources that can be used to create a disk in other projects.
    Optionally, you can
    [share snapshots across projects](https://docs.cloud.google.com/compute/docs/disks/create-snapshots#sharing_snapshots).

Global instance templates
:   A global instance template can be used to create compute instances and managed
    instance groups. Instance templates can be global or regional resources.
    However, if you specify zonal resources in a global instance template, then
    you can use that template only in the same zone as the specified zonal
    resources, and if you specify regional resources in a global instance template,
    then you can use that template only in the same region as the specified
    regional resources. Read about
    [Regional and global instance templates](https://docs.cloud.google.com/compute/docs/instance-templates#regional_and_global_instance_templates).

Cloud Interconnects
:   A Cloud Interconnect is a highly available connection from your
    on-premises network to Google's network. This connection is a global resource.
    However, interconnect attachments, which run inside of this connection, are
    regional resources.

Cloud Interconnect locations
:   A Cloud Interconnect location is a physical connection
    point for Cloud Interconnect near your network.
    There is one Cloud Interconnect location for every available
    colocation facility and edge availability domain. Cloud Interconnect
    locations are read-only, global resources.

VPC network
:   A VPC network is a global resource, but individual subnets are regional
    resources.

Firewalls
:   Firewalls apply to a single VPC network and are considered a
    global resource because packets can reach them from other networks.

Routes
:   Routes let you create complex networking scenarios. You can manage how
    traffic is routed for a specific IP range. Routes
    are similar to how a router directs traffic within a local area network.
    Routes apply to VPC networks within a Google Cloud project and are
    considered global resources.

Global operations

:   An operation is a per-zone resource, a per-region resource, or a global
    resource. If you are performing an operation on a global resource, the
    operation is considered a
    global operation. For example, inserting an image is considered a global
    operation because images are a global resource.

    > [!NOTE]
    > **Note:** Operations are unique in that they span all three scopes: global resources, regional resources, and zonal resources. A request to list operations returns operations across all three scopes.

## Regional resources

Regional resources are accessible by any resources within the same region. For
example, if you reserve a static external IP address in a specific region, that
static external IP address can only be assigned to instances within that region.
Each region also has one or more zones. For a list of available regions
and zones, see
[Regions and zones](https://docs.cloud.google.com/compute/docs/regions-zones).

Regional resources include:

Addresses
:   The Addresses collection contains any regional static external IP addresses
    that you have reserved for your project. Static external IP addresses are a
    regional resource that are used by instances that are in the same
    region as the address, by regional forwarding rules for regional load
    balancers, and for protocol forwarding.

Cloud Interconnect attachments
:   A VLAN attachment allocates a VLAN on your Cloud Interconnect
    and connects that VLAN to a VPC network. An attachment is a
    regional resource, but a Cloud Interconnect connection is a global
    resource.

Subnets
:   Subnets regionally segment the network IP space into prefixes (subnets)
    and control which prefix an instance's internal IP address is allocated from.

Placement policies
:   A [placement policy](https://docs.cloud.google.com/compute/docs/instances/placement-policies-overview)
    controls how closely to place VMs in relation to one another. This can help
    reduce the impact of host system failures or network latency.

Regional instance templates
:   A regional instance template can be used to create VMs and managed instance
    groups. A regional instance template is accessible only by resources within
    the same region. If you specify zonal resources in a regional instance
    template, then you can use that template only in the same zone as the
    specified zonal resources.

Regional managed instance groups
:   Regional managed
    [instance groups](https://docs.cloud.google.com/compute/docs/instance-groups)
    are collections of identical instances that span multiple zones. Regional
    managed instance groups let you spread app load across multiple zones, rather
    than confining your app to a single zone or having to manage multiple instance
    groups across different zones.

Regional disks
:   [Regional disks](https://docs.cloud.google.com/compute/docs/disks/about-regional-persistent-disk)
    provide durable storage and replication of data between two zones within the same region.
    In a failover situation, you can force-attach a regional disk
    to another instance within the same region. You cannot force attach a zonal
    disk to an instance. Optionally, you can
    [copy a disk to another project](https://docs.cloud.google.com/compute/docs/disks/migrate-to-hyperdisk#migrate-to-hd),
    which lets other projects make images and snapshots from these disks but
    doesn't let instances in other projects attach the disks. To protect disk data
    in the unlikely event of a regional outage, you can enable Asynchronous Replication.

Instant snapshots
:   Instant [snapshots](https://docs.cloud.google.com/compute/docs/disks/instant-snapshots) of regional disks
    are regional resources. They are only accessible within the same region as the
    disk.

Regional operations

:   An operation is a per-zone resource, a per-region resource, or a global
    resource. If you are performing an operation on a regional resource, the
    operation is considered a per-region operation. For example, reserving an
    address is considered regional operation because addresses are a
    region-specific resource.

    > [!NOTE]
    > **Note:** Operations are unique in that they span all three scopes: global resources, regional resources, and zonal resources. A request to list operations returns operations across all three scopes.

## Zonal resources

Resources that are hosted in a zone are called *per-zone resources*.
Zone-specific resources, or per-zone resources, are unique to that zone and are
only usable by other resources in the same zone. For example, an instance is a
per-zone resource. When you create an instance, you must provide the zone where
the instance is located. The instance can access other resources within the same
zone, and can access global resources, but it can't access other per-zone
resources in a different zone, such as a disk resource or a
VPC subnet.

For a list of available zones and the machine series available in each zone, see
[Regions and zones](https://docs.cloud.google.com/compute/docs/regions-zones).

> [!NOTE]
> **Note:** One exception is that instances in one zone can communicate with instances in another zone if both instances belong to the same [VPC network](https://docs.cloud.google.com/compute/docs/vpc).

Per-zone resources include:

Instances
:   A compute instance is located within a zone and can access
    global resources or resources within the same zone.

Zonal Google Cloud Hyperdisks and Persistent Disks
:   Zonal disks are accessed by other compute instances within the same zone.
    You can attach a disk only to instances in the same zone as the disk. You
    can't attach a disk to an instance in another zone. Optionally, you can
    [share disk resources across projects](https://docs.cloud.google.com/compute/docs/images/sharing-images-across-projects),
    which lets other projects make images and snapshots from these disks but
    doesn't let instances in other projects attach the disks.

Hyperdisk pools
:   Hyperdisk [pools](https://docs.cloud.google.com/compute/docs/disks/pools) are zonal
    resources. Disks in a pool must be in the same zone as the pool.

Instant snapshots
:   Instant [snapshots](https://docs.cloud.google.com/compute/docs/disks/instant-snapshots) of zonal disks
    are zonal resources. They are only accessible within the same zone as the
    disk.

Machine types
:   Machine types are per-zone resources. Instances and disks can only use
    machine types that are in the same zone.

Zonal managed instance groups
:   A zonal managed [instance group](https://docs.cloud.google.com/compute/docs/instance-groups)
    uses an
    instance template to create a group of identical instances within a single
    zone. You manage compute instances in a managed instance group as a single
    entity, rather than managing individual instances.

GPUs
:   GPUs are zonal resources. For information about the zones in which GPUs are
    available, see
    [GPU regions and zones availability](https://docs.cloud.google.com/compute/docs/gpus/gpu-regions-zones).

Cloud TPUs
:   TPUs are zonal resources. For information about the zones in which TPUs
    are available, see [Availability](https://docs.cloud.google.com/tpu/docs/tpus#availability).

Per-zone operations

:   An operation is a per-zone resource, a per-region resource, or a global
    resource. If you are performing an operation on a zone-specific resource,
    the operation is considered a per-zone operation. For
    example, inserting an instance is considered a per-zone operation
    because the operation is being performed on a zone-specific resource,
    an instance.

    > [!NOTE]
    > **Note:** Operations are unique in that they span all three scopes: global resources, regional resources, and zonal resources. A request to list operations returns operations across all three scopes.

## Aggregate lists

By default, a request to return a list of resources is scoped to
a particular control plane. For example, when you query the API for a list of
instances, you must provide the zone for which you want to list
instances. To list resources across all zones or regions, you can perform an
aggregate list query. Each per-region and per-zone resource has an aggregate
list URI that can be queried to list all resources of that type. For example,
to list all compute instances across all zones that were created in a project,
you can make a request to the following URI:

    https://compute.googleapis.com/compute/v1/projects/<var>PROJECT_ID</var>/aggregated/instances

Similarly, to list all IP addresses across all regions, make a request to the
following URI:

    https://compute.googleapis.com/compute/v1/projects/<var>PROJECT_ID</var>>/aggregated/addresses

For more information, see the
[`aggregateList`](https://docs.cloud.google.com/compute/docs/reference/latest/addresses/aggregatedList)
method for that resource.

## What's next

- Learn more about [regions and zones](https://docs.cloud.google.com/compute/docs/regions-zones).
- Learn more about [geography and regions](https://docs.cloud.google.com/docs/geography-and-regions) and [geographical management of data](https://docs.cloud.google.com/docs/geography-and-regions#geographic_management_of_data).
- Learn about [instances](https://docs.cloud.google.com/compute/docs/instances).
- Work through [Linux Getting Started](https://docs.cloud.google.com/compute/docs/create-linux-vm-instance).
- Work through [Windows Getting Started](https://docs.cloud.google.com/compute/docs/create-windows-server-vm-instance).
- Learn how to [set a default project, zone, or region](https://docs.cloud.google.com/compute/docs/gcloud-compute#default-properties).

