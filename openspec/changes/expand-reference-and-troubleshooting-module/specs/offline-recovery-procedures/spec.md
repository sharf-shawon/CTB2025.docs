## ADDED Requirements

### Requirement: Service Worker & Cache Inspection Guide

The offline mode documentation SHALL specify DevTools verification steps for auditing active service worker states and IndexedDB content.

#### Scenario: Operator debugs sync issues

- **WHEN** a local transaction fails to synchronize after internet reconnection
- **THEN** the documentation MUST outline steps to inspect the Service Worker console and IndexedDB key stores in the browser.

### Requirement: Sync Conflict Resolution Procedure

The offline mode documentation SHALL provide clear manual reconciliation steps for resolving conflicting data states (e.g. duplicate voucher or invoice entries).

#### Scenario: Operator encounters duplicate sync entries

- **WHEN** a network reconnection causes duplicate transaction sync attempts
- **THEN** the documentation MUST explain how to identify the valid entry and recover from duplicate keys.
