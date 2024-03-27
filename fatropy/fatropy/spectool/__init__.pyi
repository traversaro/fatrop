# fatropy-stubs/spectool.pyi

from __future__ import annotations
import typing
from casadi import MX, Function
__all__ = ['Hessian', 'IntegratorRk4', 'Jacobian', 'Ocp', 'SolverInterface', 'Stage', 'at', 'csDict', 'csGenericType', 'mid', 't0', 'tf', 'uStage', 'uo_map_mx_mx']


class Hessian:
    def __init__(self, arg0: MX, arg1: MX, arg2: MX, arg3: MX) -> None:
        ...
class IntegratorRk4:
    @typing.overload
    def __call__(self, arg0: MX) -> MX:
        ...
    @typing.overload
    def __call__(self, arg0: list[MX]) -> list[MX]:
        ...
    def __init__(self, arg0: list[tuple[MX, MX]], arg1: MX) -> None:
        ...
class Jacobian:
    def __init__(self, arg0: MX, arg1: MX) -> None:
        ...
class Ocp:
    @staticmethod
    def solver(*args, **kwargs) -> None:
        ...
    def __init__(self) -> None:
        ...
    def add_ustage(self, arg0: uStage) -> None:
        ...
    def all_variables(self) -> MX:
        ...
    @typing.overload
    def at_t0(self, arg0: MX) -> MX:
        ...
    @typing.overload
    def at_t0(self) -> uStage:
        ...
    @typing.overload
    def at_tf(self, arg0: MX) -> MX:
        ...
    @typing.overload
    def at_tf(self) -> uStage:
        ...
    def control(self, m: int = 1, n: int = 1) -> MX:
        ...
    def eval_at_initial(self, arg0: list[MX]) -> list[MX]:
        ...
    def get_solver(self) -> SolverInterface:
        ...
    def hybrid(self, m: int = 1, n: int = 1) -> MX:
        ...
    def new_stage(self, K: int = 1) -> Stage:
        ...
    def new_ustage(self, K: int = 1) -> uStage:
        ...
    def parameter(self, m: int = 1, n: int = 1, grid: str = 'global') -> MX:
        ...
    def sample(self, arg0: MX) -> tuple[list[int], MX]:
        ...
    def set_initial(self, arg0: MX, arg1: MX) -> None:
        ...
    def state(self, m: int = 1, n: int = 1) -> MX:
        ...
    def subject_to(self, arg0: MX) -> None:
        ...
    def to_function(self, name: str, in: list[MX], out: list[MX]) -> Function:
        ...
class SolverInterface:
    def stats(self) -> dict[str, csGenericType]:
        ...
class Stage:
    @typing.overload
    def add_objective(self, arg0: MX, arg1: at) -> None:
        ...
    @typing.overload
    def add_objective(self, arg0: MX, arg1: at, arg2: at) -> None:
        ...
    @typing.overload
    def add_objective(self, arg0: MX, arg1: at, arg2: at, arg3: at) -> None:
        ...
    def at_mid(self) -> ...:
        ...
    @typing.overload
    def at_t0(self, arg0: MX) -> MX:
        ...
    @typing.overload
    def at_t0(self) -> ...:
        ...
    @typing.overload
    def at_tf(self, arg0: MX) -> MX:
        ...
    @typing.overload
    def at_tf(self) -> ...:
        ...
    def set_next(self, x_next: MX, expr: MX, jacobian: Jacobian = ..., hessian: Hessian = ...) -> None:
        ...
    @typing.overload
    def subject_to(self, arg0: MX, arg1: at) -> None:
        ...
    @typing.overload
    def subject_to(self, arg0: MX, arg1: at, arg2: at) -> None:
        ...
    @typing.overload
    def subject_to(self, arg0: MX, arg1: at, arg2: at, arg3: at) -> None:
        ...
class at:
    """
    Members:
    
      t0
    
      mid
    
      tf
    """
    __members__: typing.ClassVar[dict[str, at]]  # value = {'t0': <at.t0: 0>, 'mid': <at.mid: 1>, 'tf': <at.tf: 2>}
    mid: typing.ClassVar[at]  # value = <at.mid: 1>
    t0: typing.ClassVar[at]  # value = <at.t0: 0>
    tf: typing.ClassVar[at]  # value = <at.tf: 2>
    def __eq__(self, other: typing.Any) -> bool:
        ...
    def __getstate__(self) -> int:
        ...
    def __hash__(self) -> int:
        ...
    def __index__(self) -> int:
        ...
    def __init__(self, value: int) -> None:
        ...
    def __int__(self) -> int:
        ...
    def __ne__(self, other: typing.Any) -> bool:
        ...
    def __repr__(self) -> str:
        ...
    def __setstate__(self, state: int) -> None:
        ...
    def __str__(self) -> str:
        ...
    @property
    def name(self) -> str:
        ...
    @property
    def value(self) -> int:
        ...
