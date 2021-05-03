import abc
import torch


class ClassifierLoss(abc.ABC):
  """
  Represents a loss function of a classifier.
  """

  def __call__(self, *args, **kwargs):
    return self.loss(*args, **kwargs)

  @abc.abstractmethod
  def loss(self, *args, **kw):
    pass

  @abc.abstractmethod
  def grad(self):
    """
    :return: Gradient of the last calculated loss w.r.t. model
        parameters, as a Tensor of shape (D, C).
    """
    pass


class SVMHingeLoss(ClassifierLoss):
  def __init__(self, delta=1.0):
    self.delta = delta
    self.grad_ctx = {}

  def loss(self, x, y, x_scores, y_predicted):
    """
    Calculates the Hinge-loss for a batch of samples.

    :param x: Batch of samples in a Tensor of shape (N, D).
    :param y: Ground-truth labels for these samples: (N,)
    :param x_scores: The predicted class score for each sample: (N, C).
    :param y_predicted: The predicted class label for each sample: (N,).
    :return: The classification loss as a Tensor of shape (1,).
    """

    assert x_scores.shape[0] == y.shape[0]
    assert y.dim() == 1

    # TODO: Implement SVM loss calculation based on the hinge-loss formula.
    #  Notes:
    #  - Use only basic pytorch tensor operations, no external code.
    #  - Full credit will be given only for a fully vectorized
    #    implementation (zero explicit loops).
    #    Hint: Create a matrix M where M[i,j] is the margin-loss
    #    for sample i and class j (i.e. s_j - s_{y_i} + delta).

    loss = None
    # ====== YOUR CODE: ======
    y_i_scores = x_scores[
      torch.LongTensor(list(range(x_scores.shape[0]))), y].view(
      (x_scores.shape[0], 1))  # the correct prediction score for every example
    M = torch.max(x_scores - y_i_scores + self.delta
                  , torch.zeros_like(x_scores))
    loss = torch.mean(M.sum(1))

    loss = loss - self.delta
    # ========================

    # TODO: Save what you need for gradient calculation in self.grad_ctx
    # ====== YOUR CODE: ======
    self.grad_ctx["g"] = (M > 0).float()
    self.grad_ctx["samples"] = torch.LongTensor(list(range(x_scores.shape[0])))
    self.grad_ctx["g"][self.grad_ctx["samples"], y] = 0
    self.grad_ctx["x"] = x
    self.grad_ctx["y"] = y
    # ========================

    return loss

  def grad(self):
    """
    Calculates the gradient of the Hinge-loss w.r.t. parameters.
    :return: The gradient, of shape (D, C).

    """
    # TODO:
    #  Implement SVM loss gradient calculation
    #  Same notes as above. Hint: Use the matrix M from above, based on
    #  it create a matrix G such that X^T * G is the gradient.

    grad = None
    # ====== YOUR CODE: ======
    G = self.grad_ctx["g"]
    N = self.grad_ctx["samples"]
    y = self.grad_ctx["y"]
    r_sum = G.sum(1)
    G[N, y] = -r_sum.T
    grad = self.grad_ctx["x"].T @ G
    grad = grad/N.shape[0]
    # ========================

    return grad