#ifndef NOSCALINGMETHODINCLUDED
#define NOSCALINGMETHODINCLUDED
#include "solver/FatropData.hpp"
#include "templates/NLPAlg.hpp"
#include "solver/AlgStrategy.hpp"
#include "OCPScalingMethod.hpp"
#include "blasfeo_wrapper/LinearAlgebraBlasfeo.hpp"
#include <memory>
namespace fatrop
{
    class OCPNoScaling : public OCPScalingMethod
    {
    public:
        OCPNoScaling(const std::shared_ptr<FatropOptions> &fatrop_params);
        virtual int ComputeScalings(
            OCPKKTMemory *OCP,
            double &obj_scale,
            FatropVecBF &x_scales,
            FatropVecBF &lam_scales, const FatropVecBF &grad_curr);
    };

} // namespace fatrop
#endif // !SCALINGMETHODINCLUDED