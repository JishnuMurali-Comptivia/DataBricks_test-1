#Starter Data


    # ================================================================
    # STARTER DATA - paste at top of file, do not modify
    # ================================================================
    
    # -- LISTS --
    claims = [
        {"claim_id":"CLM001","policy_id":"POL001","amount":4500.00, "status":"OPEN",   "type":"AUTO","days_open":12},
        {"claim_id":"CLM002","policy_id":"POL002","amount":12000.00,"status":"CLOSED", "type":"HOME","days_open":45},
        {"claim_id":"CLM003","policy_id":"POL001","amount":750.00,  "status":"OPEN",   "type":"AUTO","days_open":3},
        {"claim_id":"CLM004","policy_id":"POL003","amount":28000.00,"status":"PENDING","type":"LIFE","days_open":90},
        {"claim_id":"CLM005","policy_id":"POL002","amount":1200.00, "status":"OPEN",   "type":"HOME","days_open":7},
        {"claim_id":"CLM006","policy_id":"POL004","amount":-50.00,  "status":"OPEN",   "type":"AUTO","days_open":1},
        {"claim_id":"CLM007","policy_id":"POL003","amount":5500.00, "status":"CLOSED", "type":"LIFE","days_open":60},
        {"claim_id":"CLM008","policy_id":"POL005","amount":9200.00, "status":"PENDING","type":"AUTO","days_open":22},
    ]
    
    premiums = [1200, 850, 2400, 500, 1800, 950, 3200, 750, 1100, 2900]
    
    # -- TUPLES -- Index: 0=policy_id 1=holder_name 2=product 3=eff_date 4=status 5=premium
    policy_records = [
        ("POL001","Alice Smith",  "AUTO","2026-01-01","ACTIVE", 1200.00),
        ("POL002","Bob Johnson",  "HOME","2025-06-15","ACTIVE",  850.00),
        ("POL003","Carol White",  "LIFE","2024-03-20","ACTIVE", 2400.00),
        ("POL004","David Brown",  "AUTO","2023-11-01","EXPIRED", 500.00),
        ("POL005","Eve Martinez", "AUTO","2026-02-28","ACTIVE", 1800.00),
    ]
    
    # -- SETS --
    source_claim_ids    = {"CLM001","CLM002","CLM003","CLM004","CLM005","CLM006","CLM008","CLM009"}
    processed_claim_ids = {"CLM001","CLM002","CLM003","CLM007","CLM010"}
    valid_statuses = {"OPEN","CLOSED","PENDING","DENIED","WITHDRAWN"}
    valid_types    = {"AUTO","HOME","LIFE","HEALTH","TRAVEL"}
    
    # -- DICTIONARIES --
    status_map = {"OPN":"OPEN","CLO":"CLOSED","CLD":"CLOSED","PND":"PENDING","DNI":"DENIED","WDN":"WITHDRAWN"}
    
    adjuster_workload = {
        "ADJ001":["CLM001","CLM003","CLM008"],
        "ADJ002":["CLM002","CLM005"],
        "ADJ003":["CLM004","CLM007"],
        "ADJ004":[],
    }
    
    policy_premiums = {"POL001":1200.00,"POL002":850.00,"POL003":2400.00,"POL004":500.00,"POL005":1800.00}

# ======================================================================================================================================== #

# ================================================================ 
#   SECTION 1 (Lists)
# ================================================================

#Q1.1 [2pts] - append() - Add a new claim record
#Create a new claim dictionary with these values and append() it to claims. Print the total length after appending.

Values: claim_id="CLM009", policy_id="POL005", amount=3300.00, status="OPEN", type="HOME", days_open=5

#ANS:

new_claim = {
    "claim_id": "CLM009",
    "policy_id": "POL005",
    "amount": 3300.00,
    "status": "OPEN",
    "type": "HOME",
    "days_open": 5
}

claims.append(new_claim)

print("Total number of claims:", len(claims))


#Q1.2 [2pts] - insert() - Add a priority claim at the front
#Create the priority claim below and use insert() to place it at index 0. Print claims[0]["claim_id"] to confirm.

Values: claim_id="CLM_PRIORITY", policy_id="POL003", amount=28000.00, status="PENDING", type="LIFE", days_open=91

#ANS:

