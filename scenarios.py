"""Specify the simulation design in one place."""


def make_scenarios():
    """Return {scenario_id: settings} for experiments A and B.

    IDs are unique, stable, filename-safe strings. Each settings dictionary
    has exactly experiment ('A'/'B'), n (int), p (int), rho (float), and
    error_distribution ('normal'/'laplace'). Assume 0 < p < n, 0 <= rho < 1.
    The study supplies all generation, fitting, evaluation, and replication.

    Keep n=200. For A, use rho=0 and both error laws over the SAME chosen
    p/n values. For B, use normal errors and p=100 and choose rho values.
    Choose the values yourselves; the handout grid is only an example.
    """
    # BEGIN TASK GRID
    raise NotImplementedError('Choose and construct your scenario dictionary.')
    # END TASK GRID
    experiments = {
    "compare_est_normal_err_p_1_n": {
        "experiment": "A",
        "n": 200,
        "p": 1,
        "rho": 0,
        "error_distribution": "normal",
    },
    "compare_est_normal_err_p_1_l": {
        "experiment": "A",
        "n": 200,
        "p": 1,
        "rho": 0,
        "error_distribution": "laplace",
    },
    "compare_est_normal_err_p_20_n": {
        "experiment": "A",
        "n": 200,
        "p": 50,
        "rho": 0,
        "error_distribution": "normal",
    },
    "compare_est_normal_err_p_20_l": {
        "experiment": "A",
        "n": 200,
        "p": 50,
        "rho": 0,
        "error_distribution": "laplace",
    },
    "compare_est_normal_err_p_100_n": {
        "experiment": "A",
        "n": 200,
        "p": 100,
        "rho": 0,
        "error_distribution": "normal",
    },
    "compare_est_normal_err_p_100_l": {
        "experiment": "A",
        "n": 200,
        "p": 100,
        "rho": 0,
        "error_distribution": "laplace",
    },
    "compare_est_normal_err_p_150_n": {
        "experiment": "A",
        "n": 200,
        "p": 150,
        "rho": 0,
        "error_distribution": "normal",
    },
    "compare_est_normal_err_p_150_l": {
        "experiment": "A",
        "n": 200,
        "p": 150,
        "rho": 0,
        "error_distribution": "laplace",
    },
    "compare_est_normal_err_p_199_n": {
        "experiment": "A",
        "n": 200,
        "p": 199,
        "rho": 0,
        "error_distribution": "normal",
    },
    "compare_est_normal_err_p_199_l": {
        "experiment": "A",
        "n": 200,
        "p": 199,
        "rho": 0,
        "error_distribution": "laplace",
    },
    "est_vs_pred_rho_0_n": {
        "experiment": "B",
        "n": 200,
        "p": 100,
        "rho": 0,
        "error_distribution": "normal",
    },
    "est_vs_pred_rho_0_l": {
        "experiment": "B",
        "n": 200,
        "p": 100,
        "rho": 0,
        "error_distribution": "laplace",
    },
    "est_vs_pred_rho_20_n": {
        "experiment": "B",
        "n": 200,
        "p": 100,
        "rho": 0.2,
        "error_distribution": "normal",
    },
    "est_vs_pred_rho_20_l": {
        "experiment": "B",
        "n": 200,
        "p": 100,
        "rho": 0.2,
        "error_distribution": "laplace",
    },
    "est_vs_pred_rho_60_n": {
        "experiment": "B",
        "n": 200,
        "p": 100,
        "rho": 0.6,
        "error_distribution": "normal",
    },
    "est_vs_pred_rho_60_l": {
        "experiment": "B",
        "n": 200,
        "p": 100,
        "rho": 0.6,
        "error_distribution": "laplace",
    },
    "est_vs_pred_rho_90_n": {
        "experiment": "B",
        "n": 200,
        "p": 100,
        "rho": 0.9,
        "error_distribution": "normal",
    },
    "est_vs_pred_rho_90_l": {
        "experiment": "B",
        "n": 200,
        "p": 100,
        "rho": 0.9,
        "error_distribution": "laplace",
    },
    }
    return experiments