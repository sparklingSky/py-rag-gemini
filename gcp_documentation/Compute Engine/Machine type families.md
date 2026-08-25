## General-purpose machine family for Compute Engine

This document describes the features of the Compute Engine general-purpose machine family, which has the best price-performance with the most flexible vCPU to memory ratios, and provides features that target most standard and cloud-native workloads.

The general-purpose machine family has predefined and [custom](https://docs.cloud.google.com/compute/docs/general-purpose-machines#custom_machine_types) machine types to align with your workload, depending on your requirements.

C4D is powered by the fifth generation AMD EPYC Turin processor and [Titanium](https://cloud.google.com/titanium). These machine types have up to 384 vCPUs and 3,024 GB of DDR5 memory, a max-boost frequency of 4.1 GHz, and up to 200 Gbps per VM Tier_1 networking performance. C4D also offers Local SSD (`-lssd`) machine types and bare metal (`-metal`) machine types.

C4A is powered by Google's Axion processor built on the Arm Neoverse V2 compute core. C4A provides `standard`, `highcpu`, and `highmem` machine types with up to 72 vCPUs, 576 GB DDR5 memory, 6 TiB of local Titanium SSD, and up to 100 Gbps with per VM Tier_1 networking performance. C4A also offers Local SSD (`-lssd`) machine types and a `highmem` bare metal (`-metal`) [(Preview)](https://docs.cloud.google.com/products#product-launch-stages) machine type with 96 vCPUs and 768 GB DDR5 memory.

C4 is powered by the sixth generation (code-named Granite Rapids) and fifth generation (code-named Emerald Rapids) Intel Xeon Scalable processors. C4 instances running on Granite Rapids offer a sustained, all-core turbo frequency of 3.9 GHz and a max turbo frequency of 4.2 GHz, 2.2 TB of DDR5 memory, 18 TiB of Titanium SSD for C4. supports up to 200 Gbps of per VM Tier_1 networking performance. C4 also offers Local SSD (`-lssd`) machine types and bare metal (`-metal`) machine types.

N4D is powered by the fifth generation AMD EPYC Turin processor and [Titanium](https://cloud.google.com/titanium). These machine types have up to 96 vCPUs and 768 GB of DDR5 memory, and a max-boost frequency of 4.1 GHz. N4D offers 50 Gbps of standard network bandwidth.

N4A is powered by Google's Axion processor built on the Arm Neoverse N3 compute core. N4A provides machine types of up to 64 vCPUs and 512 GB of DDR5 memory. N4A is available in standard, high-mem, high-cpu, and custom machine types with extended memory, and up to 50 Gbps of standard networking.

N4 is powered by the fifth generation Intel Xeon Scalable processor (code-named Emerald Rapids). N4 offers a sustained, all-core turbo frequency of 2.9 GHz, 640 GB of DDR5 memory, and up to 50 Gbps of standard network bandwidth.

C3 is powered by fourth generation Intel Xeon Scalable processors and offers a sustained, all-core turbo frequency of 3.0 GHz, 8 channels of DDR5 memory, and up to 200 Gbps per VM Tier_1 networking performance.

C3D is powered by fourth generation AMD EPYC Genoa processors and offers a sustained, all-core turbo frequency of 3.3 GHz, 2,880 GB of DDR5 memory, and up to 200 Gbps per VM Tier_1 networking performance.

For bare metal machine types, choose the C4, C4D, or C3 machine series.

All [third and fourth generation](https://docs.cloud.google.com/compute/docs/machine-resource#vm_terminology) general-purpose VMs support [Titanium](https://cloud.google.com/titanium).

E2, E2 shared-core, N2, N2D, Tau T2A, and Tau T2D are second generation machine series in this family; N1 and its related shared-core machine types are the first generation machine series.

| **Machine series** | **Workloads** |
| [N4](https://docs.cloud.google.com/compute/docs/general-purpose-machines#n4_series), [N4A](https://docs.cloud.google.com/compute/docs/general-purpose-machines#n4a_series), [N4D](https://docs.cloud.google.com/compute/docs/general-purpose-machines#n4d_series), [N2](https://docs.cloud.google.com/compute/docs/general-purpose-machines#n2_series), [N2D](https://docs.cloud.google.com/compute/docs/general-purpose-machines#n2d_machines), [N1](https://docs.cloud.google.com/compute/docs/general-purpose-machines#n1_machines) | - Medium traffic web and application servers - Containerized microservices - Business intelligence applications - Virtual desktops - CRM applications - Development and test environments - Batch processing - Storage and archive |
| [C4A](https://docs.cloud.google.com/compute/docs/general-purpose-machines#c4a_series), [C4](https://docs.cloud.google.com/compute/docs/general-purpose-machines#c4_series), [C4D](https://docs.cloud.google.com/compute/docs/general-purpose-machines#c4d_series), [C3](https://docs.cloud.google.com/compute/docs/general-purpose-machines#c3_series), [C3D](https://docs.cloud.google.com/compute/docs/general-purpose-machines#c3d_series) | - High traffic web, app and ad servers - Databases and caches - Game servers - Data analytics - Media streaming and transcoding - Network appliances - CPU-based ML training and inference |
| [E2](https://docs.cloud.google.com/compute/docs/general-purpose-machines#e2_machine_types) | - Low-traffic web servers - Back office apps - Containerized microservices - Small databases - Virtual desktops - Development and test environments |
| [Tau T2A](https://docs.cloud.google.com/compute/docs/general-purpose-machines#t2a_machines), [Tau T2D](https://docs.cloud.google.com/compute/docs/general-purpose-machines#t2d_machines) | - Scale-out workloads - Web servers - Containerized microservices - Media transcoding - Large-scale Java applications |
|---|---|

## C4D machine series

C4D VMs are powered by the fifth generation AMD EPYC Turin processor and [Titanium](https://cloud.google.com/titanium). C4D delivers a 30% performance boost over C3D on the estimated [SPECrate®2017_int_base benchmark](https://www.spec.org/cpu2017/), which lets you scale performance with fewer resources, thereby optimizing your costs.

C4D is designed to run workloads including web, app and game servers, AI inference, video streaming, and data centric applications like analytics, as well as relational and in-memory databases.

For databases, C4D delivers 55% more queries per second for MySQL and 35% higher operations per second for Memorystore for Redis workloads compared to C3D due to its higher core frequency (up to 4.1 GHz) and improved Instructions Per Clock (IPC).

> [!NOTE]
> **Note:** C4D doesn't support All Core Turbo Mode setting. C4D instances always run without frequency restrictions.

For web-serving workloads, AMD EPYC Turin's advancements in L3-cache efficiency and branch prediction enable up to 80% higher throughput per vCPU with C4D.

In summary, the C4D machine series has the following features:

- Powered by the AMD EPYC Turin CPU and Titanium.
- Supports up to 384 vCPUs and 3,024 GB of DDR5 memory.
- Supports up to 12 TiB of local Titanium SSD disks.
- Offers predefined machine types that range in size from 2 to 384 vCPUs.
- Supports up to 3,024 GB of DDR5 memory for VM instances and up to 3,072 GB of memory for bare metal instances.
- Supports consumption options like on-demand, Spot VMs, and future reservations.
- Supports standard network configuration with up to 100 Gbps bandwidth.
- Supports per VM Tier_1 networking performance with up to 200 Gbps bandwidth.
- Supports only Hyperdisk volumes.
- Supports [Confidential VM](https://docs.cloud.google.com/confidential-computing/confidential-vm/docs/confidential-vm-overview) with AMD SEV, excluding bare metal instances and configurations with more than 255 vCPUs.
- Supports [resource-based and flexible committed use discounts (CUDs)](https://docs.cloud.google.com/compute/docs/instances/committed-use-discounts-overview).
- Supports [compact and spread placement policies](https://docs.cloud.google.com/compute/docs/instances/placement-policies-overview).

### C4D machine types

C4D VMs are available as predefined configurations in `standard`, `highcpu`, and `highmem` sizes ranging from 2 vCPU to 384 vCPUs and up to 3,024 GB of memory.

To use Titanium SSD with C4D, create your instance using the `-lssd` variant of the C4D machine types. Selecting this machine type creates an instance of the specified size with Titanium SSD partitions attached. You can't attach Titanium SSD volumes separately.

To create a bare metal instance with C4D, use one of the following machine types:

- `c4d-standard-384-metal`
- `c4d-highcpu-384-metal`
- `c4d-highmem-384-metal`

### C4D standard

| Machine types | vCPUs^1^ | Memory (GB) | Titanium SSD | Default egress bandwidth (Gbps)^3^ | Tier_1 egress bandwidth (Gbps)^4^ |
|---|---|---|---|---|---|
| `c4d-standard-2` | 2 | 7 | No | Up to 10 | N/A |
| `c4d-standard-4` | 4 | 15 | No | Up to 20 | N/A |
| `c4d-standard-8` | 8 | 31 | No | Up to 20 | N/A |
| `c4d-standard-16` | 16 | 62 | No | Up to 20 | N/A |
| `c4d-standard-32` | 32 | 124 | No | Up to 23 | N/A |
| `c4d-standard-48` | 48 | 186 | No | Up to 34 | Up to 50 |
| `c4d-standard-64` | 64 | 248 | No | Up to 45 | Up to 75 |
| `c4d-standard-96` | 96 | 372 | No | Up to 67 | Up to 100 |
| `c4d-standard-192` | 192 | 744 | No | Up to 100 | Up to 150 |
| `c4d-standard-384` | 384 | 1,488 | No | Up to 100 | Up to 200 |
| `c4d-standard-384-metal`^2^ | 384 | 1,536 | No | Up to 100 | Up to 200 |

^1^ A CPU uses two threads per core, and a vCPU represents a single thread. See [CPU platforms](https://docs.cloud.google.com/compute/docs/cpu-platforms).   
^2^ For bare metal instances, the number of vCPUs is equivalent to the number of hardware threads on the host server.  
^3^ Default egress bandwidth can't exceed the number given. Actual egress bandwidth depends on the destination IP address and other factors. See [Network bandwidth](https://docs.cloud.google.com/compute/docs/network-bandwidth).  
^4^ Supports [high-bandwidth networking](https://docs.cloud.google.com/compute/docs/networking/configure-vm-with-high-bandwidth-configuration) for larger machine types.

### C4D highcpu

| Machine types | vCPUs^1^ | Memory (GB) | Titanium SSD | Default egress bandwidth (Gbps)^3^ | Tier_1 egress bandwidth (Gbps)^4^ |
|---|---|---|---|---|---|
| `c4d-highcpu-2` | 2 | 3 | No | Up to 10 | N/A |
| `c4d-highcpu-4` | 4 | 7 | No | Up to 20 | N/A |
| `c4d-highcpu-8` | 8 | 15 | No | Up to 20 | N/A |
| `c4d-highcpu-16` | 16 | 30 | No | Up to 20 | N/A |
| `c4d-highcpu-32` | 32 | 60 | No | Up to 23 | N/A |
| `c4d-highcpu-48` | 48 | 90 | No | Up to 34 | Up to 50 |
| `c4d-highcpu-64` | 64 | 120 | No | Up to 45 | Up to 75 |
| `c4d-highcpu-96` | 96 | 180 | No | Up to 67 | Up to 100 |
| `c4d-highcpu-192` | 192 | 360 | No | Up to 100 | Up to 150 |
| `c4d-highcpu-384` | 384 | 720 | No | Up to 100 | Up to 200 |
| `c4d-highcpu-384-metal`^2^ | 384 | 768 | No | Up to 100 | Up to 200 |

^1^ A CPU uses two threads per core, and a vCPU represents a single thread. See [CPU platforms](https://docs.cloud.google.com/compute/docs/cpu-platforms).   
^2^ For bare metal instances, the number of vCPUs is equivalent to the number of hardware threads on the host server.  
^3^ Default egress bandwidth can't exceed the number given. Actual egress bandwidth depends on the destination IP address and other factors. See [Network bandwidth](https://docs.cloud.google.com/compute/docs/network-bandwidth).  
^4^ Supports [high-bandwidth networking](https://docs.cloud.google.com/compute/docs/networking/configure-vm-with-high-bandwidth-configuration) for larger machine types.

### C4D highmem

| Machine types | vCPUs^1^ | Memory (GB) | Titanium SSD | Default egress bandwidth (Gbps)^3^ | Tier_1 egress bandwidth (Gbps)^4^ |
|---|---|---|---|---|---|
| `c4d-highmem-2` | 2 | 15 | No | Up to 10 | N/A |
| `c4d-highmem-4` | 4 | 31 | No | Up to 20 | N/A |
| `c4d-highmem-8` | 8 | 63 | No | Up to 20 | N/A |
| `c4d-highmem-16` | 16 | 126 | No | Up to 20 | N/A |
| `c4d-highmem-32` | 32 | 252 | No | Up to 23 | N/A |
| `c4d-highmem-48` | 48 | 378 | No | Up to 34 | Up to 50 |
| `c4d-highmem-64` | 64 | 504 | No | Up to 45 | Up to 75 |
| `c4d-highmem-96` | 96 | 756 | No | Up to 67 | Up to 100 |
| `c4d-highmem-192` | 192 | 1,512 | No | Up to 100 | Up to 150 |
| `c4d-highmem-384` | 384 | 3,024 | No | Up to 100 | Up to 200 |
| `c4d-highmem-384-metal`^2^ | 384 | 3,072 | No | Up to 100 | Up to 200 |

^1^ A CPU uses two threads per core, and a vCPU represents a single thread. See [CPU platforms](https://docs.cloud.google.com/compute/docs/cpu-platforms).   
^2^ For bare metal instances, the number of vCPUs is equivalent to the number of hardware threads on the host server.  
^3^ Default egress bandwidth can't exceed the number given. Actual egress bandwidth depends on the destination IP address and other factors. See [Network bandwidth](https://docs.cloud.google.com/compute/docs/network-bandwidth).  
^4^ Supports [high-bandwidth networking](https://docs.cloud.google.com/compute/docs/networking/configure-vm-with-high-bandwidth-configuration) for larger machine types.

### C4D standard

| Machine types | vCPUs^1^ | Memory (GB) | Titanium SSD | Default egress bandwidth (Gbps)^3^ | Tier_1 egress bandwidth (Gbps)^4^ |
|---|---|---|---|---|---|
| `c4d-standard-8-lssd` | 8 | 31 | (1 x 375 GiB) 375 GiB | Up to 20 | N/A |
| `c4d-standard-16-lssd` | 16 | 62 | (1 x 375 GiB) 375 GiB | Up to 20 | N/A |
| `c4d-standard-32-lssd` | 32 | 124 | (2 x 375 GiB) 750 GiB | Up to 23 | N/A |
| `c4d-standard-48-lssd` | 48 | 186 | (4 x 375 GiB) 1,500 GiB | Up to 34 | Up to 50 |
| `c4d-standard-64-lssd` | 64 | 248 | (6 x 375 GiB) 2,250 GiB | Up to 45 | Up to 75 |
| `c4d-standard-96-lssd` | 96 | 372 | (8 x 375 GiB) 3,000 GiB | Up to 67 | Up to 100 |
| `c4d-standard-192-lssd` | 192 | 744 | (16 x 375 GiB) 6,000 GiB | Up to 100 | Up to 150 |
| `c4d-standard-384-lssd` | 384 | 1,488 | (32 x 375 GiB) 12,000 GiB | Up to 100 | Up to 200 |

^1^ A CPU uses two threads per core, and a vCPU represents a single thread. See [CPU platforms](https://docs.cloud.google.com/compute/docs/cpu-platforms).   
^2^ For bare metal instances, the number of vCPUs is equivalent to the number of hardware threads on the host server.  
^3^ Default egress bandwidth can't exceed the number given. Actual egress bandwidth depends on the destination IP address and other factors. See [Network bandwidth](https://docs.cloud.google.com/compute/docs/network-bandwidth).  
^4^ Supports [high-bandwidth networking](https://docs.cloud.google.com/compute/docs/networking/configure-vm-with-high-bandwidth-configuration) for larger machine types.

### C4D highmem

| Machine types | vCPUs^1^ | Memory (GB) | Titanium SSD | Default egress bandwidth (Gbps)^3^ | Tier_1 egress bandwidth (Gbps)^4^ |
|---|---|---|---|---|---|
| `c4d-highmem-8-lssd` | 8 | 63 | (1 x 375 GiB) 375 GiB | Up to 20 | N/A |
| `c4d-highmem-16-lssd` | 16 | 126 | (1 x 375 GiB) 375 GiB | Up to 20 | N/A |
| `c4d-highmem-32-lssd` | 32 | 252 | (2 x 375 GiB) 750 GiB | Up to 23 | N/A |
| `c4d-highmem-48-lssd` | 48 | 378 | (4 x 375 GiB) 1,500 GiB | Up to 34 | Up to 50 |
| `c4d-highmem-64-lssd` | 64 | 504 | (6 x 375 GiB) 2,250 GiB | Up to 45 | Up to 75 |
| `c4d-highmem-96-lssd` | 96 | 756 | (8 x 375 GiB) 3,000 GiB | Up to 67 | Up to 100 |
| `c4d-highmem-192-lssd` | 192 | 1,512 | (16 x 375 GiB) 6,000 GiB | Up to 100 | Up to 150 |
| `c4d-highmem-384-lssd` | 384 | 3,024 | (32 x 375 GiB) 12,000 GiB | Up to 100 | Up to 200 |

^1^ A CPU uses two threads per core, and a vCPU represents a single thread. See [CPU platforms](https://docs.cloud.google.com/compute/docs/cpu-platforms).   
^2^ For bare metal instances, the number of vCPUs is equivalent to the number of hardware threads on the host server.  
^3^ Default egress bandwidth can't exceed the number given. Actual egress bandwidth depends on the destination IP address and other factors. See [Network bandwidth](https://docs.cloud.google.com/compute/docs/network-bandwidth).  
^4^ Supports [high-bandwidth networking](https://docs.cloud.google.com/compute/docs/networking/configure-vm-with-high-bandwidth-configuration) for larger machine types.

C4D doesn't support custom machine types.

### Regional availability for C4D instances

For C4D VMs, you can view the available regions and zones in the [Available regions and zones](https://docs.cloud.google.com/compute/docs/regions-zones#available) table, as follows:

- To view all the zones where you can create a C4D VM, in the **Select a machine series** menu, select `C4D`.
- You can also use the **Select a location** menu to limit the results to a geographical area.

For regional availability of C4D bare metal instances, see [Bare metal instances on Compute Engine](https://docs.cloud.google.com/compute/docs/instances/bare-metal-instances#c4d-metal).

### Supported disk types for C4D

C4D VMs support only the NVMe disk interface and can use the following [Hyperdisk](https://docs.cloud.google.com/compute/docs/disks/hyperdisks) block storage:

- Hyperdisk Balanced (`hyperdisk-balanced`)
- Hyperdisk Extreme (`hyperdisk-extreme`)
- [Local Titanium SSD](https://docs.cloud.google.com/compute/docs/disks/local-ssd#local_ssd_types) (added automatically with `-lssd` machine types)

C4D doesn't support Persistent Disk.

#### Disk and capacity limits

<br />

You can attach a mixture of different Hyperdisk types to an instance, but the maximum total disk capacity (in TiB) across all disk types can't exceed:

- For machine types with less than 32 vCPUs: 257 TiB for all Hyperdisk

- For machine types with 32 or more vCPUs: 512 TiB for all Hyperdisk

For details about the capacity limits, see [Hyperdisk size and attachment limits](https://docs.cloud.google.com/compute/docs/disks/hyperdisk-perf-limits#limits-instance).

<br />

<br />

C4D storage limits are described in the following table:

### C4D standard

|   | Maximum number of disks ||||   |
| Machine types | Hyperdisk per VM | Hyperdisk Balanced | Hyperdisk Throughput | Hyperdisk ML | Hyperdisk Extreme |
|---|---|---|---|---|---|
| `c4d-standard-2` | 4 | 4 | 0 | 0 | 0 |
| `c4d-standard-4` | 8 | 8 | 0 | 0 | 0 |
| `c4d-standard-8` | 16 | 16 | 0 | 0 | 0 |
| `c4d-standard-16` | 32 | 32 | 0 | 0 | 0 |
| `c4d-standard-32` | 32 | 32 | 0 | 0 | 0 |
| `c4d-standard-48` | 32 | 32 | 0 | 0 | 0 |
| `c4d-standard-64` | 32 | 32 | 0 | 0 | 8 |
| `c4d-standard-96` | 32 | 32 | 0 | 0 | 8 |
| `c4d-standard-192` | 64 | 64 | 0 | 0 | 8 |
| `c4d-standard-384` | 128 | 128 | 0 | 0 | 8 |
| `c4d-standard-384-metal` | 32 | 32 | 0 | 0 | 8 |

### C4D highcpu

|   | Maximum number of disks ||||   |
| Machine types | Hyperdisk per VM | Hyperdisk Balanced | Hyperdisk Throughput | Hyperdisk ML | Hyperdisk Extreme |
|---|---|---|---|---|---|
| `c4d-highcpu-2` | 4 | 4 | 0 | 0 | 0 |
| `c4d-highcpu-4` | 8 | 8 | 0 | 0 | 0 |
| `c4d-highcpu-8` | 16 | 16 | 0 | 0 | 0 |
| `c4d-highcpu-16` | 32 | 32 | 0 | 0 | 0 |
| `c4d-highcpu-32` | 32 | 32 | 0 | 0 | 0 |
| `c4d-highcpu-48` | 32 | 32 | 0 | 0 | 0 |
| `c4d-highcpu-64` | 32 | 32 | 0 | 0 | 8 |
| `c4d-highcpu-96` | 32 | 32 | 0 | 0 | 8 |
| `c4d-highcpu-192` | 64 | 64 | 0 | 0 | 8 |
| `c4d-highcpu-384` | 128 | 128 | 0 | 0 | 8 |
| `c4d-highcpu-384-metal` | 32 | 32 | 0 | 0 | 8 |

### C4D highmem

|   | Maximum number of disks ||||   |
| Machine types | Hyperdisk per VM | Hyperdisk Balanced | Hyperdisk Throughput | Hyperdisk ML | Hyperdisk Extreme |
|---|---|---|---|---|---|
| `c4d-highmem-2` | 4 | 4 | 0 | 0 | 0 |
| `c4d-highmem-4` | 8 | 8 | 0 | 0 | 0 |
| `c4d-highmem-8` | 16 | 16 | 0 | 0 | 0 |
| `c4d-highmem-16` | 32 | 32 | 0 | 0 | 0 |
| `c4d-highmem-32` | 32 | 32 | 0 | 0 | 0 |
| `c4d-highmem-48` | 32 | 32 | 0 | 0 | 0 |
| `c4d-highmem-64` | 32 | 32 | 0 | 0 | 8 |
| `c4d-highmem-96` | 32 | 32 | 0 | 0 | 8 |
| `c4d-highmem-192` | 64 | 64 | 0 | 0 | 8 |
| `c4d-highmem-384` | 128 | 128 | 0 | 0 | 8 |
| `c4d-highmem-384-metal` | 32 | 32 | 0 | 0 | 8 |

### C4D standard

|   | Maximum number of disks ||||   |
| Machine types | Hyperdisk per VM | Hyperdisk Balanced | Hyperdisk Throughput | Hyperdisk ML | Hyperdisk Extreme |
|---|---|---|---|---|---|
| `c4d-standard-8-lssd` | 16 | 16 | 0 | 0 | 0 |
| `c4d-standard-16-lssd` | 32 | 32 | 0 | 0 | 0 |
| `c4d-standard-32-lssd` | 32 | 32 | 0 | 0 | 0 |
| `c4d-standard-48-lssd` | 32 | 32 | 0 | 0 | 0 |
| `c4d-standard-64-lssd` | 32 | 32 | 0 | 0 | 8 |
| `c4d-standard-96-lssd` | 32 | 32 | 0 | 0 | 8 |
| `c4d-standard-192-lssd` | 64 | 64 | 0 | 0 | 8 |
| `c4d-standard-384-lssd` | 128 | 128 | 0 | 0 | 8 |

### C4D highmem

|   | Maximum number of disks ||||   |
| Machine types | Hyperdisk per VM | Hyperdisk Balanced | Hyperdisk Throughput | Hyperdisk ML | Hyperdisk Extreme |
|---|---|---|---|---|---|
| `c4d-highmem-8-lssd` | 16 | 16 | 0 | 0 | 0 |
| `c4d-highmem-16-lssd` | 32 | 32 | 0 | 0 | 0 |
| `c4d-highmem-32-lssd` | 32 | 32 | 0 | 0 | 0 |
| `c4d-highmem-48-lssd` | 32 | 32 | 0 | 0 | 0 |
| `c4d-highmem-64-lssd` | 32 | 32 | 0 | 0 | 8 |
| `c4d-highmem-96-lssd` | 32 | 32 | 0 | 0 | 8 |
| `c4d-highmem-192-lssd` | 64 | 64 | 0 | 0 | 8 |
| `c4d-highmem-384-lssd` | 128 | 128 | 0 | 0 | 8 |

### Network support for C4D instances

The following network interface drivers are required:

- C4D VM instances require [gVNIC](https://docs.cloud.google.com/compute/docs/networking/using-gvnic).
- C4D bare metal instances require the [Intel IDPF LAN PF device driver](https://docs.cloud.google.com/compute/docs/networking/using-idpf).

C4D supports up to 100 Gbps network bandwidth for standard networking and up to 200 Gbps with per VM Tier_1 networking performance for VM and bare metal instances.

Before migrating to C4D or creating C4D VMs or bare metal instances, make sure that the [operating system image](https://docs.cloud.google.com/compute/docs/images/os-details#networking) that you use supports the IDPF network driver for bare metal instances or the gVNIC driver for VM instances. To get the best possible performance on C4D VMs, choose an OS image that supports both "Tier_1 Networking" and "200 Gbps network bandwidth". These images include an updated gVNIC driver, even if the guest OS shows the `gve` driver version as 1.0.0. If your C4D VM is using an operating system with an older version of gVNIC driver, this is still supported but the VM might experience suboptimal performance such as less network bandwidth or higher latency.

If you use a custom OS image to create a C4D VM, you can [manually install the most recent gVNIC driver](https://docs.cloud.google.com/compute/docs/networking/using-gvnic#manual-gvnic-setup). The gVNIC driver version v1.4.2 or later is recommended for use with C4D VMs. Google recommends using the latest gVNIC driver version to benefit from additional features and bug fixes.

### Maintenance experience for C4D instances

During the lifespan of a virtual machine (VM) instance, the host machine that your instance runs undergoes multiple host events. A host event can include the regular maintenance of Compute Engine infrastructure, or in rare cases, a host error. Compute Engine also applies some non-disruptive lightweight upgrades for the hypervisor and network in the background.

The C4D machine series offers the following features related to host maintenance:

| Machine type | Typical scheduled maintenance event frequency | [Maintenance behavior](https://docs.cloud.google.com/compute/docs/instances/host-maintenance-overview#maintenance_behaviors) | [Advanced notification](https://docs.cloud.google.com/compute/docs/instances/monitor-plan-host-maintenance-event) | [On-demand maintenance](https://docs.cloud.google.com/compute/docs/instances/trigger-host-maintenance-event) | [Simulate maintenance](https://docs.cloud.google.com/compute/docs/instances/simulating-host-maintenance) |
|---|---|---|---|---|---|
| `c4d-*-lssd` | Minimum of 30 days | Live migrate | 7 days | Yes | Yes |
| `c4d-*-384` | Minimum of 30 days | Live migrate | 7 days | Yes | Yes |
| All others | Minimum of 30 days | Live migrate | 7 days | No | Yes |

The maintenance frequencies shown in the previous table are approximations, not guarantees. Compute Engine might occasionally perform maintenance more frequently.

## C4A machine series

C4A VMs are powered by Google's first Arm Axion™ processor. C4A provides machine types with up to 72 vCPUs and 576 GB of DDR5 memory, and 6 TiB of local [Titanium SSD](https://docs.cloud.google.com/compute/docs/disks/local-ssd#local_ssd_types). C4A is available in `standard`, `highmem`, and `highcpu` machine types. It also offers`-lssd` variants for Titanium SSD and a `highmem` bare metal ([Preview](https://cloud.google.com/products#product-launch-stages)) machine type with 96 vCPUs and 768 GB of DDR5 memory. C4A uses Google Cloud's latest generation of Google Cloud Hyperdisk storage options and Titanium SSD. C4A offers up to 50 Gbps of standard network performance, and up to 100 Gbps per VM Tier_1 networking performance for your instances.

C4A VMs are placed within a single node with [Uniform Memory Access (UMA)](https://wikipedia.org/wiki/Uniform_memory_access) and also support sole tenant nodes to deliver consistent performance.

In summary, the C4A machine series has the following features:

- Is powered by the Google Axion CPU and Titanium.
- Supports multiple predefined machine types with up to 72 vCPUs and 576 GB of DDR5 memory.
- Supports up to 6 TiB of local Titanium SSD disks.
- Supports `highmem` bare metal instances with 96 vCPUs and 768 GB of DDR5 memory.
- Supports standard network configuration with up to 50 Gbps bandwidth.
- Supports per VM Tier_1 networking performance with up to 100 Gbps bandwidth.
- Supports Hyperdisk only.
- Supports the following discount and consumption options:
  - [Resource-based and flexible committed use discounts (CUDs)](https://docs.cloud.google.com/compute/docs/instances/committed-use-discounts-overview)
  - [Spot VMs](https://docs.cloud.google.com/compute/docs/instances/spot)
  - [Reservations](https://docs.cloud.google.com/compute/docs/instances/choose-reservation-type)
- Supports the [performance monitoring unit (PMU)](https://docs.cloud.google.com/compute/docs/pmu-overview).
- Doesn't support [compact placement policies](https://docs.cloud.google.com/compute/docs/instances/placement-policies-overview).
- Doesn't support [suspend](https://docs.cloud.google.com/compute/docs/instances/suspend-resume-instance#suspend-instance-local-ssd) with C4A instances that have attached Titanium SSD disks.

For information about migrating to Arm VMs, read the [Arm on Compute](https://docs.cloud.google.com/compute/docs/instances/arm-on-compute) document.

### C4A machine types

> [!NOTE]
> **Note:** Community supported Arm OSes might be supported. If the OS isn't listed on the [Operating system details](https://docs.cloud.google.com/compute/docs/images/os-details#networking) page, test the OS to learn if it is supported.

C4A VMs are available as predefined configurations in sizes ranging from 1 vCPU to 72 vCPUs and up to 576 GB of memory.

- `standard`: 4 GB memory per vCPU
- `highcpu`: 2 GB memory per vCPU
- `highmem`: 8 GB memory per vCPU

To use Titanium SSD with C4A, create your VM using the `-lssd` variant of the C4A machine types. Selecting this machine type creates a VM of the specified size with Titanium SSD partitions attached. You can't attach Titanium SSD volumes separately.

You can create a bare metal instance with a `c4a-highmem-96-metal` machine type.

### C4A standard

| Machine types | vCPUs^1^ | Memory (GB) | Titanium SSD | Default egress bandwidth (Gbps)^2^ | Tier_1 egress bandwidth (Gbps)^3^ |
|---|---|---|---|---|---|
| `c4a-standard-1` | 1 | 4 | No | Up to 10 | N/A |
| `c4a-standard-2` | 2 | 8 | No | Up to 10 | N/A |
| `c4a-standard-4` | 4 | 16 | No | Up to 23 | N/A |
| `c4a-standard-8` | 8 | 32 | No | Up to 23 | N/A |
| `c4a-standard-16` | 16 | 64 | No | Up to 23 | N/A |
| `c4a-standard-32` | 32 | 128 | No | Up to 23 | Up to 50 |
| `c4a-standard-48` | 48 | 192 | No | Up to 34 | Up to 50 |
| `c4a-standard-64` | 64 | 256 | No | Up to 45 | Up to 75 |
| `c4a-standard-72` | 72 | 288 | No | Up to 50 | Up to 100 |

^1^ SMT is not supported. Each vCPU is equivalent to an entire core. See [CPU platforms](https://docs.cloud.google.com/compute/docs/cpu-platforms).  
^2^ Maximum egress bandwidth cannot exceed the number given. Actual egress bandwidth depends on the destination IP address and other factors. See [Network bandwidth](https://docs.cloud.google.com/compute/docs/network-bandwidth).  
^3^ Supports [high-bandwidth networking](https://docs.cloud.google.com/compute/docs/networking/configure-vm-with-high-bandwidth-configuration) for larger machine types.

<br />

### C4A highcpu

| Machine types | vCPUs^1^ | Memory (GB) | Titanium SSD | Default egress bandwidth (Gbps)^2^ | Tier_1 egress bandwidth (Gbps)^3^ |
|---|---|---|---|---|---|
| `c4a-highcpu-1` | 1 | 2 | No | Up to 10 | N/A |
| `c4a-highcpu-2` | 2 | 4 | No | Up to 10 | N/A |
| `c4a-highcpu-4` | 4 | 8 | No | Up to 23 | N/A |
| `c4a-highcpu-8` | 8 | 16 | No | Up to 23 | N/A |
| `c4a-highcpu-16` | 16 | 32 | No | Up to 23 | N/A |
| `c4a-highcpu-32` | 32 | 64 | No | Up to 23 | Up to 50 |
| `c4a-highcpu-48` | 48 | 96 | No | Up to 34 | Up to 50 |
| `c4a-highcpu-64` | 64 | 128 | No | Up to 45 | Up to 75 |
| `c4a-highcpu-72` | 72 | 144 | No | Up to 50 | Up to 100 |

^1^ SMT is not supported. Each vCPU is equivalent to an entire core. See [CPU platforms](https://docs.cloud.google.com/compute/docs/cpu-platforms).  
^2^ Maximum egress bandwidth cannot exceed the number given. Actual egress bandwidth depends on the destination IP address and other factors. See [Network bandwidth](https://docs.cloud.google.com/compute/docs/network-bandwidth).  
^3^ Supports [high-bandwidth networking](https://docs.cloud.google.com/compute/docs/networking/configure-vm-with-high-bandwidth-configuration) for larger machine types.

<br />

### C4A highmem

| Machine types | vCPUs^1^ | Memory (GB) | Titanium SSD | Default egress bandwidth (Gbps)^2^ | Tier_1 egress bandwidth (Gbps)^3^ |
|---|---|---|---|---|---|
| `c4a-highmem-1` | 1 | 8 | No | Up to 10 | N/A |
| `c4a-highmem-2` | 2 | 16 | No | Up to 10 | N/A |
| `c4a-highmem-4` | 4 | 32 | No | Up to 23 | N/A |
| `c4a-highmem-8` | 8 | 64 | No | Up to 23 | N/A |
| `c4a-highmem-16` | 16 | 128 | No | Up to 23 | N/A |
| `c4a-highmem-32` | 32 | 256 | No | Up to 23 | Up to 50 |
| `c4a-highmem-48` | 48 | 384 | No | Up to 34 | Up to 50 |
| `c4a-highmem-64` | 64 | 512 | No | Up to 45 | Up to 75 |
| `c4a-highmem-72` | 72 | 576 | No | Up to 50 | Up to 100 |
| `c4a-highmem-96-metal` ([Preview](https://cloud.google.com/products#product-launch-stages)) | 96 | 768 | No | Up to 50 | Up to 100 |

^1^ SMT is not supported. Each vCPU is equivalent to an entire core. See [CPU platforms](https://docs.cloud.google.com/compute/docs/cpu-platforms).  
^2^ Maximum egress bandwidth cannot exceed the number given. Actual egress bandwidth depends on the destination IP address and other factors. See [Network bandwidth](https://docs.cloud.google.com/compute/docs/network-bandwidth).  
^3^ Supports [high-bandwidth networking](https://docs.cloud.google.com/compute/docs/networking/configure-vm-with-high-bandwidth-configuration) for larger machine types.

<br />

### C4A standard

| Machine types | vCPUs^1^ | Memory (GB) | Titanium SSD | Default egress bandwidth (Gbps)^2^ | Tier_1 egress bandwidth (Gbps)^3^ |
|---|---|---|---|---|---|
| `c4a-standard-4-lssd` | 4 | 16 | (1 x 375 GiB) 375 GiB | Up to 23 | N/A |
| `c4a-standard-8-lssd` | 8 | 32 | (2 x 375 GiB) 750 GiB | Up to 23 | N/A |
| `c4a-standard-16-lssd` | 16 | 64 | (4 x 375 GiB) 1,500 GiB | Up to 23 | N/A |
| `c4a-standard-32-lssd` | 32 | 128 | (6 x 375 GiB) 2,250 GiB | Up to 23 | Up to 50 |
| `c4a-standard-48-lssd` | 48 | 192 | (10 x 375 GiB) 3,750 GiB | Up to 34 | Up to 50 |
| `c4a-standard-64-lssd` | 64 | 256 | (14 x 375 GiB) 5,250 GiB | Up to 45 | Up to 75 |
| `c4a-standard-72-lssd` | 72 | 288 | (16 x 375 GiB) 6,000 GiB | Up to 50 | Up to 100 |

^1^ SMT is not supported. Each vCPU is equivalent to an entire core. See [CPU platforms](https://docs.cloud.google.com/compute/docs/cpu-platforms).  
^2^ Maximum egress bandwidth cannot exceed the number given. Actual egress bandwidth depends on the destination IP address and other factors. See [Network bandwidth](https://docs.cloud.google.com/compute/docs/network-bandwidth).  
^3^ Supports [high-bandwidth networking](https://docs.cloud.google.com/compute/docs/networking/configure-vm-with-high-bandwidth-configuration) for larger machine types.

<br />

### C4A highmem

| Machine types | vCPUs^\*^ | Memory (GB) | Titanium SSD | Default egress bandwidth (Gbps)^‡^ | Tier_1 egress bandwidth (Gbps)^#^ |
|---|---|---|---|---|---|
| `c4a-highmem-4-lssd` | 4 | 32 | (1 x 375 GiB) 375 GiB | Up to 23 | N/A |
| `c4a-highmem-8-lssd` | 8 | 64 | (2 x 375 GiB) 750 GiB | Up to 23 | N/A |
| `c4a-highmem-16-lssd` | 16 | 128 | (4 x 375 GiB) 1,500 GiB | Up to 23 | N/A |
| `c4a-highmem-32-lssd` | 32 | 256 | (6 x 375 GiB) 2,250 GiB | Up to 23 | Up to 50 |
| `c4a-highmem-48-lssd` | 48 | 384 | (10 x 375 GiB) 3,750 GiB | Up to 34 | Up to 50 |
| `c4a-highmem-64-lssd` | 64 | 512 | (14 x 375 GiB) 5,250 GiB | Up to 45 | Up to 75 |
| `c4a-highmem-72-lssd` | 72 | 576 | (16 x 375 GiB) 6,000 GiB | Up to 50 | Up to 100 |

^1^ SMT is not supported. Each vCPU is equivalent to an entire core. See [CPU platforms](https://docs.cloud.google.com/compute/docs/cpu-platforms).  
^2^ Maximum egress bandwidth cannot exceed the number given. Actual egress bandwidth depends on the destination IP address and other factors. See [Network bandwidth](https://docs.cloud.google.com/compute/docs/network-bandwidth).  
^3^ Supports [high-bandwidth networking](https://docs.cloud.google.com/compute/docs/networking/configure-vm-with-high-bandwidth-configuration) for larger machine types.

<br />

C4A doesn't support custom machine types.

### Supported disk types for C4A

C4A VMs support only the NVMe disk interface and can use the following [Hyperdisk](https://docs.cloud.google.com/compute/docs/disks/hyperdisks) block storage:

### VM instances

- Hyperdisk Balanced (`hyperdisk-balanced`)
- Hyperdisk Balanced High Availability (`hyperdisk-balanced-high-availability`)
- Hyperdisk Throughput (`hyperdisk-throughput`)
- Hyperdisk Extreme (`hyperdisk-extreme`)
- Hyperdisk ML (`hyperdisk-ML`)
- [Local Titanium SSD](https://docs.cloud.google.com/compute/docs/disks/local-ssd#local_ssd_types) (only available with `-lssd` machine types)

### Bare metal instances

- Hyperdisk Balanced (`hyperdisk-balanced`)
- Hyperdisk Extreme (`hyperdisk-extreme`)
- Hyperdisk ML (`hyperdisk-ML`)

C4A doesn't support Persistent Disk.

#### Disk and capacity limits

<br />

You can attach a mixture of different Hyperdisk types to an instance, but the maximum total disk capacity (in TiB) across all disk types can't exceed:

- For machine types with less than 32 vCPUs: 257 TiB for all Hyperdisk

- For machine types with 32 or more vCPUs: 512 TiB for all Hyperdisk

For details about the capacity limits, see [Hyperdisk size and attachment limits](https://docs.cloud.google.com/compute/docs/disks/hyperdisk-perf-limits#limits-instance).

<br />

<br />

### C4A standard

| Maximum number of disks |||||||
| Machine types | Hyperdisk per VM | Hyperdisk Balanced | Hyperdisk Balanced High Availability | Hyperdisk Throughput | Hyperdisk Extreme | Hyperdisk ML |
|---|---|---|---|---|---|---|
| `c4a-standard-1` | 16 | 16 | 16 | 16 | 0 | 16 |
| `c4a-standard-2` | 16 | 16 | 16 | 16 | 0 | 16 |
| `c4a-standard-4` | 16 | 16 | 16 | 16 | 0 | 16 |
| `c4a-standard-8` | 16 | 16 | 16 | 16 | 0 | 16 |
| `c4a-standard-16` | 32 | 32 | 32 | 32 | 0 | 32 |
| `c4a-standard-32` | 32 | 32 | 32 | 32 | 0 | 32 |
| `c4a-standard-48` | 32 | 32 | 32 | 32 | 0 | 32 |
| `c4a-standard-64` | 64 | 64 | 64 | 64 | 8 | 64 |
| `c4a-standard-72` | 64 | 64 | 64 | 64 | 8 | 64 |

### C4A highcpu

| Maximum number of disks |||||||
| Machine types | Hyperdisk per VM | Hyperdisk Balanced | Hyperdisk Balanced High Availability | Hyperdisk Throughput | Hyperdisk Extreme | Hyperdisk ML |
|---|---|---|---|---|---|---|
| `c4a-highcpu-1` | 16 | 16 | 16 | 16 | 0 | 16 |
| `c4a-highcpu-2` | 16 | 16 | 16 | 16 | 0 | 16 |
| `c4a-highcpu-4` | 16 | 16 | 16 | 16 | 0 | 16 |
| `c4a-highcpu-8` | 16 | 16 | 16 | 16 | 0 | 16 |
| `c4a-highcpu-16` | 32 | 32 | 32 | 32 | 0 | 32 |
| `c4a-highcpu-32` | 32 | 32 | 32 | 32 | 0 | 32 |
| `c4a-highcpu-48` | 32 | 32 | 32 | 32 | 0 | 32 |
| `c4a-highcpu-64` | 64 | 64 | 64 | 64 | 8 | 64 |
| `c4a-highcpu-72` | 64 | 64 | 64 | 64 | 8 | 64 |

### C4A highmem

| Maximum number of disks |||||||
| Machine types | Hyperdisk per VM | Hyperdisk Balanced | Hyperdisk Balanced High Availability | Hyperdisk Throughput | Hyperdisk Extreme | Hyperdisk ML |
|---|---|---|---|---|---|---|
| `c4a-highmem-1` | 16 | 8 | 16 | 16 | 0 | 16 |
| `c4a-highmem-2` | 16 | 8 | 16 | 16 | 0 | 16 |
| `c4a-highmem-4` | 16 | 16 | 16 | 16 | 0 | 16 |
| `c4a-highmem-8` | 16 | 16 | 16 | 16 | 0 | 16 |
| `c4a-highmem-16` | 32 | 32 | 32 | 32 | 0 | 32 |
| `c4a-highmem-32` | 32 | 32 | 32 | 32 | 0 | 32 |
| `c4a-highmem-48` | 32 | 32 | 32 | 32 | 0 | 32 |
| `c4a-highmem-64` | 64 | 64 | 64 | 64 | 8 | 64 |
| `c4a-highmem-72` | 64 | 64 | 64 | 64 | 8 | 64 |
| `c4a-highmem-96-metal` ([Preview](https://cloud.google.com/products#product-launch-stages)) | 32 | 32 | Not supported | Not supported | 8 | 32 |

### C4A standard

| Maximum number of disks |||||||
| Machine types | Hyperdisk per VM | Hyperdisk Balanced | Hyperdisk Balanced High Availability | Hyperdisk Throughput | Hyperdisk Extreme | Hyperdisk ML |
|---|---|---|---|---|---|---|
| `c4a-standard-4-lssd` | 16 | 16 | 16 | 16 | 0 | 16 |
| `c4a-standard-8-lssd` | 16 | 16 | 16 | 16 | 0 | 16 |
| `c4a-standard-16-lssd` | 32 | 32 | 32 | 32 | 0 | 32 |
| `c4a-standard-32-lssd` | 32 | 32 | 32 | 32 | 0 | 32 |
| `c4a-standard-48-lssd` | 32 | 32 | 32 | 32 | 0 | 32 |
| `c4a-standard-64-lssd` | 64 | 64 | 64 | 64 | 8 | 64 |
| `c4a-standard-72-lssd` | 64 | 64 | 64 | 64 | 8 | 64 |

### C4A highmem

| Maximum number of disks |||||||
| Machine types | Hyperdisk per VM | Hyperdisk Balanced | Hyperdisk Balanced High Availability | Hyperdisk Throughput | Hyperdisk Extreme | Hyperdisk ML |
|---|---|---|---|---|---|---|
| `c4a-highmem-4-lssd` | 16 | 16 | 16 | 16 | 0 | 16 |
| `c4a-highmem-8-lssd` | 16 | 16 | 16 | 16 | 0 | 16 |
| `c4a-highmem-16-lssd` | 32 | 32 | 32 | 32 | 0 | 32 |
| `c4a-highmem-32-lssd` | 32 | 32 | 32 | 32 | 0 | 32 |
| `c4a-highmem-48-lssd` | 32 | 32 | 32 | 32 | 0 | 32 |
| `c4a-highmem-64-lssd` | 64 | 64 | 64 | 64 | 8 | 64 |
| `c4a-highmem-72-lssd` | 64 | 64 | 64 | 64 | 8 | 64 |

### Network support for C4A instances

The following network interface drivers are required:

- C4A VM instances require [gVNIC network interfaces](https://docs.cloud.google.com/compute/docs/networking/using-gvnic).
- C4A bare metal instances require the [Intel IDPF LAN PF device driver](https://docs.cloud.google.com/compute/docs/networking/using-idpf).

C4A supports up to 100 Gbps network bandwidth for standard networking and bare metal instances.

Before migrating to C4A or creating C4A VMs or bare metal instances, make sure that the [operating system image](https://docs.cloud.google.com/compute/docs/images/os-details#networking) that you use supports the IDPF network driver for bare metal instances or the gVNIC driver for VM instances. To get the best possible performance on C4A VMs, choose an OS image that supports both "Tier_1 Networking" and "100 Gbps network bandwidth". These images include an updated gVNIC driver, even if the guest OS shows the `gve` driver version as 1.0.0. If your C4A VM is using an operating system with an older version of gVNIC driver, this is still supported but the VM might experience suboptimal performance such as less network bandwidth or higher latency.

If you use a custom OS image to create a C4A VM, you can [manually install the most recent gVNIC driver](https://docs.cloud.google.com/compute/docs/networking/using-gvnic#manual-gvnic-setup). The gVNIC driver version v1.4.2 or later is recommended for use with C4A VMs. Google recommends using the latest gVNIC driver version to benefit from additional features and bug fixes.

### Maintenance experience for C4A instances

During the lifespan of a virtual machine (VM) instance, the host machine that your instance runs undergoes multiple host events. A host event can include the regular maintenance of Compute Engine infrastructure, or in rare cases, a host error. Compute Engine also applies some non-disruptive lightweight upgrades for the hypervisor and network in the background.

The C4A machine series offers the following features related to host maintenance:

| Machine type | Typical scheduled maintenance event frequency | [Maintenance behavior](https://docs.cloud.google.com/compute/docs/instances/host-maintenance-overview#maintenance_behaviors) | [Advanced notification](https://docs.cloud.google.com/compute/docs/instances/monitor-plan-host-maintenance-event) | [On-demand maintenance](https://docs.cloud.google.com/compute/docs/instances/trigger-host-maintenance-event) |
|---|---|---|---|---|
| `c4a-*-lssd` | Minimum of 30 days | Live migrate | 7 days | Yes |
| `c4a-*-metal` ([Preview](https://cloud.google.com/products#product-launch-stages)) | Minimum of 30 days | Terminate | 7 days | Yes |
| All others | Minimum of 30 days | Live migrate | 7 days | No |

The maintenance frequencies shown in the previous table are approximations, not guarantees. Compute Engine might occasionally perform maintenance more frequently.

## C4 machine series

C4 VMs are powered by 6th generation (code-named Granite Rapids) or 5th generation (code-named Emerald Rapids) Intel Xeon Scalable processors and [Titanium](https://cloud.google.com/titanium). C4 Local SSD (`-lssd`) and bare metal (`-metal`) instances, as well as instances with 144 or 288 vCPUs, use the 6th generation Intel Granite Rapids processor. All other instances use the 5th generation Intel Emerald Rapids processor.

The C4 machine series is designed to deliver price-performance and enterprise-grade reliability along with a maintenance experience for your most demanding workloads. C4 instances are ideal for web and app serving, game servers, databases and caches, video streaming, data analytics, network appliances, and CPU-based ML inference.

C4 VMs are designed to achieve maximum performance from single-core turbo boosting. For more consistent vCPU performance, disable vCPU boosting and limit the vCPUs to the sustainable all-core turbo frequency. You can do this by setting `turboMode=ALL_CORE_MAX` in the [AdvancedMachineFeatures](https://docs.cloud.google.com/compute/docs/reference/rest/v1/instances/insert) settings.

In summary, the C4 machine series:

- Is powered by the 6th generation Intel Granite Rapids or 5th generation Intel Emerald Rapids processor and Titanium IPU.
- Lets you switch between core-boosting performance and steady all-core turbo performance for your vCPUs.
- Supports up to 288 vCPUs and 2.2 TB of DDR5 memory.
- Supports up to 18 TiB of local Titanium SSD disks.
- Supports compact and spread placement policies.
- Offers multiple predefined machine types.
- Supports standard network configuration with up to 100 Gbps bandwidth.
- Supports per VM Tier_1 networking performance with up to 200 Gbps bandwidth.
- Supports [Intel Advanced Matrix Extensions (AMX)](https://docs.cloud.google.com/compute/docs/cpu-platforms#intel-amx), a built-in accelerator that significantly improves the performance of deep-learning training and inference on the CPU.
- Supports the following discount and consumption options:
  - [Resource-based and flexible committed use discounts (CUDs)](https://docs.cloud.google.com/compute/docs/instances/committed-use-discounts-overview)
  - [Spot VMs](https://docs.cloud.google.com/compute/docs/instances/spot)
  - [Reservations](https://docs.cloud.google.com/compute/docs/instances/choose-reservation-type)
- Supports the [performance monitoring unit (PMU)](https://docs.cloud.google.com/compute/docs/pmu-overview).
- Supports up to 192 vCPUs for [Confidential VM](https://docs.cloud.google.com/confidential-computing/confidential-vm/docs/confidential-vm-overview) with Intel TDX ([Preview](https://cloud.google.com/products/#product-launch-stages)).

### C4 Limitations

- You can't dynamically add or remove a disk when using Windows Server 25.
- You can't dynamically add or remove multiple disks when using Windows Server 25 or Windows 11.
- C4 VM shapes powered by Granite Rapids might experience lower networking performance on Windows 11 and Debian 11 [OS images](https://docs.cloud.google.com/compute/docs/images).

### C4 machine types

C4 VMs are available as predefined configurations in sizes ranging from 2 vCPUs to 288 vCPUs and up to 2,232 GB of memory.

- `standard`: 3.75 GB memory per vCPU
- `highcpu`: 2 GB memory per vCPU
- `highmem`: 7.75 GB memory per vCPU

To use Titanium SSD with C4, create your instance using the `-lssd` variant of the C4 machine types. Selecting this machine type creates an instance of the specified size with Titanium SSD partitions attached. You can't attach Titanium SSD volumes separately.

To create a bare metal instance with C4, use one of the following machine types:

- `c4-standard-288-metal`
- `c4-standard-288-lssd-metal`
- `c4-highmem-288-metal`
- `c4-highmem-288-lssd-metal`

### C4 standard

| Machine types | vCPUs^1^ | Memory (GB) | Titanium SSD | Default egress bandwidth (Gbps)^2^ | Tier_1 egress bandwidth (Gbps)^3^ |
|---|---|---|---|---|---|
| `c4-standard-2` | 2 | 7 | No | Up to 10 | N/A |
| `c4-standard-4` | 4 | 15 | No | Up to 23 | N/A |
| `c4-standard-8` | 8 | 30 | No | Up to 23 | N/A |
| `c4-standard-16` | 16 | 60 | No | Up to 23 | N/A |
| `c4-standard-24` | 24 | 90 | No | Up to 23 | N/A |
| `c4-standard-32` | 32 | 120 | No | Up to 23 | N/A |
| `c4-standard-48` | 48 | 180 | No | Up to 34 | Up to 50 |
| `c4-standard-96` | 96 | 360 | No | Up to 67 | Up to 100 |
| `c4-standard-144` | 144 | 540 | No | Up to 100 | Up to 150 |
| `c4-standard-192` | 192 | 720 | No | Up to 100 | Up to 200 |
| `c4-standard-288` | 288 | 1,080 | No | Up to 100 | Up to 200 |
| `c4-standard-288-metal` | 288 | 1,080 | No | Up to 100 | Up to 200 |

^1^ A CPU uses two threads per core, and a vCPU represents a single thread. See [CPU platforms](https://docs.cloud.google.com/compute/docs/cpu-platforms).  
^2^ Default egress bandwidth can't exceed the number given. Actual egress bandwidth depends on the destination IP address and other factors. See [Network bandwidth](https://docs.cloud.google.com/compute/docs/network-bandwidth).  
^3^ Supports [high-bandwidth networking](https://docs.cloud.google.com/compute/docs/networking/configure-vm-with-high-bandwidth-configuration) for larger machine types.

### C4 highcpu

| Machine types | vCPUs^1^ | Memory (GB) | Titanium SSD | Default egress bandwidth (Gbps)^2^ | Tier_1 egress bandwidth (Gbps)^3^ |
|---|---|---|---|---|---|
| `c4-highcpu-2` | 2 | 4 | No | Up to 10 | N/A |
| `c4-highcpu-4` | 4 | 8 | No | Up to 23 | N/A |
| `c4-highcpu-8` | 8 | 16 | No | Up to 23 | N/A |
| `c4-highcpu-16` | 16 | 32 | No | Up to 23 | N/A |
| `c4-highcpu-24` | 24 | 48 | No | Up to 23 | N/A |
| `c4-highcpu-32` | 32 | 64 | No | Up to 23 | N/A |
| `c4-highcpu-48` | 48 | 96 | No | Up to 34 | Up to 50 |
| `c4-highcpu-96` | 96 | 192 | No | Up to 67 | Up to 100 |
| `c4-highcpu-144` | 144 | 288 | No | Up to 100 | Up to 150 |
| `c4-highcpu-192` | 192 | 384 | No | Up to 100 | Up to 200 |
| `c4-highcpu-288` | 288 | 576 | No | Up to 100 | Up to 200 |

^1^ A CPU uses two threads per core, and a vCPU represents a single thread. See [CPU platforms](https://docs.cloud.google.com/compute/docs/cpu-platforms).  
^2^ Default egress bandwidth can't exceed the number given. Actual egress bandwidth depends on the destination IP address and other factors. See [Network bandwidth](https://docs.cloud.google.com/compute/docs/network-bandwidth).  
^3^ Supports [high-bandwidth networking](https://docs.cloud.google.com/compute/docs/networking/configure-vm-with-high-bandwidth-configuration) for larger machine types.

### C4 highmem

| Machine types | vCPUs^1^ | Memory (GB) | Titanium SSD | Default egress bandwidth (Gbps)^2^ | Tier_1 egress bandwidth (Gbps)^3^ |
|---|---|---|---|---|---|
| `c4-highmem-2` | 2 | 15 | No | Up to 10 | N/A |
| `c4-highmem-4` | 4 | 31 | No | Up to 23 | N/A |
| `c4-highmem-8` | 8 | 62 | No | Up to 23 | N/A |
| `c4-highmem-16` | 16 | 124 | No | Up to 23 | N/A |
| `c4-highmem-24` | 24 | 186 | No | Up to 23 | N/A |
| `c4-highmem-32` | 32 | 248 | No | Up to 23 | N/A |
| `c4-highmem-48` | 48 | 372 | No | Up to 34 | Up to 50 |
| `c4-highmem-96` | 96 | 744 | No | Up to 67 | Up to 100 |
| `c4-highmem-144` | 144 | 1,116 | No | Up to 100 | Up to 150 |
| `c4-highmem-192` | 192 | 1,488 | No | Up to 100 | Up to 200 |
| `c4-highmem-288` | 288 | 2,232 | No | Up to 100 | Up to 200 |
| `c4-highmem-288-metal` | 288 | 2,232 | No | Up to 100 | Up to 200 |

^1^ A CPU uses two threads per core, and a vCPU represents a single thread. See [CPU platforms](https://docs.cloud.google.com/compute/docs/cpu-platforms).  
^2^ Default egress bandwidth can't exceed the number given. Actual egress bandwidth depends on the destination IP address and other factors. See [Network bandwidth](https://docs.cloud.google.com/compute/docs/network-bandwidth).  
^3^ Supports [high-bandwidth networking](https://docs.cloud.google.com/compute/docs/networking/configure-vm-with-high-bandwidth-configuration) for larger machine types.

### C4 standard

| Machine types | vCPUs^1^ | Memory (GB) | Titanium SSD | Default egress bandwidth (Gbps)^2^ | Tier_1 egress bandwidth (Gbps)^3^ |
|---|---|---|---|---|---|
| `c4-standard-4-lssd` | 4 | 15 | (1 x 375 GiB) 375 GiB | Up to 23 | N/A |
| `c4-standard-8-lssd` | 8 | 30 | (1 x 375 GiB) 375 GiB | Up to 23 | N/A |
| `c4-standard-16-lssd` | 16 | 60 | (2 x 375 GiB) 750 GiB | Up to 23 | N/A |
| `c4-standard-24-lssd` | 24 | 90 | (4 x 375 GiB) 1,500 GiB | Up to 23 | N/A |
| `c4-standard-32-lssd` | 32 | 120 | (5 x 375 GiB) 1,875 GiB | Up to 23 | N/A |
| `c4-standard-48-lssd` | 48 | 180 | (8 x 375 GiB) 3,000 GiB | Up to 34 | N/A |
| `c4-standard-96-lssd` | 96 | 360 | (16 x 375 GiB) 6,000 GiB | Up to 67 | N/A |
| `c4-standard-144-lssd` | 144 | 540 | (24 x 375 GiB) 9,000 GiB | Up to 100 | N/A |
| `c4-standard-192-lssd` | 192 | 720 | (32 x 375 GiB) 12,000 GiB | Up to 100 | N/A |
| `c4-standard-288-lssd` | 288 | 1,080 | (48 x 375 GiB) 18,000 GiB | Up to 100 | Up to 200 |
| `c4-standard-288-lssd-metal` | 288 | 1,080 | (48 x 375 GiB) 18,000 GiB | Up to 100 | Up to 200 |

^1^ A CPU uses two threads per core, and a vCPU represents a single thread. See [CPU platforms](https://docs.cloud.google.com/compute/docs/cpu-platforms).  
^2^ Default egress bandwidth can't exceed the number given. Actual egress bandwidth depends on the destination IP address and other factors. See [Network bandwidth](https://docs.cloud.google.com/compute/docs/network-bandwidth).  
^3^ Supports [high-bandwidth networking](https://docs.cloud.google.com/compute/docs/networking/configure-vm-with-high-bandwidth-configuration) for larger machine types.

### C4 highmem

| Machine types | vCPUs^1^ | Memory (GB) | Titanium SSD | Default egress bandwidth (Gbps)^2^ | Tier_1 egress bandwidth (Gbps)^3^ |
|---|---|---|---|---|---|
| `c4-highmem-4-lssd` | 4 | 31 | (1 x 375 GiB) 375 GiB | Up to 23 | N/A |
| `c4-highmem-8-lssd` | 8 | 62 | (1 x 375 GiB) 375 GiB | Up to 23 | N/A |
| `c4-highmem-16-lssd` | 16 | 124 | (2 x 375 GiB) 750 GiB | Up to 23 | N/A |
| `c4-highmem-24-lssd` | 24 | 186 | (4 x 375 GiB) 1,500 GiB | Up to 23 | N/A |
| `c4-highmem-32-lssd` | 32 | 248 | (5 x 375 GiB) 1,875 GiB | Up to 23 | N/A |
| `c4-highmem-48-lssd` | 48 | 372 | (8 x 375 GiB) 3,000 GiB | Up to 34 | N/A |
| `c4-highmem-96-lssd` | 96 | 744 | (16 x 375 GiB) 6,000 GiB | Up to 67 | N/A |
| `c4-highmem-144-lssd` | 144 | 1,116 | (24 x 375 GiB) 9,000 GiB | Up to 100 | N/A |
| `c4-highmem-192-lssd` | 192 | 1,488 | (32 x 375 GiB) 12,000 GiB | Up to 100 | N/A |
| `c4-highmem-288-lssd` | 288 | 2,232 | (48 x 375 GiB) 18,000 GiB | Up to 100 | Up to 200 |
| `c4-highmem-288-lssd-metal` | 288 | 2,232 | (48 x 375 GiB) 18,000 GiB | Up to 100 | Up to 200 |

^1^ A CPU uses two threads per core, and a vCPU represents a single thread. See [CPU platforms](https://docs.cloud.google.com/compute/docs/cpu-platforms).  
^2^ Default egress bandwidth can't exceed the number given. Actual egress bandwidth depends on the destination IP address and other factors. See [Network bandwidth](https://docs.cloud.google.com/compute/docs/network-bandwidth).  
^3^ Supports [high-bandwidth networking](https://docs.cloud.google.com/compute/docs/networking/configure-vm-with-high-bandwidth-configuration) for larger machine types.

C4 doesn't support custom machine types.

### Supported disk types for C4

C4 VMs support only the NVMe disk interface and can use the following [Hyperdisk](https://docs.cloud.google.com/compute/docs/disks/hyperdisks) block storage:

### VM instances

- Hyperdisk Balanced (`hyperdisk-balanced`)
- Hyperdisk Balanced High Availability (`hyperdisk-balanced-high-availability`)
- Hyperdisk Throughput (`hyperdisk-throughput`)
- Hyperdisk Extreme (`hyperdisk-extreme`)
- Local SSD (only available with `-lssd` machine types)

### Bare metal instances

- Hyperdisk Balanced (`hyperdisk-balanced`)
- Hyperdisk Extreme (`hyperdisk-extreme`)
- Local SSD (only available with `-lssd-metal` machine types)

C4 doesn't support Persistent Disk. When upgrading to a newer machine series, to migrate your Persistent Disk resources to Hyperdisk, see [Move your workload from an existing VM to a new VM](https://docs.cloud.google.com/compute/docs/import/migrate-to-new-vm).

#### Disk and capacity limits

<br />

You can attach a mixture of different Hyperdisk types to an instance, but the maximum total disk capacity (in TiB) across all disk types can't exceed:

- For machine types with less than 32 vCPUs: 257 TiB for all Hyperdisk

- For machine types with 32 or more vCPUs: 512 TiB for all Hyperdisk

For details about the capacity limits, see [Hyperdisk size and attachment limits](https://docs.cloud.google.com/compute/docs/disks/hyperdisk-perf-limits#limits-instance).

<br />

<br />

### C4 standard

|   | Maximum number of disks ||||   |
| Machine types | Hyperdisk per VM | Hyperdisk Balanced | Hyperdisk Balanced High Availability | Hyperdisk Throughput | Hyperdisk Extreme |
|---|---|---|---|---|---|
| `c4-standard-2` | 8 | 8 | 8 | 8 | 0 |
| `c4-standard-4` | 16 | 16 | 16 | 16 | 0 |
| `c4-standard-8` | 32 | 32 | 32 | 32 | 0 |
| `c4-standard-16` | 32 | 32 | 32 | 32 | 0 |
| `c4-standard-24` | 32 | 32 | 32 | 32 | 0 |
| `c4-standard-32` | 64 | 64 | 32 | 64 | 0 |
| `c4-standard-48` | 64 | 64 | 32 | 64 | 0 |
| `c4-standard-96` | 128 | 128 | 64 | 128 | 8 |
| `c4-standard-144` | 128 | 128 | 64 | 128 | 8 |
| `c4-standard-192` | 128 | 128 | 128 | 128 | 8 |
| `c4-standard-288` | 128 | 128 | 128 | 128 | 8 |
| `c4-standard-288-metal` | 32 | 32 | Not supported | Not supported | 8 |

### C4 highcpu

|   | Maximum number of disks ||||   |
| Machine types | Hyperdisk per VM | Hyperdisk Balanced | Hyperdisk Balanced High Availability | Hyperdisk Throughput | Hyperdisk Extreme |
|---|---|---|---|---|---|
| `c4-highcpu-2` | 8 | 8 | 8 | 8 | 0 |
| `c4-highcpu-4` | 16 | 16 | 16 | 16 | 0 |
| `c4-highcpu-8` | 32 | 32 | 32 | 32 | 0 |
| `c4-highcpu-16` | 32 | 32 | 32 | 32 | 0 |
| `c4-highcpu-24` | 32 | 32 | 32 | 32 | 0 |
| `c4-highcpu-32` | 64 | 64 | 32 | 64 | 0 |
| `c4-highcpu-48` | 64 | 64 | 32 | 64 | 0 |
| `c4-highcpu-96` | 128 | 128 | 64 | 128 | 8 |
| `c4-highcpu-144` | 128 | 128 | 64 | 128 | 8 |
| `c4-highcpu-192` | 128 | 128 | 128 | 128 | 8 |
| `c4-highcpu-288` | 128 | 128 | 128 | 128 | 8 |

### C4 highmem

|   | Maximum number of disks ||||   |
| Machine types | Hyperdisk per VM | Hyperdisk Balanced | Hyperdisk Balanced High Availability | Hyperdisk Throughput | Hyperdisk Extreme |
|---|---|---|---|---|---|
| `c4-highmem-2` | 8 | 8 | 8 | 8 | 0 |
| `c4-highmem-4` | 16 | 16 | 16 | 16 | 0 |
| `c4-highmem-8` | 32 | 32 | 32 | 32 | 0 |
| `c4-highmem-16` | 32 | 32 | 32 | 32 | 0 |
| `c4-highmem-24` | 32 | 32 | 32 | 32 | 0 |
| `c4-highmem-32` | 64 | 64 | 32 | 64 | 0 |
| `c4-highmem-48` | 64 | 64 | 32 | 64 | 0 |
| `c4-highmem-96` | 128 | 128 | 64 | 128 | 8 |
| `c4-highmem-144` | 128 | 128 | 64 | 128 | 8 |
| `c4-highmem-192` | 128 | 128 | 128 | 128 | 8 |
| `c4-highmem-288` | 128 | 128 | 128 | 128 | 8 |
| `c4-highmem-288-metal` | 32 | 32 | Not supported | Not supported | 8 |

### C4 standard

|   | Maximum number of disks ||||   |
| Machine types | Hyperdisk per VM | Hyperdisk Balanced | Hyperdisk Balanced High Availability | Hyperdisk Throughput | Hyperdisk Extreme |
|---|---|---|---|---|---|
| `c4-standard-4-lssd` | 16 | 16 | 16 | 16 | 0 |
| `c4-standard-8-lssd` | 32 | 32 | 32 | 32 | 0 |
| `c4-standard-16-lssd` | 32 | 32 | 32 | 32 | 0 |
| `c4-standard-24-lssd` | 32 | 32 | 32 | 32 | 0 |
| `c4-standard-32-lssd` | 32 | 32 | 32 | 32 | 0 |
| `c4-standard-48-lssd` | 32 | 32 | 32 | 32 | 0 |
| `c4-standard-96-lssd` | 64 | 64 | 64 | 64 | 8 |
| `c4-standard-144-lssd` | 64 | 64 | 64 | 64 | 8 |
| `c4-standard-192-lssd` | 128 | 128 | 128 | 128 | 8 |
| `c4-standard-288-lssd` | 128 | 128 | 128 | 128 | 8 |
| `c4-standard-288-lssd-metal` | 32 | 32 | Not supported | Not supported | 8 |

### C4 highmem

|   | Maximum number of disks ||||   |
| Machine types | Hyperdisk per VM | Hyperdisk Balanced | Hyperdisk Balanced High Availability | Hyperdisk Throughput | Hyperdisk Extreme |
|---|---|---|---|---|---|
| `c4-highmem-4-lssd` | 16 | 16 | 16 | 16 | 0 |
| `c4-highmem-8-lssd` | 32 | 32 | 32 | 32 | 0 |
| `c4-highmem-16-lssd` | 32 | 32 | 32 | 32 | 0 |
| `c4-highmem-24-lssd` | 32 | 32 | 32 | 32 | 0 |
| `c4-highmem-32-lssd` | 32 | 32 | 32 | 32 | 0 |
| `c4-highmem-48-lssd` | 32 | 32 | 32 | 32 | 0 |
| `c4-highmem-96-lssd` | 64 | 64 | 64 | 64 | 8 |
| `c4-highmem-144-lssd` | 64 | 64 | 64 | 64 | 8 |
| `c4-highmem-192-lssd` | 128 | 128 | 128 | 128 | 8 |
| `c4-highmem-288-lssd` | 128 | 128 | 128 | 128 | 8 |
| `c4-highmem-288-lssd-metal` | 32 | 32 | Not supported | Not supported | 8 |

### Network support for C4 VMs

The following network interface drivers are required:

- C4 VM instances require [gVNIC](https://docs.cloud.google.com/compute/docs/networking/using-gvnic).
- C4 bare metal instances require the [Intel IDPF LAN PF device driver](https://docs.cloud.google.com/compute/docs/networking/using-idpf).

C4 supports up to 100 Gbps network bandwidth for standard networking and up to 200 Gbps with per VM Tier_1 networking performance for VM and bare metal instances.

Before migrating to C4 or creating C4 VMs or bare metal instances, make sure that the [operating system image](https://docs.cloud.google.com/compute/docs/images/os-details#networking) that you use supports the IDPF network driver for bare metal instances or the gVNIC driver for VM instances. To get the best possible performance on C4 VMs, choose an OS image that supports both "Tier_1 Networking" and "200 Gbps network bandwidth". These images include an updated gVNIC driver, even if the guest OS shows the `gve` driver version as 1.0.0. If your C4 VM is using an operating system with an older version of gVNIC driver, this is still supported but the VM might experience suboptimal performance such as less network bandwidth or higher latency.

If you use a custom OS image to create a C4 VM, you can [manually install the most recent gVNIC driver](https://docs.cloud.google.com/compute/docs/networking/using-gvnic#manual-gvnic-setup). The gVNIC driver version v1.4.2 or later is recommended for use with C4 VMs. Google recommends using the latest gVNIC driver version to benefit from additional features and bug fixes.

### Maintenance experience for C4 instances

During the [lifecycle of a Compute Engine instance](https://docs.cloud.google.com/compute/docs/instances/instance-lifecycle), the host machine that your instance runs on undergoes multiple *host events*. A host event can include the regular maintenance of Compute Engine infrastructure, or in rare cases, a host error. Compute Engine also applies some non-disruptive lightweight upgrades for the hypervisor and network in the background.

The C4 machine series offers the following features related to host maintenance:

| Machine type | Typical scheduled maintenance event frequency | [Maintenance behavior](https://docs.cloud.google.com/compute/docs/instances/host-maintenance-overview#maintenance_behaviors) | [Advanced notification](https://docs.cloud.google.com/compute/docs/instances/monitor-plan-host-maintenance-event) | [On-demand maintenance](https://docs.cloud.google.com/compute/docs/instances/trigger-host-maintenance-event) |
|---|---|---|---|---|
| `c4-*-192` and `c4-*-288` | Minimum of 30 days | Live migrate | 7 days | Yes |
| `c4-*-lssd` | Minimum of 30 days | Live migrate | 7 days | Yes |
| `c4-*-288-metal` | Minimum of 30 days | Terminate | 7 days | Yes |
| `c4-*-288-lssd-metal` | Minimum of 30 days | Terminate | 7 days | Yes |
| All others | Minimum of 30 days | Live migrate | 7 days | No |

The maintenance frequencies shown in the previous table are approximations, not guarantees. Compute Engine might occasionally perform maintenance more frequently.

## N4D machine series

N4D VMs are powered by the fifth generation AMD EPYC processors (code-name Turin) and [Titanium](https://docs.cloud.google.com/titanium). N4D VMs are engineered for flexibility, cost optimization, and enhanced price-performance through their efficient architecture. N4D supports next generation dynamic resource management, making better use of resources on host machines.

In summary, the N4D machine series:

- Powered by the AMD EPYC Turin CPU and Titanium.
- Supports up to 96 vCPUs and 768 GB of DDR5 memory.
- Offers predefined machine types that range in size from 2 to 96 vCPUs.
- Supports custom machine types and extended memory.
- Supports consumption options like on-demand, Spot VMs, and future reservations.
- Supports standard network configuration with up to 50 Gbps bandwidth.
- Supports only Hyperdisk volumes.
- Supports resource-based and flexible committed use discounts [(CUDs)](https://docs.cloud.google.com/compute/docs/instances/committed-use-discounts-overview).
- Supports [spread placement policies](https://docs.cloud.google.com/compute/docs/instances/placement-policies-overview#about-spread-policies).
- Doesn't support Local SSD or per per VM Tier_1 networking performance.

### N4D machine types

N4D VMs are available as predefined configurations in sizes ranging from 2 vCPUs to 96 vCPUs and up to 768 GB of memory.

- `standard`: 4 GB memory per vCPU
- `highcpu`: 2 GB memory per vCPU
- `highmem`: 8 GB memory per vCPU

### N4D standard

| Machine types | vCPUs^1^ | Memory (GB) | Local SSD | Default egress bandwidth (Gbps) | Tier_1 egress bandwidth (Gbps) |
|---|---|---|---|---|---|
| `n4d-standard-2` | 2 | 8 | Not supported | Up to 10 | N/A |
| `n4d-standard-4` | 4 | 16 | Not supported | Up to 10 | N/A |
| `n4d-standard-8` | 8 | 32 | Not supported | Up to 16 | N/A |
| `n4d-standard-16` | 16 | 64 | Not supported | Up to 32 | N/A |
| `n4d-standard-32` | 32 | 128 | Not supported | Up to 32 | N/A |
| `n4d-standard-48` | 48 | 192 | Not supported | Up to 32 | N/A |
| `n4d-standard-64` | 64 | 256 | Not supported | Up to 45 | N/A |
| `n4d-standard-80` | 80 | 320 | Not supported | Up to 50 | N/A |
| `n4d-standard-96` | 96 | 384 | Not supported | Up to 50 | N/A |

^1^ A CPU uses two threads per core, and a vCPU represents a single thread. See [CPU platforms](https://docs.cloud.google.com/compute/docs/cpu-platforms)
.

### N4D highcpu

| Machine types | vCPUs^1^ | Memory (GB) | Local SSD | Default egress bandwidth (Gbps) | Tier_1 egress bandwidth (Gbps) |
|---|---|---|---|---|---|
| `n4d-highcpu-2` | 2 | 4 | Not supported | Up to 10 | N/A |
| `n4d-highcpu-4` | 4 | 8 | Not supported | Up to 10 | N/A |
| `n4d-highcpu-8` | 8 | 16 | Not supported | Up to 16 | N/A |
| `n4d-highcpu-16` | 16 | 32 | Not supported | Up to 32 | N/A |
| `n4d-highcpu-32` | 32 | 64 | Not supported | Up to 32 | N/A |
| `n4d-highcpu-48` | 48 | 90 | Not supported | Up to 32 | N/A |
| `n4d-highcpu-64` | 64 | 128 | Not supported | Up to 45 | N/A |
| `n4d-highcpu-80` | 80 | 160 | Not supported | Up to 50 | N/A |
| `n4d-highcpu-96` | 96 | 192 | Not supported | Up to 50 | N/A |

^1^ A CPU uses two threads per core, and a vCPU represents a single thread. See [CPU platforms](https://docs.cloud.google.com/compute/docs/cpu-platforms)
.

### N4D highmem

| Machine types | vCPUs^1^ | Memory (GB) | Local SSD | Default egress bandwidth (Gbps) | Tier_1 egress bandwidth (Gbps) |
|---|---|---|---|---|---|
| `n4d-highmem-2` | 2 | 16 | Not supported | Up to 10 | N/A |
| `n4d-highmem-4` | 4 | 32 | Not supported | Up to 10 | N/A |
| `n4d-highmem-8` | 8 | 64 | Not supported | Up to 16 | N/A |
| `n4d-highmem-16` | 16 | 128 | Not supported | Up to 32 | N/A |
| `n4d-highmem-32` | 32 | 256 | Not supported | Up to 32 | N/A |
| `n4d-highmem-48` | 48 | 384 | Not supported | Up to 32 | N/A |
| `n4d-highmem-64` | 64 | 512 | Not supported | Up to 45 | N/A |
| `n4d-highmem-80` | 80 | 640 | Not supported | Up to 50 | N/A |
| `n4d-highmem-96` | 96 | 768 | Not supported | Up to 50 | N/A |

^1^ A CPU uses two threads per core, and a vCPU represents a single thread. See [CPU platforms](https://docs.cloud.google.com/compute/docs/cpu-platforms)
.

### Supported disk types for N4D

N4D VMs support only the NVMe disk interface and can use the following [Hyperdisk](https://docs.cloud.google.com/compute/docs/disks/hyperdisks) block storage:

- Hyperdisk Balanced (`hyperdisk-balanced`)
- Hyperdisk Balanced High Availability (`hyperdisk-balanced-high-availability`)
- Hyperdisk Throughput (`hyperdisk-throughput`)

N4D doesn't support Persistent Disk or Local SSD. Read [Move your workload from an existing VM to a new VM](https://docs.cloud.google.com/compute/docs/import/migrate-to-new-vm) to migrate your Persistent Disk resources to a newer machine series.

#### Disk and capacity limits

The number of Hyperdisk volumes of all types that you can attach to a VM can't exceed the limits stated in the *Max number of Hyperdisk volumes.* For details about these limits, see [Hyperdisk capacity](https://docs.cloud.google.com/compute/docs/disks/hyperdisk-perf-limits#hyperdisk-capacity).

<br />

For instances running Microsoft Windows and using the NVMe disk interface, the combined number of both Hyperdisk and Persistent Disk attached volumes can't exceed a total of 16 disks. See [Known issues](https://docs.cloud.google.com/compute/docs/troubleshooting/known-issues#windows-disk-attachment). Local SSD volumes are excluded from this issue.

<br />

N4D storage limits are described in the following table:

### N4D standard

|   | Maximum number of disks |||   |
| Machine types | Hyperdisk per VM | Hyperdisk Balanced | Hyperdisk Balanced High Availability | Hyperdisk Throughput |
|---|---|---|---|---|
| `n4d-standard-2` | 4 | 16 | 16 | 16 |
| `n4d-standard-4` | 8 | 16 | 16 | 16 |
| `n4d-standard-8` | 16 | 16 | 16 | 16 |
| `n4d-standard-16` | 32 | 32 | 32 | 32 |
| `n4d-standard-32` | 64 | 32 | 32 | 32 |
| `n4d-standard-48` | 64 | 32 | 32 | 32 |
| `n4d-standard-64` | 64 | 32 | 32 | 32 |
| `n4d-standard-80` | 64 | 32 | 32 | 32 |
| `n4d-standard-96` | 64 | 32 | 32 | 32 |

### N4D highcpu

|   | Maximum number of disks |||   |
| Machine types | Hyperdisk per VM | Hyperdisk Balanced | Hyperdisk Balanced High Availability | Hyperdisk Throughput |
|---|---|---|---|---|
| `n4d-highcpu-2` | 4 | 16 | 16 | 16 |
| `n4d-highcpu-4` | 8 | 16 | 16 | 16 |
| `n4d-highcpu-8` | 16 | 16 | 16 | 16 |
| `n4d-highcpu-16` | 32 | 32 | 32 | 32 |
| `n4d-highcpu-32` | 64 | 32 | 32 | 32 |
| `n4d-highcpu-48` | 64 | 32 | 32 | 32 |
| `n4d-highcpu-64` | 64 | 32 | 32 | 32 |
| `n4d-highcpu-80` | 64 | 32 | 32 | 32 |
| `n4d-highcpu-96` | 64 | 32 | 32 | 32 |

### N4D highmem

|   | Maximum number of disks |||   |
| Machine types | Hyperdisk per VM | Hyperdisk Balanced | Hyperdisk Balanced High Availability | Hyperdisk Throughput |
|---|---|---|---|---|
| `n4d-highmem-2` | 4 | 16 | 16 | 16 |
| `n4d-highmem-4` | 8 | 16 | 16 | 16 |
| `n4d-highmem-8` | 16 | 16 | 16 | 16 |
| `n4d-highmem-16` | 32 | 32 | 32 | 32 |
| `n4d-highmem-32` | 64 | 32 | 32 | 32 |
| `n4d-highmem-48` | 64 | 32 | 32 | 32 |
| `n4d-highmem-64` | 64 | 32 | 32 | 32 |
| `n4d-highmem-80` | 64 | 32 | 32 | 32 |
| `n4d-highmem-96` | 64 | 32 | 32 | 32 |

### Network support for N4D VMs

N4D instances require [gVNIC network interfaces](https://docs.cloud.google.com/compute/docs/networking/using-gvnic). N4D instances support up to 50 Gbps network bandwidth for standard networking and don't support per VM Tier_1 networking performance.

Before migrating to N4D or creating N4D VM instances, make sure that the [operating system image](https://docs.cloud.google.com/compute/docs/images/os-details#networking) that you use supports the gVNIC driver for VM instances. These images include an updated gVNIC driver, even if the guest OS shows the `gve` driver version as 1.0.0. If your N4D VM is using an operating system with an older version of gVNIC driver, this is still supported but the VM might experience suboptimal performance such as less network bandwidth or higher latency.

If you use a custom OS image to create a N4D VM, you can [manually install the most recent gVNIC driver](https://docs.cloud.google.com/compute/docs/networking/using-gvnic#manual-gvnic-setup). The gVNIC driver version v1.4.2 or later is recommended for use with N4D VMs. Google recommends using the latest gVNIC driver version to benefit from additional features and bug fixes.

### Maintenance experience for N4D instances

During the [lifecycle of a Compute Engine instance](https://docs.cloud.google.com/compute/docs/instances/instance-lifecycle), the host machine that your instance runs on undergoes multiple *host events*. A host event can include the regular maintenance of Compute Engine infrastructure, or in rare cases, a host error. Compute Engine also applies some non-disruptive lightweight upgrades for the hypervisor and network in the background.

The N4D machine series offers the following features related to host maintenance:

| Machine type | Typical scheduled maintenance event frequency | [Maintenance behavior](https://docs.cloud.google.com/compute/docs/instances/host-maintenance-overview#maintenance_behaviors) | [Advanced notification](https://docs.cloud.google.com/compute/docs/instances/monitor-plan-host-maintenance-event) | [On-demand maintenance](https://docs.cloud.google.com/compute/docs/instances/trigger-host-maintenance-event) |
|---|---|---|---|---|
| All N4D machine types | Variable | Live migrate | 60 seconds | No |

The maintenance frequencies shown in the previous table are approximations, not guarantees. Compute Engine might occasionally perform maintenance more frequently.

## N4A machine series

N4A VMs are the second family of VMs powered by Google's latest custom-designed Axion processor, built on Arm Neoverse N3 compute core and powered by [Titanium](https://cloud.google.com/titanium) IPU. N4A VMs are placed within a single node with [Uniform Memory Access (UMA)](https://wikipedia.org/wiki/Uniform_memory_access). They are engineered to be our most efficient and flexible Arm VMs, delivering exceptional price-performance for a wide range of general-purpose and scale-out workloads. N4A uses next generation [dynamic resource management](https://docs.cloud.google.com/compute/docs/dynamic-resource-management), which makes better use of resources on host machines.

Ideal use cases include web and application servers, microservices, containerized applications using Google Kubernetes Engine (GKE), open-source databases, and development and testing environments.

In summary, the N4A machine series:

- Is powered by the Google Axion Arm processor and Titanium IPU.
- Supports up to 64 vCPUs and 512 GB of DDR5 memory.
- Offers multiple predefined machine types and [custom machine types](https://docs.cloud.google.com/compute/docs/general-purpose-machines#custom_machine_types) with extended custom memory up to 512 GB.
- Supports standard network configuration with up to 50 Gbps of bandwidth.
- Supports Hyperdisk only.
- Supports the following discount and consumption options:
  - [Resource-based and flexible committed use discounts (CUDs)](https://docs.cloud.google.com/compute/docs/instances/committed-use-discounts-overview)
  - [Spot VMs](https://docs.cloud.google.com/compute/docs/instances/spot)
  - [Reservations](https://docs.cloud.google.com/compute/docs/instances/choose-reservation-type)
- Doesn't support Local SSD or per VM Tier_1 networking performance.
- Confidential VM is not supported by this CPU.
- 32-bit mode EL0 (guest userspace) is not supported due to a hardware limitation.

### N4A machine types

N4A VMs are available as predefined configurations in sizes ranging from 1 vCPUs to 64 vCPUs and up to 512 GB of memory.

- `standard`: 4 GB memory per vCPU
- `highcpu`: 2 GB memory per vCPU
- `highmem`: 8 GB memory per vCPU

For information about custom machine types, see [Custom machine types](https://docs.cloud.google.com/compute/docs/general-purpose-machines#custom_machine_types).

### N4A standard

| Machine types | vCPUs^1^ | Memory (GB) | Local SSD | Default egress bandwidth (Gbps)^2^ | Tier_1 egress bandwidth (Gbps) |
|---|---|---|---|---|---|
| `n4a-standard-1` | 1 | 4 | Not supported | Up to 10 | N/A |
| `n4a-standard-2` | 2 | 8 | Not supported | Up to 10 | N/A |
| `n4a-standard-4` | 4 | 16 | Not supported | Up to 10 | N/A |
| `n4a-standard-8` | 8 | 32 | Not supported | Up to 16 | N/A |
| `n4a-standard-16` | 16 | 64 | Not supported | Up to 32 | N/A |
| `n4a-standard-32` | 32 | 128 | Not supported | Up to 32 | N/A |
| `n4a-standard-48` | 48 | 192 | Not supported | Up to 32 | N/A |
| `n4a-standard-64` | 64 | 256 | Not supported | Up to 50 | N/A |

^1^ SMT is not supported. Each vCPU is equivalent to an entire core. See [CPU platforms](https://docs.cloud.google.com/compute/docs/cpu-platforms).  
^2^ Maximum egress bandwidth cannot exceed the number given. Actual egress bandwidth depends on the destination IP address and other factors. See [Network bandwidth](https://docs.cloud.google.com/compute/docs/network-bandwidth).  

<br />

### N4A highcpu

| Machine types | vCPUs^1^ | Memory (GB) | Local SSD | Default egress bandwidth (Gbps)^2^ | Tier_1 egress bandwidth (Gbps) |
|---|---|---|---|---|---|
| `n4a-highcpu-1` | 1 | 2 | Not supported | Up to 10 | N/A |
| `n4a-highcpu-2` | 2 | 4 | Not supported | Up to 10 | N/A |
| `n4a-highcpu-4` | 4 | 8 | Not supported | Up to 10 | N/A |
| `n4a-highcpu-8` | 8 | 16 | Not supported | Up to 16 | N/A |
| `n4a-highcpu-16` | 16 | 32 | Not supported | Up to 32 | N/A |
| `n4a-highcpu-32` | 32 | 64 | Not supported | Up to 32 | N/A |
| `n4a-highcpu-48` | 48 | 96 | Not supported | Up to 32 | N/A |
| `n4a-highcpu-64` | 64 | 128 | Not supported | Up to 50 | N/A |

^1^ SMT is not supported. Each vCPU is equivalent to an entire core. See [CPU platforms](https://docs.cloud.google.com/compute/docs/cpu-platforms).  
^2^ Maximum egress bandwidth cannot exceed the number given. Actual egress bandwidth depends on the destination IP address and other factors. See [Network bandwidth](https://docs.cloud.google.com/compute/docs/network-bandwidth).  

<br />

### N4A highmem

| Machine types | vCPUs^1^ | Memory (GB) | Local SSD | Default egress bandwidth (Gbps)^2^ | Tier_1 egress bandwidth (Gbps) |
|---|---|---|---|---|---|
| `n4a-highmem-1` | 1 | 8 | Not supported | Up to 10 | N/A |
| `n4a-highmem-2` | 2 | 16 | Not supported | Up to 10 | N/A |
| `n4a-highmem-4` | 4 | 32 | Not supported | Up to 10 | N/A |
| `n4a-highmem-8` | 8 | 64 | Not supported | Up to 16 | N/A |
| `n4a-highmem-16` | 16 | 128 | Not supported | Up to 32 | N/A |
| `n4a-highmem-32` | 32 | 256 | Not supported | Up to 32 | N/A |
| `n4a-highmem-48` | 48 | 384 | Not supported | Up to 32 | N/A |
| `n4a-highmem-64` | 64 | 512 | Not supported | Up to 50 | N/A |

^1^ SMT is not supported. Each vCPU is equivalent to an entire core. See [CPU platforms](https://docs.cloud.google.com/compute/docs/cpu-platforms).  
^2^ Maximum egress bandwidth cannot exceed the number given. Actual egress bandwidth depends on the destination IP address and other factors. See [Network bandwidth](https://docs.cloud.google.com/compute/docs/network-bandwidth).  

<br />

### Supported disk types for N4A

N4A VMs support only the NVMe disk interface and can use the following [Hyperdisk](https://docs.cloud.google.com/compute/docs/disks/hyperdisks) block storage:

- Hyperdisk Balanced (`hyperdisk-balanced`)
- Hyperdisk Balanced High Availability (`hyperdisk-balanced-high-availability`)
- Hyperdisk Throughput (`hyperdisk-throughput`)

N4A doesn't support Persistent Disk or Local SSD. Read [Move your workload from an existing VM to a new VM](https://docs.cloud.google.com/compute/docs/import/migrate-to-new-vm) to migrate your Persistent Disk resources to a newer machine series.

#### Disk and capacity limits

The number of Hyperdisk volumes of all types that you can attach to a VM can't exceed the limits stated in the *Max number of Hyperdisk volumes* . For details about these limits, see [Hyperdisk capacity](https://docs.cloud.google.com/compute/docs/disks/hyperdisk-perf-limits#hyperdisk-capacity).

The combined total number of Hyperdisk Balanced volumes attached to a single VM depends on the number of vCPUs the VM has, and can't exceed these limits:

N4A storage limits are described in the following table:

### N4A standard

|   | Maximum number of disks |||   |
| Machine types | Hyperdisk per VM | Hyperdisk Balanced | Hyperdisk Balanced High Availability | Hyperdisk Throughput |
|---|---|---|---|---|
| `n4a-standard-1` | 4 | 16 | 16 | 16 |
| `n4a-standard-2` | 4 | 16 | 16 | 16 |
| `n4a-standard-4` | 8 | 16 | 16 | 16 |
| `n4a-standard-8` | 16 | 16 | 16 | 16 |
| `n4a-standard-16` | 32 | 32 | 32 | 32 |
| `n4a-standard-32` | 64 | 32 | 32 | 32 |
| `n4a-standard-48` | 64 | 32 | 32 | 32 |
| `n4a-standard-64` | 64 | 32 | 32 | 32 |

### N4A highcpu

|   | Maximum number of disks |||   |
| Machine types | Hyperdisk per VM | Hyperdisk Balanced | Hyperdisk Balanced High Availability | Hyperdisk Throughput |
|---|---|---|---|---|
| `n4a-highcpu-1` | 4 | 16 | 16 | 16 |
| `n4a-highcpu-2` | 4 | 16 | 16 | 16 |
| `n4a-highcpu-4` | 8 | 16 | 16 | 16 |
| `n4a-highcpu-8` | 16 | 16 | 16 | 16 |
| `n4a-highcpu-16` | 32 | 32 | 32 | 32 |
| `n4a-highcpu-32` | 32 | 32 | 32 | 32 |
| `n4a-highcpu-48` | 64 | 32 | 32 | 32 |
| `n4a-highcpu-64` | 64 | 32 | 32 | 32 |

### N4A highmem

|   | Maximum number of disks |||   |
| Machine types | Hyperdisk per VM | Hyperdisk Balanced | Hyperdisk Balanced High Availability | Hyperdisk Throughput |
|---|---|---|---|---|
| `n4a-highmem-1` | 4 | 16 | 16 | 16 |
| `n4a-highmem-2` | 4 | 16 | 16 | 16 |
| `n4a-highmem-4` | 8 | 16 | 16 | 16 |
| `n4a-highmem-8` | 16 | 16 | 16 | 16 |
| `n4a-highmem-16` | 32 | 32 | 32 | 32 |
| `n4a-highmem-32` | 32 | 32 | 32 | 32 |
| `n4a-highmem-48` | 64 | 32 | 32 | 32 |
| `n4a-highmem-64` | 64 | 32 | 32 | 32 |

### Network support for N4A VMs

N4A instances require [gVNIC network interfaces](https://docs.cloud.google.com/compute/docs/networking/using-gvnic). N4A instances support up to 50 Gbps network bandwidth for standard networking and don't support per VM Tier_1 networking performance.

Before migrating to N4A or creating N4A VM instances, make sure that the [operating system image](https://docs.cloud.google.com/compute/docs/images/os-details#networking) that you use supports the gVNIC driver for VM instances. These images include an updated gVNIC driver, even if the guest OS shows the `gve` driver version as 1.0.0. If your N4A VM is using an operating system with an older version of gVNIC driver, this is still supported but the VM might experience suboptimal performance such as less network bandwidth or higher latency.

If you use a custom OS image to create a N4A VM, you can [manually install the most recent gVNIC driver](https://docs.cloud.google.com/compute/docs/networking/using-gvnic#manual-gvnic-setup). The gVNIC driver version v1.4.2 or later is recommended for use with N4A VMs. Google recommends using the latest gVNIC driver version to benefit from additional features and bug fixes.

### Maintenance experience for N4A instances

During the [lifecycle of a Compute Engine instance](https://docs.cloud.google.com/compute/docs/instances/instance-lifecycle), the host machine that your instance runs on undergoes multiple *host events*. A host event can include the regular maintenance of Compute Engine infrastructure, or in rare cases, a host error. Compute Engine also applies some non-disruptive lightweight upgrades for the hypervisor and network in the background.

The N4A machine series offers the following features related to host maintenance:

| Machine type | Typical scheduled maintenance event frequency | [Maintenance behavior](https://docs.cloud.google.com/compute/docs/instances/host-maintenance-overview#maintenance_behaviors) | [Advanced notification](https://docs.cloud.google.com/compute/docs/instances/monitor-plan-host-maintenance-event) | [On-demand maintenance](https://docs.cloud.google.com/compute/docs/instances/trigger-host-maintenance-event) |
|---|---|---|---|---|
| All N4A machine types | Variable | Live migrate | 60 seconds | No |

## N4 machine series

N4 VMs are powered by the 5th generation Intel Xeon Scalable processors (code-named Emerald Rapids) and [Titanium](https://cloud.google.com/titanium). N4 machine types are built from the ground up for flexibility and cost optimization through an efficient architecture of streamlined features, shapes, and next generation [dynamic resource management](https://docs.cloud.google.com/compute/docs/dynamic-resource-management), which makes better use of resources on host machines. N4 offers flexible options like custom machine types that lets you use choose varied combinations of compute and memory to optimize costs and reduce resource waste. N4 is suited for a variety of general-purpose workloads that don't require peak processing power at all times.

In summary, the N4 machine series:

- Is powered by 5th generation Intel Emerald Rapids processor and titanium processors.
- Supports up to 80 vCPUs and 640 GB of DDR5 memory.
- Offers multiple predefined machine types and [custom machine types](https://docs.cloud.google.com/compute/docs/general-purpose-machines#custom_machine_types) and extended custom memory up to 640 GB.
- Supports standard network configuration with up to 50 Gbps bandwidth
- Supports Intel Advanced Matrix Extensions (AMX), a built-in accelerator that significantly improves the performance of deep-learning training and inference on the CPU.
- Supports the following discount and consumption options:
  - [Resource-based and flexible committed use discounts (CUDs)](https://docs.cloud.google.com/compute/docs/instances/committed-use-discounts-overview)
  - [Spot VMs](https://docs.cloud.google.com/compute/docs/instances/spot)
  - [Reservations](https://docs.cloud.google.com/compute/docs/instances/choose-reservation-type)
- Doesn't support Local SSD or per VM Tier_1 networking performance.

### N4 machine types

N4 VMs are available as predefined configurations in sizes ranging from 2 vCPUs to 80 vCPUs and up to 640 GB of memory.

- `standard`: 4 GB memory per vCPU
- `highcpu`: 2 GB memory per vCPU
- `highmem`: 8 GB memory per vCPU

### N4 standard

| Machine types | vCPUs^1^ | Memory (GB) | Local SSD | Default egress bandwidth (Gbps) | Tier_1 egress bandwidth (Gbps) |
|---|---|---|---|---|---|
| `n4-standard-2` | 2 | 8 | Not supported | Up to 10 | N/A |
| `n4-standard-4` | 4 | 16 | Not supported | Up to 10 | N/A |
| `n4-standard-8` | 8 | 32 | Not supported | Up to 16 | N/A |
| `n4-standard-16` | 16 | 64 | Not supported | Up to 32 | N/A |
| `n4-standard-32` | 32 | 128 | Not supported | Up to 32 | N/A |
| `n4-standard-48` | 48 | 192 | Not supported | Up to 32 | N/A |
| `n4-standard-64` | 64 | 256 | Not supported | Up to 45 | N/A |
| `n4-standard-80` | 80 | 320 | Not supported | Up to 50 | N/A |

^1^ A CPU uses two threads per core, and a vCPU represents a single thread. See [CPU platforms](https://docs.cloud.google.com/compute/docs/cpu-platforms)
.

### N4 highcpu

| Machine types | vCPUs^1^ | Memory (GB) | Local SSD | Default egress bandwidth (Gbps) | Tier_1 egress bandwidth (Gbps) |
|---|---|---|---|---|---|
| `n4-highcpu-2` | 2 | 4 | Not supported | Up to 10 | N/A |
| `n4-highcpu-4` | 4 | 8 | Not supported | Up to 10 | N/A |
| `n4-highcpu-8` | 8 | 16 | Not supported | Up to 16 | N/A |
| `n4-highcpu-16` | 16 | 32 | Not supported | Up to 32 | N/A |
| `n4-highcpu-32` | 32 | 64 | Not supported | Up to 32 | N/A |
| `n4-highcpu-48` | 48 | 96 | Not supported | Up to 32 | N/A |
| `n4-highcpu-64` | 64 | 128 | Not supported | Up to 45 | N/A |
| `n4-highcpu-80` | 80 | 160 | Not supported | Up to 50 | N/A |

^1^ A CPU uses two threads per core, and a vCPU represents a single thread. See [CPU platforms](https://docs.cloud.google.com/compute/docs/cpu-platforms)
.

### N4 highmem

| Machine types | vCPUs^1^ | Memory (GB) | Local SSD | Default egress bandwidth (Gbps) | Tier_1 egress bandwidth (Gbps) |
|---|---|---|---|---|---|
| `n4-highmem-2` | 2 | 16 | Not supported | Up to 10 | N/A |
| `n4-highmem-4` | 4 | 32 | Not supported | Up to 10 | N/A |
| `n4-highmem-8` | 8 | 64 | Not supported | Up to 16 | N/A |
| `n4-highmem-16` | 16 | 128 | Not supported | Up to 32 | N/A |
| `n4-highmem-32` | 32 | 256 | Not supported | Up to 32 | N/A |
| `n4-highmem-48` | 48 | 384 | Not supported | Up to 32 | N/A |
| `n4-highmem-64` | 64 | 512 | Not supported | Up to 45 | N/A |
| `n4-highmem-80` | 80 | 640 | Not supported | Up to 50 | N/A |

^1^ A CPU uses two threads per core, and a vCPU represents a single thread. See [CPU platforms](https://docs.cloud.google.com/compute/docs/cpu-platforms)
.

### Supported disk types for N4

N4 VMs supports only the NVMe disk interface and can use the following [Hyperdisk](https://docs.cloud.google.com/compute/docs/disks/hyperdisks) block storage:

- Hyperdisk Balanced (`hyperdisk-balanced`)
- Hyperdisk Balanced High Availability (`hyperdisk-balanced-high-availability`)
- Hyperdisk Throughput (`hyperdisk-throughput`)

N4 doesn't support Persistent Disk or Local SSD. Read [Move your workload from an existing VM to a new VM](https://docs.cloud.google.com/compute/docs/import/migrate-to-new-vm) to migrate your Persistent Disk resources to a newer machine series.

#### Disk and capacity limits

The number of Hyperdisk volumes of all types that you can attach to a VM can't exceed the limits stated in the *Max number of Hyperdisk volumes* . For details about these limits, see [Hyperdisk capacity](https://docs.cloud.google.com/compute/docs/disks/hyperdisk-perf-limits#hyperdisk-capacity).

N4 storage limits are described in the following table:

### N4 standard

|   | Maximum number of disks |||   |
| Machine types | Hyperdisk per VM | Hyperdisk Balanced | Hyperdisk Balanced High Availability | Hyperdisk Throughput |
|---|---|---|---|---|
| `n4-standard-2` | 16 | 16 | 16 | 16 |
| `n4-standard-4` | 16 | 16 | 16 | 16 |
| `n4-standard-8` | 16 | 16 | 16 | 16 |
| `n4-standard-16` | 32 | 32 | 32 | 32 |
| `n4-standard-32` | 32 | 32 | 32 | 32 |
| `n4-standard-48` | 32 | 32 | 32 | 32 |
| `n4-standard-64` | 32 | 32 | 32 | 32 |
| `n4-standard-80` | 32 | 32 | 32 | 32 |

### N4 highcpu

|   | Maximum number of disks |||   |
| Machine types | Hyperdisk per VM | Hyperdisk Balanced | Hyperdisk Balanced High Availability | Hyperdisk Throughput |
|---|---|---|---|---|
| `n4-highcpu-2` | 16 | 16 | 16 | 16 |
| `n4-highcpu-4` | 16 | 16 | 16 | 16 |
| `n4-highcpu-8` | 16 | 16 | 16 | 16 |
| `n4-highcpu-16` | 32 | 32 | 32 | 32 |
| `n4-highcpu-32` | 32 | 32 | 32 | 32 |
| `n4-highcpu-48` | 32 | 32 | 32 | 32 |
| `n4-highcpu-64` | 32 | 32 | 32 | 32 |
| `n4-highcpu-80` | 32 | 32 | 32 | 32 |

### N4 highmem

|   | Maximum number of disks |||   |
| Machine types | Hyperdisk per VM | Hyperdisk Balanced | Hyperdisk Balanced High Availability | Hyperdisk Throughput |
|---|---|---|---|---|
| `n4-highmem-2` | 16 | 16 | 16 | 16 |
| `n4-highmem-4` | 16 | 16 | 16 | 16 |
| `n4-highmem-8` | 16 | 16 | 16 | 16 |
| `n4-highmem-16` | 32 | 32 | 32 | 32 |
| `n4-highmem-32` | 32 | 32 | 32 | 32 |
| `n4-highmem-48` | 32 | 32 | 32 | 32 |
| `n4-highmem-64` | 32 | 32 | 32 | 32 |
| `n4-highmem-80` | 32 | 32 | 32 | 32 |

### Network support for N4 VMs

N4 instances require [gVNIC network interfaces](https://docs.cloud.google.com/compute/docs/networking/using-gvnic). N4 instances support up to 50 Gbps network bandwidth for standard networking and don't support per VM Tier_1 networking performance.

Before migrating to N4 or creating N4 VM instances, make sure that the [operating system image](https://docs.cloud.google.com/compute/docs/images/os-details#networking) that you use supports the gVNIC driver for VM instances. These images include an updated gVNIC driver, even if the guest OS shows the `gve` driver version as 1.0.0. If your N4 VM is using an operating system with an older version of gVNIC driver, this is still supported but the VM might experience suboptimal performance such as less network bandwidth or higher latency.

If you use a custom OS image to create a N4 VM, you can [manually install the most recent gVNIC driver](https://docs.cloud.google.com/compute/docs/networking/using-gvnic#manual-gvnic-setup). The gVNIC driver version v1.4.2 or later is recommended for use with N4 VMs. Google recommends using the latest gVNIC driver version to benefit from additional features and bug fixes.

### Maintenance experience for N4 instances

During the [lifecycle of a Compute Engine instance](https://docs.cloud.google.com/compute/docs/instances/instance-lifecycle), the host machine that your instance runs on undergoes multiple *host events*. A host event can include the regular maintenance of Compute Engine infrastructure, or in rare cases, a host error. Compute Engine also applies some non-disruptive lightweight upgrades for the hypervisor and network in the background.

The N4 machine series offers the following features related to host maintenance:

| Machine type | Typical scheduled maintenance event frequency | [Maintenance behavior](https://docs.cloud.google.com/compute/docs/instances/host-maintenance-overview#maintenance_behaviors) | [Advanced notification](https://docs.cloud.google.com/compute/docs/instances/monitor-plan-host-maintenance-event) | [On-demand maintenance](https://docs.cloud.google.com/compute/docs/instances/trigger-host-maintenance-event) |
|---|---|---|---|---|
| All N4 machine types | Variable | Live migrate | 60 seconds | No |

The maintenance frequencies shown in the previous table are approximations, not guarantees. Compute Engine might occasionally perform maintenance more frequently.

## C3D machine series

C3D VMs are powered by the 4th generation AMD EPYC™ (Genoa) processor with a maximum frequency of 3.7 Ghz. C3D machine types are optimized for the underlying hardware architecture to deliver optimal, reliable, and consistent performance.

C3D uses [Titanium](https://cloud.google.com/titanium), which enables higher levels of networking performance, isolation and security. The C3D machine series supports Tier_1 networking bandwidth of up to 100 Gbps and up to 200 Gbps.

In summary, the C3D machine series:

- Is powered by 4th generation AMD EPYC™ processor and Titanium.
- Supports up to 360 vCPUs and 2,880 GB of DDR5 memory.
- Supports standard network configuration with up to 100 Gbps bandwidth and Tier_1 networking with up to 200 Gbps bandwidth.
- Supports the following discount and consumption options:
  - [Resource-based and flexible committed use discounts (CUDs)](https://docs.cloud.google.com/compute/docs/instances/committed-use-discounts-overview)
  - [Spot VMs](https://docs.cloud.google.com/compute/docs/instances/spot)
  - [Reservations](https://docs.cloud.google.com/compute/docs/instances/choose-reservation-type)
- Supports [Confidential VM](https://docs.cloud.google.com/confidential-computing/confidential-vm/docs/confidential-vm-overview) with AMD SEV, excluding bare metal instances and configurations with more than 255 vCPUs.

> [!CAUTION]
> **Caution** : When you purchase resource-based commitments for C3 and C3D resources, the machine family that is specified by the commitment type changes depending on the interface:
>
> - In the gcloud CLI and REST, the commitment type values use *Compute-optimized* as the machine family, even though C3 and C3D are part of the general-purpose machine family.
> - In the Google Cloud console, the commitment type values use the correct machine series: *General-Purpose*.
>
> Make sure to select the correct commitment type value that corresponds to the interface that you're using. For more information, see the [resource-based CUDs documentation](https://docs.cloud.google.com/compute/docs/instances/signing-up-committed-use-discounts).

<br />

### C3D machine types

C3D VMs are available in `standard`, `highcpu`, `highmem`, and `lssd` configurations in sizes ranging from 4 to 360 vCPUs and up to 2,880 GB of memory. The `highcpu` configuration offers the lowest price per performance for compute-bound workloads that don't require large amounts of memory.

### C3D standard

| Machine types | vCPUs^1^ | Memory (GB) | Local SSD | Default egress bandwidth (Gbps)^2^ | Tier_1 egress bandwidth (Gbps)^3^ |
|---|---|---|---|---|---|
| `c3d-standard-4` | 4 | 16 | Not supported | Up to 20 | N/A |
| `c3d-standard-8` | 8 | 32 | Not supported | Up to 20 | N/A |
| `c3d-standard-16` | 16 | 64 | Not supported | Up to 20 | N/A |
| `c3d-standard-30` | 30 | 120 | Not supported | Up to 20 | Up to 50 |
| `c3d-standard-60` | 60 | 240 | Not supported | Up to 40 | Up to 75 |
| `c3d-standard-90` | 90 | 360 | Not supported | Up to 60 | Up to 100 |
| `c3d-standard-180` | 180 | 720 | Not supported | Up to 100 | Up to 150 |
| `c3d-standard-360` | 360 | 1,440 | Not supported | Up to 100 | Up to 200 |

^1^ A CPU uses two threads per core, and a vCPU represents a single thread. See [CPU platforms](https://docs.cloud.google.com/compute/docs/cpu-platforms).   
^2^ Default egress bandwidth can't exceed the number given. Actual egress bandwidth depends on the destination IP address and other factors. See [Network bandwidth](https://docs.cloud.google.com/compute/docs/network-bandwidth).  
^3^ Supports [high-bandwidth networking](https://docs.cloud.google.com/compute/docs/networking/configure-vm-with-high-bandwidth-configuration) for larger machine types.

### C3D highcpu

| Machine types | vCPUs^1^ | Memory (GB) | Local SSD | Default egress bandwidth (Gbps)^2^ | Tier_1 egress bandwidth (Gbps)^3^ |
|---|---|---|---|---|---|
| `c3d-highcpu-4` | 4 | 8 | Not supported | Up to 20 | N/A |
| `c3d-highcpu-8` | 8 | 16 | Not supported | Up to 20 | N/A |
| `c3d-highcpu-16` | 16 | 32 | Not supported | Up to 20 | N/A |
| `c3d-highcpu-30` | 30 | 59 | Not supported | Up to 20 | Up to 50 |
| `c3d-highcpu-60` | 60 | 118 | Not supported | Up to 40 | Up to 75 |
| `c3d-highcpu-90` | 90 | 177 | Not supported | Up to 60 | Up to 100 |
| `c3d-highcpu-180` | 180 | 354 | Not supported | Up to 100 | Up to 150 |
| `c3d-highcpu-360` | 360 | 708 | Not supported | Up to 100 | Up to 200 |

^1^ A CPU uses two threads per core, and a vCPU represents a single thread. See [CPU platforms](https://docs.cloud.google.com/compute/docs/cpu-platforms).   
^2^ Default egress bandwidth can't exceed the number given. Actual egress bandwidth depends on the destination IP address and other factors. See [Network bandwidth](https://docs.cloud.google.com/compute/docs/network-bandwidth).  
^3^ Supports [high-bandwidth networking](https://docs.cloud.google.com/compute/docs/networking/configure-vm-with-high-bandwidth-configuration) for larger machine types.

### C3D highmem

| Machine types | vCPUs^1^ | Memory (GB) | Local SSD | Default egress bandwidth (Gbps)^2^ | Tier_1 egress bandwidth (Gbps)^3^ |
|---|---|---|---|---|---|
| `c3d-highmem-4` | 4 | 32 | Not supported | Up to 20 | N/A |
| `c3d-highmem-8` | 8 | 64 | Not supported | Up to 20 | N/A |
| `c3d-highmem-16` | 16 | 128 | Not supported | Up to 20 | N/A |
| `c3d-highmem-30` | 30 | 240 | Not supported | Up to 20 | Up to 50 |
| `c3d-highmem-60` | 60 | 480 | Not supported | Up to 40 | Up to 75 |
| `c3d-highmem-90` | 90 | 720 | Not supported | Up to 60 | Up to 100 |
| `c3d-highmem-180` | 180 | 1,440 | Not supported | Up to 100 | Up to 150 |
| `c3d-highmem-360` | 360 | 2,880 | Not supported | Up to 100 | Up to 200 |

^1^ A CPU uses two threads per core, and a vCPU represents a single thread. See [CPU platforms](https://docs.cloud.google.com/compute/docs/cpu-platforms).   
^2^ Default egress bandwidth can't exceed the number given. Actual egress bandwidth depends on the destination IP address and other factors. See [Network bandwidth](https://docs.cloud.google.com/compute/docs/network-bandwidth).  
^3^ Supports [high-bandwidth networking](https://docs.cloud.google.com/compute/docs/networking/configure-vm-with-high-bandwidth-configuration) for larger machine types.

### C3D standard

| Machine types | vCPUs^1^ | Memory (GB) | Local SSD | Default egress bandwidth (Gbps)^2^ | Tier_1 egress bandwidth (Gbps)^3^ |
|---|---|---|---|---|---|
| `c3d-standard-8-lssd` | 8 | 32 | (1 x 375 GiB) 375 GiB | Up to 20 | N/A |
| `c3d-standard-16-lssd` | 16 | 64 | (1 x 375 GiB) 375 GiB | Up to 20 | N/A |
| `c3d-standard-30-lssd` | 30 | 120 | (2 x 375 GiB) 750 GiB | Up to 20 | Up to 50 |
| `c3d-standard-60-lssd` | 60 | 240 | (4 x 375 GiB) 1.5 TiB | Up to 40 | Up to 75 |
| `c3d-standard-90-lssd` | 90 | 360 | (8 x 375 GiB) 3 TiB | Up to 60 | Up to 100 |
| `c3d-standard-180-lssd` | 180 | 720 | (16 x 375 GiB) 6 TiB | Up to 100 | Up to 150 |
| `c3d-standard-360-lssd` | 360 | 1440 | (32 x 375 GiB) 12 TiB | Up to 100 | Up to 200 |

^1^ A CPU uses two threads per core, and a vCPU represents a single thread. See [CPU platforms](https://docs.cloud.google.com/compute/docs/cpu-platforms).   
^2^ Default egress bandwidth can't exceed the number given. Actual egress bandwidth depends on the destination IP address and other factors. See [Network bandwidth](https://docs.cloud.google.com/compute/docs/network-bandwidth).  
^3^ Supports [high-bandwidth networking](https://docs.cloud.google.com/compute/docs/networking/configure-vm-with-high-bandwidth-configuration) for larger machine types.

### C3D highmem

| Machine types | vCPUs^1^ | Memory (GB) | Local SSD | Default egress bandwidth (Gbps)^2^ | Tier_1 egress bandwidth (Gbps)^3^ |
|---|---|---|---|---|---|
| `c3d-highmem-8-lssd` | 8 | 64 | (1 x 375 GiB) 375 GiB | Up to 20 | N/A |
| `c3d-highmem-16-lssd` | 16 | 128 | (1 x 375 GiB) 375 GiB | Up to 20 | N/A |
| `c3d-highmem-30-lssd` | 30 | 240 | (2 x 375 GiB) 750 GiB | Up to 20 | Up to 50 |
| `c3d-highmem-60-lssd` | 60 | 480 | (4 x 375 GiB) 1.5 TiB | Up to 40 | Up to 75 |
| `c3d-highmem-90-lssd` | 90 | 720 | (8 x 375 GiB) 3 TiB | Up to 60 | Up to 100 |
| `c3d-highmem-180-lssd` | 180 | 1440 | (16 x 375 GiB) 6 TiB | Up to 100 | Up to 150 |
| `c3d-highmem-360-lssd` | 360 | 2880 | (32 x 375 GiB) 12 TiB | Up to 100 | Up to 200 |

^1^ A CPU uses two threads per core, and a vCPU represents a single thread. See [CPU platforms](https://docs.cloud.google.com/compute/docs/cpu-platforms).   
^2^ Default egress bandwidth can't exceed the number given. Actual egress bandwidth depends on the destination IP address and other factors. See [Network bandwidth](https://docs.cloud.google.com/compute/docs/network-bandwidth).  
^3^ Supports [high-bandwidth networking](https://docs.cloud.google.com/compute/docs/networking/configure-vm-with-high-bandwidth-configuration) for larger machine types.

C3D doesn't support custom machine types.

### Supported disk types for C3D

C3D VMs support only the NVMe disk interface and can use the following block storage types:

- Balanced Persistent Disk (`pd-balanced`)
- SSD (performance) Persistent Disk (`pd-ssd`)
- Hyperdisk Balanced (`hyperdisk-balanced`)
- Hyperdisk Balanced High Availability (`hyperdisk-balanced-high-availability`)
- Hyperdisk ML (`hyperdisk-ml`)
- Hyperdisk Extreme (`hyperdisk-extreme`)
- Hyperdisk Throughput (`hyperdisk-throughput`)
- Local SSD (only available with `-lssd` machine types)

To use Local SSD with C3D, create your VM using the `-lssd` variant of the C3D machine types. Selecting this machine type creates a VM of the specified size with Local SSD partitions attached. You must use a machine type that ends in `-lssd` to use Local SSD with your C3D VM; you can't attach Local SSD volumes separately.

#### Disk and capacity limits

<br />

For instances running Microsoft Windows and using the NVMe disk interface, the combined number of both Hyperdisk and Persistent Disk attached volumes can't exceed a total of 16 disks. See [Known issues](https://docs.cloud.google.com/compute/docs/troubleshooting/known-issues#windows-disk-attachment). Local SSD volumes are excluded from this issue.

<br />

C3D storage limits are described in the following table:

### C3D standard

|   | Maximum number of disks |||||   |
| Machine types | Per VM | Hyperdisk per VM | Hyperdisk Balanced | Hyperdisk Throughput | Hyperdisk ML | Hyperdisk Extreme |
|---|---|---|---|---|---|---|
| `c3d-standard-4` | 128 | 24 | 16 | 24 | 24 | 0 |
| `c3d-standard-8` | 128 | 32 | 16 | 32 | 32 | 0 |
| `c3d-standard-16` | 128 | 48 | 16 | 48 | 48 | 0 |
| `c3d-standard-30` | 128 | 64 | 16 | 64 | 64 | 0 |
| `c3d-standard-60` | 128 | 64 | 32 | 64 | 64 | 8 |
| `c3d-standard-90` | 128 | 64 | 32 | 64 | 64 | 8 |
| `c3d-standard-180` | 128 | 64 | 32 | 64 | 64 | 8 |
| `c3d-standard-360` | 128 | 64 | 32 | 64 | 64 | 8 |

### C3D highcpu

|   | Maximum number of disks |||||   |
| Machine types | Per VM | Hyperdisk per VM | Hyperdisk Balanced | Hyperdisk Throughput | Hyperdisk ML | Hyperdisk Extreme |
|---|---|---|---|---|---|---|
| `c3d-highcpu-4` | 128 | 24 | 16 | 24 | 24 | 0 |
| `c3d-highcpu-8` | 128 | 32 | 16 | 32 | 32 | 0 |
| `c3d-highcpu-16` | 128 | 48 | 16 | 48 | 48 | 0 |
| `c3d-highcpu-30` | 128 | 64 | 16 | 64 | 64 | 0 |
| `c3d-highcpu-60` | 128 | 64 | 32 | 64 | 64 | 8 |
| `c3d-highcpu-90` | 128 | 64 | 32 | 64 | 64 | 8 |
| `c3d-highcpu-180` | 128 | 64 | 32 | 64 | 64 | 8 |
| `c3d-highcpu-360` | 128 | 64 | 32 | 64 | 64 | 8 |

### C3D highmem

|   | Maximum number of disks |||||   |
| Machine types | Per VM | Hyperdisk per VM | Hyperdisk Balanced | Hyperdisk Throughput | Hyperdisk ML | Hyperdisk Extreme |
|---|---|---|---|---|---|---|
| `c3d-highmem-4` | 128 | 24 | 16 | 24 | 24 | 0 |
| `c3d-highmem-8` | 128 | 32 | 16 | 32 | 32 | 0 |
| `c3d-highmem-16` | 128 | 48 | 16 | 48 | 48 | 0 |
| `c3d-highmem-30` | 128 | 64 | 16 | 64 | 64 | 0 |
| `c3d-highmem-60` | 128 | 64 | 32 | 64 | 64 | 8 |
| `c3d-highmem-90` | 128 | 64 | 32 | 64 | 64 | 8 |
| `c3d-highmem-180` | 128 | 64 | 32 | 64 | 64 | 8 |
| `c3d-highmem-360` | 128 | 64 | 32 | 64 | 64 | 8 |

### C3D standard

|   | Maximum number of disks |||||   |
| Machine types | Per VM | Hyperdisk per VM | Hyperdisk Balanced | Hyperdisk Throughput | Hyperdisk ML | Hyperdisk Extreme |
|---|---|---|---|---|---|---|
| `c3d-standard-8-lssd` | 128 | 24 | 16 | 24 | 24 | 0 |
| `c3d-standard-16-lssd` | 128 | 48 | 16 | 48 | 48 | 0 |
| `c3d-standard-30-lssd` | 128 | 64 | 16 | 64 | 64 | 0 |
| `c3d-standard-60-lssd` | 128 | 64 | 32 | 64 | 64 | 8 |
| `c3d-standard-90-lssd` | 128 | 64 | 32 | 64 | 64 | 8 |
| `c3d-standard-180-lssd` | 128 | 64 | 32 | 64 | 64 | 8 |
| `c3d-standard-360-lssd` | 128 | 64 | 32 | 64 | 64 | 8 |

### C3D highmem

|   | Maximum number of disks |||||   |
| Machine types | Per VM | Hyperdisk per VM | Hyperdisk Balanced | Hyperdisk Throughput | Hyperdisk ML | Hyperdisk Extreme |
|---|---|---|---|---|---|---|
| `c3d-highmem-8-lssd` | 128 | 24 | 16 | 24 | 24 | 0 |
| `c3d-highmem-16-lssd` | 128 | 48 | 16 | 48 | 48 | 0 |
| `c3d-highmem-30-lssd` | 128 | 64 | 16 | 64 | 64 | 0 |
| `c3d-highmem-60-lssd` | 128 | 64 | 32 | 64 | 64 | 8 |
| `c3d-highmem-90-lssd` | 128 | 64 | 32 | 64 | 64 | 8 |
| `c3d-highmem-180-lssd` | 128 | 64 | 32 | 64 | 64 | 8 |
| `c3d-highmem-360-lssd` | 128 | 64 | 32 | 64 | 64 | 8 |

### Network support for C3D VMs

C3D instances require [gVNIC network interfaces](https://docs.cloud.google.com/compute/docs/networking/using-gvnic). C3D supports up to 100 Gbps network bandwidth for standard networking and up to 200 Gbps with per VM Tier_1 networking performance.

Before migrating to C3D or creating C3D instances, make sure that the operating system image that you use supports the gVNIC driver. To get the best possible performance on C3D instances, on the [**Networking features**](https://docs.cloud.google.com/compute/docs/images/os-details#networking-features) tab of the OS details table, choose an OS image that supports both "Tier_1 Networking" and "200 Gbps network bandwidth". These images include an updated gVNIC driver, even if the guest OS shows the `gve` driver version as 1.0.0. If your C3D instance is using an operating system with an older version of the gVNIC driver, this is still supported but the instance might experience suboptimal performance such as less network bandwidth or higher latency.

If you use a custom OS image with the C3D machine series, you can [manually install the most recent gVNIC driver](https://docs.cloud.google.com/compute/docs/networking/using-gvnic#manual-gvnic-setup). The gVNIC driver version v1.4.2 or later is recommended for use with C3D instances. Google recommends using the latest gVNIC driver version to benefit from additional features and bug fixes.

### Maintenance experience for C3D instances

During the [lifecycle of a Compute Engine instance](https://docs.cloud.google.com/compute/docs/instances/instance-lifecycle), the host machine that your instance runs on undergoes multiple *host events*. A host event can include the regular maintenance of Compute Engine infrastructure, or in rare cases, a host error. Compute Engine also applies some non-disruptive lightweight upgrades for the hypervisor and network in the background.

The C3D machine series offers the following features related to host maintenance:

| Machine type | Typical scheduled maintenance event frequency | [Maintenance behavior](https://docs.cloud.google.com/compute/docs/instances/host-maintenance-overview#maintenance_behaviors) | [Advanced notification](https://docs.cloud.google.com/compute/docs/instances/monitor-plan-host-maintenance-event) | [On-demand maintenance](https://docs.cloud.google.com/compute/docs/instances/trigger-host-maintenance-event) |
|---|---|---|---|---|
| C3D with Confidential VM | Minimum of 30 days | Terminate | 7 days | No |
| `c3d-*-lssd` | Minimum of 30 days | Live migrate | 7 days | Yes |
| `c3d-*-360` | Minimum of 30 days | Live migrate | 7 days | Yes |
| All others | Minimum of 30 days | Live migrate | 7 days | No |

The maintenance frequencies shown in the previous table are approximations, not guarantees. Compute Engine might occasionally perform maintenance more frequently.

## C3 machine series

C3 VMs are powered by the 4th generation Intel Xeon Scalable processors (code-named Sapphire Rapids), DDR5 memory, and [Titanium](https://cloud.google.com/titanium). C3 machine types are optimized for the underlying NUMA architecture to deliver optimal, reliable, and consistent performance.

The new C3 machine series is a major leap in our purpose-built infrastructure offerings:

- Leveraging Titanium processors to offload networking from the CPUs
- Delivering high performance block-storage with [Google Cloud Hyperdisk](https://docs.cloud.google.com/compute/docs/disks/hyperdisks)
- Speeding up ML training and inference with [Intel AMX](https://docs.cloud.google.com/compute/docs/cpu-platforms#intel-amx)

C3 uses Titanium to enable higher levels of networking performance, isolation and security. The C3 machine series supports a default network bandwidth of up to 100 Gbps and up to 200 Gbps with [per VM Tier_1 networking performance](https://docs.cloud.google.com/compute/docs/networking/configure-vm-with-high-bandwidth-configuration). Titanium has been designed from the ground up to enable updates that don't impact running workloads.

The C3 machine series provides some of the largest general-purpose machine types, letting you create VM instances with up to 176 vCPUs and 1.4 TB of memory.

C3 has bare metal machine types, which allow you to access all the raw compute resources of the server. You can create bare metal instances with 192 vCPUs and up to 1,536 GB of memory. Bare metal instances also provide access to several onboard, function-specific [accelerators and offloads](https://docs.cloud.google.com/compute/docs/cpu-platforms#accelerator):

- Intel-QAT
- Intel-DLB
- Intel DSA
- Intel IAA

If your organization uses a Shielded VM policy, then you must create a custom org policy that excludes bare metal shapes before you can create a bare metal instance.

In summary, the C3 machine series:

- Is powered by Intel 4th Generation Xeon processors and Titanium.
- Supports up to 176 vCPUs and 1.4 TB of DDR5 memory for VMs.
- Supports up to 192 vCPUs and 1,536 GB of memory for bare metal instances.
- Supports standard network configuration with up to 100 Gbps bandwidth and Tier_1 networking with up to 200 Gbps bandwidth.
- Supports Intel Advanced Matrix Extensions (AMX), a built-in accelerator that significantly improves the performance of deep-learning training and inference on the CPU.
- Supports the following discount and consumption options:
  - [Resource-based and flexible committed use discounts (CUDs)](https://docs.cloud.google.com/compute/docs/instances/committed-use-discounts-overview)
  - [Spot VMs](https://docs.cloud.google.com/compute/docs/instances/spot)
  - [Reservations](https://docs.cloud.google.com/compute/docs/instances/choose-reservation-type)
- Supports [Confidential VM](https://docs.cloud.google.com/confidential-computing/confidential-vm/docs/confidential-vm-overview) with Intel TDX.
- Doesn't offer [sustained use discounts (SUDs)](https://docs.cloud.google.com/compute/docs/sustained-use-discounts).
- C3 bare metal instances don't support the following:
  - [Google Kubernetes Engine](https://docs.cloud.google.com/kubernetes-engine/docs)
  - [Shielded VM](https://docs.cloud.google.com/compute/shielded-vm/docs/shielded-vm)
  - [Nested virtualization](https://docs.cloud.google.com/compute/docs/instances/nested-virtualization/overview)

<br />

> [!CAUTION]
> **Caution** : When you purchase resource-based commitments for C3 and C3D resources, the machine family that is specified by the commitment type changes depending on the interface:
>
> - In the gcloud CLI and REST, the commitment type values use *Compute-optimized* as the machine family, even though C3 and C3D are part of the general-purpose machine family.
> - In the Google Cloud console, the commitment type values use the correct machine series: *General-Purpose*.
>
> Make sure to select the correct commitment type value that corresponds to the interface that you're using. For more information, see the [resource-based CUDs documentation](https://docs.cloud.google.com/compute/docs/instances/signing-up-committed-use-discounts).

<br />

### C3 machine types

C3 VMs are available in predefined machine types with sizes ranging from 4 to 176 vCPUs and up to 1,408 GB of memory.

To use Local SSD with C3, create your VM using the `-lssd` variant of the C3 machine types. Selecting this machine type creates a VM of the specified size with Local SSD partitions attached. You must use a `c3-standard-*-lssd` machine type to use Local SSD with your VM; you can't attach Local SSD volumes separately.

To create a bare metal instance with C3, use one of the following machine types:

- `c3-standard-192-metal`
- `c3-highcpu-192-metal`
- `c3-highmem-192-metal`

### C3 standard

| Machine types | vCPUs^1^ | Memory (GB) | Local SSD | Default egress bandwidth (Gbps)^2^ | Tier_1 egress bandwidth (Gbps) |
|---|---|---|---|---|---|
| `c3-standard-4` | 4 | 16 | Not supported | Up to 23 | N/A |
| `c3-standard-8` | 8 | 32 | Not supported | Up to 23 | N/A |
| `c3-standard-22` | 22 | 88 | Not supported | Up to 23 | N/A |
| `c3-standard-44` | 44 | 176 | Not supported | Up to 32 | Up to 50 |
| `c3-standard-88` | 88 | 352 | Not supported | Up to 62 | Up to 100 |
| `c3-standard-176` | 176 | 704 | Not supported | Up to 100 | Up to 200 |
| `c3-standard-192-metal` | 192^†^ | 768 | Not supported | Up to 100 | Up to 200 |

^1^ Each CPU uses two threads per core. A vCPU is implemented as a single hardware thread.  
^2^ For bare metal instances, the number of vCPUs is equivalent to the number of hardware threads on the host server.  
^3^ Default egress bandwidth can't exceed the number given. Actual egress bandwidth depends on the destination IP address and other factors. See [Network bandwidth](https://docs.cloud.google.com/compute/docs/network-bandwidth).  

### C3 highcpu

| Machine types | vCPUs^1^ | Memory (GB) | Local SSD | Default egress bandwidth (Gbps)^2^ | Tier_1 egress bandwidth (Gbps) |
|---|---|---|---|---|---|
| `c3-highcpu-4` | 4 | 8 | Not supported | Up to 23 | N/A |
| `c3-highcpu-8` | 8 | 16 | Not supported | Up to 23 | N/A |
| `c3-highcpu-22` | 22 | 44 | Not supported | Up to 23 | N/A |
| `c3-highcpu-44` | 44 | 88 | Not supported | Up to 32 | Up to 50 |
| `c3-highcpu-88` | 88 | 176 | Not supported | Up to 62 | Up to 100 |
| `c3-highcpu-176` | 176 | 352 | Not supported | Up to 100 | Up to 200 |
| `c3-highcpu-192-metal` | 192^†^ | 512 | Not supported | Up to 100 | Up to 200 |

^1^ Each CPU uses two threads per core. A vCPU is implemented as a single hardware thread.  
^2^ For bare metal instances, the number of vCPUs is equivalent to the number of hardware threads on the host server.  
^3^ Default egress bandwidth can't exceed the number given. Actual egress bandwidth depends on the destination IP address and other factors. See [Network bandwidth](https://docs.cloud.google.com/compute/docs/network-bandwidth).  

### C3 highmem

| Machine types | vCPUs^1^ | Memory (GB) | Local SSD | Default egress bandwidth (Gbps)^2^ | Tier_1 egress bandwidth (Gbps) |
|---|---|---|---|---|---|
| `c3-highmem-4` | 4 | 32 | Not supported | Up to 23 | N/A |
| `c3-highmem-8` | 8 | 64 | Not supported | Up to 23 | N/A |
| `c3-highmem-22` | 22 | 176 | Not supported | Up to 23 | N/A |
| `c3-highmem-44` | 44 | 352 | Not supported | Up to 32 | Up to 50 |
| `c3-highmem-88` | 88 | 704 | Not supported | Up to 62 | Up to 100 |
| `c3-highmem-176` | 176 | 1408 | Not supported | Up to 100 | Up to 200 |
| `c3-highmem-192-metal` | 192^†^ | 1536 | Not supported | Up to 100 | Up to 200 |

^1^ Each CPU uses two threads per core. A vCPU is implemented as a single hardware thread.  
^2^ For bare metal instances, the number of vCPUs is equivalent to the number of hardware threads on the host server.  
^3^ Default egress bandwidth can't exceed the number given. Actual egress bandwidth depends on the destination IP address and other factors. See [Network bandwidth](https://docs.cloud.google.com/compute/docs/network-bandwidth).  

### C3 standard

| Machine types | vCPUs^1^ | Memory (GB) | Local SSD | Default egress bandwidth (Gbps)^2^ | Tier_1 egress bandwidth (Gbps) |
|---|---|---|---|---|---|
| `c3-standard-4-lssd` | 4 | 16 | (1 x 375 GiB) 375 GiB | Up to 23 | N/A |
| `c3-standard-8-lssd` | 8 | 32 | (2 x 375 GiB) 750 GiB | Up to 23 | N/A |
| `c3-standard-22-lssd` | 22 | 88 | (4 x 375 GiB) 1.5 TiB | Up to 23 | N/A |
| `c3-standard-44-lssd` | 44 | 176 | (8 x 375 GiB) 3 TiB | Up to 32 | Up to 50 |
| `c3-standard-88-lssd` | 88 | 352 | (16 x 375 GiB) 6 TiB | Up to 62 | Up to 100 |
| `c3-standard-176-lssd` | 176 | 704 | (32 x 375 GiB) 12 TiB | Up to 100 | Up to 200 |

^1^ Each CPU uses two threads per core. A vCPU is implemented as a single hardware thread.  
^2^ For bare metal instances, the number of vCPUs is equivalent to the number of hardware threads on the host server.  
^3^ Default egress bandwidth can't exceed the number given. Actual egress bandwidth depends on the destination IP address and other factors. See [Network bandwidth](https://docs.cloud.google.com/compute/docs/network-bandwidth).  

C3 doesn't support custom machine types.

### C3 regional availability for bare metal instances

For C3 VMs, you can view the available regions and zones in the [Regional availability of bare metal instances](https://docs.cloud.google.com/compute/docs/instances/bare-metal-instances#regions-zones) table.

### Supported disk types for C3

C3 VMs support only the NVMe disk interface and can use the following block storage types:

### VM instances

- Zonal balanced Persistent Disk (`pd-balanced`)
- Zonal SSD (performance) Persistent Disk (`pd-ssd`)
- Hyperdisk Extreme (`hyperdisk-extreme`)---Requires at least 64 vCPUs
- Hyperdisk ML (`hyperdisk-ml`)
- Hyperdisk Throughput (`hyperdisk-throughput`)
- Hyperdisk Balanced (`hyperdisk-balanced`)
- Hyperdisk Balanced High Availability (`hyperdisk-balanced-high-availability`)
- Local SSD (only available with `-lssd` machine types)

### Bare metal instances

- Hyperdisk Balanced (`hyperdisk-balanced`)
- Hyperdisk Extreme (`hyperdisk-extreme`)

A set amount of Local SSD disks are added to the C3 VM when you use the `-lssd` machine type. This is the only way to include Local SSD storage with a C3 VM. You can't use Local SSD disks with bare metal instances.

#### Disk and capacity limits

<br />

For instances running Microsoft Windows and using the NVMe disk interface, the combined number of both Hyperdisk and Persistent Disk attached volumes can't exceed a total of 16 disks. See [Known issues](https://docs.cloud.google.com/compute/docs/troubleshooting/known-issues#windows-disk-attachment). Local SSD volumes are excluded from this issue.

<br />

C3 storage limits are described in the following table:

### C3 standard

|   | Maximum number of disks |||||   |
| Machine types | Per instance | Hyperdisk per instance | Hyperdisk Balanced | Hyperdisk Throughput | Hyperdisk ML | Hyperdisk Extreme |
|---|---|---|---|---|---|---|
| `c3-standard-4` | 128 | 24 | 16 | 24 | 24 | 0 |
| `c3-standard-8` | 128 | 32 | 16 | 32 | 32 | 0 |
| `c3-standard-22` | 128 | 48 | 32 | 48 | 48 | 0 |
| `c3-standard-44` | 128 | 64 | 32 | 64 | 64 | 0 |
| `c3-standard-88` | 128 | 64 | 32 | 64 | 64 | 8 |
| `c3-standard-176` | 128 | 64 | 32 | 64 | 64 | 8 |
| `c3-standard-192-metal` | 16 (Hyperdisk only) | 16 | 16 | Not supported | Not supported | 16 |

### C3 highcpu

|   | Maximum number of disks |||||   |
| Machine types | Per instance | Hyperdisk per instance | Hyperdisk Balanced | Hyperdisk Throughput | Hyperdisk ML | Hyperdisk Extreme |
|---|---|---|---|---|---|---|
| `c3-highcpu-4` | 128 | 24 | 16 | 24 | 24 | 0 |
| `c3-highcpu-8` | 128 | 32 | 16 | 32 | 32 | 0 |
| `c3-highcpu-22` | 128 | 48 | 32 | 48 | 48 | 0 |
| `c3-highcpu-44` | 128 | 64 | 32 | 64 | 64 | 0 |
| `c3-highcpu-88` | 128 | 64 | 32 | 64 | 64 | 8 |
| `c3-highcpu-176` | 128 | 64 | 32 | 64 | 64 | 8 |
| `c3-highcpu-192-metal` | 16 (Hyperdisk only) | 16 | 16 | Not supported | Not supported | 16 |

### C3 highmem

|   | Maximum number of disks |||||   |
| Machine types | Per instance | Hyperdisk per instance | Hyperdisk Balanced | Hyperdisk Throughput | Hyperdisk ML | Hyperdisk Extreme |
|---|---|---|---|---|---|---|
| `c3-highmem-4` | 128 | 24 | 16 | 24 | 24 | 0 |
| `c3-highmem-8` | 128 | 32 | 16 | 32 | 32 | 0 |
| `c3-highmem-22` | 128 | 48 | 32 | 48 | 48 | 0 |
| `c3-highmem-44` | 128 | 64 | 32 | 64 | 64 | 0 |
| `c3-highmem-88` | 128 | 64 | 32 | 64 | 64 | 8 |
| `c3-highmem-176` | 128 | 64 | 32 | 64 | 64 | 8 |
| `c3-highmem-192-metal` | 16 (Hyperdisk only) | 16 | 16 | Not supported | Not supported | 16 |

### C3 standard

|   | Maximum number of disks |||||   |
| Machine types | Per VM^1^ | Hyperdisk per VM | Hyperdisk Balanced | Hyperdisk Throughput | Hyperdisk ML | Hyperdisk Extreme |
|---|---|---|---|---|---|---|
| `c3-standard-4-lssd` | 128 | 24 | 16 | 24 | 24 | 0 |
| `c3-standard-8-lssd` | 128 | 32 | 16 | 32 | 32 | 0 |
| `c3-standard-22-lssd` | 128 | 48 | 32 | 48 | 48 | 0 |
| `c3-standard-44-lssd` | 128 | 64 | 32 | 64 | 64 | 0 |
| `c3-standard-88-lssd` | 128 | 64 | 32 | 64 | 64 | 8 |
| `c3-standard-176-lssd` | 128 | 64 | 32 | 64 | 64 | 8 |

### Network support for C3 VMs

The following network interface drivers are required:

- C3 VM instances require [gVNIC](https://docs.cloud.google.com/compute/docs/networking/using-gvnic).
- C3 bare metal instances require the [Intel IDPF LAN PF device driver](https://docs.cloud.google.com/compute/docs/networking/using-idpf).

C3 supports up to 100 Gbps network bandwidth for standard networking and up to 200 Gbps with per VM Tier_1 networking performance for VM and bare metal instances.

Before migrating to C3 or creating C3 VMs or bare metal instances, make sure that the [operating system image](https://docs.cloud.google.com/compute/docs/images/os-details#networking) that you use supports the IDPF network driver for bare metal instances or the gVNIC driver for VM instances. To get the best possible performance on C3 VMs, choose an OS image that supports both "Tier_1 Networking" and "200 Gbps network bandwidth". These images include an updated gVNIC driver, even if the guest OS shows the `gve` driver version as 1.0.0. If your C3 VM is using an operating system with an older version of gVNIC driver, this is still supported but the VM might experience suboptimal performance such as less network bandwidth or higher latency.

If you use a custom OS image to create a C3 VM, you can [manually install the most recent gVNIC driver](https://docs.cloud.google.com/compute/docs/networking/using-gvnic#manual-gvnic-setup). The gVNIC driver version v1.4.2 or later is recommended for use with C3 VMs. Google recommends using the latest gVNIC driver version to benefit from additional features and bug fixes.

### Maintenance experience for C3 instances

During the [lifecycle of a Compute Engine instance](https://docs.cloud.google.com/compute/docs/instances/instance-lifecycle), the host machine that your instance runs on undergoes multiple *host events*. A host event can include the regular maintenance of Compute Engine infrastructure, or in rare cases, a host error. Compute Engine also applies some non-disruptive lightweight upgrades for the hypervisor and network in the background.

The C3 machine series offers the following features related to host maintenance:

| Machine type | Typical scheduled maintenance event frequency | [Maintenance behavior](https://docs.cloud.google.com/compute/docs/instances/host-maintenance-overview#maintenance_behaviors) | [Advanced notification](https://docs.cloud.google.com/compute/docs/instances/monitor-plan-host-maintenance-event) | [On-demand maintenance](https://docs.cloud.google.com/compute/docs/instances/trigger-host-maintenance-event) |
|---|---|---|---|---|
| C3 with Confidential VM | Minimum of 30 days | Terminate | 7 days | No |
| `c3-*-lssd` | Minimum of 30 days | Live migrate | 7 days | Yes |
| `c3-*-176` | Minimum of 30 days | Live migrate | 7 days | Yes |
| `c3-*-192-metal` | Minimum of 30 days | Terminate | 7 days | Yes |
| All others | Minimum of 30 days | Live migrate | 7 days | No |

The maintenance frequencies shown in the previous table are approximations, not guarantees. Compute Engine might occasionally perform maintenance more frequently.

## N2D machine series

The N2D machine series runs on the third generation [AMD EPYC Milan processor](https://www.amd.com/en/products/processors/server/epyc/7003-series.html) is available only in specific [regions and zones](https://docs.cloud.google.com/compute/docs/regions-zones).

The N2D series provides some of the largest general-purpose machine types with up to 224 vCPUs and 896 GB of memory and vCPU to memory ratios of 1:1, 1:4, and 1:8.

In summary, the N2D series:

- Support up to 224 vCPUs and 896 GB of memory.
- Support 50 Gbps and 100 Gbps [high-bandwidth network configurations](https://docs.cloud.google.com/compute/docs/networking/configure-vm-with-high-bandwidth-configuration).
- Available in predefined and [custom VMs](https://docs.cloud.google.com/compute/docs/general-purpose-machines#custom_machine_types).
- Offer higher memory-to-core ratios for VMs created with the extended memory feature. Using the extended memory feature helps you avoid per-CPU software licensing costs while providing access to more than 8 GB of memory per vCPU.
- Powered by the third generation AMD EPYC Milan processor.
- Supports the following discount and consumption options:
  - [Resource-based and flexible committed use discounts (CUDs)](https://docs.cloud.google.com/compute/docs/instances/committed-use-discounts-overview)
  - [Sustained use discounts (SUDs)](https://docs.cloud.google.com/compute/docs/sustained-use-discounts)
  - [Spot VMs](https://docs.cloud.google.com/compute/docs/instances/spot)
  - [Reservations](https://docs.cloud.google.com/compute/docs/instances/choose-reservation-type)
- Doesn't support GPUs or nested virtualization.
- Supports [Confidential VM](https://docs.cloud.google.com/confidential-computing/confidential-vm/docs/confidential-vm-overview) with AMD SEV and AMD SEV-SNP.

N2D VMs don't support GPUs or nested virtualization.

### N2D machine types

The following table lists the features of the N2D machine series. For some machine types, certain features are not applicable (N/A).

The amount of memory configured per vCPU differs depending on the machine type:

- `standard`: 4 GB of system memory per vCPU
- `highmem`: 8 GB of system memory per vCPU
- `highcpu`: 1 GB of system memory per vCPU

### N2D standard

| Machine types | vCPUs^1^ | Memory (GB) | Local SSD^2^ | Default egress bandwidth (Gbps)^3^ | Tier_1 egress bandwidth (Gbps)^4^ |
|---|---|---|---|---|---|
| `n2d-standard-2` | 2 | 8 | 1, 2, 4, 8, 16, or 24 | Up to 10 | N/A |
| `n2d-standard-4` | 4 | 16 | 1, 2, 4, 8, 16, or 24 | Up to 10 | N/A |
| `n2d-standard-8` | 8 | 32 | 1, 2, 4, 8, 16, or 24 | Up to 16 | N/A |
| `n2d-standard-16` | 16 | 64 | 1, 2, 4, 8, 16, or 24 | Up to 32 | N/A |
| `n2d-standard-32` | 32 | 128 | 2, 4, 8, 16, or 24 | Up to 32 | N/A |
| `n2d-standard-48` | 48 | 192 | 2, 4, 8, 16, or 24 | Up to 32 | Up to 50 |
| `n2d-standard-64` | 64 | 256 | 4, 8, 16, or 24 | Up to 32 | Up to 50 |
| `n2d-standard-80` | 80 | 320 | 4, 8, 16, or 24 | Up to 32 | Up to 50 |
| `n2d-standard-96` | 96 | 384 | 8, 16, or 24 | Up to 32 | Up to 100 |
| `n2d-standard-128` | 128 | 512 | 8, 16, or 24 | Up to 32 | Up to 100 |
| `n2d-standard-224` | 224 | 896 | 8, 16, or 24 | Up to 32 | Up to 100 |

^1^ Each CPU uses two threads per core. A vCPU is implemented as a single hardware thread on one of the available [CPU platforms](https://docs.cloud.google.com/compute/docs/cpu-platforms).   
^2^ Number of 375 GiB Local SSD disks that you can choose to add when creating the instance.  
^3^ Maximum egress bandwidth cannot exceed the number given. Actual egress bandwidth depends on the destination IP address and other factors. See [Network bandwidth](https://docs.cloud.google.com/compute/docs/network-bandwidth).  
^4^ Supports [high-bandwidth networking](https://docs.cloud.google.com/compute/docs/networking/configure-vm-with-high-bandwidth-configuration) for larger machine types. For Windows OS images, the maximum network bandwidth is limited to 50 Gbps.

### N2D high-mem

| Machine types | vCPUs^1^ | Memory (GB) | Local SSD^2^ | Default egress bandwidth (Gbps)^3^ | Tier_1 egress bandwidth (Gbps)^4^ |
|---|---|---|---|---|---|
| `n2d-highmem-2` | 2 | 16 | 1, 2, 4, 8, 16, or 24 | Up to 10 | N/A |
| `n2d-highmem-4` | 4 | 32 | 1, 2, 4, 8, 16, or 24 | Up to 10 | N/A |
| `n2d-highmem-8` | 8 | 64 | 1, 2, 4, 8, 16, or 24 | Up to 16 | N/A |
| `n2d-highmem-16` | 16 | 128 | 1, 2, 4, 8, 16, or 24 | Up to 32 | N/A |
| `n2d-highmem-32` | 32 | 256 | 2, 4, 8, 16, or 24 | Up to 32 | N/A |
| `n2d-highmem-48` | 48 | 384 | 2, 4, 8, 16, or 24 | Up to 32 | Up to 50 |
| `n2d-highmem-64` | 64 | 512 | 4, 8, 16, or 24 | Up to 32 | Up to 50 |
| `n2d-highmem-80` | 80 | 640 | 4, 8, 16, or 24 | Up to 32 | Up to 50 |
| `n2d-highmem-96` | 96 | 768 | 8, 16, or 24 | Up to 32 | Up to 100 |

^1^ Each CPU uses two threads per core. A vCPU is implemented as a single hardware thread on one of the available [CPU platforms](https://docs.cloud.google.com/compute/docs/cpu-platforms).   
^2^ Number of 375 GiB Local SSD disks that you can choose to add when creating the instance.  
^3^ Maximum egress bandwidth cannot exceed the number given. Actual egress bandwidth depends on the destination IP address and other factors. See [Network bandwidth](https://docs.cloud.google.com/compute/docs/network-bandwidth).  
^4^ Supports [high-bandwidth networking](https://docs.cloud.google.com/compute/docs/networking/configure-vm-with-high-bandwidth-configuration) for larger machine types. For Windows OS images, the maximum network bandwidth is limited to 50 Gbps.

### N2D high-cpu

| Machine types | vCPUs^1^ | Memory (GB) | Local SSD^2^ | Default egress bandwidth (Gbps)^3^ | Tier_1 egress bandwidth (Gbps)^4^ |
|---|---|---|---|---|---|
| `n2d-highcpu-2` | 2 | 2 | 1, 2, 4, 8, 16, or 24 | Up to 10 | N/A |
| `n2d-highcpu-4` | 4 | 4 | 1, 2, 4, 8, 16, or 24 | Up to 10 | N/A |
| `n2d-highcpu-8` | 8 | 8 | 1, 2, 4, 8, 16, or 24 | Up to 16 | N/A |
| `n2d-highcpu-16` | 16 | 16 | 1, 2, 4, 8, 16, or 24 | Up to 32 | N/A |
| `n2d-highcpu-32` | 32 | 32 | 2, 4, 8, 16, or 24 | Up to 32 | N/A |
| `n2d-highcpu-48` | 48 | 48 | 2, 4, 8, 16, or 24 | Up to 32 | Up to 50 |
| `n2d-highcpu-64` | 64 | 64 | 4, 8, 16, or 24 | Up to 32 | Up to 50 |
| `n2d-highcpu-80` | 80 | 80 | 4, 8, 16, or 24 | Up to 32 | Up to 50 |
| `n2d-highcpu-96` | 96 | 96 | 8, 16, or 24 | Up to 32 | Up to 100 |
| `n2d-highcpu-128` | 128 | 128 | 8, 16, or 24 | Up to 32 | Up to 100 |
| `n2d-highcpu-224` | 224 | 224 | 8, 16, or 24 | Up to 32 | Up to 100 |

^1^ Each CPU uses two threads per core. A vCPU is implemented as a single hardware thread on one of the available [CPU platforms](https://docs.cloud.google.com/compute/docs/cpu-platforms).   
^2^ Number of 375 GiB Local SSD disks that you can choose to add when creating the instance.  
^3^ Maximum egress bandwidth cannot exceed the number given. Actual egress bandwidth depends on the destination IP address and other factors. See [Network bandwidth](https://docs.cloud.google.com/compute/docs/network-bandwidth).  
^4^ Supports [high-bandwidth networking](https://docs.cloud.google.com/compute/docs/networking/configure-vm-with-high-bandwidth-configuration) for larger machine types. For Windows OS images, the maximum network bandwidth is limited to 50 Gbps.

For details on the pricing information, see the following:

- For machine type pricing, see [VM pricing page](https://docs.cloud.google.com/compute/vm-instance-pricing#n2d_machine_types).
- Disk usage and network usage is charged separately from machine type pricing. For details, see [Disk and image pricing](https://docs.cloud.google.com/compute/disks-image-pricing#disks) and [Network pricing](https://cloud.google.com/vpc/network-pricing).
- For per VM Tier_1 network performance billing rates, see [Tier_1 higher bandwidth network pricing](https://docs.cloud.google.com/compute/vm-instance-pricing#high_bandwidth_configuration).

### Supported disk types for N2D

N2D VMs can use the following block storage types:

- Zonal and regional standard Persistent Disk (`pd-standard`)
- Zonal and regional balanced Persistent Disk (`pd-balanced`)
- Zonal and regional SSD Persistent Disk (`pd-ssd`)
- Hyperdisk Throughput (`hyperdisk-throughput`)
- Local SSD

### N2D standard

| Machine types | Max number of disks per VM, across all disks^1^ | Max number of Hyperdisk volumes per VM^2^ | Max total disk size (TiB) across all disks^3^ |
|---|---|---|---|
| `n2d-standard-2` | 128 | 20 | 257 |
| `n2d-standard-4` | 128 | 24 | 257 |
| `n2d-standard-8` | 128 | 32 | 257 |
| `n2d-standard-16` | 128 | 48 | 257 |
| `n2d-standard-32` | 128 | 64 | 512 |
| `n2d-standard-48` | 128 | 64 | 512 |
| `n2d-standard-64` | 128 | 64 | 512 |
| `n2d-standard-80` | 128 | 64 | 512 |
| `n2d-standard-96` | 128 | 64 | 512 |
| `n2d-standard-128` | 128 | 64 | 512 |
| `n2d-standard-224` | 128 | 64 | 512 |

^1^ The maximum size per Persistent Disk volume is 64 TiB.

^2^The maximum size per Hyperdisk Throughput volume is 32 TiB.
^3^ The maximum total disk size applies to all Persistent Disk and Hyperdisk disk types attached to the VM.

<br />

### N2D high-mem

| Machine types | Max number of disks per VM, across all disks^1^ | Max number of Hyperdisk volumes per VM^2^ | Max total disk size (TiB) across all disks^3^ |
|---|---|---|---|
| `n2d-highmem-2` | 128 | 20 | 257 |
| `n2d-highmem-4` | 128 | 24 | 257 |
| `n2d-highmem-8` | 128 | 32 | 257 |
| `n2d-highmem-16` | 128 | 48 | 257 |
| `n2d-highmem-32` | 128 | 64 | 512 |
| `n2d-highmem-48` | 128 | 64 | 512 |
| `n2d-highmem-64` | 128 | 64 | 512 |
| `n2d-highmem-80` | 128 | 64 | 512 |
| `n2d-highmem-96` | 128 | 64 | 512 |

^1^ The maximum size per Persistent Disk volume is 64 TiB.

^2^The maximum size per Hyperdisk Throughput volume is 32 TiB.
^3^ The maximum total disk size applies to all Persistent Disk and Hyperdisk disk types attached to the VM.

<br />

### N2D high-cpu

| Machine types | Max number of disks per VM, across all disks^1^ | Max number of Hyperdisk volumes per VM^2^ | Max total disk size (TiB) across all disks^3^ |
|---|---|---|---|
| `n2d-highcpu-2` | 128 | 20 | 257 |
| `n2d-highcpu-4` | 128 | 24 | 257 |
| `n2d-highcpu-8` | 128 | 32 | 257 |
| `n2d-highcpu-16` | 128 | 48 | 257 |
| `n2d-highcpu-32` | 128 | 64 | 512 |
| `n2d-highcpu-48` | 128 | 64 | 512 |
| `n2d-highcpu-64` | 128 | 64 | 512 |
| `n2d-highcpu-80` | 128 | 64 | 512 |
| `n2d-highcpu-96` | 128 | 64 | 512 |
| `n2d-highcpu-128` | 128 | 64 | 512 |
| `n2d-highcpu-224` | 128 | 64 | 512 |

^1^ The maximum size per Persistent Disk volume is 64 TiB.

^2^The maximum size per Hyperdisk Throughput volume is 32 TiB.
^3^ The maximum total disk size applies to all Persistent Disk and Hyperdisk disk types attached to the VM.

<br />

## N2 machine series

The N2 machine series has flexible sizing between 2 to 128 vCPUs and 0.5 to 8 GB of memory per vCPU. Machine types in this series run on the following processors:

- Ice Lake---offered in specific [regions and zones](https://docs.cloud.google.com/compute/docs/regions-zones). It is the default processor for larger machine types.

- Cascade Lake---the default for machine types up to 80 vCPUs. If you want to create VMs with `Ice Lake`, you must set it as the [minimum CPU platform](https://docs.cloud.google.com/compute/docs/instances/specify-min-cpu-platform#startinginstancewithmincpuplatform).

You can find more details about these two processors on the [CPU platforms](https://docs.cloud.google.com/compute/docs/cpu-platforms#intel_cpu_processors) page.

Workloads that can take advantage of the higher clock frequency are a good choice for this series. These workloads can get higher per-thread performance while benefiting from all the flexibility that the general-purpose machine family offers.

In summary, the N2 machine series:

- Supports up to 128 vCPUs and 864 GB of memory.
- Supports 50 Gbps, 75 Gbps, and 100 Gbps [high-bandwidth network configurations](https://docs.cloud.google.com/compute/docs/networking/configure-vm-with-high-bandwidth-configuration).
- Is available in predefined and [custom VMs](https://docs.cloud.google.com/compute/docs/general-purpose-machines#custom_machine_types).
- Has higher memory-to-core ratios for VMs created with the extended memory feature. Using the extended memory feature helps control per-CPU software licensing costs while providing access to more than 8 GB of memory per vCPU.
- Supports the following discount and consumption options:
  - [Resource-based and flexible committed use discounts (CUDs)](https://docs.cloud.google.com/compute/docs/instances/committed-use-discounts-overview)
  - [Sustained use discounts (SUDs)](https://docs.cloud.google.com/compute/docs/sustained-use-discounts)
  - [Spot VMs](https://docs.cloud.google.com/compute/docs/instances/spot)
  - [Reservations](https://docs.cloud.google.com/compute/docs/instances/choose-reservation-type)

### N2 machine types

The amount of memory configured per vCPU differs depending on the machine type:

- `standard`: 4 GB of system memory per vCPU
- `highmem`: 8 GB of system memory per vCPU
- `highcpu`: 1 GB of system memory per vCPU

### N2 standard

| Machine types | vCPUs^1^ | Memory (GB) | Local SSD^2^ | Default egress bandwidth (Gbps)^3^ | Tier_1 egress bandwidth (Gbps)^4^ |
|---|---|---|---|---|---|
| `n2-standard-2` | 2 | 8 | 1, 2, 4, 8, 16, or 24 | Up to 10 | N/A |
| `n2-standard-4` | 4 | 16 | 1, 2, 4, 8, 16, or 24 | Up to 10 | N/A |
| `n2-standard-8` | 8 | 32 | 1, 2, 4, 8, 16, or 24 | Up to 16 | N/A |
| `n2-standard-16` | 16 | 64 | 2, 4, 8, 16, or 24 | Up to 32 | N/A |
| `n2-standard-32` | 32 | 128 | 4, 8, 16, or 24 | Up to 32 | Up to 50 |
| `n2-standard-48` | 48 | 192 | 8, 16, or 24 | Up to 32 | Up to 50 |
| `n2-standard-64` | 64 | 256 | 8, 16, or 24 | Up to 32 | Up to 75 |
| `n2-standard-80` | 80 | 320 | 8, 16, or 24 | Up to 32 | Up to 100 |
| `n2-standard-96` | 96 | 384 | 16 or 24 | Up to 32 | Up to 100 |
| `n2-standard-128` | 128 | 512 | 16 or 24 | Up to 32 | Up to 100 |

^1^ Each CPU uses two threads per core. A vCPU is implemented as a single hardware thread on one of the available [CPU platforms](https://docs.cloud.google.com/compute/docs/cpu-platforms).  
^2^ Number of 375 GiB Local SSD disks that you can choose to add when creating the instance.  
^3^ Maximum egress bandwidth cannot exceed the number given. Actual egress bandwidth depends on the destination IP address and other factors. See [Network bandwidth](https://docs.cloud.google.com/compute/docs/network-bandwidth).  
^4^ Supports [high-bandwidth networking](https://docs.cloud.google.com/compute/docs/networking/configure-vm-with-high-bandwidth-configuration) for larger machine types. For Windows OS images, the maximum network bandwidth is limited to 50 Gbps.

### N2 high-mem

| Machine types | vCPUs^1^ | Memory (GB) | Local SSD^2^ | Default egress bandwidth (Gbps)^3^ | Tier_1 egress bandwidth (Gbps)^4^ |
|---|---|---|---|---|---|
| `n2-highmem-2` | 2 | 16 | 1, 2, 4, 8, 16, or 24 | Up to 10 | N/A |
| `n2-highmem-4` | 4 | 32 | 1, 2, 4, 8, 16, or 24 | Up to 10 | N/A |
| `n2-highmem-8` | 8 | 64 | 1, 2, 4, 8, 16, or 24 | Up to 16 | N/A |
| `n2-highmem-16` | 16 | 128 | 1, 2, 4, 8, 16, or 24 | Up to 32 | N/A |
| `n2-highmem-32` | 32 | 256 | 4, 8, 16, or 24 | Up to 32 | Up to 50 |
| `n2-highmem-48` | 48 | 384 | 8, 16, or 24 | Up to 32 | Up to 50 |
| `n2-highmem-64` | 64 | 512 | 8, 16, or 24 | Up to 32 | Up to 75 |
| `n2-highmem-80` | 80 | 640 | 8, 16, or 24 | Up to 32 | Up to 100 |
| `n2-highmem-96` | 96 | 768 | 16 or 24 | Up to 32 | Up to 100 |
| `n2-highmem-128` | 128 | 864 | 16 or 24 | Up to 32 | Up to 100 |

^1^ Each CPU uses two threads per core. A vCPU is implemented as a single hardware thread on one of the available [CPU platforms](https://docs.cloud.google.com/compute/docs/cpu-platforms).  
^2^ Number of 375 GiB Local SSD disks that you can choose to add when creating the instance.  
^3^ Maximum egress bandwidth cannot exceed the number given. Actual egress bandwidth depends on the destination IP address and other factors. See [Network bandwidth](https://docs.cloud.google.com/compute/docs/network-bandwidth).  
^4^ Supports [high-bandwidth networking](https://docs.cloud.google.com/compute/docs/networking/configure-vm-with-high-bandwidth-configuration) for larger machine types. For Windows OS images, the maximum network bandwidth is limited to 50 Gbps.

### N2 high-cpu

| Machine types | vCPUs^1^ | Memory (GB) | Local SSD^2^ | Default egress bandwidth (Gbps)^3^ | Tier_1 egress bandwidth (Gbps)^4^ |
|---|---|---|---|---|---|
| `n2-highcpu-2` | 2 | 2 | 1, 2, 4, 8, 16, or 24 | Up to 10 | N/A |
| `n2-highcpu-4` | 4 | 4 | 1, 2, 4, 8, 16, or 24 | Up to 10 | N/A |
| `n2-highcpu-8` | 8 | 8 | 1, 2, 4, 8, 16, or 24 | Up to 16 | N/A |
| `n2-highcpu-16` | 16 | 16 | 2, 4, 8, 16, or 24 | Up to 32 | N/A |
| `n2-highcpu-32` | 32 | 32 | 4, 8, 16, or 24 | Up to 32 | Up to 50 |
| `n2-highcpu-48` | 48 | 48 | 8, 16, or 24 | Up to 32 | Up to 50 |
| `n2-highcpu-64` | 64 | 64 | 8, 16, or 24 | Up to 32 | Up to 75 |
| `n2-highcpu-80` | 80 | 80 | 8, 16, or 24 | Up to 32 | Up to 100 |
| `n2-highcpu-96` | 96 | 96 | 16 or 24 | Up to 32 | Up to 100 |

^1^ Each CPU uses two threads per core. A vCPU is implemented as a single hardware thread on one of the available [CPU platforms](https://docs.cloud.google.com/compute/docs/cpu-platforms).  
^2^ Number of 375 GiB Local SSD disks that you can choose to add when creating the instance.  
^3^ Maximum egress bandwidth cannot exceed the number given. Actual egress bandwidth depends on the destination IP address and other factors. See [Network bandwidth](https://docs.cloud.google.com/compute/docs/network-bandwidth).  
^4^ Supports [high-bandwidth networking](https://docs.cloud.google.com/compute/docs/networking/configure-vm-with-high-bandwidth-configuration) for larger machine types. For Windows OS images, the maximum network bandwidth is limited to 50 Gbps.

For details on the pricing information, see the following:

- For machine type pricing, see [VM pricing page](https://docs.cloud.google.com/compute/vm-instance-pricing#n2_predefined).
- Disk usage and network usage is charged separately from machine type pricing. For details, see [Disk and image pricing](https://docs.cloud.google.com/compute/disks-image-pricing#disks) and [Network pricing](https://cloud.google.com/vpc/network-pricing).
- For per VM Tier_1 network performance billing rates, see [Tier_1 higher bandwidth network pricing](https://docs.cloud.google.com/compute/vm-instance-pricing#high_bandwidth_configuration).

### Supported disk types for N2

N2 VMs can use the following block storage types:

- Zonal and regional standard Persistent Disk (`pd-standard`)
- Zonal and regional balanced Persistent Disk (`pd-balanced`)
- Zonal and regional SSD Persistent Disk (`pd-ssd`)
- Extreme Persistent Disk (`pd-extreme`)
- Hyperdisk Extreme (`hyperdisk-extreme`). Not supported with custom N2 machine types.
- Hyperdisk Throughput (`hyperdisk-throughput`)
- Local SSD

### N2 standard

| Machine types | Max number of disks per VM, across all disks^1^ | Max number of Hyperdisk Extreme volumes per VM^2^ | Max number of Hyperdisk Throughput volumes per VM^2^ | Max total disk size (TiB) across all disks^3^ |
|---|---|---|---|---|
| `n2-standard-2` | 128 | 0 | 20 | 257 |
| `n2-standard-4` | 128 | 0 | 24 | 257 |
| `n2-standard-8` | 128 | 0 | 32 | 257 |
| `n2-standard-16` | 128 | 0 | 48 | 257 |
| `n2-standard-32` | 128 | 0 | 64 | 512 |
| `n2-standard-48` | 128 | 0 | 64 | 512 |
| `n2-standard-64` | 128 | 0 | 64 | 512 |
| `n2-standard-80` | 128 | 8 | 64 | 512 |
| `n2-standard-96` | 128 | 8 | 64 | 512 |
| `n2-standard-128` | 128 | 8 | 64 | 512 |

^1^ The maximum size per Persistent Disk volume is 64 TiB.

^2^ The maximum size per Hyperdisk Extreme volume is 64 TiB. The maximum size per Hyperdisk Throughput volume is 32 TiB.

^3^ You can attach a mixture of Hyperdisk and Persistent Disk volumes to a VM, but the total Persistent Disk capacity can't exceed 257 TiB.

### N2 high-mem

| Machine types | Max number of disks per VM, across all disks^\*^ | Max number of Hyperdisk Extreme volumes per VM^†^ | Max number of Hyperdisk Throughput volumes per VM^†^ | Max total disk size (TiB) across all disks^‡^ |
|---|---|---|---|---|
| `n2-highmem-2` | 128 | 0 | 20 | 257 |
| `n2-highmem-4` | 128 | 0 | 24 | 257 |
| `n2-highmem-8` | 128 | 0 | 32 | 257 |
| `n2-highmem-16` | 128 | 0 | 48 | 257 |
| `n2-highmem-32` | 128 | 0 | 64 | 512 |
| `n2-highmem-48` | 128 | 0 | 64 | 512 |
| `n2-highmem-64` | 128 | 0 | 64 | 512 |
| `n2-highmem-80` | 128 | 8 | 64 | 512 |
| `n2-highmem-96` | 128 | 8 | 64 | 512 |
| `n2-highmem-128` | 128 | 8 | 64 | 512 |

^1^ The maximum size per Persistent Disk volume is 64 TiB.

^2^ The maximum size per Hyperdisk Extreme volume is 64 TiB. The maximum size per Hyperdisk Throughput volume is 32 TiB.

^3^ You can attach a mixture of Hyperdisk and Persistent Disk volumes to a VM, but the total Persistent Disk capacity can't exceed 257 TiB.

### N2 high-cpu

| Machine types | Max number of disks per VM, across all disks^\*^ | Max number of Hyperdisk Extreme volumes per VM^†^ | Max number of Hyperdisk Throughput volumes per VM^†^ | Max total disk size (TiB) across all disks^‡^ |
|---|---|---|---|---|
| `n2-highcpu-2` | 128 | 0 | 20 | 257 |
| `n2-highcpu-4` | 128 | 0 | 24 | 257 |
| `n2-highcpu-8` | 128 | 0 | 32 | 257 |
| `n2-highcpu-16` | 128 | 0 | 48 | 257 |
| `n2-highcpu-32` | 128 | 0 | 64 | 512 |
| `n2-highcpu-48` | 128 | 0 | 64 | 512 |
| `n2-highcpu-64` | 128 | 0 | 64 | 512 |
| `n2-highcpu-80` | 128 | 8 | 64 | 512 |
| `n2-highcpu-96` | 128 | 8 | 64 | 512 |

^1^ The maximum size per Persistent Disk volume is 64 TiB.

^2^ The maximum size per Hyperdisk Extreme volume is 64 TiB. The maximum size per Hyperdisk Throughput volume is 32 TiB.

^3^ You can attach a mixture of Hyperdisk and Persistent Disk volumes to a VM, but the total Persistent Disk capacity can't exceed 257 TiB.

## E2 machine series

The cost-optimized E2 machine series have between 2 to 32 vCPUs with a ratio of 0.5 GB to 8 GB of memory per vCPU for standard VMs, and 0.25 to 1 vCPUs with 0.5 GB to 8 GB of memory for shared-core E2 machine types. The E2 machine series offers both Intel and AMD EPYC processors. The processor is selected for you at the time of VM creation. Machine types in this series are available in all regions and zones and support a [virtio memory balloon device](https://docs.cloud.google.com/compute/docs/dynamic-resource-management#virtio-memory-device).

In summary, the E2 machine series:

- Supports up to 32 vCPUs and 128 GB of memory.
- Supports Intel and AMD EPYC Milan processors.
- Is available in predefined and [custom VMs](https://docs.cloud.google.com/compute/docs/general-purpose-machines#custom_machine_types).
- Offers the lowest on demand pricing across the general-purpose machine types.
- Supports the following discount and consumption options:
  - [Resource-based and flexible committed use discounts (CUDs)](https://docs.cloud.google.com/compute/docs/instances/committed-use-discounts-overview)
  - [Spot VMs](https://docs.cloud.google.com/compute/docs/instances/spot)
  - [Reservations](https://docs.cloud.google.com/compute/docs/instances/choose-reservation-type)
- Doesn't offer [sustained use discounts (SUDs)](https://docs.cloud.google.com/compute/docs/sustained-use-discounts); however, it provides consistently low on-demand and committed-use pricing.
- Doesn't support GPUs, Local SSDs, sole-tenant nodes, or nested virtualization.

### Shared-core VMs

E2 shared-core machine types are cost-effective, have a virtio memory balloon device, and are ideal for small workloads. The E2 machine series shared-core machine types use context-switching for multi-tasking, and time-share a single physical core for a specific fraction of time. Different shared-core machine types sustain different amounts of time on a physical core.

- `e2-micro` sustains 2 vCPUs, each for 12.5% of [CPU time](https://wikipedia.org/wiki/CPU_time) totaling 25% CPU time.
- `e2-small` sustains 2 vCPUs, each at 25% of CPU time, totaling 50% CPU time.
- `e2-medium` sustains 2 vCPUs, each at 50% of CPU time, totaling 100% CPU time.

Unlike predefined machine types and custom machine types, shared-core machine types have a predefined price that includes both vCPUs and memory. For more information, see [VM instance pricing](https://docs.cloud.google.com/compute/vm-instance-pricing#e2_sharedcore_machine_types).

#### CPU bursting

Shared-core machine types offer bursting capabilities that allow instances to use additional physical CPU for short periods of time. Bursting happens automatically when your VM requires more physical CPU than originally allocated. During these spikes, each vCPU can burst up to 100% of CPU time, for short periods, before returning to their normal CPU time sharing limitations. Note that bursts are not permanent and are only possible periodically.

`e2-micro`, `e2-small`, and `e2-medium` shared-core VMs can burst for dozens of seconds. If the CPU is utilized at 100%, then the burst lasts as follows:

- `e2-micro`: 30 seconds
- `e2-small`: 60 seconds
- `e2-medium` 120 seconds

The exact burst time is determined by a [Token bucket](https://wikipedia.org/wiki/Token_bucket) meaning utilizing the CPU less than 100% will result in longer bursts.

Bursting doesn't incur any additional charges. You are charged the listed on-demand price for E2 shared-core and N1 `f1-micro`, and `g1-small` shared-core VMs.

### E2 Limitations

- The E2 machine series doesn't offer sustained use discounts (SUDs); however, it provides consistently low on-demand and committed-use pricing.
- The E2 machine series doesn't support GPUs, Local SSDs, sole-tenant nodes, or nested virtualization.

### E2 machine types

E2 is available in `standard`, `highmem`, and `highcpu` configurations, as well as shared-core machine type. In general, E2 shared-core machine types can be more cost-effective for running small, non-resource intensive applications than standard, high-memory, or high-CPU machine types.

The amount of memory configured per vCPU differs depending on the machine type:

- `standard`: 4 GB of system memory per vCPU
- `highmem`: 8 GB of system memory per vCPU
- `highcpu`: 1 GB of system memory per vCPU
- Shared core:
  - `micro`: 0.5 GB of system memory per vCPU
  - `small`: 1 GB of system memory per vCPU
  - `medium`: 2 GB of system memory per vCPU

### E2 standard

| Machine types | vCPUs | Memory (GB) | Local SSD | Max number of Persistent Disk (PDs)^1^ | Max total PD size (TiB) | Maximum egress bandwidth (Gbps)^2^ |
|---|---|---|---|---|---|---|
| `e2-standard-2` | 2 | 8 | No | 128 | 257 | Up to 4 |
| `e2-standard-4` | 4 | 16 | No | 128 | 257 | Up to 8 |
| `e2-standard-8` | 8 | 32 | No | 128 | 257 | Up to 16 |
| `e2-standard-16` | 16 | 64 | No | 128 | 257 | Up to 16 |
| `e2-standard-32` | 32 | 128 | No | 128 | 257 | Up to 16 |

^1^ Persistent Disk and Hyperdisk usage is charged separately from [machine pricing](https://cloud.google.com/compute/vm-instance-pricing).  
^2^ Maximum egress bandwidth cannot exceed the number given. Actual See [Network bandwidth](https://docs.cloud.google.com/compute/docs/network-bandwidth).

### E2 high-mem

| Machine types | vCPUs | Memory (GB) | Local SSD | Max number of Persistent Disk (PDs)^1^ | Max total Persistent Disk size (TiB) | Maximum egress bandwidth (Gbps)^2^ |
|---|---|---|---|---|---|---|
| `e2-highmem-2` | 2 | 16 | No | 128 | 257 | Up to 4 |
| `e2-highmem-4` | 4 | 32 | No | 128 | 257 | Up to 8 |
| `e2-highmem-8` | 8 | 64 | No | 128 | 257 | Up to 16 |
| `e2-highmem-16` | 16 | 128 | No | 128 | 257 | Up to 16 |

^1^ Persistent Disk and Hyperdisk usage is charged separately from [machine pricing](https://cloud.google.com/compute/vm-instance-pricing).  
^2^Maximum egress bandwidth cannot exceed the number given. Actual egress bandwidth depends on the destination IP address and other factors. See [Network bandwidth](https://docs.cloud.google.com/compute/docs/network-bandwidth).

### E2 high-cpu

| Machine types | vCPUs | Memory (GB) | Local SSD | Max number of Persistent Disk (PDs)^1^ | Max total PD size (TiB) | Maximum egress bandwidth (Gbps)^2^ |
|---|---|---|---|---|---|---|
| `e2-highcpu-2` | 2 | 2 | No | 128 | 257 | Up to 4 |
| `e2-highcpu-4` | 4 | 4 | No | 128 | 257 | Up to 8 |
| `e2-highcpu-8` | 8 | 8 | No | 128 | 257 | Up to 16 |
| `e2-highcpu-16` | 16 | 16 | No | 128 | 257 | Up to 16 |
| `e2-highcpu-32` | 32 | 32 | No | 128 | 257 | Up to 16 |

^1^ Persistent Disk and Hyperdisk usage is charged separately from [machine pricing](https://cloud.google.com/compute/vm-instance-pricing).   
^2^ Maximum egress bandwidth cannot exceed the number given. Actual egress bandwidth depends on the destination IP address and other factors. See [Network bandwidth](https://docs.cloud.google.com/compute/docs/network-bandwidth).

### E2 shared-core

| Machine types | vCPUs | Fractional vCPUs^1^ | Memory (GB) | Local SSD | Max number of Persistent Disk (PDs)^2^ | Max total PD size (TiB) | Maximum egress bandwidth (Gbps)^3^ |
|---|---|---|---|---|---|---|---|
| `e2-micro` | 2 | 0.25^1^ | 1 | No | 16 | 3 | Up to 1 |
| `e2-small` | 2 | 0.5^1^ | 2 | No | 16 | 3 | Up to 1 |
| `e2-medium` | 2 | 1^1^ | 4 | No | 16 | 3 | Up to 2 |

^1^ Fractional vCPU of 0.25, 0.5, or 1.0 with 2 vCPUs exposed to the guest operating system.  
^2^ Persistent Disk and Hyperdisk usage is charged separately from [machine pricing](https://cloud.google.com/compute/vm-instance-pricing).   
^3^ Maximum egress bandwidth cannot exceed the number given. Actual egress bandwidth depends on the destination IP address and other factors. See [Network bandwidth](https://docs.cloud.google.com/compute/docs/network-bandwidth).

### Supported disk types for E2 VMs

E2 VMs can use the following block storage types:

- Zonal and regional balanced Persistent Disk (`pd-balanced`)
- Zonal and regional SSD Persistent Disk (`pd-ssd`)
- Zonal and regional standard Persistent Disk (`pd-standard`)

## N1 machine series

The N1 machine series is Compute Engine's first generation general-purpose machine series available on Intel Skylake, Broadwell, Haswell, Sandy Bridge, and Ivy Bridge CPU platforms.

In summary, the N1 machine series offers the following features:

- Supports up to 96 vCPUs and 624 GB of memory.
- Has both predefined machine types and custom machine types. Custom machine types can be created within a wide range of memory-to-core ratio, ranging from 1 GB per vCPU to 6.5 GB per vCPU.
- Offers higher memory-to-core ratios for VMs created with the extended memory feature.
- Supports the following discount and consumption options:
  - [Resource-based and flexible committed use discounts (CUDs)](https://docs.cloud.google.com/compute/docs/instances/committed-use-discounts-overview)
  - [Sustained use discounts (SUDs)](https://docs.cloud.google.com/compute/docs/sustained-use-discounts); N1 machine series offers a higher SUD percentage than the N2 machine series.
  - [Spot VMs](https://docs.cloud.google.com/compute/docs/instances/spot)
  - [Reservations](https://docs.cloud.google.com/compute/docs/instances/choose-reservation-type)
- Supports [Tensor Processing Units (TPUs)](https://docs.cloud.google.com/tpu/docs/tpus) in select [zones](https://docs.cloud.google.com/tpu/docs/types-zones).
- Can support up to [ten virtual interfaces per instance](https://docs.cloud.google.com/vpc/docs/multiple-interfaces-concepts#max-interfaces).

### N1 machine types

N1 is available in `standard`, `highmem`, and `highcpu` configurations, as well as shared-core machine types. Different shared-core machine types sustain different amounts of time on a physical core.

- An `f1-micro` VM instance sustains a single vCPU for up to 20% of [CPU time](https://wikipedia.org/wiki/CPU_time).
- A `g1-small` VM instance sustains a single vCPU for up to 50% of CPU time.

The amount of memory configured per vCPU differs depending on the machine type:

- `standard`: 3.75 GB of system memory per vCPU
- `highmem`: 6.5 GB of system memory per vCPU
- `highcpu`: 0.9 GB of system memory per vCPU
- Shared core:
  - `f1-micro`: 0.6 GB of system memory per vCPU
  - `g1-small`: 1.7 GB of system memory per vCPU

### N1 standard

| Machine types | vCPUs^1^ | Memory (GB) | Local SSD^2^ | Max number of Persistent Disk^3^ | Max total disk size (TiB) | Default egress bandwidth (Gbps)^4^ | Tier_1 egress bandwidth (Gbps) |
|---|---|---|---|---|---|---|---|
| `n1-standard-1` | 1 | 3.75 | 1 to 8, 16, or 24 | 128 | 257 | Up to 2 | N/A |
| `n1-standard-2` | 2 | 7.50 | 1 to 8, 16, or 24 | 128 | 257 | Up to 10 | N/A |
| `n1-standard-4` | 4 | 15 | 1 to 8, 16, or 24 | 128 | 257 | Up to 10 | N/A |
| `n1-standard-8` | 8 | 30 | 1 to 8, 16, or 24 | 128 | 257 | Up to 16 | N/A |
| `n1-standard-16` | 16 | 60 | 1 to 8, 16, or 24 | 128 | 257 | Up to 32^5^ | N/A |
| `n1-standard-32` | 32 | 120 | 1 to 8, 16, or 24 | 128 | 257 | Up to 32^5^ | N/A |
| `n1-standard-64` | 64 | 240 | 1 to 8, 16, or 24 | 128 | 257 | Up to 32^5^ | N/A |
| `n1-standard-96` | 96 | 360 | 1 to 8, 16, or 24 | 128 | 257 | Up to 32^5^ | N/A |

^1^ Each CPU uses two threads per core. A vCPU is implemented as a single hardware thread.  
^2^ Number of 375 GiB Local SSD disks that you can choose to add when creating the instance.  
^3^ Persistent Disk and Hyperdisk usage is charged separately from [machine type pricing](https://cloud.google.com/compute/vm-instance-pricing).   
^4^ Maximum egress bandwidth cannot exceed the number given. Actual egress bandwidth depends on the destination IP address and other factors. See [Network bandwidth](https://docs.cloud.google.com/compute/docs/network-bandwidth).  
^5^ 32 Gbps for Skylake or later [CPU platforms](https://docs.cloud.google.com/compute/docs/cpu-platforms). 16 Gbps for all other platforms.

### N1 high-memory

| Machine types | vCPUs^1^ | Memory (GB) | Local SSD^2^ | Max number of Persistent Disk^3^ | Max total disk size (TiB) | Default egress bandwidth (Gbps)^4^ | Tier_1 egress bandwidth (Gbps) |
|---|---|---|---|---|---|---|---|
| `n1-highmem-2` | 2 | 13 | 1 to 8, 16, or 24 | 128 | 257 | Up to 10 | N/A |
| `n1-highmem-4` | 4 | 26 | 1 to 8, 16, or 24 | 128 | 257 | Up to 10 | N/A |
| `n1-highmem-8` | 8 | 52 | 1 to 8, 16, or 24 | 128 | 257 | Up to 16 | N/A |
| `n1-highmem-16` | 16 | 104 | 1 to 8, 16, or 24 | 128 | 257 | Up to 32^5^ | N/A |
| `n1-highmem-32` | 32 | 208 | 1 to 8, 16, or 24 | 128 | 257 | Up to 32^5^ | N/A |
| `n1-highmem-64` | 64 | 416 | 1 to 8, 16, or 24 | 128 | 257 | Up to 32^5^ | N/A |
| `n1-highmem-96` | 96 | 624 | 1 to 8, 16, or 24 | 128 | 257 | Up to 32^5^ | N/A |

^1^ Each CPU uses two threads per core. A vCPU is implemented as a single hardware thread.  
^2^ Number of 375 GiB Local SSD disks that you can choose to add when creating the instance.  
^3^ Persistent Disk and Hyperdisk usage is charged separately from [machine type pricing](https://cloud.google.com/compute/vm-instance-pricing).   
^4^ Maximum egress bandwidth cannot exceed the number given. Actual egress bandwidth depends on the destination IP address and other factors. See [Network bandwidth](https://docs.cloud.google.com/compute/docs/network-bandwidth).  
^5^ 32 Gbps for Skylake or later [CPU platforms](https://docs.cloud.google.com/compute/docs/cpu-platforms). 16 Gbps for all other platforms.

### N1 high-cpu

| Machine types | vCPUs^1^ | Memory (GB) | Local SSD^2^ | Max number of Persistent Disk^3^ | Max total disk size (TiB) | Default egress bandwidth (Gbps)^4^ | Tier_1 egress bandwidth (Gbps) |
|---|---|---|---|---|---|---|---|
| `n1-highcpu-2` | 2 | 1.80 | 1 to 8, 16, or 24 | 128 | 257 | Up to 10 | N/A |
| `n1-highcpu-4` | 4 | 3.60 | 1 to 8, 16, or 24 | 128 | 257 | Up to 10 | N/A |
| `n1-highcpu-8` | 8 | 7.20 | 1 to 8, 16, or 24 | 128 | 257 | Up to 16 | N/A |
| `n1-highcpu-16` | 16 | 14.4 | 1 to 8, 16, or 24 | 128 | 257 | Up to 32^5^ | N/A |
| `n1-highcpu-32` | 32 | 28.8 | 1 to 8, 16, or 24 | 128 | 257 | Up to 32^5^ | N/A |
| `n1-highcpu-64` | 64 | 57.6 | 1 to 8, 16, or 24 | 128 | 257 | Up to 32^5^ | N/A |
| `n1-highcpu-96` | 96 | 86.4 | 1 to 8, 16, or 24 | 128 | 257 | Up to 32^5^ | N/A |

^1^ Each CPU uses two threads per core. A vCPU is implemented as a single hardware thread.  
^2^ Number of 375 GiB Local SSD disks that you can choose to add when creating the instance.  
^3^ Persistent Disk and Hyperdisk usage is charged separately from [machine type pricing](https://cloud.google.com/compute/vm-instance-pricing).   
^4^ Maximum egress bandwidth cannot exceed the number given. Actual egress bandwidth depends on the destination IP address and other factors. See [Network bandwidth](https://docs.cloud.google.com/compute/docs/network-bandwidth).  
^5^ 32 Gbps for Skylake or later [CPU platforms](https://docs.cloud.google.com/compute/docs/cpu-platforms). 16 Gbps for all other platforms.

### N1 shared-core

| Machine types | vCPUs | Fractional vCPUs^1^ | Memory (GB) | Local SSD | Max number of Persistent Disk^2^ | Max total disk size (TiB) | Maximum egress bandwidth (Gbps)^3^ |
|---|---|---|---|---|---|---|---|
| `f1-micro` | 1 | 0.2^1^ | 0.60 | No | 16 | 3 | Up to 1 |
| `g1-small` | 1 | 0.5^1^ | 1.70 | No | 16 | 3 | Up to 1 |

^1^ Fractional vCPU of 0.2 or 0.5, with 1 vCPU exposed to the guest operating system.  
^2^ Persistent Disk and Hyperdisk usage is charged separately from [VM pricing](https://cloud.google.com/compute/vm-instance-pricing).  
^3^ Maximum egress bandwidth cannot exceed the number given. Actual egress bandwidth depends on the destination IP address and other factors. See [Network bandwidth](https://docs.cloud.google.com/compute/docs/network-bandwidth).

### Supported disk types for N1 VMs

N1 VMs can use the following block storage types:

- Zonal and regional balanced Persistent Disk (`pd-balanced`)
- Zonal and regional SSD Persistent Disk (`pd-ssd`)
- Zonal and regional standard Persistent Disk (`pd-standard`)
- Local SSD disks

## Tau T2A machine series

The Tau T2A machine series runs on the Ampere Altra Arm processor with a base frequency of 3.0 GHz. Tau T2A offers predefined machine types with 1 to 48 vCPUs, supports 4 GB of memory per vCPU, and offers a maximum of 32 Gbps of outbound data transfer.

This series is available only in select [regions and zones](https://docs.cloud.google.com/compute/docs/regions-zones#available).

The Tau T2A machine series doesn't support simultaneous multithreading (SMT); each vCPU is equivalent to an entire core.

### Tau T2A machine types

Tau T2A standard machine types have 4 GB of system memory per vCPU.

| Machine types | vCPUs^\*^ | Memory (GB) | Local SSD | Max number of Persistent Disk (PDs)^†^ | Max total PD size (TiB) | Default egress bandwidth (Gbps)^‡^ | Tier_1 egress bandwidth (Gbps) |
|---|---|---|---|---|---|---|---|
| `t2a-standard-1` | 1 | 4 | No | 128 | 257 | Up to 10 | N/A |
| `t2a-standard-2` | 2 | 8 | No | 128 | 257 | Up to 10 | N/A |
| `t2a-standard-4` | 4 | 16 | No | 128 | 257 | Up to 10 | N/A |
| `t2a-standard-8` | 8 | 32 | No | 128 | 257 | Up to 16 | N/A |
| `t2a-standard-16` | 16 | 64 | No | 128 | 257 | Up to 32 | N/A |
| `t2a-standard-32` | 32 | 128 | No | 128 | 257 | Up to 32 | N/A |
| `t2a-standard-48` | 48 | 192 | No | 128 | 257 | Up to 32 | N/A |

<br />

^1^ SMT is not supported. Each vCPU is equivalent to an entire core. See [CPU platforms](https://docs.cloud.google.com/compute/docs/cpu-platforms).  
^2^ Maximum egress bandwidth cannot exceed the number given. Actual egress bandwidth depends on the destination IP address and other factors. See [Network bandwidth](https://docs.cloud.google.com/compute/docs/network-bandwidth).

<br />

### Tau T2A Limitations

The Tau T2A machine series doesn't support:

- [Custom machine types](https://docs.cloud.google.com/compute/docs/general-purpose-machines#custom_machine_types)
- [Sole tenant nodes](https://docs.cloud.google.com/compute/docs/nodes/sole-tenant-nodes)
- [Nested virtualization](https://docs.cloud.google.com/compute/docs/instances/nested-virtualization/overview)
- [Extreme Persistent Disk](https://docs.cloud.google.com/compute/docs/disks/extreme-persistent-disk)
- [Local SSD](https://docs.cloud.google.com/compute/docs/disks/local-ssd)
- [Regional Persistent Disk](https://docs.cloud.google.com/compute/docs/disks/high-availability-regional-persistent-disk)
- Virtio-SCSI Storage Controller and Virtio-Net Ethernet Adapter
- Windows Server or Windows Client OS
- 32-bit mode EL0 (guest userspace support)
- [Committed use discounts (CUDs)](https://docs.cloud.google.com/compute/docs/instances/committed-use-discounts-overview) or [sustained use discounts (SUDs)](https://docs.cloud.google.com/compute/docs/sustained-use-discounts); however, it offers [Spot VM discounts](https://docs.cloud.google.com/compute/docs/instances/spot).
- [Virtual display devices](https://docs.cloud.google.com/compute/docs/instances/enable-instance-virtual-display#restrictions)

T2A supports the [Secure boot](https://docs.cloud.google.com/compute/shielded-vm/docs/shielded-vm#secure-boot) feature, but not all public OS images for T2A support secure boot.

### Supported disk types for T2A

T2A VMs support only the NVMe disk interface and can use the following block storage types:

- Zonal standard Persistent Disk (`pd-standard`)
- Zonal balanced Persistent Disk (`pd-balanced`)
- Zonal SSD (performance) Persistent Disk (`pd-ssd`)

<br />

For instances running Microsoft Windows and using the NVMe disk interface, the combined number of both Hyperdisk and Persistent Disk attached volumes can't exceed a total of 16 disks. See [Known issues](https://docs.cloud.google.com/compute/docs/troubleshooting/known-issues#windows-disk-attachment). Local SSD volumes are excluded from this issue.

<br />

## Tau T2D machine series

The Tau T2D machine series run on the third generation [AMD EPYC Milan processor](https://www.amd.com/en/products/processors/server/epyc/7003-series.html) with a base frequency of 2.45 GHz, an effective frequency of 2.8 GHz, and a max boost frequency of 3.5 GHz. This series has predefined machine types of up to 60 vCPUs, support 4 GB of memory per vCPU, and a maximum of 32 Gbps outbound data transfer. It also supports the following discount and consumption options:

- [Resource-based committed use discounts (CUDs)](https://docs.cloud.google.com/compute/docs/instances/committed-use-discounts-overview#resource_based)
- [Spot VMs](https://docs.cloud.google.com/compute/docs/instances/spot)
- [Reservations](https://docs.cloud.google.com/compute/docs/instances/choose-reservation-type)

This series is available only in select [regions and zones](https://docs.cloud.google.com/compute/docs/regions-zones#available).

Machine types in the Tau T2D machine series have simultaneous multithreading (SMT) disabled; therefore a vCPU is equivalent to an entire core.

### Tau T2D Limitations

Tau T2D VMs don't support:

- Local SSD
- Regional Persistent Disk
- Custom VMs
- Sole-tenant nodes
- Extreme Persistent Disk
- GPUs
- Nested virtualization
- Flexible CUDs
- Sustained use discounts (SUDs)
- Confidential VMs

### Tau T2D machine types

Tau T2D standard machine types have 4 GB of system memory per vCPU.

| Machine types | vCPUs^\*^ | Memory (GB) | Local SSD | Default egress bandwidth (Gbps)^‡^ | Tier_1 egress bandwidth (Gbps) |
|---|---|---|---|---|---|
| `t2d-standard-1` | 1 | 4 | No | Up to 10 | N/A |
| `t2d-standard-2` | 2 | 8 | No | Up to 10 | N/A |
| `t2d-standard-4` | 4 | 16 | No | Up to 10 | N/A |
| `t2d-standard-8` | 8 | 32 | No | Up to 16 | N/A |
| `t2d-standard-16` | 16 | 64 | No | Up to 32 | N/A |
| `t2d-standard-32` | 32 | 128 | No | Up to 32 | N/A |
| `t2d-standard-48` | 48 | 192 | No | Up to 32 | N/A |
| `t2d-standard-60` | 60 | 240 | No | Up to 32 | N/A |

<br />

^1^ SMT is not supported. Each vCPU is equivalent to an entire core. See [CPU platforms](https://docs.cloud.google.com/compute/docs/cpu-platforms).  
^2^ Maximum egress bandwidth cannot exceed the number given. Actual egress bandwidth depends on the destination IP address and other factors. See [Network bandwidth](https://docs.cloud.google.com/compute/docs/network-bandwidth).

<br />

For details on the pricing information, see the following:

- For machine type pricing, see [VM pricing page](https://docs.cloud.google.com/compute/vm-instance-pricing#t2d_machine_types).
- Disk usage and network usage is charged separately from machine type pricing. For details, see [Disk and image pricing](https://docs.cloud.google.com/compute/disks-image-pricing#disks) and [Network pricing](https://cloud.google.com/vpc/network-pricing).

### Supported disk types for T2D

T2D VMs can use the following block storage types:

- Zonal standard Persistent Disk (`pd-standard`)
- Zonal balanced Persistent Disk (`pd-balanced`)
- Zonal SSD (performance) Persistent Disk (`pd-ssd`)
- Hyperdisk Throughput (`hyperdisk-throughput`)

| Machine types | Max number of disks per VM^\*^ | Max number of Hyperdisk volumes per VM^†^ | Max total disk size (TiB) across all disks^‡^ |
|---|---|---|---|
| `t2d-standard-1` | 128 | 20 | 257 |
| `t2d-standard-2` | 128 | 20 | 257 |
| `t2d-standard-4` | 128 | 24 | 257 |
| `t2d-standard-8` | 128 | 32 | 257 |
| `t2d-standard-16` | 128 | 48 | 257 |
| `t2d-standard-32` | 128 | 64 | 512 |
| `t2d-standard-48` | 128 | 64 | 512 |
| `t2d-standard-60` | 128 | 64 | 512 |

^\*^ The maximum size per Persistent Disk volume is 64 TiB.

^†^The maximum size per Hyperdisk Throughput volume is 32 TiB.

^‡^You can attach a mixture of Hyperdisk and Persistent Disk volumes to a VM, but the total Persistent Disk capacity can't exceed 257 TiB.

## Custom machine types

If none of the predefined machine types in the general-purpose machine family match your workload needs, you can create a VM with a custom machine type.

Creating a VM with a custom machine type is ideal for workloads that require more processing power or more memory, but don't need all of the upgrades that are provided by the next larger predefined machine type.

It costs slightly more to use a custom machine type than an equivalent predefined machine type, and there are limitations in the amount of memory and vCPUs that you can select. The on-demand prices for custom machine types include a 5% premium over the on-demand and commitment prices for predefined machine types.

You can create a VM with a custom machine type for only the N and E machine series in the general-purpose machine family. Custom machine types are not available for the C and Tau machine series. Custom machine types are subject to the same Persistent Disk limits as E2, N2, and N1 predefined machine types. The maximum total Persistent Disk size for each VM is 257 TiB and the max number of Persistent Disk is 128. N4, N4A, and N4D custom machines types are subject to the limitations of [Hyperdisk capacity](https://docs.cloud.google.com/compute/docs/disks/hyperdisk-perf-limits#hyperdisk-capacity)

If a custom machine type doesn't meet your requirements, it's possible to [customize the number of visible CPU cores](https://docs.cloud.google.com/compute/docs/instances/customize-visible-cores) on many machine types. It's also possible to [set the number of threads per core](https://docs.cloud.google.com/compute/docs/instances/set-threads-per-core) for certain machine types. You can make these changes during VM instance creation, or by editing an existing VM instance. Reducing the number of visible cores might impact the cost of your VMs. Be sure to review [pricing](https://docs.cloud.google.com/compute/docs/instances/customize-visible-cores#pricing) prior to making any changes.

Review the following table for the custom machine type limits for each machine series.

### N4A custom machine types

- For N4A custom machine types, you can create a machine type with 1 to 64 vCPUs and memory between 2 and 512 GB. vCPU can be adjusted in increments of 1 vCPU, and memory can be adjusted in increments of 256 MB.
- By default, the memory per vCPU that you can select for a custom machine type is determined by the machine series you use. For the N4A machine series, select between 2 GB and 8 GB per vCPU. You can access more memory beyond the default option by enabling [extended memory.](https://docs.cloud.google.com/compute/docs/instances/creating-instance-with-custom-machine-type#extendedmemory)
- N4A custom machine types are available only in select [regions and zones.](https://docs.cloud.google.com/compute/docs/regions-zones#available)

**Examples of invalid machine types:**

- **2 vCPUs, 1.5 GB of total memory**. Invalid because the total memory is less than the minimum 2 GB for an N4A VM.
- **100 vCPUs, 200 GB of memory**. Invalid because the vCPU count is too large. N4A custom machine types can use a maximum of 64 vCPUs.

**Examples of valid machine types:**

- **36 vCPUs, 72 GB of total memory**. Valid because the amount of memory per vCPU is within the acceptable range of 2 GB to 8 GB per vCPU.
- **5 vCPUs, 14 GB of total memory**. Valid because it has 5 vCPUs, which is in the acceptable range of 1 to 64 vCPUs, and the total memory is a multiple of 256 MB and is within the acceptable range of 2 GB to 8 GB per vCPU.

### N4D custom machine types

- The maximum number of vCPUs allowed for a custom machine type is determined by the machine series you choose. For the N4D machine series, which supports the AMD EPYC Turin platform, you can deploy custom machine types with 2 to 96 vCPUs and 1 to 768 GB of memory.
- You can create N4D custom machine types with 2, 4, 8, or 16 vCPUs. After 16, you can increment the number of vCPUs by 16, up to 96 vCPUs. The minimum acceptable number of vCPUs is 2.
- By default, the memory per vCPU that you can select for a custom machine type is determined by the machine series you choose. For N4D machine types, select between 0.5 GB and 8 GB per vCPU in 256 MB increments. Higher amounts of memory are possible by enabling [extended memory.](https://docs.cloud.google.com/compute/docs/instances/creating-instance-with-custom-machine-type#extendedmemory)
- N4D custom machine types are available only in select [regions and zones.](https://docs.cloud.google.com/compute/docs/regions-zones#available)
- N4D custom machine types are available only with standard networking with a maximum egress limits of 50 Gbps.

**Examples of invalid machine types:**

- **2 vCPUs, 0.4 GB of total memory**. Invalid because the total memory is less than the minimum 1 GB for an N4D VM and not in increments of 256 MB.
- **34 vCPUs, 34 GB of total memory**. Invalid because the total number of vCPUs is not divisible by 16.
- **1 vCPU, 1024 MB of memory**. Invalid because the vCPU count is too small. N4D custom machine types require a minimum of 2 vCPUs.

**Examples of valid machine types:**

- **32 vCPUs, 16 GB of total memory**. Valid because the total number of vCPUs is a multiple of 16 and the total memory is a multiple of 256 MB. The amount of memory per vCPU is 0.5 GB, which satisfies the minimum requirement. Because the number of vCPUs is larger than 8 vCPUs, the number of vCPUs must be divisible by 16.
- **2 vCPUs, 7 GB of total memory**. Valid because it has 2 vCPUs, which is the minimum value, and the total memory is a multiple of 256 MB. The amount of memory per vCPU is also within the acceptable range of 0.5 GB to 8 GB per vCPU.

### N4 custom machine types

- For N4 custom machine types, you can create a machine type with 2 to 80 vCPUs with the vCPUs in multiples of 2, and memory between 4 and 640 GB.
- By default, the memory per vCPU that you can select for a custom machine type is determined by the machine series you use. For the N4 machine series, select between 2 GB and 8 GB per vCPU in 256 MB increments. When creating a standard N4 machine type, the minimum memory you can select is 4 GB. Higher amounts of memory are possible by enabling [extended memory.](https://docs.cloud.google.com/compute/docs/instances/creating-instance-with-custom-machine-type#extendedmemory)

**Examples of invalid machine types:**

- **2 vCPUs, 0.5 GB of total memory**. Invalid because the total memory is less than the minimum 4 GB for an N4 VM.
- **1 vCPU, 8 GB of memory**. Invalid because the vCPU count is too small. N4 custom machine types require a minimum of 2 vCPUs.

**Examples of valid machine types:**

- **36 vCPUs, 72 GB of total memory**. Valid because the total number of vCPUs is even and the total memory is a multiple of 256 MB. The amount of memory per vCPU is also within the acceptable range of 2 GB to 8 GB per vCPU.
- **2 vCPUs, 14 GB of total memory**. Valid because it has 2 vCPUs, which is the minimum value, and the total memory is a multiple of 256 MB. The amount of memory per vCPU is also within the acceptable range of 2 GB to 8 GB per vCPU.

### N2D custom machine types

- The maximum number of vCPUs allowed for a custom machine type is determined by the machine series you choose. For the N2D machine series, which supports the AMD EPYC Milan platform, you can deploy custom machine types with 2 to 96 vCPUs.
- You can create N2D custom machine types with 2, 4, 8, or 16 vCPUs. After 16, you can increment the number of vCPUs by 16, up to 96 vCPUs. The minimum acceptable number of vCPUs is 2.
- By default, the memory per vCPU that you can select for a custom machine type is determined by the machine series you choose. For N2D machine types, select between 0.5 GB and 8.0 GB per vCPU in 256 MB increments. Higher amounts of memory are possible by enabling [extended memory.](https://docs.cloud.google.com/compute/docs/instances/creating-instance-with-custom-machine-type#extendedmemory)
- N2D custom machine types are available only in select [regions and zones.](https://docs.cloud.google.com/compute/docs/regions-zones#available)
- N2D custom machine types support per VM Tier_1 networking performance maximum egress limits of 50 Gbps to 100 Gbps. When enabled:
  - VMs with 48 to 94 vCPUs have a total egress limit of 50 Gbps.
  - VMs with 96 vCPUs have a total egress limit of 100 Gbps.

**Examples of invalid machine types:**

- **2 vCPUs, 0.4 GB of total memory**. Invalid because the total memory is less than the minimum 1 GB for an N2D VM.
- **34 vCPUs, 34 GB of total memory**. Invalid because the total number of vCPUs is not divisible by 16.
- **1 vCPU, 1024 MB of memory**. Invalid because the vCPU count is too small. N2D custom machine types require a minimum of 2 vCPUs.

**Examples of valid machine types:**

- **32 vCPUs, 16 GB of total memory**. Valid because the total number of vCPUs is even and the total memory is a multiple of 256 MB. The amount of memory per vCPU is 1 GB, which satisfies the minimum requirement. Because the number of vCPUs is larger than 8 vCPUs, the number of vCPUs must be divisible by 16.
- **2 vCPUs, 7 GB of total memory**. Valid because it has 2 vCPUs, which is the minimum value, and the total memory is a multiple of 256 MB. The amount of memory per vCPU is also within the acceptable range of 1 GB to 8 GB per vCPU.

### N2 custom machine types

- For N2 custom machine types, you can create a machine type with 2 to 80 vCPUs and memory between 1 and 864 GB. For machine types with up to 32 vCPUs, you can select a vCPU count that is a multiple of 2. For machine types with greater than 32 vCPUs, you must select a vCPU count that is a multiple of 4 (for example, 36, 40, 56, or 80).
- You can create N2 custom machine types on different processors:
  - **Cascade Lake**, the 2nd generation of the Intel Xeon processor. This is the default processor for N2 custom machine types with less than 80 vCPUs.
  - **Ice Lake** , the 3rd generation of the Intel Xeon processor. Ice Lake processors are available in specific [regions and zones](https://docs.cloud.google.com/compute/docs/regions-zones).
- By default, the memory per vCPU that you can select for a custom machine type is determined by the machine series you use. For the N2 machine series, select between 0.5 GB and 8.0 GB per vCPU in 256 MB increments. Higher amounts of memory are possible by enabling [extended memory.](https://docs.cloud.google.com/compute/docs/instances/creating-instance-with-custom-machine-type#extendedmemory)
- N2 custom machine types have an option for a per VM Tier_1 networking performance maximum egress of 50 Gbps to 100 Gbps with a minimum of 30 vCPUs.
  - 32 to 62 vCPUs have a total egress of 50 Gbps
  - 64 to 78 vCPUs have a total egress of 75 Gbps
  - 80 vCPUs have a total egress of 100 Gbps

**Examples of invalid machine types:**

- **2 vCPUs, 0.5 GB of total memory**. Invalid because the total memory is less than the minimum 1 GB for an N2 VM.
- **34 vCPUs, 34 GB of total memory**. Invalid because the total number of vCPUs is not divisible by 4.
- **1 vCPU, 1024 MB of memory**. Invalid because the vCPU count is too small. N2 custom machine types require a minimum of 2 vCPUs.

**Examples of valid machine types:**

- **36 vCPUs, 18 GB of total memory**. Valid because the total number of vCPUs is even and the total memory is a multiple of 256 MB. The amount of memory per vCPU is also within the acceptable range of 0.5 GB to 8 GB per vCPU. Because the number of vCPUs is larger than 32 vCPUs, the number of vCPUs must be divisible by 4.
- **2 vCPUs, 7 GB of total memory**. Valid because it has 2 vCPUs, which is the minimum value, and the total memory is a multiple of 256 MB. The amount of memory per vCPU is also within the acceptable range of 0.5 GB to 8 GB per vCPU.

### E2 custom machine types

- E2 custom machine types support predefined platforms with Intel or AMD EPYC processors. You can create E2 custom machine types with vCPUs in multiples of 2, up to 32 vCPUs. The minimum acceptable number of vCPUs for a VM is 2.
- By default, the general-purpose machine series you choose determines the memory per vCPU that you can select for a custom machine type. For E2, the ratio of memory per vCPU is 0.5 GB to 8 GB inclusive. When creating a standard E2 machine type, the minimum memory you can select is 1 GB.
- An exception to the minimum vCPU limitation is to create an e2-standard-2 VM, then customize the visible core to 1 vCPU. The resulting VM is an e2-custom VM. For example, you create an E2 VM using the `e2-standard-2` machine type, stop the VM, and edit it by changing the visible core to 1 vCPU with 1.25 GB of memory. As a result, the machine type changes to `e2-custom-2-1280`. Pricing is described in the [Customize the number of visible CPU cores](https://docs.cloud.google.com/compute/docs/instances/customize-visible-cores#pricing)) document.

**Examples of invalid machine types:**

- **1 vCPU, 1024 MB of memory**. Invalid because the vCPU count is too small. E2 custom machine types require a minimum of 2 vCPUs.
- **32 vCPUs, 1 GB of total memory**. Invalid because the ratio of vCPUs to memory is incorrect. The acceptable ratio is 0.5 GB of memory to 1 vCPU.

**Examples of valid machine types:**

- **32 vCPUs, 16 GB of total memory**. Valid because the total number of vCPUs is even and the total memory is an acceptable ratio of memory to vCPU.
- **2 vCPUs, 8 GB of total memory**. Valid because it has 2 vCPUs, which is the minimum value, and the total memory is a multiple of 256 MB. The amount of memory per vCPU is also within the acceptable range of 0.5 GB to 8 GB per vCPU.

### E2 shared-core custom machine types

E2 shared-core machine types support predefined Intel or AMD EPYC processors, which are preselected for you at the time of VM creation. You can create shared-core machine types with a vCPU range of 0.25 to 1 vCPU. The memory range is 1 to 8 GB, with a maximum ratio of 8 GB per vCPU.

You can't customize the number of visible cores on a shared-core E2 VM.

- `e2-micro`: 0.25 vCPU, 1 to 2 GB of memory
- `e2-small`: 0.50 vCPU, 1 to 4 GB of memory
- `e2-medium`: 1 vCPU, 1 to 8 GB of memory

### N1 custom machine types

- You can create N1 custom machine types with 1 or more vCPUs. For VMs with more than 1 vCPU, you must increment the number of vCPUs by 2, up to 96 vCPUs for Intel Skylake platform,or up to 64 vCPUs for Intel Broadwell, Haswell, or Ivy Bridge CPU platforms.
- By default, the memory per vCPU that you can select for a custom machine type is determined by the machine series you choose. For N1 machine types, select between 0.9 GB and 6.5 GB per vCPU, inclusive. N1 custom machine types with 1 or 2 vCPUs require a minimum of 1 GB per vCPU. Higher amounts of memory are possible by enabling extended memory.

**Examples of invalid machine types:**

- **1 vCPU, 0.2 GB of total memory**. Invalid because the total memory is less than the minimum 1 GB for an N1 VM.
- **3 vCPU, 1 GB of total memory**. Invalid because the number of vCPU cores must be 1 or an even number up to 96.

**Examples of valid machine types:**

- **32 vCPUs, 29 GB of total memory**. Valid because the total number of vCPUs is even and the total memory is a multiple of 256 MB. The total memory is an acceptable ratio of memory to vCPU.
- **1 vCPU, 1 GB of total memory**. Valid because it has one vCPU, which is the minimum value, and the total memory is a multiple of 256 MB. The amount of memory per vCPU is also within the acceptable range of 1 GB to 6.5 GB per vCPU.

## What's next

- [Network bandwidth](https://docs.cloud.google.com/compute/docs/network-bandwidth)
- [Configuring a VM with a high-bandwidth network](https://docs.cloud.google.com/compute/docs/networking/configure-vm-with-high-bandwidth-configuration)
- [Virtual machine instances](https://docs.cloud.google.com/compute/docs/instances)
- [VM instance pricing](https://docs.cloud.google.com/compute/vm-instance-pricing#general-purpose_machine_type_family)

## Storage-optimized machine family for Compute Engine

The storage-optimized machine family is suitable for workloads that are low in core usage and high in storage density. For example, the Z3 machine series is useful for scale-out analytics workloads, flash-optimized databases, and other database workloads.

Z3 also offers two machine types with different amounts of Titanium SSD storage: `standardlssd` and `highlssd`. These machine types are ideal for high performance workloads that need fast access to data stored in local storage, such as data streaming, SQL and NoSQL databases, data search, data analytics, and data warehousing. For more information, see [Z3 machine types](https://docs.cloud.google.com/compute/docs/storage-optimized-machines#z3_machine_types).

| **Machine series** | **Workloads** |
| [Z3](https://docs.cloud.google.com/compute/docs/storage-optimized-machines#z3_machine_types) | - SQL, NoSQL, and vector databases - Data analytics and data warehouses - Search - Media streaming - Large distributed parallel file systems |
|---|---|

## Z3 machine series

Z3 instances are powered by the fourth generation Intel Xeon Scalable processor (code-named Sapphire Rapids), DDR5 memory, and [Titanium offload processors](https://cloud.google.com/titanium). Z3 machine types are optimized for the underlying NUMA architecture to deliver optimal, reliable, and consistent performance.

The Z3 machine series offers the following Local SSD storage capacities using [Titanium SSD](https://docs.cloud.google.com/compute/docs/disks/local-ssd#local_ssd_types):

- Up to 36,000 GiB with VM instances
- 72,000 GiB with bare metal instances

Titanium SSD is custom-designed Local SSD based on Titanium I/O offload processing. It offers enhanced security, performance, and management compared to Local SSD.

Z3 offers the following features:

- Uses Titanium to offload networking and storage processing from the host CPU onto silicon devices deployed throughout the data center
- Delivers high performance block storage with [Google Cloud Hyperdisk](https://docs.cloud.google.com/compute/docs/disks/hyperdisks)
- Offers the largest amount of Local SSD storage capacity of any Compute Engine machine series with Titanium SSD
- Supports [Intel Advanced Matrix Extensions (AMX)](https://docs.cloud.google.com/compute/docs/cpu-platforms#intel-amx), which is a built-in accelerator that significantly improves the performance of deep-learning training and inference on the CPU.
- Offers bare metal instances that provide access to several onboard, function-specific [accelerators and offloads](https://docs.cloud.google.com/compute/docs/cpu-platforms#accelerator) like Intel QAT, Intel DLB, Intel DSA, Intel TDX, and Intel IAA.
- Supports the following discount and consumption options:
  - Resource-based committed use discounts (CUDs)
  - Flexible CUDs
  - Spot VMs (excluding bare metal machine types)
  - Reservations

Z3 instances use Titanium to enable higher levels of networking performance, isolation, and security. The Z3 machine series supports a default network bandwidth of up to 100 Gbps and up to 200 Gbps with [per VM Tier_1 networking performance](https://docs.cloud.google.com/compute/docs/networking/configure-vm-with-high-bandwidth-configuration).

For details on pricing, see the [VM pricing page](https://docs.cloud.google.com/compute/vm-instance-pricing#z3_machine_types). Disk usage and network usage is charged separately from machine type pricing. For more information, see [Disk and image pricing](https://cloud.google.com/compute/disks-image-pricing) and [Network pricing](https://cloud.google.com/vpc/network-pricing). For Titanium SSD pricing, see [Storage-optimized machine type family pricing](https://docs.cloud.google.com/compute/vm-instance-pricing?e=48754805#section-4).

### Z3 Limitations

The following restrictions apply:

- You can't use [regional Persistent Disk](https://docs.cloud.google.com/compute/docs/disks/regional-persistent-disk) with Z3 instances.
- Z3 instances are only available in [select zones and regions](https://docs.cloud.google.com/compute/docs/regions-zones#available). For regional availability of bare metal instances, see [Bare metal instances](https://docs.cloud.google.com/compute/docs/instances/bare-metal-instances#regions_zones).
- You can't use [GPUs](https://docs.cloud.google.com/compute/docs/gpus) with Z3 instances.
- Z3 doesn't support sole tenancy.
- You can't suspend a Z3 instance.
- You can't create custom machine types for Z3 instances.
- Live migration is only supported for Z3 instances with 18 TiB or less of attached Titanium SSD.
- Z3 isn't supported on Windows images.

### Z3 machine types

> [!NOTE]
> **Note:** In June 2025, some Z3 machine types listed in the following table were renamed. `z3-highmem-176` is now `z3-highmem-176-standardlssd` and `z3-highmem-88` is now `z3-highmem-88-highlssd` The allocated resources remain the same.

The Z3 machine series supports the following predefined `lssd` machine subtypes:

- `standardlssd`: offers high performance search and data analysis for medium-sized data sets. This machine type has a vCPU to Titanium SSD capacity ratio of less than 1:350 and offers the highest Titanium SSD performance per vCPU.
- `highlssd`: offers high performance and storage intensive streaming and data analysis for large-sized data sets. This machine type has a vCPU to Titanium SSD capacity ratio between 1:350 and 1:600 and offers a higher total Titanium SSD capacity than `standardlssd`.

To create a bare metal instance with Z3, use the `z3-highmem-192-highlssd-metal` machine type.

### Z3 standardlssd

| Machine types | vCPUs^1^ | Memory (GB) | Titanium SSD | Default egress bandwidth (Gbps)^2^ | Tier_1 egress bandwidth (Gbps)^2^ |
|---|---|---|---|---|---|
| `z3-highmem-14-standardlssd` | 14 | 112 | (1 x 3000 GiB) 3,000 GiB | Up to 23 | N/A |
| `z3-highmem-22-standardlssd` | 22 | 176 | (2 x 3000 GiB) 6,000 GiB | Up to 23 | N/A |
| `z3-highmem-44-standardlssd` | 44 | 352 | (3 x 3000 GiB) 9,000 GiB | Up to 32 | Up to 50 |
| `z3-highmem-88-standardlssd` | 88 | 704 | (6 x 3000 GiB) 18,000 GiB | Up to 62 | Up to 100 |
| `z3-highmem-176-standardlssd` | 176 | 1,406 | (12 x 3000 GiB) 36,000 GiB | Up to 100 | Up to 200 |

^1^A vCPU is implemented as a single hardware thread on the available [CPU platform](https://docs.cloud.google.com/compute/docs/cpu-platforms).  
^2^ Maximum egress bandwidth cannot exceed the number given. Actual egress bandwidth depends on the destination IP address and other factors. See [Network bandwidth](https://docs.cloud.google.com/compute/docs/network-bandwidth).

### Z3 highlssd

| Machine types | vCPUs^1^ | Memory (GB) | Titanium SSD | Default egress bandwidth (Gbps)^2^ | Tier_1 egress bandwidth (Gbps)^2^ |
|---|---|---|---|---|---|
| `z3-highmem-8-highlssd` | 8 | 64 | (1 x 3000 GiB) 3,000 GiB | Up to 23 | N/A |
| `z3-highmem-16-highlssd` | 16 | 128 | (2 x 3000 GiB) 6,000 GiB | Up to 23 | N/A |
| `z3-highmem-22-highlssd` | 22 | 176 | (3 x 3000 GiB) 9,000 GiB | Up to 23 | N/A |
| `z3-highmem-32-highlssd` | 32 | 256 | (4 x 3000 GiB) 12,000 GiB | Up to 32 | N/A |
| `z3-highmem-44-highlssd` | 44 | 352 | (6 x 3000 GiB) 18,000 GiB | Up to 32 | Up to 50 |
| `z3-highmem-88-highlssd` | 88 | 704 | (12 x 3000 GiB) 36,000 GiB | Up to 62 | Up to 100 |
| `z3-highmem-192-highlssd-metal` | 192^3^ | 1,536 | (12 x 6000 GiB) 72,000 GiB | Up to 100 | Up to 200 |

^1^A vCPU is implemented as a single hardware thread on the available [CPU platform](https://docs.cloud.google.com/compute/docs/cpu-platforms).  
^2^ Maximum egress bandwidth cannot exceed the number given. Actual egress bandwidth depends on the destination IP address and other factors. See [Network bandwidth](https://docs.cloud.google.com/compute/docs/network-bandwidth).  
^3^ For bare metal instances, the number of vCPUs is equivalent to the number of hardware threads on the host server.

### Supported disk types for Z3

Z3 VMs support only the NVMe disk interface and can use the following block storage types:

- Hyperdisk Balanced (`hyperdisk-balanced`)
- Hyperdisk Balanced High Availability (`hyperdisk-balanced-high-availability`)
- Hyperdisk Extreme (`hyperdisk-extreme`)
- Hyperdisk Throughput (`hyperdisk-throughput`)
- Balanced Persistent Disk (`pd-balanced`)
- SSD (performance) Persistent Disk (`pd-ssd`)
- Titanium SSD

Z3 bare metal instances can use the following block storage types:

- Hyperdisk Balanced (`hyperdisk-balanced`)
- Hyperdisk Extreme (`hyperdisk-extreme`)
- Titanium SSD

Every machine type in the Z3 machine series comes with locally attached Titanium SSD disks. The disks are added automatically when you create an instance. The capacity and performance for Titanium SSD disks for Z3 are listed in the following table:

### Z3 standardlssd

<br />

|   |||| IOPS |   | Throughput (MiBps) ||
| Machine type | # of attached Titanium disks | Disk size (GiB) | Total size (GiB) | Read | Write | Read | Write |
|---|---|---|---|---|---|---|---|
| `z3-highmem-14-standardlssd` | 1 | 3,000 | 3,000 | 750,000 | 500,000 | 3,000 | 2,500 |
| `z3-highmem-22-standardlssd` | 2 | 3,000 | 6,000 | 1,500,000 | 1,000,000 | 6,000 | 5,000 |
| `z3-highmem-44-standardlssd` | 3 | 3,000 | 9,000 | 2,250,000 | 1,500,000 | 9,000 | 7,500 |
| `z3-highmem-88-standardlssd` | 6 | 3,000 | 18,000 | 4,500,000 | 3,000,000 | 18,000 | 15,000 |
| `z3-highmem-176-standardlssd` | 12 | 3,000 | 36,000 | 9,000,000 | 6,000,000 | 36,000 | 30,000 |

<br />

### Z3 highlssd

<br />

|   |||| IOPS |   | Throughput (MiBps) ||
| Machine type | # of attached Titanium disks | Disk size (GiB) | Total size (GiB) | Read | Write | Read | Write |
|---|---|---|---|---|---|---|---|
| `z3-highmem-8-highlssd` | 1 | 3,000 | 3,000 | 750,000 | 500,000 | 3,000 | 2,500 |
| `z3-highmem-16-highlssd` | 2 | 3,000 | 6,000 | 1,500,000 | 1,000,000 | 6,000 | 5,000 |
| `z3-highmem-22-highlssd` | 3 | 3,000 | 9,000 | 2,250,000 | 1,500,000 | 9,000 | 7,500 |
| `z3-highmem-32-highlssd` | 4 | 3,000 | 12,000 | 3,000,000 | 2,000,000 | 12,000 | 10,000 |
| `z3-highmem-44-highlssd` | 6 | 3,000 | 18,000 | 4,500,000 | 3,000,000 | 18,000 | 15,000 |
| `z3-highmem-88-highlssd` | 12 | 3,000 | 36,000 | 9,000,000 | 6,000,000 | 36,000 | 30,000 |
| `z3-highmem-192-highlssd-metal` | 12 | 6,000 | 72,000 | 9,000,000 | 6,000,000 | 36,000 | 30,000 |

<br />

For the performance limits of Hyperdisk and Persistent Disk, see the following:

- [Hyperdisk performance limits](https://docs.cloud.google.com/compute/docs/disks/hyperdisk-perf-limits)
- [Persistent Disk performance limits for Z3 VMs](https://docs.cloud.google.com/compute/docs/disks/performance#z3_vms)

#### Disk and capacity limits

<br />

For details about the capacity limits, see [Hyperdisk size and attachment limits](https://docs.cloud.google.com/compute/docs/disks/hyperdisk-perf-limits#limits-instance) and [Persistent Disk maximum capacity](https://docs.cloud.google.com/compute/docs/disks/persistent-disks#capacity_257tb).

<br />

Z3 storage limits are described in the following table:

### Z3 standardlssd

|   | Maximum number of disks |||   |   |
| Machine type | Per VM^1^ | Hyperdisk volumes per VM | Hyperdisk Balanced | Hyperdisk Throughput | Hyperdisk Extreme |
|---|---|---|---|---|---|
| `z3-highmem-14-standardlssd` | 128 | 16 | 16 | 16 | 0 |
| `z3-highmem-22-standardlssd` | 128 | 32 | 32 | 32 | 0 |
| `z3-highmem-44-standardlssd` | 128 | 32 | 32 | 32 | 0 |
| `z3-highmem-88-standardlssd` | 128 | 32 | 32 | 32 | 8 |
| `z3-highmem-176-standardlssd` | 128 | 32 | 32 | 32 | 8 |

^1^ The maximum size per Hyperdisk volume is 64 TiB.

### Z3 highlssd

|   | Maximum number of disks |||   |   |
| Machine type | Per VM^1^ | Hyperdisk volumes per VM | Hyperdisk Balanced | Hyperdisk Throughput | Hyperdisk Extreme |
|---|---|---|---|---|---|
| `z3-highmem-8-highlssd` | 128 | 16 | 16 | 16 | 0 |
| `z3-highmem-16-highlssd` | 128 | 16 | 16 | 16 | 0 |
| `z3-highmem-22-highlssd` | 128 | 32 | 32 | 32 | 0 |
| `z3-highmem-32-highlssd` | 128 | 32 | 32 | 32 | 0 |
| `z3-highmem-44-highlssd` | 128 | 32 | 32 | 32 | 0 |
| `z3-highmem-88-highlssd` | 128 | 32 | 32 | 32 | 8 |
| `z3-highmem-192-highlssd-metal` | 32 | 32 | 16 | 0 | 16 |

^1^ The maximum size per Hyperdisk volume is 64 TiB.

### Network support for Z3 VMs

The following network interface drivers are required:

- Z3 VM instances require [gVNIC](https://docs.cloud.google.com/compute/docs/networking/using-gvnic).
- Z3 bare metal instances require the [Intel IDPF LAN PF device driver](https://docs.cloud.google.com/compute/docs/networking/using-idpf).

Z3 supports up to 100 Gbps network bandwidth for standard networking and up to 200 Gbps with per VM Tier_1 networking performance for VM and bare metal instances.

Before migrating to Z3 or creating Z3 VMs or bare metal instances, make sure that the [operating system image](https://docs.cloud.google.com/compute/docs/images/os-details#networking) that you use supports the IDPF network driver for bare metal instances or the gVNIC driver for VM instances. To get the best possible performance on Z3 VMs, choose an OS image that supports both "Tier_1 Networking" and "200 Gbps network bandwidth". These images include an updated gVNIC driver, even if the guest OS shows the `gve` driver version as 1.0.0. If your Z3 VM is using an operating system with an older version of gVNIC driver, this is still supported but the VM might experience suboptimal performance such as less network bandwidth or higher latency.

If you use a custom OS image to create a Z3 VM, you can [manually install the most recent gVNIC driver](https://docs.cloud.google.com/compute/docs/networking/using-gvnic#manual-gvnic-setup). The gVNIC driver version v1.4.2 or later is recommended for use with Z3 VMs. Google recommends using the latest gVNIC driver version to benefit from additional features and bug fixes.

### Maintenance experience for Z3 instances

During the [lifecycle of a Compute Engine instance](https://docs.cloud.google.com/compute/docs/instances/instance-lifecycle), the host machine that your instance runs on undergoes multiple *host events*. A host event can include the regular maintenance of Compute Engine infrastructure, or in rare cases, a host error. Compute Engine also applies some non-disruptive lightweight upgrades for the hypervisor and network in the background.

The Z3 machine series supports on-demand maintenance and offers the following features related to host maintenance:

| Attached Titanium SSD (TiB) | Typical scheduled maintenance event frequency | [Maintenance behavior](https://docs.cloud.google.com/compute/docs/instances/host-maintenance-overview#maintenance_behaviors) | [Advanced notification](https://docs.cloud.google.com/compute/docs/instances/monitor-plan-host-maintenance-event) | [On-demand maintenance](https://docs.cloud.google.com/compute/docs/instances/trigger-host-maintenance-event) | [Simulate maintenance](https://docs.cloud.google.com/compute/docs/instances/simulating-host-maintenance) |
|---|---|---|---|---|---|
| 18 or less | Minimum of 30 days | Live migrate | 7 days | Yes | Yes |
| 36 | Minimum of 30 days | Terminates with Local SSD data persistence | 7 days | Yes | Yes |
| 72 (bare metal) | Minimum of 180 days | Terminates with Local SSD data persistence | 90 days | Yes | Yes |

The maintenance frequencies shown in the previous table are approximations, not guarantees. Compute Engine might occasionally perform maintenance more frequently.

Compute Engine preserves data on the local Titanium SSD disks for Z3 instances during maintenance events.

If a host event occurs, Compute Engine tries to recover any Titanium SSD disks attached to the instance. By default, Compute Engine spends up to 1 hour recovering the data. For Z3 instances, Compute Engine spends up to 6 hours trying to recover the Titanium SSD data before reaching the timeout limit. This timeout limit is customizable. For more information about Local SSD and Titanium SSD recovery options, see [Disk persistence following instance termination](https://docs.cloud.google.com/compute/docs/instances/host-maintenance-overview#disk-persistence).

## What's next

- [Creating and starting a virtual machine instance](https://docs.cloud.google.com/compute/docs/instances/create-start-instance)
- Learn about the different [Storage options](https://docs.cloud.google.com/compute/docs/disks) for your VM
- [Move your workload to a new compute instance](https://docs.cloud.google.com/compute/docs/import/migrate-to-new-vm)
- [VM instance pricing](https://docs.cloud.google.com/compute/vm-instance-pricing#storage-optimized)

## Compute-optimized machine family for Compute Engine

Compute-optimized instances are ideal for compute-intensive and high performance computing (HPC) workloads. Compute-optimized instances offer the highest performance per core and are built on architecture that utilizes features like non-uniform memory access (NUMA) for optimal, reliable, and uniform performance.

> [!NOTE]
> **Note:** For the C3, C3D, C4, C4D, or C4A machine series, see [General-purpose machine family](https://docs.cloud.google.com/compute/docs/general-purpose-machines).

| **Machine** | **Workloads** |
| [H4D machine series](https://docs.cloud.google.com/compute/docs/compute-optimized-machines#h4d_series) | - HPC workloads and multi-node workloads - Manufacturing - Weather forecasting - Electronic design automation (EDA) - Healthcare and life sciences - Scientific computing |
| [H3 machine series](https://docs.cloud.google.com/compute/docs/compute-optimized-machines#h3_series) | - HPC workloads - Computational fluid dynamics - Crash safety - Genomics - Financial modeling - General scientific and engineering computing |
| [C2D machine series](https://docs.cloud.google.com/compute/docs/compute-optimized-machines#c2d_machine_types) | - Memory-bound workloads - Gaming (AAA game servers) - High performance computing (HPC) - High performance databases - Electronic Design Automation (EDA) - Media transcoding |
| [C2 machine series](https://docs.cloud.google.com/compute/docs/compute-optimized-machines#c2_machine_types) | - Compute-bound workloads - High-performance web serving - Gaming (AAA game servers) - Ad serving - High performance computing (HPC) - Media transcoding - AI/ML |
|---|---|

The following machine series are available in this machine family:

- H4D instances are powered by [Titanium](https://cloud.google.com/titanium) and fifth generation AMD EPYC Turin processors which have a base frequency of 2.7 GHz and a maximum frequency of 4.1 GHz. H4D instances have 192 cores (vCPUs) and up to 1,488 GB of memory. H4D instances can be used with Local SSD storage and Cloud RDMA networking.
- H3 instances are powered by [Titanium](https://cloud.google.com/titanium) and two fourth generation Intel Xeon Scalable processors (code-named Sapphire Rapids) which have an all-core frequency of 3.0 GHz. H3 instances have 88 vCPUs and 352 GB of DDR5 memory.
- C2D instances run on the third generation AMD EPYC Milan processor and offer up to 3.5 GHz max boost frequency. C2D instances have flexible sizing between 2 to 112 vCPUs and 2 to 8 GB of memory per vCPU.
- C2 instances run on the second generation Intel Xeon Scalable processor (Cascade Lake) which offers up to 3.9 GHz sustained single-core max turbo frequency. C2 offers instances with 4 to 60 vCPUs and 4 GB of memory per vCPU.

## H4D machine series

H4D instances are powered by the AMD EPYC Turin 5th Generation processors and [Titanium](https://cloud.google.com/titanium) offload processors.

H4D instances deliver high performance, low cost, and scalability for multi-node workloads. H4D instances are single-threaded and are optimized for tightly-coupled applications that scale across multiple nodes. Leveraging technologies like Titanium SSD, RDMA-enabled 200 Gbps networking and cluster management capabilities, these instances prioritize performance and workload-specific optimizations. Additionally, you can use [Dynamic Workload Scheduler](https://cloud.google.com/blog/products/compute/introducing-dynamic-workload-scheduler) for scheduled or immediate cluster deployment, making H4D ideal for HPC bursty workload needs.

An H4D instance uses all the vCPUs on an entire host server. H4D instances can use the entire host network bandwidth and come with a default network bandwidth rate of up to 200 Gbps. However, the bandwidth from the instance to the internet is limited to 1 Gbps.

Simultaneous multithreading (SMT) is disabled for H4D instances and can't be enabled. There is also no overcommitting to ensure optimal performance consistency.

H4D instances are available on-demand, or with one- and three-year committed use discounts (CUDs). To compare these methods, see [Compute Engine instances provisioning models](https://docs.cloud.google.com/compute/docs/instances/provisioning-models).

### H4D Limitations

The H4D machine series has the following restrictions:

- The H4D machine types are only available in a predefined machine type. Custom machine types aren't available.
- You can't use GPUs with H4D instances.
- Outbound data transfer is limited to 1 Gbps.
- You can't create machine images from H4D instances.
- H4D machine images can't be used to [create disks](https://docs.cloud.google.com/compute/docs/disks/create-disk-from-source).
- You can't share disks between instances, either in [multi-writer mode](https://docs.cloud.google.com/compute/docs/disks/sharing-disks-between-vms#multi_writer_mode) or [read-only mode](https://docs.cloud.google.com/compute/docs/disks/sharing-disks-between-vms#use-multi-instance).
- Hyperdisk Balanced performance is capped at 15,000 IOPS and 240 MBps throughput.
- Live migration isn't supported for H4D instances.

<br />

### H4D machine types

<br />

| Machine types | vCPUs^1^ | Memory (GB) | Titanium SSD | Default egress bandwidth (Gbps)^2^ |
|---|---|---|---|---|
| `h4d-standard-192` | 192 | 720 | Not supported | Up to 200 Gbps |
| `h4d-highmem-192` | 192 | 1,488 | Not supported | Up to 200 Gbps |
| `h4d-highmem-192-lssd` | 192 | 1,488 | (10 x 375 GiB) 3,750 GiB | Up to 200 Gbps |

<br />

<br />

^1^ A vCPU represents an entire core---no simultaneous multithreading (SMT).  
^2^ Default egress bandwidth cannot exceed the number given. Actual egress bandwidth depends on the destination IP address and other factors. See [Network bandwidth](https://docs.cloud.google.com/compute/docs/network-bandwidth).

<br />

### Supported disk types for H4D

H4D instances can use the following block storage types:

- Hyperdisk Balanced (`hyperdisk-balanced`)
- Local Titanium SSD

#### Disk and capacity limits

The following restrictions apply:

- The number of Hyperdisk volumes can't exceed 64 per VM.
- The maximum total disk capacity across all disks can't exceed 512 TiB.

For details about the capacity limits, see [Hyperdisk capacity limits per VM](https://docs.cloud.google.com/compute/docs/disks/hyperdisks#limits-instance).

H4D storage limits are described in the following table:

<br />

| Maximum number of disks per instance |||||
| Machine types | All Hyperdisk types | Hyperdisk Balanced | Hyperdisk Throughput | Hyperdisk Extreme |
|---|---|---|---|---|
| `h4d-standard-192` | 64 | 8 | 0 | 0 |
| `h4d-highmem-192` | 64 | 8 | 0 | 0 |
| `h4d-highmem-192-lssd` | 64 | 8 | 0 | 0 |

<br />

### Network support for H4D instances

H4D instances require [gVNIC network interfaces](https://docs.cloud.google.com/compute/docs/networking/using-gvnic). H4D supports up to 200 Gbps network bandwidth for standard networking. Instance to Internet egress bandwidth is limited to 1 Gbps.

If using Cloud RDMA, you must configure at least two network interfaces (vNICs) when you create each instance:

- GVNIC: This vNIC uses the gVNIC driver and is used for normal networking communication. It is fully connected to the Google network and can connect to the Internet.
- IRDMA: The other vNIC uses an Intel iDPF/iRDMA driver and is used only for Cloud RDMA communication. This network interface doesn't connect to the Internet.

Before migrating to H4D or creating H4D instances, make sure that the [operating system image](https://docs.cloud.google.com/compute/docs/images/os-details#networking) that you use is fully supported for H4D. Fully supported images include support for **200 Gbps network bandwidth** . If you are using Cloud RDMA, then the OS image must also support the [IRDMA network interface type](https://docs.cloud.google.com/compute/docs/networking/using-irdma#os-support). If your H4D instance is using an operating system that is not fully supported or has earlier versions of the network drivers, then your instance might not be able to achieve the maximum network bandwidth for H4D instances.

### Maintenance experience for H4D instances

During the [lifecycle of a Compute Engine instance](https://docs.cloud.google.com/compute/docs/instances/instance-lifecycle), the host machine that your instance runs on undergoes multiple *host events*. A host event can include the regular maintenance of Compute Engine infrastructure, or in rare cases, a host error. Compute Engine also applies some non-disruptive lightweight upgrades for the hypervisor and network in the background.

The H4D machine series offers the following features related to host maintenance:

<br />

| Machine type | Typical scheduled maintenance event frequency | [Maintenance behavior](https://docs.cloud.google.com/compute/docs/instances/host-maintenance-overview#maintenance_behaviors) | [Advanced notification](https://docs.cloud.google.com/compute/docs/instances/monitor-plan-host-maintenance-event) | [On-demand maintenance](https://docs.cloud.google.com/compute/docs/instances/trigger-host-maintenance-event) | [Simulate maintenance](https://docs.cloud.google.com/compute/docs/instances/simulating-host-maintenance) |
|---|---|---|---|---|---|
| `h4d-standard-192` | Minimum of 30 days | Terminate | 7 days | Yes | No |
| `h4d-highmem-192` | Minimum of 30 days | Terminate | 7 days | Yes | No |
| `h4d-highmem-192-lssd` | Minimum of 30 days | Terminates with Local SSD data persistence | 7 days | Yes | No |

<br />

The maintenance frequencies shown in the previous table are approximations, not guarantees. Compute Engine might occasionally perform maintenance more frequently.

## H3 machine series

H3 instances are powered by the fourth generation Intel Xeon Scalable processors (code-named Sapphire Rapids), DDR5 memory, and [Titanium](https://cloud.google.com/titanium) offload processors.

H3 instances offer the best price performance for compute-intensive high performance computing (HPC) workloads in Compute Engine. H3 instances are [single-threaded](https://docs.cloud.google.com/compute/docs/cpu-platforms) and are ideal for a variety of modeling and simulation workloads including computational fluid dynamics, crash safety, genomics, financial modeling, and general scientific and engineering computing. H3 instances support compact placement, which is optimized for tightly-coupled applications that scale across multiple nodes.

The H3 series is available in one size, comprising an entire host server. To save on licensing costs, you can customize the number of visible cores, but you are charged the same price for the instance. H3 instances can use the entire host network bandwidth and come with a default network bandwidth rate of up to 200 Gbps. However, the bandwidth from the instance to the internet is limited to 1 Gbps.

Simultaneous multithreading (SMT) is disabled for H3 instances and can't be enabled. There is also no overcommitting to ensure optimal performance consistency.

H3 instances are available on-demand, or with one- and three-year committed use discounts (CUDs). H3 instances can be used with Google Kubernetes Engine.

### H3 Limitations

The H3 machine series has the following restrictions:

- The H3 machine series is only available in a predefined machine type. Custom machine shapes aren't available.
- You can't use GPUs with H3 instances.
- Outbound data transfer is limited to 1 Gbps.
- Persistent Disk and Google Cloud Hyperdisk performance is capped at 15,000 IOPS and 240 MBps throughput.
- H3 instances don't support [machine images](https://docs.cloud.google.com/compute/docs/machine-images).
- H3 instances support only the NVMe [storage interface](https://docs.cloud.google.com/compute/docs/disks/persistent-disks#choose_an_interface).
- H3 instance images can't be used to [create disks](https://docs.cloud.google.com/compute/docs/disks/create-disk-from-source).
- H3 instances don't support sharing disks between instances, either in [multi-writer mode](https://docs.cloud.google.com/compute/docs/disks/sharing-disks-between-vms#multi_writer_mode) or [read-only mode](https://docs.cloud.google.com/compute/docs/disks/sharing-disks-between-vms#use-multi-instances).

### H3 machine types

H3 instances are available as a predefined configuration with 88 vCPUs and 352 GB of memory.

| Machine types | vCPUs^1^ | Memory (GB) | Local SSD | Default egress bandwidth (Gbps)^2^ |
|---|---|---|---|---|
| `h3-standard-88` | 88 | 352 | Not supported | Up to 200 Gbps |

^1^ A vCPU represents an entire core---no simultaneous multithreading (SMT).  
^2^ Default egress bandwidth cannot exceed the number given. Actual egress bandwidth depends on the destination IP address and other factors. See [Network bandwidth](https://docs.cloud.google.com/compute/docs/network-bandwidth).

### Supported disk types for H3

H3 instances can use the following block storage types:

- Balanced Persistent Disk (`pd-balanced`)
- Hyperdisk Balanced (`hyperdisk-balanced`)
- Hyperdisk Throughput (`hyperdisk-throughput`)

#### Disk and capacity limits

<br />

If supported by the machine type, you can attach a mixture of Hyperdisk and Persistent Disk volumes to an instance, but the following restrictions apply:

- The combined number of both Hyperdisk and Persistent Disk volumes can't exceed 128 per instance.
- The maximum total disk capacity (in TiB) across all disk types can't exceed:

  - 512 TiB for all Hyperdisk
  - 512 TiB for a mixture of Hyperdisk and Persistent Disk
  - 257 TiB for all Persistent Disk

For details about the capacity limits, see [Hyperdisk size and attachment limits](https://docs.cloud.google.com/compute/docs/disks/hyperdisk-perf-limits#limits-instance) and [Persistent Disk maximum capacity](https://docs.cloud.google.com/compute/docs/disks/persistent-disks#capacity_257tb).

<br />

H3 storage limits are described in the following table:

|   | Maximum number of disks per instance ||||   |
| Machine types | All disk types ^1^ | All Hyperdisk types | Hyperdisk Balanced | Hyperdisk Throughput | Hyperdisk Extreme |
|---|---|---|---|---|---|
| `h3-standard-88` | 128 | 64 | 8 | 64 | 0 |

^1^ This limit applies to Persistent Disk and Hyperdisk, but doesn't include Local SSD disks.

### Network support for H3 instances

H3 instances require [gVNIC network interfaces](https://docs.cloud.google.com/compute/docs/networking/using-gvnic). H3 supports up to 200 Gbps network bandwidth for standard networking and doesn't support per VM Tier_1 networking performance.

Before migrating to H3 or creating H3 instances, make sure that the operating system image that you use supports the gVNIC driver. To get the best possible performance on H3 instances, on the [**Networking features**](https://docs.cloud.google.com/compute/docs/images/os-details#networking-features) tab of the OS details table, choose an OS image that supports both "Tier_1 Networking" and "200 Gbps network bandwidth". These images include an updated gVNIC driver, even if the guest OS shows the `gve` driver version as 1.0.0. If your H3 instance is using an operating system with an older version of the gVNIC driver, this is still supported but the instance might experience suboptimal performance such as less network bandwidth or higher latency.

If you use a custom OS image with the H3 machine series, you can [manually install the most recent gVNIC driver](https://docs.cloud.google.com/compute/docs/networking/using-gvnic#manual-gvnic-setup). The gVNIC driver version v1.4.2 or later is recommended for use with H3 instances. Google recommends using the latest gVNIC driver version to benefit from additional features and bug fixes.

### Maintenance experience for H3 instances

During the [lifecycle of a Compute Engine instance](https://docs.cloud.google.com/compute/docs/instances/instance-lifecycle), the host machine that your instance runs on undergoes multiple *host events*. A host event can include the regular maintenance of Compute Engine infrastructure, or in rare cases, a host error. Compute Engine also applies some non-disruptive lightweight upgrades for the hypervisor and network in the background.

The H3 machine series offers the following features related to host maintenance:

| Machine type | Typical scheduled maintenance event frequency | [Maintenance behavior](https://docs.cloud.google.com/compute/docs/instances/host-maintenance-overview#maintenance_behaviors) | [Advanced notification](https://docs.cloud.google.com/compute/docs/instances/monitor-plan-host-maintenance-event) | [On-demand maintenance](https://docs.cloud.google.com/compute/docs/instances/trigger-host-maintenance-event) | [Simulate maintenance](https://docs.cloud.google.com/compute/docs/instances/simulating-host-maintenance) |
|---|---|---|---|---|---|
| `h3-standard-88` | Minimum of 30 days | Live migrate | 7 days | Yes | Yes |

The maintenance frequencies shown in the previous table are approximations, not guarantees. Compute Engine might occasionally perform maintenance more frequently.

## C2D machine series

The C2D machine series provides the largest instance sizes and are best-suited for high performance computing (HPC). The C2D series also has the largest available last-level cache (LLC) cache per core.

The C2D machine series comes in different machine types ranging from 2 to 112 vCPUs, and offer up to 896 GB of memory. You can attach up to 3 TiB of Local SSD storage to these machine types for applications that require higher storage performance.

- C2D standard and C2D high-cpu machines serve existing compute-bound workloads including high-performance web servers, media transcoding, and gaming.
- C2D high-memory machines serve specialized workloads such as HPC and EDA, which need more memory.

The C2D series supports these compute-bound workloads by using the third generation AMD EPYC Milan platform.

The C2D series supports [Confidential VM](https://docs.cloud.google.com/confidential-computing/confidential-vm/docs/confidential-vm-overview).

### C2D Limitations

The C2D machine series has the following restrictions:

- You can't attach [regional persistent disks](https://docs.cloud.google.com/compute/docs/disks/regional-persistent-disk) to a C2D instance.
- The C2D machine series is subject to different [disk performance limits](https://docs.cloud.google.com/compute/docs/disks/performance#c2d_vms) than the general-purpose and memory-optimized machine families.
- The C2D machine series is available only in [select zones and regions](https://docs.cloud.google.com/compute/docs/regions-zones#available) on specific [CPU processors](https://docs.cloud.google.com/compute/docs/machine-resource#machine_type_comparison).
- The C2D machine series doesn't support GPUs.
- The C2D machine series doesn't support sole-tenant nodes.

### C2D machine types

C2D instances are available as predefined configurations in sizes ranging from 2 vCPUs to 112 vCPUs and up to 896 GB of memory.

- standard: 4 GB memory per vCPU
- highcpu: 2 GB memory per vCPU
- highmem: 8 GB memory per vCPU

### C2D standard

| Machine types | vCPUs^1^ | Memory (GB) | Local SSD^2^ | Default egress bandwidth (Gbps)^3^ | Tier_1 egress bandwidth (Gbps)^4^ |
|---|---|---|---|---|---|
| `c2d-standard-2` | 2 | 8 | 1, 2, 4, or 8 | Up to 10 | N/A |
| `c2d-standard-4` | 4 | 16 | 1, 2, 4, or 8 | Up to 10 | N/A |
| `c2d-standard-8` | 8 | 32 | 1, 2, 4, or 8 | Up to 16 | N/A |
| `c2d-standard-16` | 16 | 64 | 1, 2, 4, or 8 | Up to 32 | N/A |
| `c2d-standard-32` | 32 | 128 | 2, 4, or 8 | Up to 32 | Up to 50 |
| `c2d-standard-56` | 56 | 224 | 4 or 8 | Up to 32 | Up to 50 |
| `c2d-standard-112` | 112 | 448 | 8 | Up to 32 | Up to 100 |

<br />

^1^ A vCPU represents a single logical CPU thread. See [CPU platforms](https://docs.cloud.google.com/compute/docs/cpu-platforms).  
^2^ Number of 375 GiB Local SSD disks that you can choose to add when creating the instance.  
^3^ Default egress bandwidth cannot exceed the number given. Actual egress bandwidth depends on the destination IP address and other factors. See [Network bandwidth](https://docs.cloud.google.com/compute/docs/network-bandwidth).  
^4^ Supports [high-bandwidth networking](https://docs.cloud.google.com/compute/docs/networking/configure-vm-with-high-bandwidth-configuration) for larger machine types. For Windows OS images, the maximum network bandwidth is limited to 50 Gbps.

<br />

### C2D high-cpu

| Machine types | vCPUs^1^ | Memory (GB) | Local SSD^2^ | Default egress bandwidth (Gbps)^3^ | Tier_1 egress bandwidth (Gbps)^4^ |
|---|---|---|---|---|---|
| `c2d-highcpu-2` | 2 | 4 | 1, 2, 4, or 8 | Up to 10 | N/A |
| `c2d-highcpu-4` | 4 | 8 | 1, 2, 4, or 8 | Up to 10 | N/A |
| `c2d-highcpu-8` | 8 | 16 | 1, 2, 4, or 8 | Up to 16 | N/A |
| `c2d-highcpu-16` | 16 | 32 | 1, 2, 4, or 8 | Up to 32 | N/A |
| `c2d-highcpu-32` | 32 | 64 | 2, 4, or 8 | Up to 32 | Up to 50 |
| `c2d-highcpu-56` | 56 | 112 | 4 or 8 | Up to 32 | Up to 50 |
| `c2d-highcpu-112` | 112 | 224 | 8 | Up to 32 | Up to 100 |

<br />

^1^ A vCPU represents a single logical CPU thread. See [CPU platforms](https://docs.cloud.google.com/compute/docs/cpu-platforms).  
^2^ Number of 375 GiB Local SSD disks that you can choose to add when creating the instance.  
^3^ Default egress bandwidth cannot exceed the number given. Actual egress bandwidth depends on the destination IP address and other factors. See [Network bandwidth](https://docs.cloud.google.com/compute/docs/network-bandwidth).  
^4^ Supports [high-bandwidth networking](https://docs.cloud.google.com/compute/docs/networking/configure-vm-with-high-bandwidth-configuration) for larger machine types. For Windows OS images, the maximum network bandwidth is limited to 50 Gbps.

<br />

### C2D high-mem

| Machine types | vCPUs^1^ | Memory (GB) | Local SSD^2^ | Default egress bandwidth (Gbps)^3^ | Tier_1 egress bandwidth (Gbps)^4^ |
|---|---|---|---|---|---|
| `c2d-highmem-2` | 2 | 16 | 1, 2, 4, or 8 | Up to 10 | N/A |
| `c2d-highmem-4` | 4 | 32 | 1, 2, 4, or 8 | Up to 10 | N/A |
| `c2d-highmem-8` | 8 | 64 | 1, 2, 4, or 8 | Up to 16 | N/A |
| `c2d-highmem-16` | 16 | 128 | 1, 2, 4, or 8 | Up to 32 | N/A |
| `c2d-highmem-32` | 32 | 256 | 2, 4, or 8 | Up to 32 | Up to 50 |
| `c2d-highmem-56` | 56 | 448 | 4 or 8 | Up to 32 | Up to 50 |
| `c2d-highmem-112` | 112 | 896 | 8 | Up to 32 | Up to 100 |

<br />

^1^ A vCPU represents a single logical CPU thread. See [CPU platforms](https://docs.cloud.google.com/compute/docs/cpu-platforms).  
^2^ Number of 375 GiB Local SSD disks that you can choose to add when creating the instance.  
^3^ Default egress bandwidth cannot exceed the number given. Actual egress bandwidth depends on the destination IP address and other factors. See [Network bandwidth](https://docs.cloud.google.com/compute/docs/network-bandwidth).  
^4^ Supports [high-bandwidth networking](https://docs.cloud.google.com/compute/docs/networking/configure-vm-with-high-bandwidth-configuration) for larger machine types. For Windows OS images, the maximum network bandwidth is limited to 50 Gbps.

<br />

### Supported disk types for C2D

C2D instances can use the following block storage types:

- Standard Persistent Disk (`pd-standard`)
- Balanced Persistent Disk (`pd-balanced`)
- SSD (performance) Persistent Disk (`pd-ssd`)

Each C2D instance can have a maximum of 128 Persistent Disk volumes (including the boot disk) attached to the instance, and a total of 257 GiB disk capacity.

C2D instances with Confidential Computing running Microsoft Windows with the NVMe disk interface have a disk attachment limitation of 16 disks. See [Known issues](https://docs.cloud.google.com/compute/docs/troubleshooting/known-issues#windows-disk-attachment) for details.

> [!NOTE]
> **Note:** Persistent Disk usage is charged separately from [machine type pricing](https://cloud.google.com/compute/vm-instance-pricing).

### Network support for C2D instances

The C2D machine types support either the VirtIO or gVNIC network driver. C2D instances with 32 or more vCPUS support higher network bandwidths of 50 Gbps and 100 Gbps with gVNIC and [per VM Tier_1 networking performance](https://docs.cloud.google.com/compute/docs/networking/configure-vm-with-high-bandwidth-configuration).

### Maintenance experience for C2D instances

During the [lifecycle of a Compute Engine instance](https://docs.cloud.google.com/compute/docs/instances/instance-lifecycle), the host machine that your instance runs on undergoes multiple *host events*. A host event can include the regular maintenance of Compute Engine infrastructure, or in rare cases, a host error. Compute Engine also applies some non-disruptive lightweight upgrades for the hypervisor and network in the background.

The C2D machine series offers the following features related to host maintenance:

| Machine type | Typical scheduled maintenance event frequency | [Maintenance behavior](https://docs.cloud.google.com/compute/docs/instances/host-maintenance-overview#maintenance_behaviors) | [Advanced notification](https://docs.cloud.google.com/compute/docs/instances/monitor-plan-host-maintenance-event) | [On-demand maintenance](https://docs.cloud.google.com/compute/docs/instances/trigger-host-maintenance-event) | [Simulate maintenance](https://docs.cloud.google.com/compute/docs/instances/simulating-host-maintenance) |
|---|---|---|---|---|---|
| All machine types | Minimum of 30 days | Live migrate | 60 seconds | No | Yes |
| Confidential VM | Minimum of 30 days | Restart in place | 60 seconds | No | Yes |

The maintenance frequencies shown in the previous table are approximations, not guarantees. Compute Engine might occasionally perform maintenance more frequently.

## C2 machine series

The C2 machine series provides full transparency into the architecture of the underlying server platforms, letting you fine-tune the performance. Machine types in this series offer much more computing power, and are generally more robust for compute-intensive workloads compared to N1 high-CPU machine types.

The C2 series comes in different machine types ranging from 4 to 60 vCPUs, and offers up to 240 GB of memory. You can attach up to 3 TiB of Local SSD storage to these instances for applications that require higher storage performance.

This series also produces a greater than 40% performance improvement compared to the previous generation N1 machines and offer higher performance per thread and isolation for latency-sensitive workloads.

The C2 series enables the highest performance per core and the highest frequency for compute-bound workloads using Intel 3.9 GHz Cascade Lake processors. If you are looking to optimize workloads for [single thread performance](https://docs.cloud.google.com/compute/docs/instances/set-threads-per-core), particularly with respect to floating point, choose a machine type in this series to take advantage of AVX-512 capabilities only available on Intel.

### C2 Limitations

The C2 machine series has the following restrictions:

- You cannot use [regional persistent disks](https://docs.cloud.google.com/compute/docs/disks/regional-persistent-disk).
- The C2 machine series is subject to different [disk limits](https://docs.cloud.google.com/compute/docs/disks/performance#c2_vms) than the general-purpose and memory-optimized machine families.
- The C2 machine series is available only in [select zones and regions](https://docs.cloud.google.com/compute/docs/regions-zones#available) on specific [CPU processors](https://docs.cloud.google.com/compute/docs/machine-types#machine_type_comparison).
- The C2 machine series doesn't support GPUs.

### C2 machine types

C2 instances are available as predefined configurations with 4 to 60 vCPUs and 4 GB memory per vCPU.

| Machine types | vCPUs^1^ | Memory (GB) | Local SSD^2^ | Default egress bandwidth (Gbps)^3^ | Tier_1 egress bandwidth (Gbps)^4^ |
|---|---|---|---|---|---|
| `c2-standard-4` | 4 | 16 | 1, 2, 4, or 8 | Up to 10 | N/A |
| `c2-standard-8` | 8 | 32 | 1, 2, 4, or 8 | Up to 16 | N/A |
| `c2-standard-16` | 16 | 64 | 2, 4, or 8 | Up to 32 | N/A |
| `c2-standard-30` | 30 | 120 | 4 or 8 | Up to 32 | Up to 50 |
| `c2-standard-60` | 60 | 240 | 8 | Up to 32 | Up to 100 |

<br />

^1^ A vCPU represents a single logical CPU thread. See [CPU platforms](https://docs.cloud.google.com/compute/docs/cpu-platforms).  
^2^ Number of 375 GiB Local SSD disks that you can choose to add when creating the instance.  
^3^ Default egress bandwidth cannot exceed the number given. Actual egress bandwidth depends on the destination IP address and other factors. See [Network bandwidth](https://docs.cloud.google.com/compute/docs/network-bandwidth).  
^4^ Supports [high-bandwidth networking](https://docs.cloud.google.com/compute/docs/networking/configure-vm-with-high-bandwidth-configuration) for larger machine types. For Windows OS images, the maximum network bandwidth is limited to 50 Gbps.

<br />

### Supported disk types for C2

C2 instances can use the following block storage types:

- Standard Persistent Disk (`pd-standard`)
- Balanced Persistent Disk (`pd-balanced`)
- SSD (performance) Persistent Disk (`pd-ssd`)

Each C2 instance can have a maximum of 128 Persistent Disk volumes (including the boot disk) attached to the instance, and a total of 257 GiB disk capacity.

> [!NOTE]
> **Note:** Persistent Disk usage is charged separately from [machine type pricing](https://cloud.google.com/compute/vm-instance-pricing).

### Network support for C2 instances

The C2 machine types support either the VirtIO or gVNIC network driver. C2 instances with 30 or more vCPUS support higher network bandwidths of 50 Gbps and 100 Gbps with gVNIC and [per VM Tier_1 networking performance](https://docs.cloud.google.com/compute/docs/networking/configure-vm-with-high-bandwidth-configuration).

### Maintenance experience for C2 instances

During the [lifecycle of a Compute Engine instance](https://docs.cloud.google.com/compute/docs/instances/instance-lifecycle), the host machine that your instance runs on undergoes multiple *host events*. A host event can include the regular maintenance of Compute Engine infrastructure, or in rare cases, a host error. Compute Engine also applies some non-disruptive lightweight upgrades for the hypervisor and network in the background.

The C2 machine series offers the following features related to host maintenance:

| Machine type | Typical scheduled maintenance event frequency | [Maintenance behavior](https://docs.cloud.google.com/compute/docs/instances/host-maintenance-overview#maintenance_behaviors) | [Advanced notification](https://docs.cloud.google.com/compute/docs/instances/monitor-plan-host-maintenance-event) | [On-demand maintenance](https://docs.cloud.google.com/compute/docs/instances/trigger-host-maintenance-event) | [Simulate maintenance](https://docs.cloud.google.com/compute/docs/instances/simulating-host-maintenance) |
|---|---|---|---|---|---|
| All machine types | Minimum of 30 days | Live migrate | 60 seconds | No | Yes |
| Confidential VM | Minimum of 30 days | Restart in place | 60 seconds | No | Yes |
| Sole tenant node VMs | 4 to 6 weeks | Live migrate, restart in place, or migrate with a node group | none | No | Yes |

The maintenance frequencies shown in the previous table are approximations, not guarantees. Compute Engine might occasionally perform maintenance more frequently.

## What's next

- [Learn about the HPC VM image](https://docs.cloud.google.com/compute/docs/instances/create-hpc-vm)
- [Create an instance](https://docs.cloud.google.com/compute/docs/instances/create-start-instance).
- [Create an instance that uses Cloud RDMA](https://docs.cloud.google.com/compute/docs/instances/create-vm-with-rdma)
- Review [Compute Engine instance pricing](https://cloud.google.com/compute/vm-instance-pricing).
- [Configure an instance with a high-bandwidth network](https://docs.cloud.google.com/compute/docs/networking/configure-vm-with-high-bandwidth-configuration).

## Network-optimized machine family for Compute Engine

The network-optimized machine family delivers the highest network and block storage performance within Compute Engine. They offer best-in-class price-performance optimized for demanding I/O bound applications such as network and security appliances, high-performance databases, Telco 5G UPF, high-scale data analytics, and distributed file systems. Compared to the general-purpose machine family, the machine series in the network-optimized machine family offer significantly higher:

- Network bandwidth
- Packet processing performance (PPS)
- Storage throughput and IOPS per vCPU

By eliminating the need to over-provision compute resources just to scale I/O capabilities, the network-optimized family delivers significant Total Cost of Ownership (TCO) benefits.

| **Machine series** | **Workloads** |
| [C4N](https://docs.cloud.google.com/compute/docs/network-optimized-machines#c4n_series) | - Network and Security appliances - Firewall - Load balancers - Virtual routers - DDOS mitigation appliances - NatProxy - CDN - Telco (5G UPF) - High density containers - Filesystems - High performance databases - Large-scale data analytics - CPU-based AI/ML workloads |
| [M4N](https://docs.cloud.google.com/compute/docs/network-optimized-machines#m4n_series) | - High-performance vector databases - Retrieval-augmented generation (RAG) data layers - Massive in-memory context caching - Real-time semantic search |
|---|---|

## C4N machine series

C4N instances are powered by 5th Generation Intel Xeon Scalable processors (code named Emerald Rapids) running high-frequency DDR5 memory and dual-NIC [Titanium](https://cloud.google.com/titanium) offloaded architecture. The C4N machine series is engineered to maximize both networking throughput and extreme block storage performance without requiring premium infrastructure add-ons (such as per VM Tier_1 networking performance).

- **For databases**: When compared to similarly sized C4 instances, C4N delivers 45% better queries per second for MySQL when the data resides primarily on disk.
- **For web-serving workloads**: C4N significantly boosts performance for network-bound web applications. C4N delivers up to 55% additional Nginx requests per second for typical web request sizes (100-300kb) when compared to C4.

C4N instances are available in 8 predefined machine types across standard, high CPU, and high memory configurations, scaling from 2 to 192 vCPUs and up to 1.5 TB of memory.

C4N offers the following features:

- **Superior VM-to-VM network bandwidth**: Achieves up to 400 Gbps of VM-to-VM network bandwidth and supports up to 50 Gbps single-flow bandwidth between C4N instances routed within the same VPC network.
- **Enhanced VM to Internet performance**: Internet egress network bandwidth can reach up to 200 Gbps. Internet egress packet processing performance can scale up to 48 million packets per second (MPPS).
- **Industry-leading packet processing**: Up to 95 MPPS of sustained packet processing performance (measured using DPDK Pktgen).
- **Optimized I/O for smaller shapes**: Up to 25 to 50 Gbps of network bandwidth specifically for machine types with 2 to 16 vCPUs. Additionally, these smaller machine types introduce predictable, steady-state baseline bandwidth limits to provide consistent performance at a lower cost.
- **Enhanced out-of-the-box networking**: gVNIC-type network interfaces on C4N now start with more Tx/Rx queues by default, and scale with the number of vCPUs up to a maximum of 64 per vNIC.
- **Titanium-powered efficiency with Dual-NIC Titanium architecture**: Features two 200G Titanium network adapters (2 x 200G) to fully offload network and storage management, ensuring your applications run with maximum performance and predictability.
- **Leading Block Storage performance and options**: Supports the complete Hyperdisk portfolio, including Hyperdisk Balanced, Hyperdisk Balanced High Availability, Hyperdisk Extreme, Hyperdisk Throughput, and Hyperdisk ML block storage options. C4N with Hyperdisk Extreme provides the low-latency, high-speed data access that modern databases and enterprise AI applications need, with up to 25 GiB/s of block storage throughput and nearly 1M IOPS. C4N offers a 2.5x increase in storage performance over C4.

C4N supports the following discount and consumption options:

- Resource-based committed use discounts (CUDs)
- Flexible CUDs
- Spot VMs
- Reservations
- Sole-tenancy
- Spread and compact placement policies

### C4N Limitations

The C4N machine series has the following restrictions:

- C4N machine types are only available as predefined machine types. Custom machine types aren't available.
- You can't use GPUs with C4N instances.

<br />

### C4N machine types

<br />

### C4N highcpu

| Machine types | vCPUs^1^ | Memory (GB) | Titanium SSD | Physical NIC count | NUMA domains | Maximum internal bandwidth (Gbps) | Maximum external bandwidth (Gbps) |
|---|---|---|---|---|---|---|---|
| `c4n-highcpu-2` | 2 | 4 | Not supported | 1 | 1 shared | Up to 25 | Up to 7 |
| `c4n-highcpu-4` | 4 | 8 | Not supported | 1 | 1 shared | Up to 30 | Up to 7 |
| `c4n-highcpu-8` | 8 | 16 | Not supported | 1 | 1 shared | Up to 40 | Up to 15 |
| `c4n-highcpu-16` | 16 | 32 | Not supported | 1 | 1 shared | Up to 50 | Up to 25 |
| `c4n-highcpu-24` | 24 | 48 | Not supported | 1 | 1 shared | 50 | Up to 25 |
| `c4n-highcpu-48` | 48 | 96 | Not supported | 1 | 1 isolated | 100 | Up to 50 |
| `c4n-highcpu-96` | 96 | 192 | Not supported | 1 | 2 | 200 | Up to 100 |
| `c4n-highcpu-192` | 192 | 384 | Not supported | 2 | 4 (full machine) | 400^2^ | Up to 200 |

### C4N standard

| Machine types | vCPUs^1^ | Memory (GB) | Titanium SSD | Physical NIC count | NUMA domains | Maximum internal bandwidth (Gbps) | Maximum external bandwidth (Gbps) |
|---|---|---|---|---|---|---|---|
| `c4n-standard-2` | 2 | 7 | Not supported | 1 | 1 shared | Up to 25 | Up to 7 |
| `c4n-standard-4` | 4 | 15 | Not supported | 1 | 1 shared | Up to 30 | Up to 7 |
| `c4n-standard-8` | 8 | 30 | Not supported | 1 | 1 shared | Up to 40 | Up to 15 |
| `c4n-standard-16` | 16 | 60 | Not supported | 1 | 1 shared | Up to 50 | Up to 25 |
| `c4n-standard-24` | 24 | 90 | Not supported | 1 | 1 shared | 50 | Up to 25 |
| `c4n-standard-48` | 48 | 180 | Not supported | 1 | 1 isolated | 100 | Up to 50 |
| `c4n-standard-96` | 96 | 360 | Not supported | 1 | 2 | 200 | Up to 100 |
| `c4n-standard-192` | 192 | 720 | Not supported | 2 | 4 (full machine) | 400^2^ | Up to 200 |

### C4N highmem

| Machine types | vCPUs^1^ | Memory (GB) | Titanium SSD | Physical NIC count | NUMA domains | Maximum internal bandwidth (Gbps) | Maximum external bandwidth (Gbps) |
|---|---|---|---|---|---|---|---|
| `c4n-highmem-2` | 2 | 15 | Not supported | 1 | 1 shared | Up to 25 | Up to 7 |
| `c4n-highmem-4` | 4 | 31 | Not supported | 1 | 1 shared | Up to 30 | Up to 7 |
| `c4n-highmem-8` | 8 | 62 | Not supported | 1 | 1 shared | Up to 40 | Up to 15 |
| `c4n-highmem-16` | 16 | 124 | Not supported | 1 | 1 shared | Up to 50 | Up to 25 |
| `c4n-highmem-24` | 24 | 186 | Not supported | 1 | 1 shared | 50 | Up to 25 |
| `c4n-highmem-48` | 48 | 372 | Not supported | 1 | 1 isolated | 100 | Up to 50 |
| `c4n-highmem-96` | 96 | 744 | Not supported | 1 | 2 | 200 | Up to 100 |
| `c4n-highmem-192` | 192 | 1488 | Not supported | 2 | 4 (full machine) | 400^2^ | Up to 200 |

### C4N standard

| Machine types | vCPUs^1^ | Memory (GB) | Titanium SSD | Physical NIC count | NUMA domains | Maximum internal bandwidth (Gbps) | Maximum external bandwidth (Gbps) |
|---|---|---|---|---|---|---|---|
| `c4n-standard-4-lssd` ([Preview](https://cloud.google.com/products#product-launch-stages)) | 4 | 15 | (1 x 375 GiB) 375 GiB | 1 | 1 shared | Up to 30 | Up to 7 |
| `c4n-standard-8-lssd` ([Preview](https://cloud.google.com/products#product-launch-stages)) | 8 | 30 | (1 x 375 GiB) 375 GiB | 1 | 1 shared | Up to 40 | Up to 15 |
| `c4n-standard-16-lssd` ([Preview](https://cloud.google.com/products#product-launch-stages)) | 16 | 60 | (2 x 375 GiB) 750 GiB | 1 | 1 shared | Up to 50 | Up to 25 |
| `c4n-standard-24-lssd` ([Preview](https://cloud.google.com/products#product-launch-stages)) | 24 | 90 | (4 x 375 GiB) 1,500 GiB | 1 | 1 shared | 50 | Up to 25 |
| `c4n-standard-48-lssd` ([Preview](https://cloud.google.com/products#product-launch-stages)) | 48 | 180 | (8 x 375 GiB) 3,000 GiB | 1 | 1 isolated | 100 | Up to 50 |
| `c4n-standard-96-lssd` ([Preview](https://cloud.google.com/products#product-launch-stages)) | 96 | 360 | (16 x 375 GiB) 6,000 GiB | 1 | 2 | 200 | Up to 100 |
| `c4n-standard-192-lssd` ([Preview](https://cloud.google.com/products#product-launch-stages)) | 192 | 720 | (32 x 375 GiB) 12,000 GiB | 2 | 4 (full machine) | 400^2^ | Up to 200 |

### C4N highmem

| Machine types | vCPUs^1^ | Memory (GB) | Titanium SSD | Physical NIC count | NUMA domains | Maximum internal bandwidth (Gbps) | Maximum external bandwidth (Gbps) |
|---|---|---|---|---|---|---|---|
| `c4n-highmem-4-lssd` ([Preview](https://cloud.google.com/products#product-launch-stages)) | 4 | 31 | (1 x 375 GiB) 375 GiB | 1 | 1 shared | Up to 30 | Up to 7 |
| `c4n-highmem-8-lssd` ([Preview](https://cloud.google.com/products#product-launch-stages)) | 8 | 62 | (1 x 375 GiB) 375 GiB | 1 | 1 shared | Up to 40 | Up to 15 |
| `c4n-highmem-16-lssd` ([Preview](https://cloud.google.com/products#product-launch-stages)) | 16 | 124 | (2 x 375 GiB) 750 GiB | 1 | 1 shared | Up to 50 | Up to 25 |
| `c4n-highmem-24-lssd` ([Preview](https://cloud.google.com/products#product-launch-stages)) | 24 | 186 | (4 x 375 GiB) 1,500 GiB | 1 | 1 shared | 50 | Up to 25 |
| `c4n-highmem-48-lssd` ([Preview](https://cloud.google.com/products#product-launch-stages)) | 48 | 372 | (8 x 375 GiB) 3,000 GiB | 1 | 1 isolated | 100 | Up to 50 |
| `c4n-highmem-96-lssd` ([Preview](https://cloud.google.com/products#product-launch-stages)) | 96 | 744 | (16 x 375 GiB) 6,000 GiB | 1 | 2 | 200 | Up to 100 |
| `c4n-highmem-192-lssd` ([Preview](https://cloud.google.com/products#product-launch-stages)) | 192 | 1,488 | (32 x 375 GiB) 12,000 GiB | 2 | 4 (full machine) | 400^2^ | Up to 200 |

<br />

<br />

^1^ Each virtual CPU (vCPU) is implemented as a single hardware multithread. By default, two vCPUs share each physical CPU core.  
^2^ For instances with 192 vCPUs, you must configure at least 2 network interfaces (vNIC), with each network interface attached to a different physical NIC, to achieve the full network throughput. Compute Engine automatically maps the vNIC to a physical NIC in a round-robin fashion.

<br />

### Supported disk types for C4N

C4N instances support only the NVMe disk interface and can use the following block storage types:

- Hyperdisk Balanced (`hyperdisk-balanced`)
- Hyperdisk Balanced High Availability (`hyperdisk-balanced-high-availability`)
- Hyperdisk Throughput (`hyperdisk-throughput`)
- Hyperdisk Extreme (`hyperdisk-extreme`)
- Hyperdisk ML (`hyperdisk-ml`)
- Titanium SSD ([Preview](https://cloud.google.com/products#product-launch-stages))

For the performance limits of each Hyperdisk type, see [Hyperdisk performance limits](https://docs.cloud.google.com/compute/docs/disks/hyperdisk-perf-limits).

> [!NOTE]
> **Note:** To use Local SSD disks with C4N instances, you must first [Request access](https://forms.gle/ehRSqssSEavKt1Fh7).

#### Disk and capacity limits

The following restrictions apply:

- The number of Hyperdisk volumes can't exceed 64 per VM.
- The maximum total disk capacity across all disks can't exceed 512 TiB.

For details about the capacity limits, see [Hyperdisk capacity limits per VM](https://docs.cloud.google.com/compute/docs/disks/hyperdisks#limits-instance).

C4N storage limits are described in the following table:

<br />

### C4N highcpu

| Maximum number of disks per instance |||||||
| Machine types | All Hyperdisk types | Hyperdisk Balanced | Hyperdisk Balanced High Availability | Hyperdisk Throughput | Hyperdisk Extreme | Hyperdisk ML |
|---|---|---|---|---|---|---|
| `c4n-highcpu-2` | 8 | 8 | 8 | 8 | 8 | 8 |
| `c4n-highcpu-4` | 16 | 16 | 16 | 16 | 16 | 16 |
| `c4n-highcpu-8` | 32 | 32 | 32 | 32 | 32 | 32 |
| `c4n-highcpu-16` | 32 | 32 | 32 | 32 | 32 | 32 |
| `c4n-highcpu-24` | 32 | 32 | 32 | 32 | 32 | 32 |
| `c4n-highcpu-48` | 64 | 64 | 64 | 64 | 64 | 64 |
| `c4n-highcpu-96` | 128 | 128 | 128 | 128 | 128 | 128 |
| `c4n-highcpu-192` | 128 | 128 | 128 | 128 | 128 | 128 |

### C4N standard

| Maximum number of disks per instance |||||||
| Machine types | All Hyperdisk types | Hyperdisk Balanced | Hyperdisk Balanced High Availability | Hyperdisk Throughput | Hyperdisk Extreme | Hyperdisk ML |
|---|---|---|---|---|---|---|
| `c4n-standard-2` | 8 | 8 | 8 | 8 | 8 | 8 |
| `c4n-standard-4` | 16 | 16 | 16 | 16 | 16 | 16 |
| `c4n-standard-8` | 32 | 32 | 32 | 32 | 32 | 32 |
| `c4n-standard-16` | 32 | 32 | 32 | 32 | 32 | 32 |
| `c4n-standard-24` | 32 | 32 | 32 | 32 | 32 | 32 |
| `c4n-standard-48` | 64 | 64 | 64 | 64 | 64 | 64 |
| `c4n-standard-96` | 128 | 128 | 128 | 128 | 128 | 128 |
| `c4n-standard-192` | 128 | 128 | 128 | 128 | 128 | 128 |

### C4N highmem

| Maximum number of disks per instance |||||||
| Machine types | All Hyperdisk types | Hyperdisk Balanced | Hyperdisk Balanced High Availability | Hyperdisk Throughput | Hyperdisk Extreme | Hyperdisk ML |
|---|---|---|---|---|---|---|
| `c4n-highmem-2` | 8 | 8 | 8 | 8 | 8 | 8 |
| `c4n-highmem-4` | 16 | 16 | 16 | 16 | 16 | 16 |
| `c4n-highmem-8` | 32 | 32 | 32 | 32 | 32 | 32 |
| `c4n-highmem-16` | 32 | 32 | 32 | 32 | 32 | 32 |
| `c4n-highmem-24` | 32 | 32 | 32 | 32 | 32 | 32 |
| `c4n-highmem-48` | 64 | 64 | 64 | 64 | 64 | 64 |
| `c4n-highmem-96` | 128 | 128 | 128 | 128 | 128 | 128 |
| `c4n-highmem-192` | 128 | 128 | 128 | 128 | 128 | 128 |

### C4N standard

| Maximum number of disks per instance |||||||
| Machine types | All Hyperdisk types | Hyperdisk Balanced | Hyperdisk Balanced High Availability | Hyperdisk Throughput | Hyperdisk Extreme | Hyperdisk ML |
|---|---|---|---|---|---|---|
| `c4n-standard-4-lssd` ([Preview](https://cloud.google.com/products#product-launch-stages)) | 16 | 16 | 16 | 16 | 16 | 16 |
| `c4n-standard-8-lssd` ([Preview](https://cloud.google.com/products#product-launch-stages)) | 32 | 32 | 32 | 32 | 32 | 32 |
| `c4n-standard-16-lssd` ([Preview](https://cloud.google.com/products#product-launch-stages)) | 32 | 32 | 32 | 32 | 32 | 32 |
| `c4n-standard-24-lssd` ([Preview](https://cloud.google.com/products#product-launch-stages)) | 32 | 32 | 32 | 32 | 32 | 32 |
| `c4n-standard-48-lssd` ([Preview](https://cloud.google.com/products#product-launch-stages)) | 64 | 64 | 64 | 64 | 64 | 64 |
| `c4n-standard-96-lssd` ([Preview](https://cloud.google.com/products#product-launch-stages)) | 128 | 128 | 128 | 128 | 128 | 128 |
| `c4n-standard-192-lssd` ([Preview](https://cloud.google.com/products#product-launch-stages)) | 128 | 128 | 128 | 128 | 128 | 128 |

### C4N highmem

| Maximum number of disks per instance |||||||
| Machine types | All Hyperdisk types | Hyperdisk Balanced | Hyperdisk Balanced High Availability | Hyperdisk Throughput | Hyperdisk Extreme | Hyperdisk ML |
|---|---|---|---|---|---|---|
| `c4n-highmem-4-lssd` ([Preview](https://cloud.google.com/products#product-launch-stages)) | 16 | 16 | 16 | 16 | 16 | 16 |
| `c4n-highmem-8-lssd` ([Preview](https://cloud.google.com/products#product-launch-stages)) | 32 | 32 | 32 | 32 | 32 | 32 |
| `c4n-highmem-16-lssd` ([Preview](https://cloud.google.com/products#product-launch-stages)) | 32 | 32 | 32 | 32 | 32 | 32 |
| `c4n-highmem-24-lssd` ([Preview](https://cloud.google.com/products#product-launch-stages)) | 32 | 32 | 32 | 32 | 32 | 32 |
| `c4n-highmem-48-lssd` ([Preview](https://cloud.google.com/products#product-launch-stages)) | 64 | 64 | 64 | 64 | 64 | 64 |
| `c4n-highmem-96-lssd` ([Preview](https://cloud.google.com/products#product-launch-stages)) | 128 | 128 | 128 | 128 | 128 | 128 |
| `c4n-highmem-192-lssd` ([Preview](https://cloud.google.com/products#product-launch-stages)) | 128 | 128 | 128 | 128 | 128 | 128 |

<br />

### Network support for C4N instances

C4N instances deliver up to 400 Gbps standard network bandwidth for VM-to-VM networking, a 4x increase in network bandwidth per vCPU when compared to standard C4 instances. C4N instances don't use per VM Tier_1 networking performance.

For the largest C4N machine types (192 vCPUs), during instance creation you must configure at least 2 network interfaces (vNICs) that use [Jumbo frames (8896B)](https://docs.cloud.google.com/compute/docs/network-bandwidth#jumbo-mtu) to achieve the full network throughput. Compute Engine maps the vNICs automatically to physical NICs (pNICs) in a round-robin way. The guest OS or your application can then divide the network load across at least two vNICs (mapped to separate pNICs) to achieve the full network throughput and ensure optimal performance.

C4N instances require [gVNIC network interfaces](https://docs.cloud.google.com/compute/docs/networking/using-gvnic). The maximum number of network interfaces that you can attach to an instance scales with the number of vCPUs, up to a maximum of 10 network interfaces. For more information about using multiple network interfaces with Compute Engine, see [Multiple network interfaces](https://docs.cloud.google.com/vpc/docs/multiple-interfaces-concepts).

Before migrating to C4N or creating C4N instances, make sure that the [operating system image](https://docs.cloud.google.com/compute/docs/images/os-details#networking) that you use fully supports C4N and higher network bandwidths. Google recommends using the latest gVNIC driver version to benefit from additional features and bug fixes.

### Maintenance experience for C4N instances

During the [lifecycle of a Compute Engine instance](https://docs.cloud.google.com/compute/docs/instances/instance-lifecycle), the host machine that your instance runs on undergoes multiple *host events*. A host event can include the regular maintenance of Compute Engine infrastructure, or in rare cases, a host error. Compute Engine also applies some non-disruptive lightweight upgrades for the hypervisor and network in the background.

The C4N machine series offers the following features related to host maintenance:

<br />

| Machine type | Typical scheduled maintenance event frequency | [Maintenance behavior](https://docs.cloud.google.com/compute/docs/instances/host-maintenance-overview#maintenance_behaviors) | [Advanced notification](https://docs.cloud.google.com/compute/docs/instances/monitor-plan-host-maintenance-event) | [On-demand maintenance](https://docs.cloud.google.com/compute/docs/instances/trigger-host-maintenance-event) | [Simulate maintenance](https://docs.cloud.google.com/compute/docs/instances/simulating-host-maintenance) |
|---|---|---|---|---|---|
| `c4n-*-192` | Minimum of 30 days | Live migrate | Up to 7 days | Yes | Yes |
| `c4n-*-lssd` ([Preview](https://cloud.google.com/products#product-launch-stages)) | Minimum of 30 days | Live migrate | Up to 7 days | Yes | Yes |
| All others | Minimum of 30 days | Live migrate | Up to 7 days | No | Yes |

<br />

The maintenance frequencies shown in the previous table are approximations, not guarantees. Compute Engine might occasionally perform maintenance more frequently.

## M4N machine series

M4N is engineered to deliver the highest I/O performance available, reaching up to 12,500 MiB/s of combined host storage performance and up to 200 Gbps network bandwidth. This new level of performance opens up new possibilities for I/O-intensive workloads that require extreme bandwidth for data access and processing.

M4N instances are powered by the Intel Emerald Rapids processors and [Titanium](https://cloud.google.com/titanium) offload processors. This machine series is well-suited for large in-memory databases such as SAP HANA, as well as online analytical processing (OLAP) and in-memory data analytics workloads. The M4N machine series offers a lower cost per transaction for Oracle Database workloads and the best TCO when compared to any other compute instance for databases that require licensing per core.

M4N machine types allow you to provision up to 112 vCPUs and up to 2.9 TB of RAM. M4N instances use only NVMe for storage, and support [Hyperdisk Balanced](https://docs.cloud.google.com/compute/docs/disks/hd-types/hyperdisk-balanced) and [Hyperdisk Extreme](https://docs.cloud.google.com/compute/docs/disks/hd-types/hyperdisk-extreme). M4N instances use only [gVNIC for networking](https://docs.cloud.google.com/compute/docs/networking/using-gvnic). VirtIO-net and SCSI interfaces are not supported.

### M4N Limitations

The M4N machine series has the following restrictions:

- M4N machine types are only available as predefined machine types. Custom machine types aren't available.
- You can't use GPUs with M4N instances.
- M4N instances are available in only [select zones and regions](https://docs.cloud.google.com/compute/docs/regions-zones#available).

<br />

### M4N machine types

<br />

| Machine types | vCPUs^1^ | Memory (GB) | Local SSD | Maximum internal network bandwidth (Gbps)^2^ | Maximum external network bandwidth (Gbps)^2^ | NUMA domains |
|---|---|---|---|---|---|---|
| `m4n-hypermem-16` | 16 | 248 | Not available | Up to 50 | Up to 25 | 1 |
| `m4n-hypermem-32` | 32 | 496 | Not available | 57 | 28 | 1 |
| `m4n-hypermem-64` | 64 | 992 | Not available | 114 | 57 | 2 |
| `m4n-megamem-28` | 28 | 372 | Not available | 50 | 25 | 1 |
| `m4n-megamem-56` | 56 | 744 | Not available | 100 | 50 | 1 |
| `m4n-megamem-112` | 112 | 1,488 | Not available | 200 | 100 | 2 |
| `m4n-ultramem-56` | 56 | 1,488 | Not available | 100 | 50 | 2 |
| `m4n-ultramem-112` | 112 | 2,976 | Not available | 200 | 100 | 4 |

^1^ Each virtual CPU (vCPU) is implemented as a single hardware multithread, and two vCPUs share each physical CPU core by default.  
^2^ Maximum egress bandwidth cannot exceed the number given. Actual egress bandwidth depends on the destination IP address and other factors. See [Network bandwidth](https://docs.cloud.google.com/compute/docs/network-bandwidth).  

<br />

### Supported disk types for M4N

M4N instances can use the following block storage types:

- Hyperdisk Balanced (`hyperdisk-balanced`)
- Hyperdisk Extreme (`hyperdisk-extreme`)

#### Disk and capacity limits

The following restrictions apply:

- The number of Hyperdisk volumes can't exceed 64 per VM.
- The maximum total disk capacity across all disks can't exceed 512 TiB.

For details about the capacity limits, see [Hyperdisk capacity limits per VM](https://docs.cloud.google.com/compute/docs/disks/hyperdisks#limits-instance).

M4N storage limits are described in the following table:

<br />

|   | Maximum number of disks |||   |
| Machine types | Hyperdisk per VM | Hyperdisk Balanced | Hyperdisk Throughput | Hyperdisk Extreme |
|---|---|---|---|---|
| `m4n-hypermem-16` | 16 | 16 | 0 | 8 |
| `m4n-hypermem-32` | 32 | 32 | 0 | 8 |
| `m4n-hypermem-64` | 32 | 32 | 0 | 8 |
| `m4n-megamem-28` | 32 | 32 | 0 | 8 |
| `m4n-megamem-56` | 32 | 32 | 0 | 8 |
| `m4n-megamem-112` | 64 | 64 | 0 | 8 |
| `m4n-ultramem-56` | 32 | 32 | 0 | 8 |
| `m4n-ultramem-112` | 64 | 64 | 0 | 8 |

<br />

### Network support for M4N instances

M4N instances require [gVNIC network interfaces](https://docs.cloud.google.com/compute/docs/networking/using-gvnic). M4N supports up to 200 Gbps network bandwidth for standard networking and doesn't support per VM Tier_1 networking performance.

Before migrating to M4N or creating M4N VM instances, make sure that the [operating system image](https://docs.cloud.google.com/compute/docs/images/os-details#networking) that you use supports the gVNIC driver for VM instances. These images include an updated gVNIC driver, even if the guest OS shows the `gve` driver version as 1.0.0. If your M4N VM is using an operating system with an older version of gVNIC driver, this is still supported but the VM might experience suboptimal performance such as less network bandwidth or higher latency.

If you use a custom OS image to create a M4N VM, you can [manually install the most recent gVNIC driver](https://docs.cloud.google.com/compute/docs/networking/using-gvnic#manual-gvnic-setup). The gVNIC driver version v1.4.2 or later is recommended for use with M4N VMs. Google recommends using the latest gVNIC driver version to benefit from additional features and bug fixes.

### Maintenance experience for M4N instances

During the [lifecycle of a Compute Engine instance](https://docs.cloud.google.com/compute/docs/instances/instance-lifecycle), the host machine that your instance runs on undergoes multiple *host events*. A host event can include the regular maintenance of Compute Engine infrastructure, or in rare cases, a host error. Compute Engine also applies some non-disruptive lightweight upgrades for the hypervisor and network in the background.

The M4N machine series offers the following features related to host maintenance:

<br />

| Machine type | Typical scheduled maintenance event frequency | [Maintenance behavior](https://docs.cloud.google.com/compute/docs/instances/host-maintenance-overview#maintenance_behaviors) | [Advanced notification](https://docs.cloud.google.com/compute/docs/instances/monitor-plan-host-maintenance-event) | [On-demand maintenance](https://docs.cloud.google.com/compute/docs/instances/trigger-host-maintenance-event) | [Simulate maintenance](https://docs.cloud.google.com/compute/docs/instances/simulating-host-maintenance) |
|---|---|---|---|---|---|
| All machine types | Monthly | Live migrate | 7 days | Yes | Yes |

<br />

The maintenance frequencies shown in the previous table are approximations, not guarantees. Compute Engine might occasionally perform maintenance more frequently.

## What's next

- [Create and start a Compute Engine instance](https://docs.cloud.google.com/compute/docs/instances/create-start-instance)
- Learn about the different [block storage options](https://docs.cloud.google.com/compute/docs/disks) for your compute instance
- Learn how to [move your workload to a new compute instance](https://docs.cloud.google.com/compute/docs/import/migrate-to-new-vm)
- Review [Virtual machine pricing](https://docs.cloud.google.com/compute/vm-instance-pricing#network-optimized)

## Memory-optimized machine family for Compute Engine

The memory-optimized machine family provides the most compute and memory resources of any Compute Engine machine family offering. They are ideal for workloads that require higher memory-to-vCPU ratios than the high-memory machine types in the general-purpose machine series.

- The X4 machine series offers bare metal instances with 6 to 32 TB of memory.
- The M4N machine series offers VM instances with up to 3 TB of memory.
- The M4 machine series offers VM instances with up to 6 TB of memory.
- The M3 machine series offers VM instances with 1 to 4 TB of memory.
- The M2 machine series offers VM instances with up to 12 TB of memory.
- The M1 machine series offers VM instances with up to 4 TB of memory.

These machine series are well-suited for large in-memory databases such as SAP HANA, as well as online analytical processing (OLAP) and in-memory data analytics workloads.

The X4, M4N, M4, M3, M2, and M1 machine series offer the lowest cost per GB of memory on Compute Engine, making them a great choice for workloads that utilize higher memory configurations with low compute resources requirements. Additionally, M2 and M1 offer savings of up to 30% with sustained use discounts. X4, M4N, M4, M3, M2, and M1 are eligible for [resource-based committed use discounts (CUDs)](https://docs.cloud.google.com/compute/docs/instances/signing-up-committed-use-discounts), that bring savings of greater than 60% in exchange for 3-year commitments.

| **Machine series** | **Workloads** |
| [X4 machine series](https://docs.cloud.google.com/compute/docs/memory-optimized-machines#x4_machine_types) | - Extra large SAP HANA systems - On-demand, enterprise grade, ultra memory-equipped IaaS - High performance computing |
| [M4N machine series](https://docs.cloud.google.com/compute/docs/memory-optimized-machines#m4n_machine_types) | - High-performance vector databases - Retrieval-augmented generation (RAG) data layers - Massive in-memory context caching - Real-time semantic search |
| [M4 machine series](https://docs.cloud.google.com/compute/docs/memory-optimized-machines#m4_machine_types) | - OLAP and OLTP SAP workloads - Memory intensive applications, such as genomic modeling and electronic design automation - Small to medium in-memory databases such as SAP HANA - High performance computing |
| [M3 machine series](https://docs.cloud.google.com/compute/docs/memory-optimized-machines#m3_machine_types) | - OLAP and OLTP SAP workloads - Memory intensive applications, such as genomic modeling and electronic design automation - High performance computing |
| [M2 machine series](https://docs.cloud.google.com/compute/docs/memory-optimized-machines#m2_machine_types) | - Large in-memory databases such as SAP HANA - In-memory databases and in-memory analytics, business warehousing (BW) workloads, genomics analysis, SQL analysis services |
| [M1 machine series](https://docs.cloud.google.com/compute/docs/memory-optimized-machines#m1_machine_types) | - Medium in-memory databases such as SAP HANA - Tasks that require intensive use of memory with higher memory-to-vCPU ratios than the general-purpose high-memory machine types. - In-memory databases and in-memory analytics, business warehousing (BW) workloads, genomics analysis, SQL analysis services. - Microsoft SQL Server and similar databases. |
|---|---|

## X4 machine series

The X4 machine series offers more storage and networking options to support your most demanding workloads. The X4 machine series offers six predefined machine types. These machine types provide you with the capability to provision bare metal instances with up to 1,920 vCPUs and up to 32 TB of RAM.

X4 instances are powered by the 4th generation Intel Xeon Scalable processors (code-named Sapphire Rapids) and [Titanium](https://cloud.google.com/titanium). X4 instances use only the NVMe disk interface for storage, and only use [Google Cloud Hyperdisk storage](https://docs.cloud.google.com/compute/docs/disks/hyperdisks). X4 instances use a version of the Intel [Infrastructure Data Plane Function (IDPF) driver](https://docs.cloud.google.com/compute/docs/networking/using-idpf) that has been optimized for use with Google Cloud. VirtIO-net, gVNIC, and SCSI interfaces are not supported.

X4 instances give you access to the raw compute resources of the server. Bare metal instances also provide access to several on-board, function-specific [accelerators and offloads](https://docs.cloud.google.com/compute/docs/cpu-platforms#accelerator):

- Intel QuickAssist Technology (QAT): 1 accelerator
- Intel Dynamic Load Balancer (DLB): 1 accelerator
- Intel Data Streaming Accelerator (DSA): up to 4 accelerators
- Intel In-Memory Analytics Accelerator (IAA): up to 4 accelerators

To move your workload from a VM instance to an X4 bare metal instance, see [Move your workload to a new compute instance](https://docs.cloud.google.com/compute/docs/import/migrate-to-new-vm).

Contact your [Google Cloud account manager](https://cloud.google.com/tam) for pricing and ordering information for X4, or to discuss on-demand pricing for testing X4 instances.

When purchasing [resource-based commitments](https://docs.cloud.google.com/compute/docs/committed-use-discounts/purchase-commitments) for X4 machine types, note that the commitment type is separate for each X4 machine type.

### X4 Limitations

The X4 machine series is only available as predefined machine types. Custom machine shapes are not available. The following additional restrictions apply:

- You can't attach Persistent Disk volumes to an X4 instance, only Hyperdisk volumes.
- The X4 machine series is available in only [select zones and regions](https://docs.cloud.google.com/compute/docs/regions-zones#available).
- X4 instances aren't supported with all operating system images. The [operating system details](https://docs.cloud.google.com/compute/docs/images/os-details) page shows which operating system versions can be used with X4 instances.
- If using a custom image, when you create the image, you must enable the [UEFI-compatible](https://docs.cloud.google.com/compute/docs/images/create-custom#guest-os-features) OS feature.
- [Shielded VM](https://docs.cloud.google.com/compute/shielded-vm/docs/shielded-vm) isn't supported with bare metal instances.
- Live migration is not supported with X4 instances.
- There's no hypervisor provided with X4 bare metal instances and [nested virtualization](https://docs.cloud.google.com/compute/docs/instances/nested-virtualization/overview) isn't enabled.
- X4 machine series instances can take up to 30 mins to boot due to large hardware and the Power-On Self-Test (POST).

### X4 machine types

The following table lists the hardware characteristics of each machine type for the X4 machine series:

| Machine types | vCPUs^1^ | Memory (GB) | Local SSD | Default egress bandwidth (Gbps)^2^ | Tier_1 egress bandwidth (Gbps) |
|---|---|---|---|---|---|
| `x4-480-6t-metal` | 480 | 6,144 | Not available | Up to 100 | Not available |
| `x4-480-8t-metal` | 480 | 8,192 | Not available | Up to 100 | Not available |
| `x4-960-12t-metal` | 960 | 12,288 | Not available | Up to 100 | Not available |
| `x4-960-16t-metal` | 960 | 16,384 | Not available | Up to 100 | Not available |
| `x4-1440-24t-metal` | 1,440 | 24,576 | Not available | Up to 100 | Not available |
| `x4-1920-32t-metal` | 1,920 | 32,768 | Not available | Up to 100 | Not available |

^1^ A vCPU represents a single hardware thread, or logical core. The number of available hardware threads is equivalent to the number of hardware threads on the host server.  
^2^ Maximum egress bandwidth cannot exceed the number given. Actual egress bandwidth depends on the destination IP address and other factors. See [Network bandwidth](https://docs.cloud.google.com/compute/docs/network-bandwidth).  

### Supported disk types for X4

X4 machine types support the following block storage options:

- Hyperdisk Balanced (`hyperdisk-balanced`)
- Hyperdisk Extreme (`hyperdisk-extreme`)

For disks attached to an X4 instance:

- The number of Google Cloud Hyperdisk volumes can't exceed 8 Hyperdisk Extreme or 32 Hyperdisk Balanced per instance. The total number of Google Cloud Hyperdisk volumes can't exceed 32 per instance.
- The maximum total disk capacity (in TiB) across all disk types can't exceed 512 TiB.

For details about the capacity limits, see [Hyperdisk capacity limits per VM](https://docs.cloud.google.com/compute/docs/disks/hyperdisk-perf-limits#limits-instance).

X4 storage limits are described in the following table:

| Maximum number of disks |||||
| Machine types | Google Cloud Hyperdisk per VM | Hyperdisk Balanced | Hyperdisk Throughput | Hyperdisk Extreme |
|---|---|---|---|---|
| `x4-480-6t-metal` | 32 | 32 | Not available | 8 |
| `x4-480-8t-metal` | 32 | 32 | Not available | 8 |
| `x4-960-12t-metal` | 32 | 32 | Not available | 8 |
| `x4-960-16t-metal` | 32 | 32 | Not available | 8 |
| `x4-1440-24t-metal` | 32 | 32 | Not available | 8 |
| `x4-1920-32t-metal` | 32 | 32 | Not available | 8 |

### Network support for X4 instances

X4 bare metal instances require the [Intel IDPF LAN PF device driver](https://docs.cloud.google.com/compute/docs/networking/using-idpf). X4 supports up to 100 Gbps network bandwidth for standard networking. The gVNIC network interface isn't supported with bare metal instances.

Before migrating to X4 or creating X4 instances, make sure that the [operating system image](https://docs.cloud.google.com/compute/docs/images/os-details#networking) that you use supports the IDPF network driver. If you create an X4 instance with an operating system that doesn't support the IDPF driver, then you might not be able to connect to the instance.

### Maintenance experience for X4 instances

During the [lifecycle of a Compute Engine instance](https://docs.cloud.google.com/compute/docs/instances/instance-lifecycle), the host machine that your instance runs on undergoes multiple *host events*. A host event can include the regular maintenance of Compute Engine infrastructure, or in rare cases, a host error. Compute Engine also applies some non-disruptive lightweight upgrades for the hypervisor and network in the background.

The X4 machine series offers the following features related to host maintenance:

| Machine type | Typical scheduled maintenance event frequency | [Maintenance behavior](https://docs.cloud.google.com/compute/docs/instances/host-maintenance-overview#maintenance_behaviors) | [Advanced notification](https://docs.cloud.google.com/compute/docs/instances/monitor-plan-host-maintenance-event) | On-demand maintenance | [Simulate maintenance](https://docs.cloud.google.com/compute/docs/instances/simulating-host-maintenance) |
|---|---|---|---|---|---|
| All machine types | Minimum of 90 days | Restart in place | 60 days | Yes | Yes |

The maintenance frequencies shown in the previous table are approximations, not guarantees. Compute Engine might occasionally perform maintenance more frequently.
X4 also lets you perform maintenance for unplanned emergent maintenance events within a short window of time. Emergent maintenance events are typically needed to address security, hardware, or software issues of medium to high severity that have a high potential for causing outages. These maintenance events are deemed important and time-sensitive, but not critical enough to require an immediate outage to perform the maintenance. Emergent maintenance events have the following features for X4 machine types:

<br />

- [Advanced notification](https://docs.cloud.google.com/compute/docs/instances/monitor-plan-host-maintenance-event): 14 days
- [Maintenance behavior](https://docs.cloud.google.com/compute/docs/instances/host-maintenance-overview#maintenance_behaviors): Restart in place

During emergent maintenance maintenance, X4 instances are moved to a different, healthy host.

For emergent maintenance events, you can trigger the maintenance at any time within the 14 day advance notification period. If you don't begin the maintenance operation within the 14-day period, then the maintenance starts automatically at the end of the advanced notification period.

For information about how to manually start host maintenance events for X4 instances, see [Manually starting host maintenance doesn't work for X4 instances](https://docs.cloud.google.com/compute/docs/troubleshooting/known-issues#x4-ctm).

## M4N machine series

M4N is engineered to deliver the highest I/O performance available, reaching up to 12,500 MiB/s of combined host storage performance and up to 200 Gbps network bandwidth. This new level of performance opens up new possibilities for I/O-intensive workloads that require extreme bandwidth for data access and processing.

M4N instances are powered by the Intel Emerald Rapids processors and [Titanium](https://cloud.google.com/titanium) offload processors. This machine series is well-suited for large in-memory databases such as SAP HANA, as well as online analytical processing (OLAP) and in-memory data analytics workloads. The M4N machine series offers a lower cost per transaction for Oracle Database workloads and the best TCO when compared to any other compute instance for databases that require licensing per core.

M4N machine types allow you to provision up to 112 vCPUs and up to 2.9 TB of RAM. M4N instances use only NVMe for storage, and support [Hyperdisk Balanced](https://docs.cloud.google.com/compute/docs/disks/hd-types/hyperdisk-balanced) and [Hyperdisk Extreme](https://docs.cloud.google.com/compute/docs/disks/hd-types/hyperdisk-extreme). M4N instances use only [gVNIC for networking](https://docs.cloud.google.com/compute/docs/networking/using-gvnic). VirtIO-net and SCSI interfaces are not supported.

### M4N Limitations

The M4N machine series has the following restrictions:

- M4N machine types are only available as predefined machine types. Custom machine types aren't available.
- You can't use GPUs with M4N instances.
- M4N instances are available in only [select zones and regions](https://docs.cloud.google.com/compute/docs/regions-zones#available).

<br />

### M4N machine types

<br />

| Machine types | vCPUs^1^ | Memory (GB) | Local SSD | Maximum internal network bandwidth (Gbps)^2^ | Maximum external network bandwidth (Gbps)^2^ | NUMA domains |
|---|---|---|---|---|---|---|
| `m4n-hypermem-16` | 16 | 248 | Not available | Up to 50 | Up to 25 | 1 |
| `m4n-hypermem-32` | 32 | 496 | Not available | 57 | 28 | 1 |
| `m4n-hypermem-64` | 64 | 992 | Not available | 114 | 57 | 2 |
| `m4n-megamem-28` | 28 | 372 | Not available | 50 | 25 | 1 |
| `m4n-megamem-56` | 56 | 744 | Not available | 100 | 50 | 1 |
| `m4n-megamem-112` | 112 | 1,488 | Not available | 200 | 100 | 2 |
| `m4n-ultramem-56` | 56 | 1,488 | Not available | 100 | 50 | 2 |
| `m4n-ultramem-112` | 112 | 2,976 | Not available | 200 | 100 | 4 |

^1^ Each virtual CPU (vCPU) is implemented as a single hardware multithread, and two vCPUs share each physical CPU core by default.  
^2^ Maximum egress bandwidth cannot exceed the number given. Actual egress bandwidth depends on the destination IP address and other factors. See [Network bandwidth](https://docs.cloud.google.com/compute/docs/network-bandwidth).  

<br />

### Supported disk types for M4N

M4N instances can use the following block storage types:

- Hyperdisk Balanced (`hyperdisk-balanced`)
- Hyperdisk Extreme (`hyperdisk-extreme`)

#### Disk and capacity limits

The following restrictions apply:

- The number of Hyperdisk volumes can't exceed 64 per VM.
- The maximum total disk capacity across all disks can't exceed 512 TiB.

For details about the capacity limits, see [Hyperdisk capacity limits per VM](https://docs.cloud.google.com/compute/docs/disks/hyperdisks#limits-instance).

M4N storage limits are described in the following table:

<br />

|   | Maximum number of disks |||   |
| Machine types | Hyperdisk per VM | Hyperdisk Balanced | Hyperdisk Throughput | Hyperdisk Extreme |
|---|---|---|---|---|
| `m4n-hypermem-16` | 16 | 16 | 0 | 8 |
| `m4n-hypermem-32` | 32 | 32 | 0 | 8 |
| `m4n-hypermem-64` | 32 | 32 | 0 | 8 |
| `m4n-megamem-28` | 32 | 32 | 0 | 8 |
| `m4n-megamem-56` | 32 | 32 | 0 | 8 |
| `m4n-megamem-112` | 64 | 64 | 0 | 8 |
| `m4n-ultramem-56` | 32 | 32 | 0 | 8 |
| `m4n-ultramem-112` | 64 | 64 | 0 | 8 |

<br />

### Network support for M4N instances

M4N instances require [gVNIC network interfaces](https://docs.cloud.google.com/compute/docs/networking/using-gvnic). M4N supports up to 200 Gbps network bandwidth for standard networking and doesn't support per VM Tier_1 networking performance.

Before migrating to M4N or creating M4N VM instances, make sure that the [operating system image](https://docs.cloud.google.com/compute/docs/images/os-details#networking) that you use supports the gVNIC driver for VM instances. These images include an updated gVNIC driver, even if the guest OS shows the `gve` driver version as 1.0.0. If your M4N VM is using an operating system with an older version of gVNIC driver, this is still supported but the VM might experience suboptimal performance such as less network bandwidth or higher latency.

If you use a custom OS image to create a M4N VM, you can [manually install the most recent gVNIC driver](https://docs.cloud.google.com/compute/docs/networking/using-gvnic#manual-gvnic-setup). The gVNIC driver version v1.4.2 or later is recommended for use with M4N VMs. Google recommends using the latest gVNIC driver version to benefit from additional features and bug fixes.

### Maintenance experience for M4N instances

During the [lifecycle of a Compute Engine instance](https://docs.cloud.google.com/compute/docs/instances/instance-lifecycle), the host machine that your instance runs on undergoes multiple *host events*. A host event can include the regular maintenance of Compute Engine infrastructure, or in rare cases, a host error. Compute Engine also applies some non-disruptive lightweight upgrades for the hypervisor and network in the background.

The M4N machine series offers the following features related to host maintenance:

<br />

| Machine type | Typical scheduled maintenance event frequency | [Maintenance behavior](https://docs.cloud.google.com/compute/docs/instances/host-maintenance-overview#maintenance_behaviors) | [Advanced notification](https://docs.cloud.google.com/compute/docs/instances/monitor-plan-host-maintenance-event) | [On-demand maintenance](https://docs.cloud.google.com/compute/docs/instances/trigger-host-maintenance-event) | [Simulate maintenance](https://docs.cloud.google.com/compute/docs/instances/simulating-host-maintenance) |
|---|---|---|---|---|---|
| All machine types | Monthly | Live migrate | 7 days | Yes | Yes |

<br />

The maintenance frequencies shown in the previous table are approximations, not guarantees. Compute Engine might occasionally perform maintenance more frequently.

## M4 machine series

The M4 machine series offers machine types that are suitable for OLTP and OLAP workloads running on SAP HANA. These machine types allow you to provision up to 224 vCPUs and up to 6 TB of RAM. M4 instances use only NVMe for storage, and support [Hyperdisk Balanced](https://docs.cloud.google.com/compute/docs/disks/hd-types/hyperdisk-balanced) and [Hyperdisk Extreme](https://docs.cloud.google.com/compute/docs/disks/hd-types/hyperdisk-extreme). M4 instances use only [gVNIC for networking](https://docs.cloud.google.com/compute/docs/networking/using-gvnic). VirtIO-net and SCSI interfaces are not supported.

M4 instances support resource-based CUDs, Spot VMs, and reservations, as well as performance monitoring unit (PMU), and compact placement policies.

Resource-based CUDs for M4 instances are available under two separate commitment types, each applying to specific machine types. When you purchase a commitment, ensure that you select the correct commitment type, as follows:

- For `m4-ultramem-224` (6 TB), select **Memory-optimized M4 6TB** as the commitment type in the Google Cloud console.
- For any other M4 machine type, select **Memory-optimized M4** as the commitment type in the Google Cloud console.
- If you use gcloud CLI or REST to purchase commitments, see the [resource-based CUDs documentation](https://docs.cloud.google.com/compute/docs/committed-use-discounts/purchase-commitments) for the commitment type values to use.

### M4 machine types

The following table lists the hardware characteristics of each machine type for the M4 machine series:

| Machine types | vCPUs | Memory (GB) | Local SSD | NUMA domains^2^ | Default egress bandwidth (Gbps)^1^ | Tier_1 egress bandwidth (Gbps) |
|---|---|---|---|---|---|---|
| `m4-hypermem-16` | 16 | 248 | Not available | 1 shared | Up to 16 | Not available |
| `m4-hypermem-32` | 32 | 496 | Not available | 1 shared | Up to 32 | Not available |
| `m4-hypermem-64` | 64 | 992 | Not available | 2 shared | Up to 32 | Not available |
| `m4-megamem-28` | 28 | 372 | Not available | 1 shared | Up to 32 | Not available |
| `m4-megamem-56` | 56 | 744 | Not available | 1 isolated | Up to 32 | Not available |
| `m4-megamem-112` | 112 | 1,488 | Not available | 2 isolated | Up to 50 | Not available |
| `m4-megamem-224` | 224 | 2,976 | Not available | 4 (full machine) | Up to 100 | Not available |
| `m4-ultramem-56` | 56 | 1,488 | Not available | 2 shared | Up to 32 | Not available |
| `m4-ultramem-112` | 112 | 2,976 | Not available | 4 shared | Up to 50 | Not available |
| `m4-ultramem-224` | 224 | 5,952 | Not available | 4 (full machine) | Up to 100 | Not available |

^1^ Maximum egress bandwidth can't exceed the number given. Actual egress bandwidth depends on the destination IP address and other factors. See [Network bandwidth](https://docs.cloud.google.com/compute/docs/network-bandwidth).  
^2^ The "NUMA domains" column in the tables shows the number of vNUMA nodes exposed to the guest OS.

### Supported disk types for M4

M4 machine types support the following block storage options:

- Hyperdisk Balanced (`hyperdisk-balanced`)
- Hyperdisk Extreme (`hyperdisk-extreme`)

M4 machine types support only the NVMe disk interface.

M4 instances don't support Persistent Disk or Local SSD. Read [Move your workload from an existing VM to a new VM](https://docs.cloud.google.com/compute/docs/import/migrate-to-new-vm) to migrate your Persistent Disk resources to a newer machine series.

#### Disk and capacity limits

<br />

You can attach a mixture of different Hyperdisk types to an instance, but the maximum total disk capacity (in TiB) across all disk types can't exceed:

- For machine types with less than 32 vCPUs: 257 TiB for all Hyperdisk

- For machine types with 32 or more vCPUs: 512 TiB for all Hyperdisk

For details about the capacity limits, see [Hyperdisk size and attachment limits](https://docs.cloud.google.com/compute/docs/disks/hyperdisk-perf-limits#limits-instance).

<br />

<br />

M4 instance storage limits are described in the following table:

|   | Maximum number of disks ||||
| Machine types | Hyperdisk per VM | Hyperdisk Balanced | Hyperdisk Throughput | Hyperdisk Extreme |
|---|---|---|---|---|
| `m4-hypermem-16` | 16 | 16 | 0 | 0 |
| `m4-hypermem-32` | 32 | 32 | 0 | 0 |
| `m4-hypermem-64` | 32 | 32 | 0 | 8 |
| `m4-megamem-28` | 32 | 32 | 0 | 0 |
| `m4-megamem-56` | 32 | 32 | 0 | 0 |
| `m4-megamem-112` | 64 | 64 | 0 | 8 |
| `m4-ultramem-56` | 32 | 32 | 0 | 0 |
| `m4-ultramem-112` | 64 | 64 | 0 | 8 |
| `m4-ultramem-224` | 128 | 128 | 0 | 8 |

### Network support for M4 instances

M4 instances require [gVNIC network interfaces](https://docs.cloud.google.com/compute/docs/networking/using-gvnic). M4 instances support up to 100 Gbps network bandwidth for standard networking and don't support per VM Tier_1 networking performance.

M4 instances require [gVNIC network interfaces](https://docs.cloud.google.com/compute/docs/networking/using-gvnic). The maximum number of network interfaces that you can attach to an instance scales with the number of vCPUs, up to a maximum of 10 network interfaces. For more information about using multiple network interfaces with Compute Engine, see [Multiple network interfaces](https://docs.cloud.google.com/vpc/docs/multiple-interfaces-concepts).

Before migrating to M4 or creating M4 VM instances, make sure that the [operating system image](https://docs.cloud.google.com/compute/docs/images/os-details#networking) that you use supports the gVNIC driver for VM instances. These images include an updated gVNIC driver, even if the guest OS shows the `gve` driver version as 1.0.0. If your M4 VM is using an operating system with an older version of gVNIC driver, this is still supported but the VM might experience suboptimal performance such as less network bandwidth or higher latency.

If you use a custom OS image to create a M4 VM, you can [manually install the most recent gVNIC driver](https://docs.cloud.google.com/compute/docs/networking/using-gvnic#manual-gvnic-setup). The gVNIC driver version v1.4.2 or later is recommended for use with M4 VMs. Google recommends using the latest gVNIC driver version to benefit from additional features and bug fixes.

### M4 Limitations

The M4 machine series is only available as predefined machine types. Custom machine shapes are not available. The M4 instances are available in only [select zones and regions](https://docs.cloud.google.com/compute/docs/regions-zones#available).

### Maintenance experience for M4 instances

During the [lifecycle of a Compute Engine instance](https://docs.cloud.google.com/compute/docs/instances/instance-lifecycle), the host machine that your instance runs on undergoes multiple *host events*. A host event can include the regular maintenance of Compute Engine infrastructure, or in rare cases, a host error. Compute Engine also applies some non-disruptive lightweight upgrades for the hypervisor and network in the background.

The M4 machine series offers the following features related to host maintenance:

| Machine type | Typical scheduled maintenance event frequency | [Maintenance behavior](https://docs.cloud.google.com/compute/docs/instances/host-maintenance-overview#maintenance_behaviors) | [Advanced notification](https://docs.cloud.google.com/compute/docs/instances/monitor-plan-host-maintenance-event) | [On-demand maintenance](https://docs.cloud.google.com/compute/docs/instances/trigger-host-maintenance-event) | [Simulate maintenance](https://docs.cloud.google.com/compute/docs/instances/simulating-host-maintenance) |
|---|---|---|---|---|---|
| All machine types | Monthly | Live migrate | 7 days | Yes | Yes |

The maintenance frequencies shown in the previous table are approximations, not guarantees. Compute Engine might occasionally perform maintenance more frequently.

## M3 machine series

The M3 machine series introduces two new OLAP shapes for 2 TiB and 1 TiB SAP HANA systems. These machine types allow you to provision up to 128 vCPUs and up to 4 TB of RAM. M3 instances use only NVMe for storage, and support [Hyperdisk Balanced storage](https://docs.cloud.google.com/compute/docs/disks/hd-types/hyperdisk-balanced). M3 machines use only [gVNIC for networking](https://docs.cloud.google.com/compute/docs/networking/using-gvnic). VirtIO-net and SCSI interfaces are not supported.

[Pricing](https://docs.cloud.google.com/compute/all-pricing#memory-optimized) for these instances per vCPU hour and per GB of memory is similar to the pricing for M1 instances. Disk usage and network usage is charged separately from machine type pricing. For details, see [Disk and image pricing](https://cloud.google.com/compute/disks-image-pricing) and [Network pricing](https://cloud.google.com/vpc/network-pricing).

M3 instances support resource-based CUDs, Spot VMs, and reservations, as well as compact placement policies. The commitment type that you must use to purchase M3 instances is separate from the one for M1 or M2 instances. You can purchase a single commitment to cover both M1 and M2 instances, but you can't group M3 instances in that commitment. For more information, see the [Commitment types](https://docs.cloud.google.com/compute/docs/instances/signing-up-committed-use-discounts#commitment_types) section for resource-based commitments.

To update a current instance to use the M3 machine series, see [Move your workload to a new compute instance](https://docs.cloud.google.com/compute/docs/import/migrate-to-new-vm).

### M3 machine types

The following table lists the hardware characteristics of each machine type for the M3 machine series:

| Machine types | vCPUs | Memory (GB) | Local SSD^1^ | Default egress bandwidth (Gbps)^2^ | Tier_1 egress bandwidth (Gbps)^3^ |
|---|---|---|---|---|---|
| `m3-ultramem-32` | 32 | 976 | 4 or 8 | Up to 32 | Not available |
| `m3-ultramem-64` | 64 | 1,952 | 4 or 8 | Up to 32 | Up to 50 |
| `m3-ultramem-128` | 128 | 3,904 | 8 | Up to 32 | Up to 100 |
| `m3-megamem-64` | 64 | 976 | 4 or 8 | Up to 32 | Up to 50 |
| `m3-megamem-128` | 128 | 1,952 | 8 | Up to 32 | Up to 100 |

^1^ Number of 375 GiB Local SSD disks that you can choose to add when creating the instance.  
^2^ Maximum egress bandwidth cannot exceed the number given. Actual egress bandwidth depends on the destination IP address and other factors. See [Network bandwidth](https://docs.cloud.google.com/compute/docs/network-bandwidth).  
^3^ Available with [high-bandwidth networking](https://docs.cloud.google.com/compute/docs/networking/configure-vm-with-high-bandwidth-configuration) on larger machine shapes.

### Supported disk types for M3

M3 machine types support the following block storage options:

- Zonal balanced Persistent Disk (`pd-balanced`)
- Zonal SSD (performance) Persistent Disk (`pd-ssd`)
- [Extreme Persistent Disk](https://docs.cloud.google.com/compute/docs/disks/extreme-persistent-disk) (`pd-extreme`)
- Hyperdisk Balanced (`hyperdisk-balanced`)
- Hyperdisk Balanced High Availability (`hyperdisk-balanced-high-availability`)
- Hyperdisk Extreme (`hyperdisk-extreme`)
- Hyperdisk Throughput (`hyperdisk-throughput`)
- Local SSD

M3 machine types support only the NVMe disk interface.

#### Disk and capacity limits

<br />

If supported by the machine type, you can attach a mixture of Hyperdisk and Persistent Disk volumes to an instance, but the following restrictions apply:

- The combined number of both Hyperdisk and Persistent Disk volumes can't exceed 128 per instance.
- The maximum total disk capacity (in TiB) across all disk types can't exceed:

  - For machine types with less than 32 vCPUs:

    - 257 TiB for all Hyperdisk or all Persistent Disk
    - 257 TiB for a mixture of Hyperdisk and Persistent Disk
  - For machine types with 32 or more vCPUs:

    - 512 TiB for all Hyperdisk
    - 512 TiB for a mixture of Hyperdisk and Persistent Disk
    - 257 TiB for all Persistent Disk

For details about the capacity limits, see [Hyperdisk size and attachment limits](https://docs.cloud.google.com/compute/docs/disks/hyperdisk-perf-limits#limits-instance) and [Persistent Disk maximum capacity](https://docs.cloud.google.com/compute/docs/disks/persistent-disks#capacity_257tb).

<br />

The maximum number of disks that you can attach to M3 instances are described in the following table:

| Machine types | Per VM^1^ | Hyperdisk per VM | Hyperdisk Balanced | Hyperdisk Throughput | Hyperdisk Extreme |
|---|---|---|---|---|---|
| `m3-ultramem-32` | 128 | 64 | 32 | 64 | 0 |
| `m3-ultramem-64` | 128 | 64 | 32 | 64 | 8 |
| `m3-ultramem-128` | 128 | 64 | 32 | 64 | 8 |
| `m3-megamem-64` | 128 | 64 | 32 | 64 | 8 |
| `m3-megamem-128` | 128 | 64 | 32 | 64 | 8 |

^1^ This limit applies to Persistent Disk and Hyperdisk, but doesn't include Local SSD disks.

### Network support for M3 instances

M3 instances require [gVNIC network interfaces](https://docs.cloud.google.com/compute/docs/networking/using-gvnic). M3 instances support up to 32 Gbps network bandwidth for standard networking and up to 100 Gbps network bandwidth per VM Tier_1 networking performance.

Before migrating to M3 or creating M3 VM instances, make sure that the [operating system image](https://docs.cloud.google.com/compute/docs/images/os-details#networking) that you use supports the gVNIC driver for VM instances. These images include an updated gVNIC driver, even if the guest OS shows the `gve` driver version as 1.0.0. If your M3 VM is using an operating system with an older version of gVNIC driver, this is still supported but the VM might experience suboptimal performance such as less network bandwidth or higher latency.

If you use a custom OS image to create a M3 VM, you can [manually install the most recent gVNIC driver](https://docs.cloud.google.com/compute/docs/networking/using-gvnic#manual-gvnic-setup). The gVNIC driver version v1.4.2 or later is recommended for use with M3 VMs. Google recommends using the latest gVNIC driver version to benefit from additional features and bug fixes.

### M3 Limitations

The M3 machine series is only available as predefined machine types. Custom machine shapes are not available. The following additional restrictions apply:

- You can't use [regional Persistent Disk](https://docs.cloud.google.com/compute/docs/disks/regional-persistent-disk) with the M3 machine series.
- The M3 machine series is available in only [select zones and regions](https://docs.cloud.google.com/compute/docs/regions-zones#available).
- M3 instances aren't available with all operating system images. The [operating system details](https://docs.cloud.google.com/compute/docs/images/os-details) page shows which operating system versions can be used with M3 instances.
- The M3 machine series doesn't support standard Persistent Disk (`pd-standard`).
- The ability to add or resize a Persistent Disk for a running M3 instance doesn't work as expected on Windows Server 2016 or Windows Server 2012 R2 operating systems. For more information, see [Generic disk error on Windows Server 2016 and 2012 R2 for M3 VMs](https://docs.cloud.google.com/compute/docs/troubleshooting/known-issues#windows_nvme_disks).

### Maintenance experience for M3 instances

During the [lifecycle of a Compute Engine instance](https://docs.cloud.google.com/compute/docs/instances/instance-lifecycle), the host machine that your instance runs on undergoes multiple *host events*. A host event can include the regular maintenance of Compute Engine infrastructure, or in rare cases, a host error. Compute Engine also applies some non-disruptive lightweight upgrades for the hypervisor and network in the background.

The M3 machine series offers the following features related to host maintenance:

| Machine type | Typical scheduled maintenance event frequency | [Maintenance behavior](https://docs.cloud.google.com/compute/docs/instances/host-maintenance-overview#maintenance_behaviors) | [Advanced notification](https://docs.cloud.google.com/compute/docs/instances/monitor-plan-host-maintenance-event) | [On-demand maintenance](https://docs.cloud.google.com/compute/docs/instances/trigger-host-maintenance-event) | [Simulate maintenance](https://docs.cloud.google.com/compute/docs/instances/simulating-host-maintenance) |
|---|---|---|---|---|---|
| All machine types | Minimum of 30 days | Live migrate | 7 days | Yes | Yes |

The maintenance frequencies shown in the previous table are approximations, not guarantees. Compute Engine might occasionally perform maintenance more frequently.

## M2 machine series

With 6 TiB, 9 TiB, and 12 TiB machine types in the M2 machine series, SAP customers can run their largest SAP HANA databases on Google Cloud.

The M2 series is available with on-demand and spot pricing for an evaluation period only. Long running usage requires purchasing a resource-based commitment. For more information, see the [VM pricing page](https://docs.cloud.google.com/compute/vm-instance-pricing#larger_ultramem). Disk usage and network usage is charged separately from machine type pricing. For details, see [Disk and image pricing](https://cloud.google.com/compute/disks-image-pricing) and [Network pricing](https://cloud.google.com/vpc/network-pricing).

M2 instances support resource-based CUDs, Spot VMs, reservations, and compact placement policies.

### M2 machine types

The following table lists the hardware characteristics of each machine type for the M2 machine series:

| Machine types | vCPUs^1^ | Memory (GB) | Local SSD | Default egress bandwidth (Gbps)^2^ |
|---|---|---|---|---|
| `m2-ultramem-208` | 208 | 5,888 | Not available | Up to 32^3^ |
| `m2-ultramem-416` | 416 | 11,776 | Not available | Up to 32^3^ |
| `m2-megamem-416` | 416 | 5,888 | Not available | Up to 32^3^ |
| `m2-hypermem-416` | 416 | 8,832 | Not available | Up to 32^3^ |

^1^ A vCPU is implemented as a single hardware Hyper-thread on one of the available [CPU platforms](https://docs.cloud.google.com/compute/docs/cpu-platforms).  
^2^ Maximum egress bandwidth cannot exceed the number given. Actual egress bandwidth depends on the destination IP address and other factors. See [Network bandwidth](https://docs.cloud.google.com/compute/docs/network-bandwidth).  
^3^ 32 Gbps for Cascade Lake or later [CPU platforms](https://docs.cloud.google.com/compute/docs/cpu-platforms). 16 Gbps for all other platforms.

### Supported disk types for M2

M2 machine types can use the following block storage options:

- Zonal balanced Persistent Disk (`pd-balanced`)
- Zonal SSD (Performance) Persistent Disk (`pd-ssd`)
- Extreme Persistent Disk (`pd-extreme`)
- Hyperdisk Balanced (`hyperdisk-balanced`)
- Hyperdisk Extreme (`hyperdisk-extreme`)

<br />

If supported by the machine type, you can attach a mixture of Hyperdisk and Persistent Disk volumes to an instance, but the following restrictions apply:

- The combined number of both Hyperdisk and Persistent Disk volumes can't exceed 128 per instance.
- The maximum total disk capacity (in TiB) across all disk types can't exceed:

  - For machine types with less than 32 vCPUs:

    - 257 TiB for all Hyperdisk or all Persistent Disk
    - 257 TiB for a mixture of Hyperdisk and Persistent Disk
  - For machine types with 32 or more vCPUs:

    - 512 TiB for all Hyperdisk
    - 512 TiB for a mixture of Hyperdisk and Persistent Disk
    - 257 TiB for all Persistent Disk

For details about the capacity limits, see [Hyperdisk size and attachment limits](https://docs.cloud.google.com/compute/docs/disks/hyperdisk-perf-limits#limits-instance) and [Persistent Disk maximum capacity](https://docs.cloud.google.com/compute/docs/disks/persistent-disks#capacity_257tb).

<br />

The maximum number of disks that you can attach to M2 instances are described in the following table:

| Machine types | Per VM | Hyperdisk per VM | Hyperdisk Balanced | Hyperdisk Throughput | Hyperdisk Extreme |
|---|---|---|---|---|---|
| `m2-ultramem-208` | 128 | 64 | 32 | 0 | 8 |
| `m2-ultramem-416` | 128 | 64 | 32 | 0 | 8 |
| `m2-megamem-416` | 128 | 64 | 32 | 0 | 8 |
| `m2-hypermem-416` | 128 | 64 | 32 | 0 | 8 |

### M2 Limitations

The M2 machine series is available only as predefined machine types. This series offers from 14 GB to 28 GB memory per vCPU. The following restrictions apply:

- The M2 machine series is available in only [select zones and regions](https://docs.cloud.google.com/compute/docs/regions-zones#available) on specific [CPU processors](https://docs.cloud.google.com/compute/docs/machine-resource#machine_type_comparison).
- You can't use [regional Persistent Disk](https://docs.cloud.google.com/compute/docs/disks/regional-persistent-disk) with the M2 machine series.
- The M2 machine series uses only the SCSI interface for attached disks.
- [Sole tenant nodes](https://docs.cloud.google.com/compute/docs/nodes/sole-tenant-nodes) are available for only the `m2-ultramem-416` shape.
- You can't use Windows Server 2016 OS images with machine types that have more than 255 vCPUs.

### Maintenance experience for M2 instances

During the [lifecycle of a Compute Engine instance](https://docs.cloud.google.com/compute/docs/instances/instance-lifecycle), the host machine that your instance runs on undergoes multiple *host events*. A host event can include the regular maintenance of Compute Engine infrastructure, or in rare cases, a host error. Compute Engine also applies some non-disruptive lightweight upgrades for the hypervisor and network in the background.

The M2 machine series offers the following features related to host maintenance:

| Machine type | Typical scheduled maintenance event frequency | [Maintenance behavior](https://docs.cloud.google.com/compute/docs/instances/host-maintenance-overview#maintenance_behaviors) | [Advanced notification](https://docs.cloud.google.com/compute/docs/instances/monitor-plan-host-maintenance-event) | [On-demand maintenance](https://docs.cloud.google.com/compute/docs/instances/trigger-host-maintenance-event) | [Simulate maintenance](https://docs.cloud.google.com/compute/docs/instances/simulating-host-maintenance) |
|---|---|---|---|---|---|
| All machine types | Minimum of 30 days | Live migrate | 7 days | Yes | Yes |

The maintenance frequencies shown in the previous table are approximations, not guarantees. Compute Engine might occasionally perform maintenance more frequently.

## M1 machine series

The M1 machine series is the older generation memory-optimized machine series that offers 14.9 to 24 GB of memory per vCPU. This series offers the `m1-ultramem` and `m1-megamem` machine types and are only available in specific [regions and zones](https://docs.cloud.google.com/compute/docs/regions-zones#available).
**Note:** The prefix in the following machine names changed from "`n1`" to "`m1`" to more clearly identify the machines as members of the memory-optimized machine family:

- `n1-megamem-96` is now `m1-megamem-96`
- `n1-ultramem-40` is now `m1-ultramem-40`
- `n1-ultramem-80` is now `m1-ultramem-80`
- `n1-ultramem-160` is now `m1-ultramem-160`
The machines themselves did not change and the former names are still supported as aliases for these machines.

For details on pricing, see the [VM pricing page](https://docs.cloud.google.com/compute/vm-instance-pricing#m1_machine_types). Disk usage and network usage is charged separately from machine type pricing. For more information, see [Disk and image pricing](https://cloud.google.com/compute/disks-image-pricing) and [Network pricing](https://cloud.google.com/vpc/network-pricing).

M1 instances support resource-based CUDs, Spot VMs, reservations, and compact placement policies.

### M1 machine types

The following table lists the hardware characteristics of each machine type for the M1 machine series:

| Machine types | vCPUs^1^ | Memory (GB) | Local SSD^2^ | Default egress bandwidth (Gbps)^3^ |
|---|---|---|---|---|
| `m1-ultramem-40` | 40 | 961 | 5 | Up to 32 |
| `m1-ultramem-80` | 80 | 1922 | 8 | Up to 32 |
| `m1-ultramem-160` | 160 | 3844 | Not available | Up to 32 |
| `m1-megamem-96` | 96 | 1433.6 | Not available | Up to 32 |

^1^ A vCPU is implemented as a single hardware thread on one of the available [CPU platforms](https://docs.cloud.google.com/compute/docs/cpu-platforms).  
^2^ Number of 375 GiB Local SSD disks that you can choose to add when creating the instance.  
^3^ Maximum egress bandwidth cannot exceed the number given. Actual egress bandwidth depends on the destination IP address and other factors. See [Network bandwidth](https://docs.cloud.google.com/compute/docs/network-bandwidth).

### Supported disk types for M1

M1 machine types can use the following block storage options:

- Zonal balanced Persistent Disk (`pd-balanced`)
- Zonal SSD (Performance) Persistent Disk (`pd-ssd`)
- Extreme Persistent Disk (`pd-extreme`)
- Hyperdisk Balanced (`hyperdisk-balanced`)
- Hyperdisk Extreme (`hyperdisk-extreme`)
- Local SSD

<br />

If supported by the machine type, you can attach a mixture of Hyperdisk and Persistent Disk volumes to an instance, but the following restrictions apply:

- The combined number of both Hyperdisk and Persistent Disk volumes can't exceed 128 per instance.
- The maximum total disk capacity (in TiB) across all disk types can't exceed:

  - For machine types with less than 32 vCPUs:

    - 257 TiB for all Hyperdisk or all Persistent Disk
    - 257 TiB for a mixture of Hyperdisk and Persistent Disk
  - For machine types with 32 or more vCPUs:

    - 512 TiB for all Hyperdisk
    - 512 TiB for a mixture of Hyperdisk and Persistent Disk
    - 257 TiB for all Persistent Disk

For details about the capacity limits, see [Hyperdisk size and attachment limits](https://docs.cloud.google.com/compute/docs/disks/hyperdisk-perf-limits#limits-instance) and [Persistent Disk maximum capacity](https://docs.cloud.google.com/compute/docs/disks/persistent-disks#capacity_257tb).

<br />

The maximum number of disks that you can attach to M1 instances are described in the following table:

| Machine types | Per VM^1^ | Hyperdisk per VM | Hyperdisk Balanced | Hyperdisk Throughput | Hyperdisk Extreme |
|---|---|---|---|---|---|
| `m1-ultramem-40` | 128 | 64 | 32 | 0 | 0 |
| `m1-ultramem-80` | 128 | 64 | 32 | 0 | 8 |
| `m1-ultramem-160` | 128 | 64 | 32 | 0 | 8 |
| `m1-megamem-96` | 128 | 64 | 32 | 0 | 8 |

### M1 Limitations

The M1 machine series is only available as predefined machine types. This series offers 14 GB to 28 GB of memory per vCPU. The following restrictions apply:

- You can't use [regional Persistent Disk](https://docs.cloud.google.com/compute/docs/disks/regional-persistent-disk) with the M1 series.
- M1 instances are only available in [select zones and regions](https://docs.cloud.google.com/compute/docs/regions-zones#available) on specific [CPU processors](https://docs.cloud.google.com/compute/docs/machine-resource#machine_type_comparison).

### Maintenance experience for M1 instances

During the [lifecycle of a Compute Engine instance](https://docs.cloud.google.com/compute/docs/instances/instance-lifecycle), the host machine that your instance runs on undergoes multiple *host events*. A host event can include the regular maintenance of Compute Engine infrastructure, or in rare cases, a host error. Compute Engine also applies some non-disruptive lightweight upgrades for the hypervisor and network in the background.

The M1 machine series offers the following features related to host maintenance:

| Machine type | Typical scheduled maintenance event frequency | [Maintenance behavior](https://docs.cloud.google.com/compute/docs/instances/host-maintenance-overview#maintenance_behaviors) | [Advanced notification](https://docs.cloud.google.com/compute/docs/instances/monitor-plan-host-maintenance-event) | [On-demand maintenance](https://docs.cloud.google.com/compute/docs/instances/trigger-host-maintenance-event) | [Simulate maintenance](https://docs.cloud.google.com/compute/docs/instances/simulating-host-maintenance) |
|---|---|---|---|---|---|
| All machine types | Minimum of 30 days | Live migrate | 7 days | Yes | Yes |

The maintenance frequencies shown in the previous table are approximations, not guarantees. Compute Engine might occasionally perform maintenance more frequently.

## What's next

- [Creating and starting a virtual machine instance](https://docs.cloud.google.com/compute/docs/instances/create-start-instance)
- Learn about the different [Storage options](https://docs.cloud.google.com/compute/docs/disks) for your instance.
- [Move your workload to a new compute instance](https://docs.cloud.google.com/compute/docs/import/migrate-to-new-vm)
- [Using Google Virtual NIC](https://docs.cloud.google.com/compute/docs/networking/using-gvnic)
- [VM instance pricing](https://cloud.google.com/compute/vm-instance-pricing)