priority_claim = {
    "claim_id": "CLM_PRIORITY",
    "policy_id": "POL003",
    "amount": 28000.00,
    "status": "PENDING",
    "type": "LIFE",
    "days_open": 91
}


claims.insert(0, priority_claim)
print(claims[0]["claim_id"])


#Q1.3 [2pts] - sort() - In-place sort by amount ascending
#Sort claims IN-PLACE by the "amount" field ascending. Print claim_id and amount of the first 3 claims to verify.
    # Sort in-place ascending by amount
    
#ANS:
claims.sort(key=lambda x: x["amount"])

for claim in claims[:3]:
    print(claim["claim_id"], claim["amount"])
    
 #EXPLAIN (as a comment): What is the difference between sort() and sorted()? When would you use each?   
#ANS:
# -->sort()

# sort() is a list method that sorts the original list in-place, meaning it changes the actual list and does not return a new list.
# Use sort() when you want to permanently change the order of the existing list and save memory.

#-->sorted()

# sorted() is a built-in function that returns a new sorted list without modifying the original list.
# Use sorted() when you want to keep the original list unchanged and create a new sorted version of it.

#Q1.4 [3pts] - sorted() - New list sorted by days_open descending
#Create aged_claims - a NEW list sorted by "days_open" descending using sorted(). The original claims list must stay unchanged. Print claim_id + days_open for each item.
    # sorted() - descending by days_open - original unchanged

#ANS:

aged_claims = sorted(claims, key=lambda x: x["days_open"], reverse=True)

for claim in aged_claims:
    print(claim["claim_id"], claim["days_open"])    



#Q1.5 [2pts] - pop() - Remove and capture last claim
#Use pop() to remove the last claim. Store it in removed_claim. Print the removed claim_id and the new list length.
    # pop() last item, store and print

#ANS:
removed_claim = claims.pop()

print("Removed claim_id =", removed_claim["claim_id"])
print("New length of claims list =", len(claims))



#Q1.6 [3pts] - extend() + index() - Merge batch and find record
#Extend claims with batch_2 below, then use index() to find the position of "CLM_BATCH2_001" in the merged list.
batch_2 = [
        {"claim_id":"CLM_BATCH2_001","policy_id":"POL006","amount":6700.00,"status":"OPEN","type":"AUTO","days_open":9},
        {"claim_id":"CLM_BATCH2_002","policy_id":"POL007","amount":320.00,"status":"CLOSED","type":"HOME","days_open":30},
    ]
    
    # Extend claims with batch_2, then find index of CLM_BATCH2_001

#ANS:
claims.extend(batch_2)

position = None
for claim in claims:
    if claim["claim_id"] == "CLM_BATCH2_001":
        position = claims.index(claim)
        break

print("Index of CLM_BATCH2_001 =", position)
    


#Q1.7 [3pts] - Slicing - Extract sub-lists (no loops allowed)
#Using only slicing (no for-loops), extract and print these four sub-lists from claims:
#First 3 claims (batch 1 processing)
#Last 2 claims (most recently added)
#Every other claim starting at index 0 (parallel processing)
#Entire list reversed (audit log order)
    # a) First 3
    
    # b) Last 2
    
    # c) Every other (0, 2, 4...)
    
    # d) Reversed

#ANS:
# a) First 3
print(claims[:3])

# b) Last 2
print(claims[-2:])

# c) Every other (0, 2, 4...)
print(claims[0::2])

# d) Reversed
print(claims[::-1])

#Q1.8 [3pts] - count() + remove() - Audit and clean invalid claims
#Count how many claims have amount <= 0. Then remove CLM006 using remove(). Print: count found, length before removal, length after removal.
    # Count claims with amount <= 0
    
    # Remove CLM006, print length before and after

#ANS:
#count()
invalid_count = 0
for claim in claims:
    if claim["amount"] <= 0:
        invalid_count += 1

print("Invalid claims count =", invalid_count)

#remove()
length_before = len(claims)

for claim in claims:
    if claim["claim_id"] == "CLM006":
        claims.remove(claim)
        break

length_after = len(claims)

print("Length before removal =", length_before)
print("Length after removal =", length_after)
    
    
# ================================================================
#   SECTION 2 (Tuples)
# ================================================================

