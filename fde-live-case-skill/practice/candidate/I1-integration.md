# I1 · Enterprise ticketing with uncertain results

**Time:** 60 minutes. **Your role:** FDE integrating a third-party ITSM API. No credentials or network access to the provider; model the boundary with a local fake and reproducible tests. No scope changes or production writes are authorized.

The flow creates a ticket when an operator confirms an incident. `POST /tickets` accepts `operation_id` and `Idempotency-Key`. In sandbox, POST may time out **after** the server creates the ticket. `GET /operations/{operation_id}` returns `applied`, `not_found`, or error. Client documentation does not guarantee the production service principal has sandbox-equivalent permissions.

**Agreed fake contract for this exercise, not a real provider guarantee:**

- `operation_id` and `Idempotency-Key` identify the same intent within a tenant and ticket-creation action. They remain stable throughout the round, including client restarts. The fake retains its record throughout the round; no guarantee is declared beyond that horizon.
- Repeated or concurrent requests with the same intent and payload produce at most one ticket and return its recorded result. Reusing a key with another payload is rejected without another effect. Internal mechanism is the candidate's technical decision.
- GET=`applied` confirms creation and returns ticket ID. GET=`not_found` is, **in this fake**, authoritative absence: the previous attempt ended without effect and no pending work can apply it later. Error, timeout, or uninterpretable response supplies no such guarantee. Real permissions remain unconfirmed.

Design and implement the minimum flow avoiding duplicate tickets when results are uncertain. Show happy path, timeout after application, and priority failure. Separate local proof from pending IT/provider validation. If a restriction changes, adjust strategy and handoff.
