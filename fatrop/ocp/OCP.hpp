#ifndef OCPINCLUDED
#define OCPINCLUDED
#include "blasfeo_wrapper/LinearAlgebraBlasfeo.hpp"
#include "OCPDims.hpp"
#include "ocp/OCPKKT.hpp"
#include "solver/FatropData.hpp"
#include <memory>
namespace fatrop
{
    /** \brief interface class for OCP operations*/
    class OCP
    {
    public:
        virtual int evalHess(
            OCPKKTMemory *OCP,
            double obj_scale,
            const FatropVecBF &primal_vars,
            const FatropVecBF &lam) = 0;
        virtual int evalJac(
            OCPKKTMemory *OCP,
            const FatropVecBF &primal_vars,
            const FatropVecBF &slack_vars) = 0;
        virtual int EvalConstraintViolation(
            OCPKKTMemory *OCP,
            const FatropVecBF &primal_vars,
            const FatropVecBF &slack_vars,
            FatropVecBF &constraint_violation) = 0;
        virtual int EvalGrad(
            OCPKKTMemory *OCP,
            double obj_scale,
            const FatropVecBF &primal_vars,
            FatropVecBF &gradient) = 0;
        virtual int EvalObj(
            OCPKKTMemory *OCP,
            double obj_scale,
            const FatropVecBF &primal_vars,
            double &res) = 0;
        virtual int EvalDynamics(
            OCPKKTMemory *OCP,
            const int k,
            const FatropVecBF &uk,
            const FatropVecBF &xk,
            FatropVecBF &xkp1) = 0;
        virtual OCPDims GetOCPDims() const = 0;
        virtual int GetBounds(
            FatropVecBF &lower,
            FatropVecBF &upper) const = 0;
        virtual int GetInitialGuess(
            FatropVecBF &initial) const = 0;
        // virtual int GetDefaultParams(
        //     FatropOptions &params) const = 0;
        virtual void SetParams(const std::vector<double> &stage_params_in, const std::vector<double> &global_params_in) = 0;
        virtual void SetInitial(const std::shared_ptr<FatropData> &fatropdata, std::vector<double> &initial_u, std::vector<double> &initial_x) = 0;
        virtual void GetSolution(const std::shared_ptr<FatropData> &fatropdata, std::vector<double> &u, std::vector<double> &x) = 0;
    };
} // namespace fatrop
#endif // OCPINCLUDED