#Q2.1 [4pts] - namedtuple - Create a typed PolicyRecord
#Using collections.namedtuple, define a PolicyRecord with all 6 fields. Convert all 5 rows in policy_records to PolicyRecord objects stored in typed_policies. Print typed_policies[0].policy_id and typed_policies[0].premium using field names (not indexes).
#    from collections import namedtuple
    
    # Define PolicyRecord namedtuple - 6 fields
    # Convert all 5 tuples using PolicyRecord(*row)
    # YOUR CODE HERE:
    
    
    # Print .policy_id and .premium of first record
    
#HINT: namedtuple("TypeName", ["field1","field2",...]) creates the class. Use PolicyRecord(*row) to convert.

#ANS:
PolicyRecord = namedtuple("PolicyRecord", ["policy_id", "holder_name", "product", "eff_date", "status", "premium"])

typed_policies = []
for row in policy_records:
    typed_policies.append(PolicyRecord(*row))

print(typed_policies[0].policy_id)
print(typed_policies[0].premium)

#Q2.2 [4pts] - Tuple unpacking - Format active policy lines
#Loop over policy_records using tuple unpacking in the for statement. Print one formatted line per ACTIVE policy:
#    [POL001] Alice Smith | AUTO | Premium: $1,200.00 | Valid from: 2026-01-01
    # for policy_id, holder_name, product, eff_date, status, premium in policy_records:
    #     if status == 'ACTIVE': print formatted line
    
#ANS:

for policy_id, holder_name, product, eff_date, status, premium in policy_records:
    if status == "ACTIVE":
        print(f"[{policy_id}] {holder_name} | {product} | Premium: ${premium:,.2f} | Valid from: {eff_date}")


#Q2.3 [4pts] - Tuple as dict key - Coverage cache lookup
#Build coverage_cache - a dict where each key is a (policy_id, effective_date) tuple and the value is the premium. Look up and print the premium for ("POL003","2024-03-20").
    # coverage_cache: {(policy_id, effective_date): premium}
   

#ANS:

coverage_cache = {}
for policy_id, holder_name, product, eff_date, status, premium in policy_records:
    coverage_cache[(policy_id, eff_date)] = premium

print(coverage_cache[("POL003", "2024-03-20")])


#Q2.4 [3pts] - Immutability - Handle and work around it
#Part A: Try changing policy_records[3][4] (status) to "RENEWED". Wrap in try/except and print the exception type and message.
#Part B: Create updated_record - a NEW tuple identical to policy_records[3] but with status changed to "RENEWED". Print it.
    # Part A: attempt mutation - catch TypeError and print it
    # YOUR CODE HERE:
    
    
    # Part B: build new tuple with status changed (slicing trick)
    # Hint: new_t = old_t[:4] + ("RENEWED",) + old_t[5:]

#ANS:

try:
    policy_records[3][4] = "RENEWED"
except TypeError as e:
    print(type(e).__name__, "-", e)


old_t = policy_records[3]
updated_record = old_t[:4] + ("RENEWED",) + old_t[5:]

print(updated_record)
    
# ================================================================
#   SECTION 3 (Sets)
# ================================================================

#Q3.1 [4pts] - Difference & Intersection - Reconciliation report
#Part A (Difference): Find claim IDs in source_claim_ids but NOT in processed_claim_ids. Store in unprocessed. Print the set and its length.
#Part B (Intersection): Find IDs that exist in BOTH sets. Store in reconciled. Print reconciliation rate as a percentage.
    # Part A - difference (use - operator)
    # Part B - intersection (use & operator) + reconciliation %

#ANS:
# Part A - difference (use - operator)
unprocessed = source_claim_ids - processed_claim_ids
print("Unprocessed claim IDs:", unprocessed)
print("Count of unprocessed:", len(unprocessed))


# Part B - intersection (use & operator) + reconciliation %
reconciled = source_claim_ids & processed_claim_ids

print("Reconciled claim IDs:", reconciled)

reconciliation_rate = (len(reconciled) / len(source_claim_ids)) * 100
print("Reconciliation rate:", f"{reconciliation_rate:.2f}%")


#Q3.2 [4pts] - Union & Symmetric Difference - Audit universe
#Part A (Union): Combine both sets into all_claim_ids. Print sorted list of all unique IDs.
#Part B (Symmetric Difference): Find IDs that appear in ONE set but not both. Store in discrepancies. Print the result and add a comment explaining what each group means.
    # Part A - union (use | operator)
    # Part B - symmetric difference (use ^ operator)

