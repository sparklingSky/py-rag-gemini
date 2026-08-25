## Overview of creating Compute Engine instances

[Video](https://www.youtube.com/watch?v=jVPPQ8jCFrE)

Compute Engine lets you create and run [instances](https://docs.cloud.google.com/compute/docs/instances) on Google infrastructure. This document provides an overview of the various configuration parameters that are available to you during a Compute Engine instance creation. If you are creating an instance for the first time, then this document provides a starting point for understanding the process.

The terms *Compute Engine instance*, *compute instance* or *instance* are synonymous. Based on the [machine type](https://docs.cloud.google.com/compute/docs/machine-resource) that you specify, an instance can be either a bare metal instance or a virtual machine (VM) instance, as follows:

- If the name of its machine type ends in `-metal`, an instance is a [bare metal instance](https://docs.cloud.google.com/compute/docs/machine-resource#bare-metal-types), which does not have a hypervisor installed.
- Otherwise, an instance is a VM instance. The terms *virtual machine instance*, *VM instance*, and *VM* are synonymous.

Synonymous terms are used interchangeably across the documentation and Google Cloud interfaces such as the [Google Cloud console](https://console.cloud.google.com/), the [gcloud](https://docs.cloud.google.com/compute/docs/gcloud-compute) command-line tool, and the [REST API](https://docs.cloud.google.com/compute/docs/reference/latest).

<br />

## Before you begin

- Review the basics about [Compute Engine instances](https://docs.cloud.google.com/compute/docs/instances).
- If you haven't already, set up [authentication](https://docs.cloud.google.com/compute/docs/authentication). Authentication verifies your identity for access to Google Cloud services and APIs. To run code or samples from a local development environment, you can authenticate to Compute Engine by selecting one of the following options:

  Select the tab for how you plan to use the samples on this page:

  ### Console

  When you use the Google Cloud console to access Google Cloud services and APIs, you don't need to set up authentication.

  ### gcloud

  1. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. After installation, [initialize](https://docs.cloud.google.com/sdk/docs/initializing) the Google Cloud CLI by running the following command:

     ```bash
     gcloud init
     ```

     If you're using an external identity provider (IdP), you must first [sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud).

     > [!NOTE]
     > **Note:** If you installed the gcloud CLI previously, make sure you have the latest version by running `gcloud components update`.

  2. [Set a default region and zone](https://docs.cloud.google.com/compute/docs/gcloud-compute#set_default_zone_and_region_in_your_local_client).

  ### REST

  To use the REST API samples on this page in a local development environment, you use the credentials you provide to the gcloud CLI.
  1. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI.
  2. If you're using an external identity provider (IdP), you must first [sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud).

  For more information, see [Authenticate for using REST](https://docs.cloud.google.com/docs/authentication/rest) in the Google Cloud authentication documentation.

## Ways to create and configure instances

You can create instances in multiple ways, each with its own method of configuration, as follows:

- **[Create your instance by manually specifying a custom configuration](https://docs.cloud.google.com/compute/docs/instances/create-start-instance#custom-vm-configuration-documents).** Choose this option if you're creating an instance from the scratch and are facing any of the following scenarios:

  - You know the specific configuration that is required for your workload.
  - You want to create an instance with a complicated configuration.
  - You want to create an instance by using the Google Cloud CLI or REST.

  If you choose this method, then also review the list of all [configuration options available during instance creation](https://docs.cloud.google.com/compute/docs/instances/instance-creation-overview#new-instance-configuration-options).
- **[Create a workload-optimized instance](https://docs.cloud.google.com/compute/docs/instances/create-workload-optimized-instance).** In this method, you select your workload type while creating your instance and Google automatically populates a preset configuration that suits your workload. Choose this option if you're starting out with Compute Engine and don't know which configuration best suits your intended workload. This option is available only in the Google Cloud console.

- **[Create your instance by using an instance template](https://docs.cloud.google.com/compute/docs/instances/create-vm-from-instance-template).** An instance template is a resource that defines configuration settings for instances. Choose this option if you have a defined configuration template and want to create a lot of VMs with the same configuration.

- **[Create your instance by making copies of a machine image](https://docs.cloud.google.com/compute/docs/machine-images/create-instance-from-machine-image).** A machine image contains most of the information and data needed for cloning an instance. Choose this option if you want to make multiple copies of an existing source instance.

After you create your compute instance, Compute Engine automatically starts the instance.

## Configuration options available during instance creation

When you create a Compute Engine instance, you specify the configuration that you want for your instance. Compute Engine uses this configuration to create your instance. The following table lists the various parameters that you configure when you create a Compute Engine instance. To get AI-powered assistance when you evaluate which configurations best fit your workload requirements, comparing pricing trade-offs, you can interact with Gemini in the Google Cloud console. For more information, see [Design your compute infrastructure with Gemini](https://docs.cloud.google.com/compute/docs/design-with-gemini).
Machine configuration Operating system (OS) and storage Data protection Networking Observability Security Advanced configuration <button class="clear-all">Clear all</button>

| **Parameter** | **What you can configure** |
|---|---|
| Machine configuration | - **Hardware** : You specify a [machine family, series, and type](https://docs.cloud.google.com/compute/docs/machine-resource), which determines the number of vCPUs, memory, and the [CPU platform](https://docs.cloud.google.com/compute/docs/cpu-platforms) that Compute Engine allocates for your instance. If the machine type is available on multiple CPU platforms, you can choose the earliest CPU platform to use when creating the instance. For the machine type, you can choose either a predefined machine type or create a [custom machine type](https://docs.cloud.google.com/compute/docs/machine-resource#custom-types) for some machine series. <!-- --> - **Location** : You can choose the [region and zone](https://docs.cloud.google.com/compute/docs/regions-zones) where you want to create your instance. <!-- --> - **Instance name** : Specify a [name](https://docs.cloud.google.com/compute/docs/naming-resources) for the instance that is unique within your project and the selected zone. <!-- --> - You can also configure more specific and advanced machine configuration settings such as: - [Simultaneous multi-threading (SMT)](https://docs.cloud.google.com/compute/docs/instances/set-threads-per-core) - The [number of visible cores](https://docs.cloud.google.com/compute/docs/instances/customize-visible-cores) - For C4 instances only: whether the instance runs in [all-core-max turbo mode](https://docs.cloud.google.com/compute/docs/cpu-platforms#frequency_behavior). |
| Operating system (OS) and storage | - **Boot disk and OS** : Every instance comes with a boot disk for which you can specify a disk name, size, and [disk type](https://docs.cloud.google.com/compute/docs/disks). You also select the [OS image](https://docs.cloud.google.com/compute/docs/images) to install on the boot disk in one of the following ways: - If you want to use a preconfigured OS image to create your instance, then use a [public image](https://docs.cloud.google.com/compute/docs/images#os-compute-support). Public images have all the drivers that are necessary to run the instance in Google Cloud. Compute Engine offers many preconfigured public OS images that have compatible Linux or Windows operating systems. - If you are creating an instance for an application, you can use a [custom image](https://docs.cloud.google.com/compute/docs/images/create-custom) or a [shared image](https://docs.cloud.google.com/compute/docs/images/managing-access-custom-images) to which you added additional drivers and software that support your application. - You can also use a [snapshot](https://docs.cloud.google.com/compute/docs/disks/snapshots) or an existing disk as the source for creating the OS image on the boot disk. <!-- --> - **Additional disks** : You can create and attach one or more non-boot disks to the new instance in the following ways: - You can choose to create and attach new, blank disks. - You can choose to create and attach new disks from an existing source image or an existing disk. - You can choose to attach existing disks. - For some machine types, Local SSD disks are [automatically attached during instance creation](https://docs.cloud.google.com/compute/docs/disks/local-ssd#lssd_disks_fixed). For a few other machine types, you can choose to [attach Local SSD disks during instance creation](https://docs.cloud.google.com/compute/docs/disks/local-ssd#lssd_disk_options). - For Local SSD disks, you can optionally configure the [Local SSD recovery timeout](https://docs.cloud.google.com/compute/docs/instances/host-maintenance-overview#local-ssd-timeout), and which interface to use - [NVMe or SCSI](https://docs.cloud.google.com/compute/docs/disks/local-ssd#choose_an_interface) <!-- --> - **Disk configuration** : Whether you're configuring a boot disk or an additional data disk, you can specify the following configuration details: - Disk name (and optionally a custom device name) - Disk size - [Encryption](https://docs.cloud.google.com/compute/docs/disks/disk-encryption) - For [Google Cloud Hyperdisk](https://docs.cloud.google.com/compute/docs/disks/hyperdisks) and [Extreme Persistent Disk](https://docs.cloud.google.com/compute/docs/disks/extreme-persistent-disk) volumes only: the IOPS and throughput performance limits - For Hyperdisk Balanced and Hyperdisk Throughput volumes only: whether the disk is created using resources in a [Hyperdisk Storage Pool](https://docs.cloud.google.com/compute/docs/disks#storage_pools) - The [disk attachment mode](https://docs.cloud.google.com/compute/docs/disks/attach-disks#attachment_mode) (Read-only or Read-write) - A [label](https://docs.cloud.google.com/compute/docs/labeling-resources) or [tag](https://docs.cloud.google.com/compute/docs/tag-resources) for the disk - You can also enable a setting that prevents your disk from being deleted if the attached instance is deleted. <!-- --> - **Container** : You can run containers such as Docker or Kubernetes on any of the following images: - Linux public VM images - Windows Server public VM images - A [Container-Optimized OS](https://docs.cloud.google.com/container-optimized-os/docs/concepts/features-and-benefits) image. You specify a container image name and other [container configuration details](https://docs.cloud.google.com/compute/docs/containers/configuring-options-to-run-containers). You can also specify mount directories to add \`tmpfs\` storage and additional disks to the container. > [!CAUTION] > **Caution:** The container startup agent (konlet) that deploys containers on VMs during VM creation is deprecated. Use the `docker run` commands in a startup script or use the `cloud-init` tool to configure and to run containers on your VMs and MIGs. For more information, see [Migrate containers that were deployed on VMs during VM creation](https://docs.cloud.google.com/compute/docs/containers/migrate-containers). |
| Data protection | - **Data backup** : You can automate recurring backups of your disk and instance data and prepare for disaster recovery in the following ways: - Use [Backup and DR Service backup plans](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/backup-dr#backup_plans) to back up your entire instance. - Use [snapshot schedules](https://docs.cloud.google.com/compute/docs/disks/scheduled-snapshots) to automate your disk data backup. - To learn how to choose the correct data protection option for your use case, see [Data protection options](https://docs.cloud.google.com/compute/docs/disks/data-protection). > [!NOTE] > You can also configure a project-wide default backup setting. This setting specifies which backup method is preselected by default every time you create an instance in the Google Cloud console. To learn more, see [Configure the default backup setting for the console](https://docs.cloud.google.com/compute/docs/disks/default-backup) <!-- --> - **Data replication** : You can continuously replicate your disk data for disaster protection using [cross-zone synchronous replication](https://docs.cloud.google.com/compute/docs/disks/about-regional-persistent-disk) or [cross-region asynchronous replication](https://docs.cloud.google.com/compute/docs/disks/async-pd/about). - **Protect non-boot disks only**: You can also enable an option that applies your snapshot schedules and data replication settings only to non-boot disks. Choosing this setting can help you reduce costs. However, this setting doesn't apply to backup plans. |
| Networking | - **Firewall rules** : You can set up a [firewall](https://docs.cloud.google.com/firewall/docs/firewalls) and configure the type of network traffic that you want to allow from the internet. You can also specify a [network tag for the firewall rules](https://docs.cloud.google.com/vpc/docs/add-remove-network-tags). <!-- --> - **Custom hostname** : You can specify that Google Cloud should use a [custom name for the instance](https://docs.cloud.google.com/compute/docs/instances/custom-hostname-vm#requirements) other than the internal DNS name. If you choose this option, then you must manually configure an internal DNS record for the custom hostname. <!-- --> - **IP forwarding** : You can choose whether to [configure IP forwarding](https://docs.cloud.google.com/vpc/docs/using-routes#canipforward) for the new instance. <!-- --> - **Network performance** : You can configure the instance to use [per VM Tier_1 networking performance](https://docs.cloud.google.com/compute/docs/networking/configure-vm-with-high-bandwidth-configuration) for higher network performance at additional cost. <!-- --> - **Network interfaces** : By default, a new instance is configured with a single interface that uses the [default auto mode Virtual Private Cloud (VPC) network](https://docs.cloud.google.com/compute/docs/networking/network-overview#subnets). Alternatively, you can specify a [custom mode VPC network and subnet](https://docs.cloud.google.com/vpc/docs/create-modify-vpc-networks#create-custom-network) that you created previously. You can also configure [additional network interfaces](https://docs.cloud.google.com/vpc/docs/multiple-interfaces-concepts) and Dynamic NICs for the instance. For each network interface, you can configure the following properties: - The network interface type - The IP stack type (IPv4 only, IPv6 only, or dual-stack) - The [type of IP address](https://docs.cloud.google.com/vpc/docs/ip-addresses) for the internal and optional external IP addresses (ephemeral address or a reserved, static address) - An alias IP range for the network interface - The [Network Service Tier](https://docs.cloud.google.com/network-tiers) that the network interface uses - Whether a public DNS [PTR record](https://docs.cloud.google.com/compute/docs/instances/create-ptr-record) is associated with the external IP address for the network interface |
| Observability | - **Ops agent** : You can choose to install [Ops agent](https://docs.cloud.google.com/stackdriver/docs/solutions/agents/ops-agent) on your instance to collect logs and metrics and [monitor instance activity](https://docs.cloud.google.com/compute/docs/instances/observe-monitor-vms). <!-- --> - **Virtual displays** : You can [enable virtual displays](https://docs.cloud.google.com/compute/docs/instances/enable-instance-virtual-display) on your instance to run screen capturing or remote system management tools on your VM. |
| Security | - **Service account** : You can attach a [service account](https://docs.cloud.google.com/compute/docs/access/service-accounts) to your instance. Service accounts allow applications that run on an instance to make authorized Google Cloud API calls and access Google Cloud resources. You can also select the type and level of API access to grant the VM. - **Confidential computing** : You can prevent your data from being accessed while you use an instance by using [Confidential Computing](https://docs.cloud.google.com/confidential-computing/docs/confidential-computing-overview) to encrypt your data. - **Shielded VM features** : You can make your instance more secure against boot- or kernel-level malware and rootkits by enabling [Shielded VM features](https://docs.cloud.google.com/compute/shielded-vm/docs/shielded-vm). - **VM access** : You can [control the users who have access](https://docs.cloud.google.com/compute/docs/access) to an instance by setting up [IAM roles and permissions](https://docs.cloud.google.com/compute/docs/access/iam) and [SSH keys for authentication](https://docs.cloud.google.com/compute/docs/instances/ssh). |
| Advanced configuration | - **Tags and Labels** : To assist with resource organization, you can add [Tags](https://docs.cloud.google.com/resource-manager/docs/tags/tags-overview) and [Labels](https://docs.cloud.google.com/compute/docs/labeling-resources) to the instance. <!-- --> - **Deletion protection** : You can protect your instances from being [accidentally deleted](https://docs.cloud.google.com/compute/docs/instances/preventing-accidental-vm-deletion). <!-- --> - **Placement policy** : You can control instance placement in a data center by applying a [placement policy to your instances](https://docs.cloud.google.com/compute/docs/instances/placement-policies-overview). <!-- --> - **Reservations** : You can configure your instance to consume any [reserved zonal resource capacity](https://docs.cloud.google.com/compute/docs/instances/reservations-consume#consuming_instances_from_any_matching_reservation) to ensure better resource availability. <!-- --> - **Automation** : You can specify a [startup script](https://docs.cloud.google.com/compute/docs/instances/startup-scripts) that runs each time the instance starts or reboots. <!-- --> - **Metadata** : You can set [custom metadata](https://docs.cloud.google.com/compute/docs/metadata/overview#custom-metadata-keys) for your instance to store unique information about the instance. <!-- --> - **Encryption** : You can choose the encryption method and keys to use to protect disk data, memory contents, and metadata when the instance is suspended. This can be different from the encryption used to protect the disk data while the instance is running. You can also configure how the instance behaves if a specified [Cloud KMS key is revoked](https://docs.cloud.google.com/compute/docs/disks/customer-managed-encryption#vm-shutdown). <!-- --> - **Provisioning model** : You can choose among the standard, spot, flex-start ([Preview](https://cloud.google.com/products#product-launch-stages)), or reservation-bound provisioning model. For more information, see [Compute Engine instances provisioning model](https://docs.cloud.google.com/compute/docs/instances/provisioning-models). <!-- --> - **Sole-tenancy** : You can opt for having dedicated physical servers for your instances and specify a [sole-tenant node](https://docs.cloud.google.com/compute/docs/nodes/sole-tenant-nodes) or [node group](https://docs.cloud.google.com/compute/docs/nodes/autoscaling-node-groups) to create the instance in. For general-purpose N series machine types, you can specify whether to [enable CPU overcommit](https://docs.cloud.google.com/compute/docs/nodes/overcommitting-cpus-sole-tenant-vms) for instances running on sole tenant nodes. |

## What's next

- Learn how to [create and start a Compute Engine instance](https://docs.cloud.google.com/compute/docs/instances/create-start-instance).
- If you're creating an instance for the first time, then try one of the following tutorials for a basic configuration:
  - [Create a Linux VM instance in Compute Engine](https://docs.cloud.google.com/compute/docs/create-linux-vm-instance)
  - [Create a Windows Server VM instance in Compute Engine](https://docs.cloud.google.com/compute/docs/create-windows-server-vm-instance)
- Learn how to [design your compute infrastructure by using Gemini](https://docs.cloud.google.com/compute/docs/design-with-gemini).
- Learn about [what happens to an instance after creation](https://docs.cloud.google.com/compute/docs/instances/instance-life-cycle).

## Create and start a Compute Engine instance

Compute Engine lets you create and run [instances](https://docs.cloud.google.com/compute/docs/instances) on Google infrastructure. This document shows how to create a Compute Engine instance.

The terms *Compute Engine instance*, *compute instance* or *instance* are synonymous. Based on the [machine type](https://docs.cloud.google.com/compute/docs/machine-resource) that you specify, an instance can be either a bare metal instance or a virtual machine (VM) instance, as follows:

- If the name of its machine type ends in `-metal`, an instance is a [bare metal instance](https://docs.cloud.google.com/compute/docs/machine-resource#bare-metal-types), which does not have a hypervisor installed.
- Otherwise, an instance is a VM instance. The terms *virtual machine instance*, *VM instance*, and *VM* are synonymous.

Synonymous terms are used interchangeably across the documentation and Google Cloud interfaces such as the [Google Cloud console](https://console.cloud.google.com/), the [gcloud](https://docs.cloud.google.com/compute/docs/gcloud-compute) command-line tool, and the [REST API](https://docs.cloud.google.com/compute/docs/reference/latest).

<br />

The instructions in this document only introduce you to instance creation and provide a starting point for creating an instance. For detailed steps on how to create instances with specific or complicated configurations, see instead the [Create and start instances with specific configurations](https://docs.cloud.google.com/compute/docs/instances/create-start-instance#custom-vm-configuration-documents).

## Before you begin

- Review the basics about [creating instances](https://docs.cloud.google.com/compute/docs/instances/instance-creation-overview).
- If you haven't already, set up [authentication](https://docs.cloud.google.com/compute/docs/authentication). Authentication verifies your identity for access to Google Cloud services and APIs. To run code or samples from a local development environment, you can authenticate to Compute Engine by selecting one of the following options:

  Select the tab for how you plan to use the samples on this page:

  ### Console

  When you use the Google Cloud console to access Google Cloud services and APIs, you don't need to set up authentication.

  ### gcloud

  1. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. After installation, [initialize](https://docs.cloud.google.com/sdk/docs/initializing) the Google Cloud CLI by running the following command:

     ```bash
     gcloud init
     ```

     If you're using an external identity provider (IdP), you must first [sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud).

     > [!NOTE]
     > **Note:** If you installed the gcloud CLI previously, make sure you have the latest version by running `gcloud components update`.

  2. [Set a default region and zone](https://docs.cloud.google.com/compute/docs/gcloud-compute#set_default_zone_and_region_in_your_local_client).

  ### Terraform

  To use the Terraform samples on this page in a local development environment, install and initialize the gcloud CLI, and then set up Application Default Credentials with your user credentials.
  1. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI.

  2. If you're using an external identity provider (IdP), you must first [sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud).

  3. If you're using a local shell, then create local authentication credentials for your user account:

     ```bash
     gcloud auth application-default login
     ```

     You don't need to do this if you're using Cloud Shell.

     If an authentication error is returned, and you are using an external identity provider (IdP), confirm that you have [signed in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud).

  For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/compute/docs/authentication#local-development).

  ### C#

  To use the .NET samples on this page in a local development environment, install and initialize the gcloud CLI, and then set up Application Default Credentials with your user credentials.
  1. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI.

  2. If you're using an external identity provider (IdP), you must first [sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud).

  3. If you're using a local shell, then create local authentication credentials for your user account:

     ```bash
     gcloud auth application-default login
     ```

     You don't need to do this if you're using Cloud Shell.

     If an authentication error is returned, and you are using an external identity provider (IdP), confirm that you have [signed in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud).

  For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/compute/docs/authentication#local-development).

  ### Go

  To use the Go samples on this page in a local development environment, install and initialize the gcloud CLI, and then set up Application Default Credentials with your user credentials.
  1. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI.

  2. If you're using an external identity provider (IdP), you must first [sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud).

  3. If you're using a local shell, then create local authentication credentials for your user account:

     ```bash
     gcloud auth application-default login
     ```

     You don't need to do this if you're using Cloud Shell.

     If an authentication error is returned, and you are using an external identity provider (IdP), confirm that you have [signed in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud).

  For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/compute/docs/authentication#local-development).

  ### Java

  To use the Java samples on this page in a local development environment, install and initialize the gcloud CLI, and then set up Application Default Credentials with your user credentials.
  1. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI.

  2. If you're using an external identity provider (IdP), you must first [sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud).

  3. If you're using a local shell, then create local authentication credentials for your user account:

     ```bash
     gcloud auth application-default login
     ```

     You don't need to do this if you're using Cloud Shell.

     If an authentication error is returned, and you are using an external identity provider (IdP), confirm that you have [signed in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud).

  For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/compute/docs/authentication#local-development).

  ### Node.js

  To use the Node.js samples on this page in a local development environment, install and initialize the gcloud CLI, and then set up Application Default Credentials with your user credentials.
  1. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI.

  2. If you're using an external identity provider (IdP), you must first [sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud).

  3. If you're using a local shell, then create local authentication credentials for your user account:

     ```bash
     gcloud auth application-default login
     ```

     You don't need to do this if you're using Cloud Shell.

     If an authentication error is returned, and you are using an external identity provider (IdP), confirm that you have [signed in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud).

  For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/compute/docs/authentication#local-development).

  ### PHP

  To use the PHP samples on this page in a local development environment, install and initialize the gcloud CLI, and then set up Application Default Credentials with your user credentials.
  1. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI.

  2. If you're using an external identity provider (IdP), you must first [sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud).

  3. If you're using a local shell, then create local authentication credentials for your user account:

     ```bash
     gcloud auth application-default login
     ```

     You don't need to do this if you're using Cloud Shell.

     If an authentication error is returned, and you are using an external identity provider (IdP), confirm that you have [signed in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud).

  For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/compute/docs/authentication#local-development).

  ### Python

  To use the Python samples on this page in a local development environment, install and initialize the gcloud CLI, and then set up Application Default Credentials with your user credentials.
  1. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI.

  2. If you're using an external identity provider (IdP), you must first [sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud).

  3. If you're using a local shell, then create local authentication credentials for your user account:

     ```bash
     gcloud auth application-default login
     ```

     You don't need to do this if you're using Cloud Shell.

     If an authentication error is returned, and you are using an external identity provider (IdP), confirm that you have [signed in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud).

  For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/compute/docs/authentication#local-development).

  ### Ruby

  To use the Ruby samples on this page in a local development environment, install and initialize the gcloud CLI, and then set up Application Default Credentials with your user credentials.
  1. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI.

  2. If you're using an external identity provider (IdP), you must first [sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud).

  3. If you're using a local shell, then create local authentication credentials for your user account:

     ```bash
     gcloud auth application-default login
     ```

     You don't need to do this if you're using Cloud Shell.

     If an authentication error is returned, and you are using an external identity provider (IdP), confirm that you have [signed in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud).

  For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/compute/docs/authentication#local-development).

  ### REST

  To use the REST API samples on this page in a local development environment, you use the credentials you provide to the gcloud CLI.
  1. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI.
  2. If you're using an external identity provider (IdP), you must first [sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud).

  For more information, see [Authenticate for using REST](https://docs.cloud.google.com/docs/authentication/rest) in the Google Cloud authentication documentation.

### Required roles

To get the permissions that you need to create instances, ask your administrator to grant you the [Compute Instance Admin (v1)](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.instanceAdmin.v1) (`roles/compute.instanceAdmin.v1`) IAM role on the project. For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access).

This predefined role contains the permissions required to create instances. To see the exact permissions that are required, expand the **Required permissions** section:

#### Required permissions

The following permissions are required to create instances:

- `compute.instances.create` on the project
- To use a custom image to create the VM: `compute.images.useReadOnly` on the image
- To use a snapshot to create the VM: `compute.snapshots.useReadOnly` on the snapshot
- To use an instance template to create the VM: `compute.instanceTemplates.useReadOnly` on the instance template
- To specify a subnet for your VM: `compute.subnetworks.use` on the project or on the chosen subnet
- To specify a static IP address for the VM: `compute.addresses.use` on the project
- To assign an external IP address to the VM when using a VPC network: `compute.subnetworks.useExternalIp` on the project or on the chosen subnet
- To assign a [legacy network](https://docs.cloud.google.com/vpc/docs/legacy) to the VM: `compute.networks.use` on the project
- To assign an external IP address to the VM when using a legacy network: `compute.networks.useExternalIp` on the project
- To set VM instance metadata for the VM: `compute.instances.setMetadata` on the project
- To set tags for the VM: `compute.instances.setTags` on the VM
- To set labels for the VM: `compute.instances.setLabels` on the VM
- To set a service account for the VM to use: `compute.instances.setServiceAccount` on the VM
- To create a new disk for the VM: `compute.disks.create` on the project
- To attach an existing disk in read-only or read-write mode: `compute.disks.use` on the disk
- To attach an existing disk in read-only mode: `compute.disks.useReadOnly` on the disk

You might also be able to get these permissions with [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined).

## Methods to create and start an instance

This section describes the basic methods that you can use to create and start a Compute Engine instance. This procedure is intended for introductory purposes only. For detailed steps on how to configure and create your instances, see the [Create and start instances with specific configurations](https://docs.cloud.google.com/compute/docs/instances/create-start-instance#custom-vm-configuration-documents) section instead.

For beginners, Google recommends using the Google Cloud console, the Google Cloud CLI, or the REST API. Review the following instructions to learn the general process for creating an instance with each method. Optionally, you can generate the code to create an instance for Google Cloud CLI, REST, or Terraform by using the **Equivalent code** button on the **Create an instance** page in the Google Cloud console. Generating code can help you learn syntax and prevent errors. Learn more about [Google Cloud console features for Compute Engine](https://docs.cloud.google.com/compute/docs/console).

### Console

1. In the Google Cloud console, go to the **Create an instance** page.

   [Go to Create an instance](https://console.cloud.google.com/compute/instancesAdd)

   The **Create an instance** screen appears and displays the **Machine configuration** pane.
2. To configure instance properties, use the options in the navigation menu as follows.

   > [!TIP]
   > **Tip:** For a summary of the options in the navigation menu, see [Configuration options during instance creation](https://docs.cloud.google.com/compute/docs/instances/instance-creation-overview#new-instance-configuration-options).

   - To configure instance properties related to name, location, or machine configuration, click **Machine configuration** . In the **Machine configuration** pane that appears, specify values for the properties that you want to configure.

   - To configure instance properties related to boot disk, operating system (OS), and additional non-boot storage options, click **OS and storage** . In the **Operating system and storage** pane that appears, specify values for the properties that you want to configure.

   - To configure instance properties related to backup and data replication, click **Data protection** . In the **Data protection** pane that appears, specify values for the properties that you want to configure.

   - To configure instance properties related to network interface and firewall settings, click **Networking** . In the **Networking** pane that appears, specify values for the properties that you want to configure.

   - To configure instance properties related to Ops agent and virtual displays, click **Observability** . In the **Observability** pane that appears, specify values for the properties that you want to configure.

   - To configure instance properties related to security and access, click **Security** . In the **Security** pane that appears, specify values for the properties that you want to configure.

   - To configure instance properties related to metadata, reservations, resource organization, provisioning type, and sole-tenancy, click **Advanced** . In the **Advanced** pane that appears, specify values for the properties that you want to configure.

3. To create and start your instance, click **Create**.

### gcloud

To create an instance with your own configuration, use the [`gcloud compute instances create` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instances/create).

You can't use this command to create [instances in bulk](https://docs.cloud.google.com/compute/docs/instances/multiple/create-in-bulk) or [instances that run container images](https://docs.cloud.google.com/compute/docs/containers/deploying-containers). Instead, do the following:

- To create instances in bulk, use the [`gcloud compute instances bulk create` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instances/bulk/create).
- To create instances to deploy containers, use the [`gcloud compute instances create-with-container` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instances/create-with-container).

### REST

To create an instance with your own configuration, make a `POST` request to the [`instances.insert` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/instances/insert).

You can't use this method to create [instances in bulk](https://docs.cloud.google.com/compute/docs/instances/multiple/create-in-bulk). Instead, make a `POST` request to the [`instances.bulkInsert` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/instances/bulkInsert).

## Create and start instances with specific configurations

Each of the following documents provides instructions for how to create and start an instance that uses one or more specific configuration options. Based on your use case, you can create an instance that uses configuration options from multiple documents by combining the instructions. To learn about the various parameters that you can configure while creating your instance, review [Configuration options available during instance creation](https://docs.cloud.google.com/compute/docs/instances/instance-creation-overview#new-instance-configuration-options).


Preconfigured for you
:
    [Create a Google-configured, workload-optimized instance](https://docs.cloud.google.com/compute/docs/instances/create-workload-optimized-instance)


Customized machine configuration
:
    [Create an instance with a custom hostname](https://docs.cloud.google.com/compute/docs/instances/custom-hostname-vm)
:
    [Create an instance with a custom machine type](https://docs.cloud.google.com/compute/docs/instances/creating-instance-with-custom-machine-type)
:
    [Create an instance with attached GPUs](https://docs.cloud.google.com/compute/docs/gpus/create-vm-with-gpus)
:
    [Create an instance with attached TPUs](https://docs.cloud.google.com/compute/docs/tpus/create-tpu-vm-instance)
:
    [Specify a minimum CPU platform for an instance](https://docs.cloud.google.com/compute/docs/instances/specify-min-cpu-platform)


Customized OS configuration
:
    [Create an instance from a public image](https://docs.cloud.google.com/compute/docs/instances/create-vm-from-public-image)
:
    [Create an instance from a custom image](https://docs.cloud.google.com/compute/docs/instances/create-vm-from-custom-image)
:
    [Create an instance from a shared image](https://docs.cloud.google.com/compute/docs/instances/create-vm-from-shared-image)
:
    [Create an instance using a RHEL BYOS image](https://docs.cloud.google.com/compute/docs/instances/create-rhel-byos-vm)


Customized networking configuration
:
    [Create an instance in a specific subnet](https://docs.cloud.google.com/compute/docs/instances/create-vm-specific-subnet)
:
    [Create an instance that uses IPv6 addresses](https://docs.cloud.google.com/compute/docs/instances/create-ipv6-instance)
:
    [Create instances that use the gVNIC network interface](https://docs.cloud.google.com/compute/docs/networking/using-gvnic#create_a_vm_with_gvnic_support)
:
    [Configure an instance with higher bandwidth](https://docs.cloud.google.com/compute/docs/networking/configure-vm-with-high-bandwidth-configuration)


Customized observability configuration
:
    [Create an instance that's configured for Ops Agent monitoring and logging](https://docs.cloud.google.com/compute/docs/instances/create-vm-ops-agent-monitoring-logging)
:
    [Enable virtual displays on an instance](https://docs.cloud.google.com/compute/docs/instances/enable-instance-virtual-display)


Customized security configuration
:
    [Create an instance that uses a user-managed service account](https://docs.cloud.google.com/compute/docs/access/create-enable-service-accounts-for-instances)
:
    [Create VMs with managed workload identities enabled](https://docs.cloud.google.com/compute/docs/access/authenticate-workloads-over-mtls#create-workload-id-vms)
:
    [Enable OS Login during VM creation](https://docs.cloud.google.com/compute/docs/oslogin/set-up-oslogin#enable_os_login_during_vm_creation)


Configured for disaster recovery
:
    [Create an instance with a Backup and DR backup plan](https://docs.cloud.google.com/compute/docs/instances/create-instance-with-gcbdr-backup-plan)


From a backup
:
    [Create an instance from a machine image](https://docs.cloud.google.com/compute/docs/machine-images/create-instance-from-machine-image)
:
    [Create an instance from a disk snapshot](https://docs.cloud.google.com/compute/docs/disks/restore-snapshot)
:
    [Restore an instance from a backup vault](https://docs.cloud.google.com/backup-disaster-recovery/docs/cloud-console/compute/compute-instance-restore)


From existing configurations
:
    [Create an instance from an instance template](https://docs.cloud.google.com/compute/docs/instances/create-vm-from-instance-template)
:
    [Create an instance similar to an existing instance](https://docs.cloud.google.com/compute/docs/instances/create-vm-from-similar-instance)


Configured for specific workloads
:
    [Create an instance to deploy a container](https://docs.cloud.google.com/compute/docs/containers/deploying-containers#deploying_a_container_on_a_new_vm_instance)
:
    [Create Windows Server instances](https://docs.cloud.google.com/compute/docs/instances/windows/creating-managing-windows-instances)
:
    [Create SQL Server instances](https://docs.cloud.google.com/compute/docs/instances/sql-server/creating-sql-server-instances)
:
    [Create an instance with a high performance computing (HPC) image](https://docs.cloud.google.com/compute/docs/instances/create-hpc-vm)


Customized provisioning type
:
    [Create a Spot instance](https://docs.cloud.google.com/compute/docs/instances/create-use-spot)
:
    [Create instances that consume reserved instances](https://docs.cloud.google.com/compute/docs/instances/reservations-consume)


Multiple instances at once
:
    [Create a managed instance group (MIG)](https://docs.cloud.google.com/compute/docs/instance-groups/creating-groups-of-managed-instances#basic_scenarios_for_creating_a_mig)
:
    [Create instances in bulk](https://docs.cloud.google.com/compute/docs/instances/multiple/create-in-bulk)


Sole-tenant nodes
:
    [Create instances on sole-tenant nodes](https://docs.cloud.google.com/compute/docs/nodes/create-nodes)


Efficient instances
:
    [Create an instance with an attached instance schedule](https://docs.cloud.google.com/compute/docs/instances/schedule-instance-start-stop#attaching_to_a_new_VM)

## Troubleshooting

To find methods for resolving common instance creation errors, see [Troubleshooting instance creation](https://docs.cloud.google.com/compute/docs/troubleshooting/troubleshooting-vm-creation).

## What's next?

- Learn how to [check the status of an instance](https://docs.cloud.google.com/compute/docs/instances/instance-life-cycle) to see when it is ready to use.
- Learn how to [connect to your instance](https://docs.cloud.google.com/compute/docs/instances/connecting-to-instance).
- Learn how to [scale out your instance into a group of instances](https://docs.cloud.google.com/compute/docs/instance-groups/create-mig-from-vm).
- Learn how to [reserve capacity for your instances](https://docs.cloud.google.com/compute/docs/instances/choose-reservation-type).
- Learn how to save on instance costs through [committed use discounts](https://docs.cloud.google.com/compute/docs/instances/committed-use-discounts-overview) and [sustained use discounts](https://docs.cloud.google.com/compute/docs/sustained-use-discounts).

## Create and start a Compute Engine instance

Compute Engine lets you create and run [instances](https://docs.cloud.google.com/compute/docs/instances) on Google infrastructure. This document shows how to create a Compute Engine instance.

The terms *Compute Engine instance*, *compute instance* or *instance* are synonymous. Based on the [machine type](https://docs.cloud.google.com/compute/docs/machine-resource) that you specify, an instance can be either a bare metal instance or a virtual machine (VM) instance, as follows:

- If the name of its machine type ends in `-metal`, an instance is a [bare metal instance](https://docs.cloud.google.com/compute/docs/machine-resource#bare-metal-types), which does not have a hypervisor installed.
- Otherwise, an instance is a VM instance. The terms *virtual machine instance*, *VM instance*, and *VM* are synonymous.

Synonymous terms are used interchangeably across the documentation and Google Cloud interfaces such as the [Google Cloud console](https://console.cloud.google.com/), the [gcloud](https://docs.cloud.google.com/compute/docs/gcloud-compute) command-line tool, and the [REST API](https://docs.cloud.google.com/compute/docs/reference/latest).

<br />

The instructions in this document only introduce you to instance creation and provide a starting point for creating an instance. For detailed steps on how to create instances with specific or complicated configurations, see instead the [Create and start instances with specific configurations](https://docs.cloud.google.com/compute/docs/instances/create-start-instance#custom-vm-configuration-documents).

## Before you begin

- Review the basics about [creating instances](https://docs.cloud.google.com/compute/docs/instances/instance-creation-overview).
- If you haven't already, set up [authentication](https://docs.cloud.google.com/compute/docs/authentication). Authentication verifies your identity for access to Google Cloud services and APIs. To run code or samples from a local development environment, you can authenticate to Compute Engine by selecting one of the following options:

  Select the tab for how you plan to use the samples on this page:

  ### Console

  When you use the Google Cloud console to access Google Cloud services and APIs, you don't need to set up authentication.

  ### gcloud

  1. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. After installation, [initialize](https://docs.cloud.google.com/sdk/docs/initializing) the Google Cloud CLI by running the following command:

     ```bash
     gcloud init
     ```

     If you're using an external identity provider (IdP), you must first [sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud).

     > [!NOTE]
     > **Note:** If you installed the gcloud CLI previously, make sure you have the latest version by running `gcloud components update`.

  2. [Set a default region and zone](https://docs.cloud.google.com/compute/docs/gcloud-compute#set_default_zone_and_region_in_your_local_client).

  ### Terraform

  To use the Terraform samples on this page in a local development environment, install and initialize the gcloud CLI, and then set up Application Default Credentials with your user credentials.
  1. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI.

  2. If you're using an external identity provider (IdP), you must first [sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud).

  3. If you're using a local shell, then create local authentication credentials for your user account:

     ```bash
     gcloud auth application-default login
     ```

     You don't need to do this if you're using Cloud Shell.

     If an authentication error is returned, and you are using an external identity provider (IdP), confirm that you have [signed in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud).

  For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/compute/docs/authentication#local-development).

  ### C#

  To use the .NET samples on this page in a local development environment, install and initialize the gcloud CLI, and then set up Application Default Credentials with your user credentials.
  1. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI.

  2. If you're using an external identity provider (IdP), you must first [sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud).

  3. If you're using a local shell, then create local authentication credentials for your user account:

     ```bash
     gcloud auth application-default login
     ```

     You don't need to do this if you're using Cloud Shell.

     If an authentication error is returned, and you are using an external identity provider (IdP), confirm that you have [signed in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud).

  For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/compute/docs/authentication#local-development).

  ### Go

  To use the Go samples on this page in a local development environment, install and initialize the gcloud CLI, and then set up Application Default Credentials with your user credentials.
  1. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI.

  2. If you're using an external identity provider (IdP), you must first [sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud).

  3. If you're using a local shell, then create local authentication credentials for your user account:

     ```bash
     gcloud auth application-default login
     ```

     You don't need to do this if you're using Cloud Shell.

     If an authentication error is returned, and you are using an external identity provider (IdP), confirm that you have [signed in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud).

  For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/compute/docs/authentication#local-development).

  ### Java

  To use the Java samples on this page in a local development environment, install and initialize the gcloud CLI, and then set up Application Default Credentials with your user credentials.
  1. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI.

  2. If you're using an external identity provider (IdP), you must first [sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud).

  3. If you're using a local shell, then create local authentication credentials for your user account:

     ```bash
     gcloud auth application-default login
     ```

     You don't need to do this if you're using Cloud Shell.

     If an authentication error is returned, and you are using an external identity provider (IdP), confirm that you have [signed in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud).

  For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/compute/docs/authentication#local-development).

  ### Node.js

  To use the Node.js samples on this page in a local development environment, install and initialize the gcloud CLI, and then set up Application Default Credentials with your user credentials.
  1. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI.

  2. If you're using an external identity provider (IdP), you must first [sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud).

  3. If you're using a local shell, then create local authentication credentials for your user account:

     ```bash
     gcloud auth application-default login
     ```

     You don't need to do this if you're using Cloud Shell.

     If an authentication error is returned, and you are using an external identity provider (IdP), confirm that you have [signed in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud).

  For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/compute/docs/authentication#local-development).

  ### PHP

  To use the PHP samples on this page in a local development environment, install and initialize the gcloud CLI, and then set up Application Default Credentials with your user credentials.
  1. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI.

  2. If you're using an external identity provider (IdP), you must first [sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud).

  3. If you're using a local shell, then create local authentication credentials for your user account:

     ```bash
     gcloud auth application-default login
     ```

     You don't need to do this if you're using Cloud Shell.

     If an authentication error is returned, and you are using an external identity provider (IdP), confirm that you have [signed in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud).

  For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/compute/docs/authentication#local-development).

  ### Python

  To use the Python samples on this page in a local development environment, install and initialize the gcloud CLI, and then set up Application Default Credentials with your user credentials.
  1. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI.

  2. If you're using an external identity provider (IdP), you must first [sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud).

  3. If you're using a local shell, then create local authentication credentials for your user account:

     ```bash
     gcloud auth application-default login
     ```

     You don't need to do this if you're using Cloud Shell.

     If an authentication error is returned, and you are using an external identity provider (IdP), confirm that you have [signed in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud).

  For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/compute/docs/authentication#local-development).

  ### Ruby

  To use the Ruby samples on this page in a local development environment, install and initialize the gcloud CLI, and then set up Application Default Credentials with your user credentials.
  1. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI.

  2. If you're using an external identity provider (IdP), you must first [sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud).

  3. If you're using a local shell, then create local authentication credentials for your user account:

     ```bash
     gcloud auth application-default login
     ```

     You don't need to do this if you're using Cloud Shell.

     If an authentication error is returned, and you are using an external identity provider (IdP), confirm that you have [signed in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud).

  For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/compute/docs/authentication#local-development).

  ### REST

  To use the REST API samples on this page in a local development environment, you use the credentials you provide to the gcloud CLI.
  1. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI.
  2. If you're using an external identity provider (IdP), you must first [sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud).

  For more information, see [Authenticate for using REST](https://docs.cloud.google.com/docs/authentication/rest) in the Google Cloud authentication documentation.

### Required roles

To get the permissions that you need to create instances, ask your administrator to grant you the [Compute Instance Admin (v1)](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.instanceAdmin.v1) (`roles/compute.instanceAdmin.v1`) IAM role on the project. For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access).

This predefined role contains the permissions required to create instances. To see the exact permissions that are required, expand the **Required permissions** section:

#### Required permissions

The following permissions are required to create instances:

- `compute.instances.create` on the project
- To use a custom image to create the VM: `compute.images.useReadOnly` on the image
- To use a snapshot to create the VM: `compute.snapshots.useReadOnly` on the snapshot
- To use an instance template to create the VM: `compute.instanceTemplates.useReadOnly` on the instance template
- To specify a subnet for your VM: `compute.subnetworks.use` on the project or on the chosen subnet
- To specify a static IP address for the VM: `compute.addresses.use` on the project
- To assign an external IP address to the VM when using a VPC network: `compute.subnetworks.useExternalIp` on the project or on the chosen subnet
- To assign a [legacy network](https://docs.cloud.google.com/vpc/docs/legacy) to the VM: `compute.networks.use` on the project
- To assign an external IP address to the VM when using a legacy network: `compute.networks.useExternalIp` on the project
- To set VM instance metadata for the VM: `compute.instances.setMetadata` on the project
- To set tags for the VM: `compute.instances.setTags` on the VM
- To set labels for the VM: `compute.instances.setLabels` on the VM
- To set a service account for the VM to use: `compute.instances.setServiceAccount` on the VM
- To create a new disk for the VM: `compute.disks.create` on the project
- To attach an existing disk in read-only or read-write mode: `compute.disks.use` on the disk
- To attach an existing disk in read-only mode: `compute.disks.useReadOnly` on the disk

You might also be able to get these permissions with [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined).

## Methods to create and start an instance

This section describes the basic methods that you can use to create and start a Compute Engine instance. This procedure is intended for introductory purposes only. For detailed steps on how to configure and create your instances, see the [Create and start instances with specific configurations](https://docs.cloud.google.com/compute/docs/instances/create-start-instance#custom-vm-configuration-documents) section instead.

For beginners, Google recommends using the Google Cloud console, the Google Cloud CLI, or the REST API. Review the following instructions to learn the general process for creating an instance with each method. Optionally, you can generate the code to create an instance for Google Cloud CLI, REST, or Terraform by using the **Equivalent code** button on the **Create an instance** page in the Google Cloud console. Generating code can help you learn syntax and prevent errors. Learn more about [Google Cloud console features for Compute Engine](https://docs.cloud.google.com/compute/docs/console).

### Console

1. In the Google Cloud console, go to the **Create an instance** page.

   [Go to Create an instance](https://console.cloud.google.com/compute/instancesAdd)

   The **Create an instance** screen appears and displays the **Machine configuration** pane.
2. To configure instance properties, use the options in the navigation menu as follows.

   > [!TIP]
   > **Tip:** For a summary of the options in the navigation menu, see [Configuration options during instance creation](https://docs.cloud.google.com/compute/docs/instances/instance-creation-overview#new-instance-configuration-options).

   - To configure instance properties related to name, location, or machine configuration, click **Machine configuration** . In the **Machine configuration** pane that appears, specify values for the properties that you want to configure.

   - To configure instance properties related to boot disk, operating system (OS), and additional non-boot storage options, click **OS and storage** . In the **Operating system and storage** pane that appears, specify values for the properties that you want to configure.

   - To configure instance properties related to backup and data replication, click **Data protection** . In the **Data protection** pane that appears, specify values for the properties that you want to configure.

   - To configure instance properties related to network interface and firewall settings, click **Networking** . In the **Networking** pane that appears, specify values for the properties that you want to configure.

   - To configure instance properties related to Ops agent and virtual displays, click **Observability** . In the **Observability** pane that appears, specify values for the properties that you want to configure.

   - To configure instance properties related to security and access, click **Security** . In the **Security** pane that appears, specify values for the properties that you want to configure.

   - To configure instance properties related to metadata, reservations, resource organization, provisioning type, and sole-tenancy, click **Advanced** . In the **Advanced** pane that appears, specify values for the properties that you want to configure.

3. To create and start your instance, click **Create**.

### gcloud

To create an instance with your own configuration, use the [`gcloud compute instances create` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instances/create).

You can't use this command to create [instances in bulk](https://docs.cloud.google.com/compute/docs/instances/multiple/create-in-bulk) or [instances that run container images](https://docs.cloud.google.com/compute/docs/containers/deploying-containers). Instead, do the following:

- To create instances in bulk, use the [`gcloud compute instances bulk create` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instances/bulk/create).
- To create instances to deploy containers, use the [`gcloud compute instances create-with-container` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instances/create-with-container).

### REST

To create an instance with your own configuration, make a `POST` request to the [`instances.insert` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/instances/insert).

You can't use this method to create [instances in bulk](https://docs.cloud.google.com/compute/docs/instances/multiple/create-in-bulk). Instead, make a `POST` request to the [`instances.bulkInsert` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/instances/bulkInsert).

## Create and start instances with specific configurations

Each of the following documents provides instructions for how to create and start an instance that uses one or more specific configuration options. Based on your use case, you can create an instance that uses configuration options from multiple documents by combining the instructions. To learn about the various parameters that you can configure while creating your instance, review [Configuration options available during instance creation](https://docs.cloud.google.com/compute/docs/instances/instance-creation-overview#new-instance-configuration-options).


Preconfigured for you
:
    [Create a Google-configured, workload-optimized instance](https://docs.cloud.google.com/compute/docs/instances/create-workload-optimized-instance)


Customized machine configuration
:
    [Create an instance with a custom hostname](https://docs.cloud.google.com/compute/docs/instances/custom-hostname-vm)
:
    [Create an instance with a custom machine type](https://docs.cloud.google.com/compute/docs/instances/creating-instance-with-custom-machine-type)
:
    [Create an instance with attached GPUs](https://docs.cloud.google.com/compute/docs/gpus/create-vm-with-gpus)
:
    [Create an instance with attached TPUs](https://docs.cloud.google.com/compute/docs/tpus/create-tpu-vm-instance)
:
    [Specify a minimum CPU platform for an instance](https://docs.cloud.google.com/compute/docs/instances/specify-min-cpu-platform)


Customized OS configuration
:
    [Create an instance from a public image](https://docs.cloud.google.com/compute/docs/instances/create-vm-from-public-image)
:
    [Create an instance from a custom image](https://docs.cloud.google.com/compute/docs/instances/create-vm-from-custom-image)
:
    [Create an instance from a shared image](https://docs.cloud.google.com/compute/docs/instances/create-vm-from-shared-image)
:
    [Create an instance using a RHEL BYOS image](https://docs.cloud.google.com/compute/docs/instances/create-rhel-byos-vm)


Customized networking configuration
:
    [Create an instance in a specific subnet](https://docs.cloud.google.com/compute/docs/instances/create-vm-specific-subnet)
:
    [Create an instance that uses IPv6 addresses](https://docs.cloud.google.com/compute/docs/instances/create-ipv6-instance)
:
    [Create instances that use the gVNIC network interface](https://docs.cloud.google.com/compute/docs/networking/using-gvnic#create_a_vm_with_gvnic_support)
:
    [Configure an instance with higher bandwidth](https://docs.cloud.google.com/compute/docs/networking/configure-vm-with-high-bandwidth-configuration)


Customized observability configuration
:
    [Create an instance that's configured for Ops Agent monitoring and logging](https://docs.cloud.google.com/compute/docs/instances/create-vm-ops-agent-monitoring-logging)
:
    [Enable virtual displays on an instance](https://docs.cloud.google.com/compute/docs/instances/enable-instance-virtual-display)


Customized security configuration
:
    [Create an instance that uses a user-managed service account](https://docs.cloud.google.com/compute/docs/access/create-enable-service-accounts-for-instances)
:
    [Create VMs with managed workload identities enabled](https://docs.cloud.google.com/compute/docs/access/authenticate-workloads-over-mtls#create-workload-id-vms)
:
    [Enable OS Login during VM creation](https://docs.cloud.google.com/compute/docs/oslogin/set-up-oslogin#enable_os_login_during_vm_creation)


Configured for disaster recovery
:
    [Create an instance with a Backup and DR backup plan](https://docs.cloud.google.com/compute/docs/instances/create-instance-with-gcbdr-backup-plan)


From a backup
:
    [Create an instance from a machine image](https://docs.cloud.google.com/compute/docs/machine-images/create-instance-from-machine-image)
:
    [Create an instance from a disk snapshot](https://docs.cloud.google.com/compute/docs/disks/restore-snapshot)
:
    [Restore an instance from a backup vault](https://docs.cloud.google.com/backup-disaster-recovery/docs/cloud-console/compute/compute-instance-restore)


From existing configurations
:
    [Create an instance from an instance template](https://docs.cloud.google.com/compute/docs/instances/create-vm-from-instance-template)
:
    [Create an instance similar to an existing instance](https://docs.cloud.google.com/compute/docs/instances/create-vm-from-similar-instance)


Configured for specific workloads
:
    [Create an instance to deploy a container](https://docs.cloud.google.com/compute/docs/containers/deploying-containers#deploying_a_container_on_a_new_vm_instance)
:
    [Create Windows Server instances](https://docs.cloud.google.com/compute/docs/instances/windows/creating-managing-windows-instances)
:
    [Create SQL Server instances](https://docs.cloud.google.com/compute/docs/instances/sql-server/creating-sql-server-instances)
:
    [Create an instance with a high performance computing (HPC) image](https://docs.cloud.google.com/compute/docs/instances/create-hpc-vm)


Customized provisioning type
:
    [Create a Spot instance](https://docs.cloud.google.com/compute/docs/instances/create-use-spot)
:
    [Create instances that consume reserved instances](https://docs.cloud.google.com/compute/docs/instances/reservations-consume)


Multiple instances at once
:
    [Create a managed instance group (MIG)](https://docs.cloud.google.com/compute/docs/instance-groups/creating-groups-of-managed-instances#basic_scenarios_for_creating_a_mig)
:
    [Create instances in bulk](https://docs.cloud.google.com/compute/docs/instances/multiple/create-in-bulk)


Sole-tenant nodes
:
    [Create instances on sole-tenant nodes](https://docs.cloud.google.com/compute/docs/nodes/create-nodes)


Efficient instances
:
    [Create an instance with an attached instance schedule](https://docs.cloud.google.com/compute/docs/instances/schedule-instance-start-stop#attaching_to_a_new_VM)

## Troubleshooting

To find methods for resolving common instance creation errors, see [Troubleshooting instance creation](https://docs.cloud.google.com/compute/docs/troubleshooting/troubleshooting-vm-creation).

## What's next?

- Learn how to [check the status of an instance](https://docs.cloud.google.com/compute/docs/instances/instance-life-cycle) to see when it is ready to use.
- Learn how to [connect to your instance](https://docs.cloud.google.com/compute/docs/instances/connecting-to-instance).
- Learn how to [scale out your instance into a group of instances](https://docs.cloud.google.com/compute/docs/instance-groups/create-mig-from-vm).
- Learn how to [reserve capacity for your instances](https://docs.cloud.google.com/compute/docs/instances/choose-reservation-type).
- Learn how to save on instance costs through [committed use discounts](https://docs.cloud.google.com/compute/docs/instances/committed-use-discounts-overview) and [sustained use discounts](https://docs.cloud.google.com/compute/docs/sustained-use-discounts).

## 