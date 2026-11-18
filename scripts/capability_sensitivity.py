#!/usr/bin/env python3
"""RIR scenario sensitivity only; not a calibrated capability predictor.

Example: python3 scripts/capability_sensitivity.py --weight 155 --reps 5 \
    --rir-low 2 --rir-high 3 --rir-errors 0 1 2
An unbounded report such as '3+' cannot be supplied as a closed RIR interval.
"""
import argparse
import json
import math


def sensitivity(weight, reps, rir_low, rir_high, rir_errors):
    values = [weight, reps, rir_low, rir_high, *rir_errors]
    if not all(math.isfinite(v) for v in values):
        raise ValueError('All inputs must be finite.')
    if weight <= 0 or reps < 1 or int(reps) != reps:
        raise ValueError('Positive weight and positive integer repetitions required.')
    if rir_low < 0 or rir_high < rir_low or any(e < 0 for e in rir_errors):
        raise ValueError('RIR must be a closed ordered nonnegative interval; errors nonnegative.')
    scenarios = []
    for error in rir_errors:
        low, high = max(0, rir_low - error), rir_high + error
        supported = reps + high <= 10
        scenarios.append({
            'assumed_rir_error_each_direction': error,
            'effective_rir_interval': [low, high],
            'supported_by_project_repetition_limit': supported,
            'e1rm_lb': [round(weight * 36 / (37 - reps - low), 1),
                         round(weight * 36 / (37 - reps - high), 1)] if supported else None,
            'note': 'Scenario only; formula error not quantified.' if supported else
                    'Whole scenario withheld: effective repetitions exceed project limit 10.'
        })
    return {
        'formula': 'Brzycki: weight_lb * 36 / (37 - reps - RIR)',
        'input': {'weight_lb': weight, 'reps': reps, 'reported_rir_interval': [rir_low, rir_high]},
        'scenarios': scenarios,
        'limitations': [
            'RIR error sizes are user-selected assumptions, not measured personal errors.',
            'Ranges are not confidence intervals or bounds on true 1RM.',
            'Exercise technique, readiness and individual formula error are not modelled.',
            'Multiple sets from one session are not independent replications.'
        ]
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--weight', type=float, required=True, help='Load in lb')
    parser.add_argument('--reps', type=int, required=True)
    parser.add_argument('--rir-low', type=float, required=True)
    parser.add_argument('--rir-high', type=float, required=True,
                        help='Explicit finite upper bound; do not substitute for a 3+ report')
    parser.add_argument('--rir-errors', type=float, nargs='+', required=True)
    args = parser.parse_args()
    try:
        result = sensitivity(args.weight, args.reps, args.rir_low, args.rir_high, args.rir_errors)
    except ValueError as exc:
        parser.error(str(exc))
    print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == '__main__':
    main()