#ANS:
# Part A - union (use | operator)
all_claim_ids = source_claim_ids | processed_claim_ids

print("All unique claim IDs:", sorted(all_claim_ids))


# Part B - symmetric difference (use ^ operator)
discrepancies = source_claim_ids ^ processed_claim_ids

print("Discrepancies:", discrepancies)

#Q3.3 [4pts] - issubset() / issuperset() - Validate pipeline output
#After a pipeline run you receive output_ids. Verify: (1) were all source IDs processed? (2) did the pipeline produce any unexpected IDs? Print PASS/FAIL for each check.
#    output_ids = {"CLM001","CLM002","CLM003","CLM004","CLM005","CLM006","CLM008"}
    
    # Check 1: source_claim_ids.issubset(output_ids)? - all source IDs processed?
    # Check 2: output_ids.issubset(source_claim_ids)? - no unexpected IDs?

#ANS:
# Check 1: source_claim_ids.issubset(output_ids)? - all source IDs processed?
if source_claim_ids.issubset(output_ids):
    print("Check 1: PASS - All source IDs were processed")
else:
    print("Check 1: FAIL - Some source IDs were not processed")


# Check 2: output_ids.issubset(source_claim_ids)? - no unexpected IDs?
if output_ids.issubset(source_claim_ids):
    print("Check 2: PASS - No unexpected IDs produced")
else:
    print("Check 2: FAIL - Pipeline produced unexpected IDs")
    
#Q3.4 [3pts] - add() / discard() / update() - Live set updates
#Simulate real-time updates to processed_claim_ids:
#add(): CLM006 was just processed - add it
#discard(): safely remove "CLM_GHOST" (non-existent) - must not raise an error - print length before and after
#update(): new batch {"CLM009","CLM010"} arrived - update the set and print final set
    
#ANS:

# add()
processed_claim_ids.add("CLM006")

# discard()
length_before = len(processed_claim_ids)

processed_claim_ids.discard("CLM_GHOST")  # will not raise error if not present

length_after = len(processed_claim_ids)

print("Length before discard =", length_before)
print("Length after discard =", length_after)

# update()
processed_claim_ids.update({"CLM009", "CLM010"})

print("Final processed_claim_ids:", processed_claim_ids)
    
# ================================================================
#   SECTION 4 (Dictionaries)
# ================================================================

#Q4.1 [3pts] - get() - Standardize raw status codes
U#sing status_map.get(), standardize each code in raw_statuses. If a code is not in the map, keep the original value as default. Print "OPN -> OPEN" format for each.
#    raw_statuses = ['OPN','CLD','PND','OPEN','DNI','ACTIVE','WDN','CLO']
    
    # For each raw code: status_map.get(code, code)
    # Print: "OPN -> OPEN", "ACTIVE -> ACTIVE" etc.

#ANS:

for code in raw_statuses:
    standardized = status_map.get(code, code)
    print(f"{code} -> {standardized}")
    

#Q4.2 [4pts] - update() + items() + values() - Adjuster analysis
#Part A (update): Add new_assignments to adjuster_workload using update(). Note: existing keys are overwritten.
#Part B (items): Print each adjuster and their claim count using .items().
#Part C (values): Sum all values in policy_premiums using .values() and print the total.
    new_assignments = {
        "ADJ005":["CLM_BATCH2_001","CLM_BATCH2_002"],
        "ADJ001":["CLM001","CLM003","CLM008","CLM009"],  # overwrites existing ADJ001
    }
    
    # Part A - update adjuster_workload
    # Part B - print each adjuster: count using .items()
    # Part C - sum all policy_premiums using .values()

#ANS:

# Part A - update adjuster_workload
adjuster_workload.update(new_assignments)

# Part B - print each adjuster and their claim count
for adjuster, claims_list in adjuster_workload.items():
    print(adjuster, "has", len(claims_list), "claims")

# Part C - sum all policy_premiums using .values()
total_premiums = sum(policy_premiums.values())
print("Total policy premiums =", total_premiums)
    
    
#Q4.3 [3pts] - pop() - Remove inactive adjuster
#ADJ004 has no claims. Use pop() to remove them. Store result in removed_adj. Print the removed data, then confirm "ADJ004" not in adjuster_workload.
    # pop ADJ004, print removed data, confirm it is gone
    
