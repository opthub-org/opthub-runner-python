"""This module implements the tests for the evaluator."""

from opthub_evaluator.main import Evaluator


def test_evaluator() -> None:
    """Test the evaluator."""
    docker_image = "opthub/sphere:latest"
    evaluator = Evaluator(docker_image, {"SPHERE_OPTIMA": "[[1, 0, 0], [0, 1, 0]]"})

    result = evaluator.run([0, 0, 0])

    eps = 1e-2

    if not isinstance(result["objective"], list):
        msg = f"The objective value is not correct: result is {result['objective']}, expected list."
        raise TypeError(msg)

    if abs(result["objective"][0] - 1) > eps or abs(result["objective"][1] - 1) > eps:
        msg = f"The objective value is not correct: result is {result['objective']}, expected [1, 1]."
        raise ValueError(msg)

    result = evaluator.run([0.5, 0, 0.5])

    if not isinstance(result["objective"], list):
        msg = f"The objective value is not correct: result is {result['objective']}, expected list."
        raise TypeError(msg)

    if abs(result["objective"][0] - 0.5) > eps or abs(result["objective"][1] - 1.5) > eps:
        msg = f"The objective value is not correct: result is {result['objective']}, expected [0.5, 1.5]."
        raise ValueError(msg)
