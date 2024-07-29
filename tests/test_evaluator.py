"""This module implements the tests for the evaluator."""

from opthub_runner.evaluator import Evaluator


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


def test_evaluator_with_non_str_envvars() -> None:
    """Test the evaluator in case the environment type is not str."""
    docker_image = "opthub/sphere:latest"
    evaluator = Evaluator(docker_image, {"SPHERE_OPTIMA": [[1, 0, 0], [0, 1, 0]]})

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

def test_evaluator_with_local_images() -> None:
    """Test the evaluator in case the image is on the local machine."""
    docker_image = "sphere:latest" # You need to have the image locally.
    evaluator = Evaluator(docker_image, {"SPHERE_OPTIMA": "[[1, 0]]"})

    result = evaluator.run([0, 0])

    eps = 1e-2

    if not isinstance(result["objective"], float):
        msg = f"The objective value is not correct: result is {result['objective']}, expected float."
        raise TypeError(msg)

    if abs(result["objective"] - 1) > eps:
        msg = f"The objective value is not correct: result is {result['objective']}, expected 1."
        raise ValueError(msg)
