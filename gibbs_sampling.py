import random

# Variable & domain
variables = ["A", "B", "C", "D", "E", "F"]
domain = {
    "A": ["a0", "a1"],
    "B": ["b0", "b1"],
    "C": ["c0", "c1"],
    "D": ["d0", "d1"],
    "E": ["e0", "e1"],
    "F": ["f0", "f1"]
}

# Factors
factors = {
    "AB": {
        ("a0", "b0"): 50,
        ("a0", "b1"): 25,
        ("a1", "b0"): 50,
        ("a1", "b1"): 10
    },
    "BC": {
        ("b0", "c0"): 50,
        ("b0", "c1"): 10,
        ("b1", "c0"): 5,
        ("b1", "c1"): 50
    },
    "CD": {
        ("c0", "d0"): 1,
        ("c0", "d1"): 50,
        ("c1", "d0"): 35,
        ("c1", "d1"): 1
    },
    "DE": {
        ("d0", "e0"): 1,
        ("d0", "e1"): 1,
        ("d1", "e0"): 25,
        ("d1", "e1"): 50
    },
    "EF": {
        ("e0", "f0"): 20,
        ("e0", "f1"): 10,
        ("e1", "f0"): 50,
        ("e1", "f1"): 40
    },
    "AF": {
        ("a0", "f0"): 1,
        ("a0", "f1"): 10,
        ("a1", "f0"): 100,
        ("a1", "f1"): 5
    }
}

# Functions
def get_factor(sample, variable):
    related_factors = {}
    for factor_key, factor_data in factors.items():
        if variable in factor_key:
            related_factors[factor_key] = factor_data

    calculated_factor = {val: 1 for val in domain[variable]}

    for factor_key, factor_data in related_factors.items():
        other_variable = factor_key.replace(variable, "")
        other_variable_val_in_sample = sample[other_variable]

        for (val_0, val_1), val in factor_data.items():
            if val_0 == other_variable_val_in_sample or val_1 == other_variable_val_in_sample:
                if val_0 in domain[variable]:
                    matched = val_0
                else:
                    matched = val_1
                if matched in calculated_factor:
                    calculated_factor[matched] *= val

    return calculated_factor

def cal_probability(sample, variable):
    probs = []
    factor = get_factor(sample, variable)
    total = sum(factor.values())

    for val in domain[variable]:
        prob = factor[val] / total
        probs.append(prob)

    return probs

def generate_sample(sample, variable):
    new_sample = sample.copy()
    probs = cal_probability(sample, variable)
    random_num = random.random()
    # print(f"probabilities: {probs}, random_num: {random_num}")

    if probs[0] > random_num:
        new_sample[variable] = domain[variable][0]
    else:
        new_sample[variable] = domain[variable][1]

    print(new_sample.values())
    return new_sample

def gibbs_sampling(iteration):
    curr_sample = {"A": "a0", "B": "b1", "C": "c0", "D": "d0", "E": "e0", "F": "f0"}
    resample_order = ["A", "D", "E", "F"]
    variable_index = 0
    e0_count, e1_count = 0, 0

    for _ in range(iteration):
        variable = resample_order[variable_index]
        curr_sample = generate_sample(curr_sample, variable)
        if curr_sample["E"] == "e0":
            e0_count += 1
        else:
            e1_count += 1
        variable_index = (variable_index + 1) % len(resample_order)

    # Compute the probability P(E|b1, c0)
    print("")
    print(f"e0_count: {e0_count}, e1_count: {e1_count}, total: {e0_count + e1_count}")
    print(f"P(E|b1, c0) = <{e0_count / (e0_count + e1_count)}, {e1_count / (e0_count + e1_count)}>")

if __name__ == "__main__":
    gibbs_sampling(100000)