#ANS:

# pop ADJ004, print removed data, confirm it is gone

removed_adj = adjuster_workload.pop("ADJ004")

print("Removed data:", removed_adj)

print("ADJ004 in adjuster_workload:", "ADJ004" in adjuster_workload)


#Q4.4 [4pts] - setdefault() - Group claims by type
#Using setdefault() and a plain for-loop (no defaultdict, no comprehension), build claims_by_type - a dict where each key is a claim type and each value is a list of claim_ids. Print each type and its list.
claims_by_type = {}
    # for claim in claims:
    #     claims_by_type.setdefault(claim["type"], []).append(claim["claim_id"])
    
#ANS:


for claim in claims:
    claims_by_type.setdefault(claim["type"], []).append(claim["claim_id"])

# Print result
for claim_type, claim_ids in claims_by_type.items():
    print(claim_type, ":", claim_ids)
    


#Q4.5 [3pts] - Counter + defaultdict - Frequency analysis
#Part A: Use Counter to count claims per type. Print sorted by most common.
#Part B: Use defaultdict(list) to group claim_ids by "status". Print each status and claim count.
    from collections import Counter, defaultdict
    
    # Part A - Counter by claim type
    
    # Part B - defaultdict(list) by status

#ANS:

# Part A - Counter by claim type
type_counter = Counter()

for claim in claims:
    type_counter[claim["type"]] += 1

print("Claims per type (most common first):")
for claim_type, count in type_counter.most_common():
    print(claim_type, count)


# Part B - defaultdict(list) by status
status_groups = defaultdict(list)

for claim in claims:
    status_groups[claim["status"]].append(claim["claim_id"])

print("\nClaims grouped by status:")
for status, ids in status_groups.items():
    print(status, "->", len(ids), "claims:", ids)
    
    
#Q4.6 [3pts] - Nested dict - Policy-to-claims index
#Build policy_claims_index - a nested dict where each key is policy_id and value is {"count": N, "total_amount": X.XX}. Print each line as: POL001: 2 claims, $5,250.00 total
    # Expected: {"POL001":{"count":2,"total_amount":5250.0}, "POL002":{...}, ...}
    

#ANS:

policy_claims_index = {}

for claim in claims:
    policy_id = claim["policy_id"]
    amount = claim["amount"]

    if policy_id not in policy_claims_index:
        policy_claims_index[policy_id] = {"count": 0, "total_amount": 0.0}

    policy_claims_index[policy_id]["count"] += 1
    policy_claims_index[policy_id]["total_amount"] += amount

for policy_id, data in policy_claims_index.items():
    print(f"{policy_id}: {data['count']} claims, ${data['total_amount']:,.2f} total")
    

# ================================================================
#   SECTION 5 (Comprehensions)  
# ================================================================

#Q5.1 [4pts] - List comprehension - Filter high-value open claims
#Create high_value_open - claims where status == "OPEN" AND amount >= 3000. One-line comprehension. Print claim_id and amount for each.
    # One-line list comprehension - two conditions
    
#ANS:

# One-line list comprehension - two conditions
high_value_open = [c for c in claims if c["status"] == "OPEN" and c["amount"] >= 3000]

for c in high_value_open:
    print(c["claim_id"], c["amount"])

total_high_value_open = sum(c["amount"] for c in claims if c["status"] == "OPEN" and c["amount"] >= 3000)
print("Total amount:", total_high_value_open)


#Q5.2 [4pts] - Dict comprehension - claim_id to amount lookup
#Build amount_lookup - a dict of {claim_id: amount} using one dict comprehension. Look up and print the amount for "CLM004".
    # Dict comprehension - claim_id: amount
   

#ANS:

# Dict comprehension - claim_id: amount
amount_lookup = {c["claim_id"]: c["amount"] for c in claims}


#Q5.3 [4pts] - Set comprehension - Unique policy IDs with open claims
#Build open_policy_ids - a set of all policy_id values where status == "OPEN". Print the set. Then check if "POL003" has any open claims.
    # Set comprehension
    # YOUR CODE HERE:
    
    
    # Check if "POL003" is in open_policy_ids - print True/False

#ANS:

# Set comprehension
open_policy_ids = {c["policy_id"] for c in claims if c["status"] == "OPEN"}