class csDict:
    def __bool__(self: dict[str, csGenericType]) -> bool:
        """
        Check whether the map is nonempty
        """
    @typing.overload
    def __contains__(self: dict[str, csGenericType], arg0: str) -> bool:
        ...
    @typing.overload
    def __contains__(self: dict[str, csGenericType], arg0: typing.Any) -> bool:
        ...
    def __delitem__(self: dict[str, csGenericType], arg0: str) -> None:
        ...
    def __getitem__(self: dict[str, csGenericType], arg0: str) -> csGenericType:
        ...
    def __init__(self) -> None:
        ...
    def __iter__(self: dict[str, csGenericType]) -> typing.Iterator:
        ...
    def __len__(self: dict[str, csGenericType]) -> int:
        ...
    def __repr__(self: dict[str, csGenericType]) -> str:
        """
        Return the canonical string representation of this map.
        """
    def __setitem__(self: dict[str, csGenericType], arg0: str, arg1: csGenericType) -> None:
        ...
    def items(self: dict[str, csGenericType]) -> typing.ItemsView[str, csGenericType]:
        ...
    def keys(self: dict[str, csGenericType]) -> typing.KeysView[str]:
        ...
    def values(self: dict[str, csGenericType]) -> typing.ValuesView[csGenericType]:
        ...
class csGenericType:
    @typing.overload
    def __init__(self, arg0: bool) -> None:
        ...
    @typing.overload
    def __init__(self, arg0: int) -> None:
        ...
    @typing.overload
    def __init__(self, arg0: int) -> None:
        ...
    @typing.overload
    def __init__(self, arg0: float) -> None:
        ...
    @typing.overload
    def __init__(self, arg0: str) -> None:
        ...
    @typing.overload
    def __init__(self, arg0: list[bool]) -> None:
        ...
    @typing.overload
    def __init__(self, arg0: list[int]) -> None:
        ...
    @typing.overload
    def __init__(self, arg0: list[int]) -> None:
        ...
    @typing.overload
    def __init__(self, arg0: list[list[int]]) -> None:
        ...
    @typing.overload
    def __init__(self, arg0: list[float]) -> None:
        ...
    @typing.overload
    def __init__(self, arg0: list[list[float]]) -> None:
        ...
    @typing.overload
    def __init__(self, arg0: list[str]) -> None:
        ...
    @typing.overload
    def __init__(self, arg0: Function) -> None:
        ...
    @typing.overload
    def __init__(self, arg0: list[Function]) -> None:
        ...
    @typing.overload
    def __init__(self, arg0: dict[str, csGenericType]) -> None:
        ...
    @typing.overload
    def __init__(self, arg0: capsule) -> None:
        ...
    def bool(self) -> bool:
        ...
    def double(self) -> float:
        ...
    def int(self) -> int:
        ...
class uStage:
    def K(self) -> int:
        ...
    @typing.overload
    def __init__(self) -> None:
        ...
    @typing.overload
    def __init__(self, arg0: int) -> None:
        ...
    def add_objective(self, arg0: MX) -> None:
        ...
    def at_t0(self, arg0: MX) -> MX:
        ...
    def at_tf(self, arg0: MX) -> MX:
        ...
    def clone(self) -> uStage:
        ...
    def dynamics(self) -> ...:
        ...
    def eval_at_control(self, arg0: MX, arg1: int) -> MX:
        ...
    def register_control(self, arg0: list[MX]) -> None:
        ...
    def register_control_parameter(self, arg0: list[MX]) -> None:
        ...
    def register_global_parameter(self, arg0: list[MX]) -> None:
        ...
    def register_hybrid(self, arg0: list[MX]) -> None:
        ...
    def register_state(self, arg0: list[MX]) -> None:
        ...
    def sample(self, arg0: MX) -> tuple[list[int], MX]:
        ...
    def set_next(self, x_next: MX, expr: MX, jacobian: Jacobian = ..., hessian: Hessian = ...) -> None:
        ...
    def subject_to(self, constraint: MX, jacobian: Jacobian = ..., hessian: Hessian = ...) -> None:
        ...
class uo_map_mx_mx:
    def __bool__(self: dict[MX, MX]) -> bool:
        """
        Check whether the map is nonempty
        """
    @typing.overload
    def __contains__(self: dict[MX, MX], arg0: MX) -> bool:
        ...
    @typing.overload
    def __contains__(self: dict[MX, MX], arg0: typing.Any) -> bool:
        ...
    def __delitem__(self: dict[MX, MX], arg0: MX) -> None:
        ...
    def __getitem__(self: dict[MX, MX], arg0: MX) -> MX:
        ...
    def __init__(self) -> None:
        ...
    def __iter__(self: dict[MX, MX]) -> typing.Iterator:
        ...
    def __len__(self: dict[MX, MX]) -> int:
        ...
    def __repr__(self: dict[MX, MX]) -> str:
        """
        Return the canonical string representation of this map.
        """
    def __setitem__(self: dict[MX, MX], arg0: MX, arg1: MX) -> None:
        ...
    def items(self: dict[MX, MX]) -> typing.ItemsView[MX, MX]:
        ...
    def keys(self: dict[MX, MX]) -> typing.KeysView[MX]:
        ...
    def values(self: dict[MX, MX]) -> typing.ValuesView[MX]:
        ...
mid: at  # value = <at.mid: 1>
t0: at  # value = <at.t0: 0>
tf: at  # value = <at.tf: 2>