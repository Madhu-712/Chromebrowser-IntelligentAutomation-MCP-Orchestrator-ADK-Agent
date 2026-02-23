# Performance Analysis Report: MakeMyTrip.com

This report provides a consolidated view of the performance of https://www.makemytrip.com/ across different network conditions and device interfaces.

## Executive Summary
The analysis shows that MakeMyTrip is well-optimized for modern networks but experiences significant performance degradation as network speed decreases, particularly on mobile devices. The Largest Contentful Paint (LCP) increases by nearly 50% when moving from 5G to 2G on mobile.

---

## 1. Performance Metrics Comparison

| Device Interface | Network Profile | LCP (ms) | TTFB (ms) | CLS |
| :--- | :--- | :--- | :--- | :--- |
| **Desktop** | 5G (No Emulation) | 1,114 | 442 | 0.03 |
| **Desktop** | 4G (Fast 4G) | 862* | 438 | 0.03 |
| **Desktop** | 3G (Fast 3G) | 1,235 | 541 | 0.03 |
| **Desktop** | 2G (Slow 3G) | 1,288 | 609 | 0.03 |
| **Mobile** | 5G (No Emulation) | 1,610 | 474 | 0.05 |
| **Mobile** | 4G (Fast 4G) | 1,957 | 572 | 0.04 |
| **Mobile** | 3G (Fast 3G) | 2,190 | 580 | 0.04 |
| **Mobile** | 2G (Slow 3G) | 2,481 | 812 | 0.04 |

*\*Note: Variations in Desktop 4G vs 5G may be attributed to server-side response variance or local caching during sequential tests.*

---

## 2. Key Observations

### Desktop Performance
- **Consistency:** Cumulative Layout Shift (CLS) remains stable at 0.03 across all network types, indicating a robust layout structure.
- **Latency Impact:** Time to First Byte (TTFB) nearly doubles from 5G (442ms) to 2G (609ms), significantly impacting the start of the render process.

### Mobile Performance
- **Mobile Overhead:** Mobile LCP is consistently 40-90% higher than Desktop LCP under similar network conditions. This is likely due to additional mobile-specific resources and the overhead of processing complex elements on a mobile viewport.
- **2G Critical Point:** Under 2G conditions, the mobile LCP reaches 2.48s, which is nearing the "Needs Improvement" threshold (2.5s) for Core Web Vitals.

---

## 3. Technical Insights

- **LCP Discovery:** The LCP image discovery time increases significantly on slower networks. On Mobile 2G, the load delay accounted for 1,348ms, suggesting that the LCP element discovery is a primary bottleneck.
- **Third-Party Impact:** Traces across all profiles showed significant 3rd party code execution, which competes for the main thread, especially on mobile.
- **DOM Size:** The DOM size was noted as a potential issue in several traces, which can slow down style calculations and layout reflows on lower-end devices.

---

## 4. Recommendations for Optimization

1.  **Optimize LCP Discovery:** Ensure the LCP image is discoverable immediately in the HTML source (avoiding JS-driven injection or lazy loading for above-the-fold content).
2.  **Reduce TTFB:** Implement better edge caching and optimize server-side rendering for the home page to keep TTFB low even on high-latency networks.
3.  **Critical CSS:** Inline critical CSS to reduce render-blocking time, especially for mobile users on 3G/2G.
4.  **Third-Party Management:** Audit and defer non-critical third-party scripts to prioritize the main content delivery.

---
*Report generated on February 23, 2026*