print(open_policy_ids)

print("POL003" in open_policy_ids)


#Q5.4 [3pts] - Transform comprehension - Standardize all statuses
#Create standardized_claims - a new list where every "status" is mapped through status_map (keep original if not found). Use dict unpacking {**c, ...} inside the comprehension. Print status before/after for first 3 claims.
    # Pattern: [{**c, "status": status_map.get(c["status"], c["status"])} for c in claims]
    
    # YOUR CODE HERE:
    
    
    # Print before/after for claims[0], [1], [2]

#ANS:

# Create standardized_claims using comprehension and dict unpacking
standardized_claims = [{**c, "status": status_map.get(c["status"], c["status"])} for c in claims]

# Print before/after for first 3 claims
for i in range(3):
    print(claims[i]["status"], "->", standardized_claims[i]["status"])

# ================================================================
#   SECTION 6 (Integrated Challenge)
# ================================================================

##Q6 [15pts] - Write generate_claims_report() and call it on the starter claims list
    def generate_claims_report(claims):
        """
        Produce a summary report from a list of claim dicts.
        Must use: list method, tuple, set, dict method, comprehension.
        """
        report = {}
    
        # 1. total_claims
    
        # 2. total_exposure
    
        # 3. open_exposure  <-- use a comprehension
    
        # 4. by_status
    
        # 5. by_type
    
        # 6. top_3_claims  <-- use sorted()
    
        # 7. invalid_claims  <-- list comprehension
    
        # 8. unique_policies  <-- set comprehension
    
        # 9. avg_days_open  <-- round to 2dp
    
        # 10. status_breakdown  <-- MUST be a tuple
    
        return report
    
    
    # -- Run it --
    report = generate_claims_report(claims)
    for key, value in report.items():
        print(f"{key:<20}: {value}")

###Expected output:
    total_claims        : 8
    total_exposure      : 61100.0
    open_exposure       : 15450.0
    by_status           : {'OPEN': 4, 'CLOSED': 2, 'PENDING': 2}
    by_type             : {'AUTO': 14450.0, 'HOME': 13200.0, 'LIFE': 33500.0}
    top_3_claims        : [CLM004 28000.0, CLM008 9200.0, CLM007 5500.0]
    invalid_claims      : ['CLM006']
    unique_policies     : {'POL001','POL002','POL003','POL004','POL005'}
    avg_days_open       : 30.0
    status_breakdown    : (4, 2, 2)

#ANS:

def generate_claims_report(claims):
    
    report = {}

    # 1. total_claims
    report["total_claims"] = len(claims)

    # 2. total_exposure
    report["total_exposure"] = sum(c["amount"] for c in claims)

    # 3. open_exposure  <-- use a comprehension
    report["open_exposure"] = sum(c["amount"] for c in claims if c["status"] == "OPEN")

    # 4. by_status
    by_status = {}
    for c in claims:
        by_status[c["status"]] = by_status.get(c["status"], 0) + 1
    report["by_status"] = by_status

    # 5. by_type
    by_type = {}
    for c in claims:
        by_type[c["type"]] = by_type.get(c["type"], 0) + c["amount"]
    report["by_type"] = by_type

    # 6. top_3_claims  <-- use sorted()
    top3 = sorted(claims, key=lambda c: c["amount"], reverse=True)[:3]
    top3_list = []
    for c in top3:
        top3_list.append(f"{c['claim_id']} {c['amount']}")   # list method append()
    report["top_3_claims"] = top3_list

    # 7. invalid_claims  <-- list comprehension
    report["invalid_claims"] = [c["claim_id"] for c in claims if c["amount"] <= 0]

    # 8. unique_policies  <-- set comprehension
    report["unique_policies"] = {c["policy_id"] for c in claims}

    # 9. avg_days_open  <-- round to 2dp
    report["avg_days_open"] = round(sum(c["days_open"] for c in claims) / len(claims), 2)

    # 10. status_breakdown  <-- MUST be a tuple
    open_count = by_status.get("OPEN", 0)
    closed_count = by_status.get("CLOSED", 0)
    pending_count = by_status.get("PENDING", 0)
    report["status_breakdown"] = (open_count, closed_count, pending_count)

    return report


# -- Run it --
report = generate_claims_report(claims)
for key, value in report.items():
    print(f"{key:<20}: {value}")


